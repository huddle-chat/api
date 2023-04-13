import grpc
from app.proto import guilds_pb2, guilds_pb2_grpc
from dotenv import load_dotenv
from google.protobuf.json_format import MessageToDict
import os

load_dotenv()

grpc_env = os.getenv("GRPC_URI")
base_url = grpc_env if grpc_env is not None else "127.0.0.1:50051"


def get_guilds_by_user_id(user_id: int):
    with grpc.insecure_channel(base_url) as channel:
        stub = guilds_pb2_grpc.GuildServiceStub(channel)

        request = guilds_pb2.GuildsByUserIdRequest(user_id=user_id)

        response = stub.GetGuildsByUserId(request)

        response_dict = MessageToDict(response)

        if 'guilds' in response_dict:
            return response_dict
        else:
            return {"guilds": []}

def create_guild(user_id: int, name: str, description=None, icon=None):
    with grpc.insecure_channel(base_url) as channel:
        stub = guilds_pb2_grpc.GuildServiceStub(channel)

        request = guilds_pb2.CreateGuildRequest(
            user_id=user_id,
            name=name,
            description=description,
            icon=icon
        )

        response = stub.CreateGuild(request)

        response_dict = MessageToDict(response)

        if 'guild' in response_dict:
            response_dict['guild']['has_unread'] = False

        return response_dict
