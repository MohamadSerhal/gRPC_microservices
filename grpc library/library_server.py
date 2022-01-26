from concurrent import futures
import logging

import grpc
import library_service_pb2
import library_service_pb2_grpc

import pymongo
from google.protobuf.json_format import MessageToJson, MessageToDict

client = pymongo.MongoClient("mongodb+srv://user1:user1password@libraryapp.bssao.mongodb.net/myFirstDatabase"
                             "?retryWrites=true&w=majority")
db = client.get_database("Library")
books_collection = db.get_collection("books")
books_collection.create_index([("name", 1)], unique=True)


class Library_manager(library_service_pb2_grpc.LibraryServicer):

    def get_book(self, request, context):
        book = books_collection.find_one({"name": request.name}, {"_id": 0})
        if book is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Book with name " + request.name + " not found in DB.")
            return library_service_pb2.Book()

        book_name = book.get("name")
        book_authors = book.get("authors", [])
        book_genre = book.get("genre", "ACTION")
        book_pub = book.get("publisher", None)
        book_desc = book.get("description", None)
        book_release = book.get("date_of_release", None)
        response = library_service_pb2.Book(name=book_name, authors=book_authors, genre=book_genre, publisher=book_pub,
                                            description=book_desc, date_of_release=book_release)
        return response

    def delete_book(self, request, context):
        result = books_collection.delete_one({"name": request.name})
        if result.deleted_count:
            return library_service_pb2.Message(message=request.name + " successfully deleted from DB.")
        return library_service_pb2.Message(message="No book was deleted from the DB.")

    def update_book(self, request, context):
        return

    def add_book(self, request, context):
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
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    library_service_pb2_grpc.add_LibraryServicer_to_server(Library_manager(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
