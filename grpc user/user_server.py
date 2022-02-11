from concurrent import futures
import logging
import random
import grpc
import user_pb2
import user_pb2_grpc
import library_service_pb2
import library_service_pb2_grpc
from google.protobuf.json_format import MessageToDict
import string
import os

required_fields = {"get_book_price": ['name']}


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


# library_server_URL = "localhost:50051"
# library_server_URL = "grpcLibrary-container:50051"
library_server_URL = os.getenv('LIBRARY_HOST', 'localhost:50051')

class UserServicer(user_pb2_grpc.userServicer):

    @check_pagination
    def extra_info(self, request, context):
        # call library server to get array of Books
        response = None
        with grpc.insecure_channel(library_server_URL) as channel:
            stub = library_service_pb2_grpc.LibraryStub(channel)
            try:
                response = stub.get_books_list(request=library_service_pb2.Pagination(offset=request.offset,
                                                                                      limit=request.limit))
            except Exception as e:
                context.abort(grpc.StatusCode.UNAVAILABLE, "Couldn't get info from library service.\n"
                                                           "Error: " + str(e))
        # Go through array to add extra info to it
        ans = []
        for book in response.book:
            book_dict = MessageToDict(book)
            book_dict = get_book_as_dict(book_dict)
            book_dict["extra_info"] = ''.join(random.choice(string.ascii_letters) for i in range(10))
            ans.append(user_pb2.Book(**book_dict))
        # return the info in message format (arrBooks)
        return user_pb2.arrBooks(books=ans)

    @check_required_fields
    def get_book_price(self, request, context):
        # call library server to get a book of name: request.name
        response = None
        with grpc.insecure_channel(library_server_URL) as channel:
            stub = library_service_pb2_grpc.LibraryStub(channel)
            try:
                response = stub.get_book(
                    request=library_service_pb2.BookName(name=request.name))
            except grpc.RpcError as rpc_error:
                if rpc_error.code() == grpc.StatusCode.NOT_FOUND:
                    context.abort(grpc.StatusCode.NOT_FOUND, f"Book with {request.name} name not found in DB.")
            except Exception as e:
                context.abort(grpc.StatusCode.UNAVAILABLE, "Couldn't get info from library service.\n"
                                                           "Error: " + str(e))
        # Use its info to generate a random number
        secret = len(response.name)
        return user_pb2.BookPrice(price=random.randrange(5, 50 + secret))


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
    options = (('grpc.so_reuseport', 1),)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),
                         options=options)
    user_pb2_grpc.add_userServicer_to_server(UserServicer(), server)
    server.add_insecure_port('[::]:50000')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
