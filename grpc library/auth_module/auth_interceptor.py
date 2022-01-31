import jwt
import pymongo
from grpc_interceptor import ServerInterceptor
from grpc_interceptor.exceptions import GrpcException
from bson.objectid import ObjectId
from . import authentication_module
import grpc

client = pymongo.MongoClient("mongodb+srv://user1:user1password@libraryapp.bssao.mongodb.net/myFirstDatabase"
                             "?retryWrites=true&w=majority")
users_db = client.get_database("Authentication")
users_collection = users_db.get_collection("users")

auth_processes = ["delete_book", "update_book", "add_book"]


class ExceptionToAuthenticationInterceptor(ServerInterceptor):
    def intercept(self, method, request, context, method_name):
        """Override this method to implement a custom interceptor.
         You should call method(request, context) to invoke the
         next handler (either the RPC method implementation, or the
         next interceptor in the list).
         Args:
             method: The next interceptor, or method implementation.
             request: The RPC request, as a protobuf message.
             context: The ServicerContext pass by gRPC to the service.
             method_name: A string of the form
                 "/protobuf.package.Service/Method"
         Returns:
             This should generally return the result of
             method(request, context), which is typically the RPC
             method response, as a protobuf message. The interceptor
             is free to modify this in some way, however.
         """
        # get the name of the request
        curr_method = method_name.split('/')[-1]
        # if the request does not need authentication, we just call it
        if curr_method not in auth_processes:
            try:
                return method(request, context)
            except GrpcException as e:
                context.set_code(e.status_code)
                context.set_details(e.details)
                raise
        # request needs to be authenticated (made by a librarian)
        metadata = context.invocation_metadata()
        authenticated, message = check_if_librarian_using_JWT(metadata)
        if not authenticated:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, message)
        return method(request, context)


def check_if_librarian_using_JWT(metadata):
    for metadatum in metadata:
        key = metadatum.key
        value = metadatum.value
        if key == "authorization":
            token = value.split(" ")[-1]
            if token is None:
                return False, "Token was not passed correctly."
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
                return False, "Token does not point to valid user."
            # return true if Librarian
            user_type = user.get("type", "")
            if user_type == "LIBRARIAN":
                return True, None
            else:
                return False, "User is not a librarian."
    return False, None
