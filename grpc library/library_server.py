from concurrent import futures
import logging

import grpc
import library_service_pb2
import library_service_pb2_grpc

import pymongo
from auth_module.auth_interceptor import ExceptionToAuthenticationInterceptor
from google.protobuf.json_format import MessageToDict

client = pymongo.MongoClient("mongodb+srv://user1:user1password@libraryapp.bssao.mongodb.net/myFirstDatabase"
                             "?retryWrites=true&w=majority")
db = client.get_database("Library")
books_collection = db.get_collection("books")
books_collection.create_index([("name", 1)], unique=True)

users_db = client.get_database("Authentication")
users_collection = users_db.get_collection("users")

array_fields = ["authors"]
string_fields = ["publisher", "name", "date_of_release", "description"]
enum_fields = ["genre"]

# dict to know which fields are required by each function
required_fields = {'add_book': ["name"],
                   "get_book": ["name"],
                   "delete_book": ["name"],
                   "update_book": ["name", "field"]}


def check_required_fields(func):
    def func_wrapper(self, request, context):
        function_name = func.__name__
        fields = required_fields.get(function_name, None)
        request_dict = MessageToDict(request)
        for field in fields:
            if field not in request_dict:
                context.abort(grpc.StatusCode.INVALID_ARGUMENT,
                              f"ERROR: Request message to function '{function_name}' needs to contain field '{field}'")
        return func(self, request, context)

    return func_wrapper


def check_pagination(func):
    def func_wrapper(self, request, context):
        if request.offset < 0 or request.limit <= 0:
            raise Exception("Limit has to be positive and offset has to be non negative for function {} to work".
                            format(func.__name__))
        res = func(self, request, context)
        return res

    return func_wrapper


class Library_manager(library_service_pb2_grpc.LibraryServicer):

    @check_required_fields
    def get_book(self, request, context):
        book = books_collection.find_one({"name": request.name}, {"_id": 0})
        if book is None:
            context.abort(grpc.StatusCode.NOT_FOUND, "Book with name " + request.name + " not found in DB.")
        response = library_service_pb2.Book(**book)
        return response

    @check_required_fields
    def delete_book(self, request, context):
        result = books_collection.delete_one({"name": request.name})
        if result.deleted_count:
            return library_service_pb2.Message(message=request.name + " successfully deleted from DB.")
        return library_service_pb2.Message(message="No book was deleted from the DB.")

    @check_required_fields
    def update_book(self, request, context):
        request_formatted = MessageToDict(request)

        field_to_update = request_formatted.get("field", None)
        field_value_to_update = None
        current_book_name = request_formatted.get("name", None)

        if field_to_update in array_fields:
            field_value_to_update = request_formatted.get("newArray", None)

        elif field_to_update in string_fields:
            field_value_to_update = request_formatted.get("newValue", None)

        elif field_to_update in enum_fields:
            field_value_to_update = request_formatted.get("newGenre", None)
        
        else:
            return library_service_pb2.Message(message="Field to update does not exist in the current DB.")

        if field_to_update == "name":
            if not field_value_to_update:
                return library_service_pb2.Message(message="Cannot set the new name to NONE")
        try:
            book = books_collection.update_one({"name": current_book_name},
                                               {"$set": {field_to_update: field_value_to_update}})

            if not book.matched_count:
                return library_service_pb2.Message(message="Book with {name} name doesnt exist."
                                                   .format(name=current_book_name))

            return library_service_pb2.Message(message="Successfully updated document.")
        except pymongo.errors.DuplicateKeyError:
            return library_service_pb2.Message(message="Cant update name, other book with this new name exists.")
        except Exception as e:
            return library_service_pb2.Message(message="Error: " + str(e))

    @check_required_fields
    def add_book(self, request, context):
        try:
            book_dict = MessageToDict(request)
            book = get_book_as_dict(book_dict)
            # if book["name"] is None:
            #     return library_service_pb2.Message(message="Cannot add book with no name.")
            books_collection.insert_one(book)
            return library_service_pb2.Message(message="Book added to DB successfully.")
        except pymongo.errors.DuplicateKeyError:
            return library_service_pb2.Message(message="Book with this name already exists in the DB.")
        except pymongo.errors.NetworkTimeout:
            return library_service_pb2.Message(message="Error: Network Timeout")
        except Exception as e:
            return library_service_pb2.Message(message="Exception: " + str(e))

    # Dont need to check for required fields since if limit or offset dont exist,
    # their value is set to 0 by default
    @check_pagination
    def get_books_list(self, request, context):
        limit = request.limit
        offset = request.offset
        try:
            books = books_collection.aggregate([
                {
                    '$addFields': {
                        'lower_name': {
                            '$toLower': '$name'
                        }
                    }
                }, {
                    '$sort': {
                        'lower_name': 1
                    }
                }, {
                    '$skip': offset * limit
                }, {
                    '$limit': limit
                }, {
                    '$project': {
                        '_id': 0,
                        'lower_name': 0
                    }
                }
            ])
            # Translate books into an array of Book message
            array_of_books = []
            for book in books:
                array_of_books.append(library_service_pb2.Book(**book))
            return library_service_pb2.Books(book=array_of_books)
        except Exception as e:
            context.abort(grpc.StatusCode.UNKNOWN, str(e))


def get_book_as_dict(book_dict):
    book = {
        "name": book_dict.get("name", None),
        "authors": book_dict.get("authors", []),
        "genre": book_dict.get("genre", "ACTION"),
        "publisher": book_dict.get("publisher", ""),
        "description": book_dict.get("description", ""),
        "date_of_release": book_dict.get("date_of_release", "")
    }
    return book


def serve():
    interceptors = [ExceptionToAuthenticationInterceptor()]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),
                         options=(('grpc.so_reuseport', 1),),
                         interceptors=interceptors)
    library_service_pb2_grpc.add_LibraryServicer_to_server(Library_manager(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
