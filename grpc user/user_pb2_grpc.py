# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import user_pb2 as user__pb2


class userStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_book_price = channel.unary_unary(
                '/user/get_book_price',
                request_serializer=user__pb2.BookName.SerializeToString,
                response_deserializer=user__pb2.BookPrice.FromString,
                )
        self.extra_info = channel.unary_unary(
                '/user/extra_info',
                request_serializer=user__pb2.Pagination.SerializeToString,
                response_deserializer=user__pb2.arrBooks.FromString,
                )


class userServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_book_price(self, request, context):
        """Returns price of book
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def extra_info(self, request, context):
        """Gets array of books using pagination and adds an extra field to it
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_userServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_book_price': grpc.unary_unary_rpc_method_handler(
                    servicer.get_book_price,
                    request_deserializer=user__pb2.BookName.FromString,
                    response_serializer=user__pb2.BookPrice.SerializeToString,
            ),
            'extra_info': grpc.unary_unary_rpc_method_handler(
                    servicer.extra_info,
                    request_deserializer=user__pb2.Pagination.FromString,
                    response_serializer=user__pb2.arrBooks.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class user(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_book_price(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user/get_book_price',
            user__pb2.BookName.SerializeToString,
            user__pb2.BookPrice.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def extra_info(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user/extra_info',
            user__pb2.Pagination.SerializeToString,
            user__pb2.arrBooks.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
