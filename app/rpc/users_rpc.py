import grpc
from app.proto import users_pb2, users_pb2_grpc
from google.protobuf.json_format import MessageToDict
from dotenv import load_dotenv
import os

load_dotenv()

grpc_env = os.getenv("GRPC_URI")
base_url = grpc_env if grpc_env is not None else "127.0.0.1:50051"

print(base_url)

def register_user(username: str, password: str, email: str):
    with grpc.insecure_channel(base_url) as channel:
        stub = users_pb2_grpc.UserServiceStub(channel)
        request = users_pb2.RegisterRequest(
            username=username,
            password=password,
            email=email
        )
        response = stub.RegisterUser(request)

        response_dict = MessageToDict(response)

        verification_code = response_dict['verificationCode']

    return email, verification_code


def get_user_for_login(email: str):
    with grpc.insecure_channel(base_url) as channel:
        stub = users_pb2_grpc.UserServiceStub(channel)
        request = users_pb2.LoginRequest(
            email=email
        )
        response = stub.GetUserForLogin(request)
        response_dict = MessageToDict(response)

    return response_dict['user']


def get_user_verification_code(email: str):
    with grpc.insecure_channel(base_url) as channel:
        stub = users_pb2_grpc.UserServiceStub(channel)
        request = users_pb2.VerificationRequest(email=email)
        response = stub.GetUserVerification(request)
        response_dict = MessageToDict(response)

        return response_dict


def verify_user(email: str):
    with grpc.insecure_channel(base_url) as channel:
        stub = users_pb2_grpc.UserServiceStub(channel)
        request = users_pb2.VerificationRequest(email=email)
        response = stub.VerifyUser(request)
        response_dict = MessageToDict(response)

        return response_dict


def get_current_user_by_id(user_id: int):
    with grpc.insecure_channel(base_url) as channel:
        stub = users_pb2_grpc.UserServiceStub(channel)
        request = users_pb2.CurrentUserByIdRequest(user_id=user_id)
        response = stub.GetCurrentUserById(request)

        response_dict = MessageToDict(response)

        return response_dict['user']
