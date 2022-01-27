from __future__ import print_function

import logging

import grpc
import library_service_pb2
import library_service_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = library_service_pb2_grpc.LibraryStub(channel)
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NDM2NjA4NjIsImlhdCI6MTY0MzMxNTI2Miwic3ViIjoiNjFlOTg0ZThiYjFhYTEyMTQxMTk4Yzg1In0.VuUb7xe_0f_2SgVTxhPTw0yJiDrvuogoQWubhBnorzU"
        metadata = [('authorization', 'Bearer ' + token)]
        # print("-----------------------------------------------------------")
        # response = stub.get_book(library_service_pb2.BookName(name="Game Of Thrones"))
        # print("Client tries to get the 'Game Of Thrones' book:\n")
        # print(response)
        print("-----------------------------------------------------------")
        response = stub.delete_book(request=library_service_pb2.BookName(name="Malibu"), metadata=metadata)
        print("Client tries to delete book: Malibu\n")
        print(response)
        print("-----------------------------------------------------------")
        book_to_add = library_service_pb2.Book(name="Test Book2")
        book_to_add.authors.append("auth 1")
        book_to_add.authors.append("auth 2")
        response = stub.add_book(request=book_to_add, metadata=metadata)
        print("Adding test book to db\n")
        print(response)
        # print("-----------------------------------------------------------")
        # response = stub.get_books_list(library_service_pb2.Pagination(limit=3, offset=1))
        # print("Testing pagination")
        # print(response)
        print("-----------------------------------------------------------")
        updated_book = library_service_pb2.UpdatedBook(name="Book1Updated", field="authors")
        updated_book.newArray.append('new updated author 1')
        updated_book.newArray.append('new updated author 2')
        response = stub.update_book(request=updated_book, metadata=metadata)
        print("Changing authors")
        print(response)


if __name__ == '__main__':
    logging.basicConfig()
    run()
