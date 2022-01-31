from concurrent import futures
import logging

import grpc
import library_service_pb2
import library_service_pb2_grpc

import pymongo
from auth_module import authentication_module
import jwt
from bson.objectid import ObjectId
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


class Library_manager(library_service_pb2_grpc.LibraryServicer):

    def get_book(self, request, context):
        book = books_collection.find_one({"name": request.name}, {"_id": 0})
        if book is None:
            # context.set_code(grpc.StatusCode.NOT_FOUND)
            # context.set_details("Book with name " + request.name + " not found in DB.")
            # return library_service_pb2.Book()
            context.abort(grpc.StatusCode.NOT_FOUND, "Book with name " + request.name + " not found in DB.")
        response = library_service_pb2.Book(**book)
        return response

    def delete_book(self, request, context):
        metadata = context.invocation_metadata()
        if not check_if_librarian_using_JWT(metadata):
            return library_service_pb2.Message(message="Only librarians can delete a book from the DB.")
        result = books_collection.delete_one({"name": request.name})
        if result.deleted_count:
            return library_service_pb2.Message(message=request.name + " successfully deleted from DB.")
        return library_service_pb2.Message(message="No book was deleted from the DB.")

    def update_book(self, request, context):
        metadata = context.invocation_metadata()
        if not check_if_librarian_using_JWT(metadata):
            return library_service_pb2.Message(message="Only librarians can update a book's info on the DB.")
        current_book_name = request.name
        book = books_collection.find_one({"name": current_book_name})
        # If we dont find the book with that current name, throw an error
        if book is None:
            return library_service_pb2.Message(message="Book with {name} name doesnt exist."
                                               .format(name=current_book_name))
        field_to_update = request.field
        if field_to_update in array_fields:
            try:
                updated_array = []
                for newauthor in request.newArray:
                    updated_array.append(newauthor)
                books_collection.update_one({"name": current_book_name}, {"$set": {field_to_update: updated_array}})
                return library_service_pb2.Message(message="Successfully updated document.")
            except pymongo.errors.DuplicateKeyError:
                return library_service_pb2.Message(message="Cant update name, other book with this name exists.")
            except Exception as e:
                return library_service_pb2.Message(message="Error: " + str(e))
        elif field_to_update in string_fields:
            try:
                books_collection.update_one({"name": current_book_name}, {"$set": {field_to_update: request.newValue}})
                return library_service_pb2.Message(message="Successfully updated document.")
            except Exception as e:
                return library_service_pb2.Message(message="Error: " + str(e))
        elif field_to_update in enum_fields:
            try:
                books_collection.update_one({"name": current_book_name}, {"$set": {field_to_update: request.newGenre}})
                return library_service_pb2.Message(message="Successfully updated document.")
            except Exception as e:
                return library_service_pb2.Message(message="Error: " + str(e))

        return library_service_pb2.Message(message="Field to update does not exist in the current DB.")

    def add_book(self, request, context):
        metadata = context.invocation_metadata()
        if not check_if_librarian_using_JWT(metadata):
            return library_service_pb2.Message(message="Only librarians can add a book to the DB.")
        try:
            book_dict = MessageToDict(request)
            book = get_book_as_dict(book_dict)
            if book["name"] is None:
                return library_service_pb2.Message(message="Cannot add book with no name.")
            books_collection.insert_one(book)
            return library_service_pb2.Message(message="Book added to DB successfully.")
        except pymongo.errors.DuplicateKeyError:
            return library_service_pb2.Message(message="Book with this name already exists in the DB.")
        except pymongo.errors.NetworkTimeout:
            return library_service_pb2.Message(message="Error: Network Timeout")
        except Exception as e:
            return library_service_pb2.Message(message="Exception: " + str(e))

    def get_books_list(self, request, context):
        limit = request.limit
        offset = request.offset
        if limit is None:
            limit = 0
        if offset is None:
            offset = 0
        if limit < 0 or offset < 0:
            # context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            # context.set_details("Limit and offset must be non negative.")
            # return library_service_pb2.Books(list_of_books=[])
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Limit and offset must be non negative.")
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
            # context.set_code(grpc.StatusCode.UNKNOWN)
            # context.set_details(str(e))
            # return library_service_pb2.Books(book=[])
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


def check_if_librarian_using_JWT(metadata):
    for metadatum in metadata:
        key = metadatum.key
        value = metadatum.value
        if key == "authorization":
            token = value.split(" ")[-1]
            if token is None:
                return False, None
            # Now decode token to get user id
            try:
                user_id = authentication_module.decode_token(token)
            except jwt.exceptions.ExpiredSignatureError:
                return False, "Error: Token has expired."
            except Exception as e:
                return False, "Error: " + str(e)
            # check if user is Librarian
            user = users_collection.find_one({"_id": ObjectId(user_id)}, {"type": 1})
            if user is None:
                return False, None
            # return true if Librarian
            user_type = user.get("type", "")
            if user_type == "LIBRARIAN":
                return True, None
            else:
                return False, None
    return False, None


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=(('grpc.so_reuseport', 1),))
    library_service_pb2_grpc.add_LibraryServicer_to_server(Library_manager(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
