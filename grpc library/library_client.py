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
        print("-----------------------------------------------------------")
        response = stub.get_book(library_service_pb2.BookName(name="Game Of Thrones"))
        print("Client tries to get the 'Game Of Thrones' book:\n")
        print(response)
        print("-----------------------------------------------------------")
        response = stub.delete_book(library_service_pb2.BookName(name="Malibu"))
        print("Client tries to delete book: Malibu\n")
        print(response)
        print("-----------------------------------------------------------")
        response = stub.add_book(library_service_pb2.Book(name="Test Book"))
        print("Adding test book to db\n")
        print(response)


if __name__ == '__main__':
    logging.basicConfig()
    run()
