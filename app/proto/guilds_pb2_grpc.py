# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from app.proto import guilds_pb2 as app_dot_proto_dot_guilds__pb2


class GuildServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetGuildsByUserId = channel.unary_unary(
                '/huddle_chat.GuildService/GetGuildsByUserId',
                request_serializer=app_dot_proto_dot_guilds__pb2.GuildsByUserIdRequest.SerializeToString,
                response_deserializer=app_dot_proto_dot_guilds__pb2.GuildsByUserIdResponse.FromString,
                )
        self.CreateGuild = channel.unary_unary(
                '/huddle_chat.GuildService/CreateGuild',
                request_serializer=app_dot_proto_dot_guilds__pb2.CreateGuildRequest.SerializeToString,
                response_deserializer=app_dot_proto_dot_guilds__pb2.CreateGuildResponse.FromString,
                )
        self.DeleteGuild = channel.unary_unary(
                '/huddle_chat.GuildService/DeleteGuild',
                request_serializer=app_dot_proto_dot_guilds__pb2.DeleteGuildRequest.SerializeToString,
                response_deserializer=app_dot_proto_dot_guilds__pb2.DeleteGuildResponse.FromString,
                )


class GuildServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetGuildsByUserId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateGuild(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteGuild(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GuildServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetGuildsByUserId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGuildsByUserId,
                    request_deserializer=app_dot_proto_dot_guilds__pb2.GuildsByUserIdRequest.FromString,
                    response_serializer=app_dot_proto_dot_guilds__pb2.GuildsByUserIdResponse.SerializeToString,
            ),
            'CreateGuild': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateGuild,
                    request_deserializer=app_dot_proto_dot_guilds__pb2.CreateGuildRequest.FromString,
                    response_serializer=app_dot_proto_dot_guilds__pb2.CreateGuildResponse.SerializeToString,
            ),
            'DeleteGuild': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteGuild,
                    request_deserializer=app_dot_proto_dot_guilds__pb2.DeleteGuildRequest.FromString,
                    response_serializer=app_dot_proto_dot_guilds__pb2.DeleteGuildResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'huddle_chat.GuildService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GuildService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetGuildsByUserId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/huddle_chat.GuildService/GetGuildsByUserId',
            app_dot_proto_dot_guilds__pb2.GuildsByUserIdRequest.SerializeToString,
            app_dot_proto_dot_guilds__pb2.GuildsByUserIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateGuild(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/huddle_chat.GuildService/CreateGuild',
            app_dot_proto_dot_guilds__pb2.CreateGuildRequest.SerializeToString,
            app_dot_proto_dot_guilds__pb2.CreateGuildResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteGuild(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/huddle_chat.GuildService/DeleteGuild',
            app_dot_proto_dot_guilds__pb2.DeleteGuildRequest.SerializeToString,
            app_dot_proto_dot_guilds__pb2.DeleteGuildResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
