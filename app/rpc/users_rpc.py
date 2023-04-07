import grpc
from app.proto import users_pb2, users_pb2_grpc
from google.protobuf.json_format import MessageToDict


def register_user(username: str, password: str, email: str):
    with grpc.insecure_channel("localhost:50051") as channel:
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
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = users_pb2_grpc.UserServiceStub(channel)
        request = users_pb2.LoginRequest(
            email=email
        )
        response = stub.GetUserForLogin(request)
        response_dict = MessageToDict(response)
        print(response_dict)
    return response_dict['user']


def get_user_verification_code(email: str):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = users_pb2_grpc.UserServiceStub(channel)
        request = users_pb2.VerificationRequest(email=email)
        response = stub.GetUserVerification(request)
        response_dict = MessageToDict(response)
        print(response_dict)
        return response_dict


def verify_user(email: str):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = users_pb2_grpc.UserServiceStub(channel)
        request = users_pb2.VerificationRequest(email=email)
        response = stub.VerifyUser(request)
        response_dict = MessageToDict(response)
        print(response_dict)
        return response_dict
