# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/proto/users.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61pp/proto/users.proto\x12\x0bhuddle_chat\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa9\x01\n\x0cUserForLogin\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x04 \x01(\t\x12\x15\n\ronline_status\x18\x05 \x01(\x05\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08password\x18\x07 \x01(\t\"\x1d\n\x0cLoginRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"8\n\rLoginResponse\x12\'\n\x04user\x18\x01 \x01(\x0b\x32\x19.huddle_chat.UserForLogin\"D\n\x0fRegisterRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"4\n\x10RegisterResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xa8\x01\n\x0bUserService\x12J\n\x0fGetUserForLogin\x12\x19.huddle_chat.LoginRequest\x1a\x1a.huddle_chat.LoginResponse\"\x00\x12M\n\x0cRegisterUser\x12\x1c.huddle_chat.RegisterRequest\x1a\x1d.huddle_chat.RegisterResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.proto.users_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USERFORLOGIN._serialized_start=72
  _USERFORLOGIN._serialized_end=241
  _LOGINREQUEST._serialized_start=243
  _LOGINREQUEST._serialized_end=272
  _LOGINRESPONSE._serialized_start=274
  _LOGINRESPONSE._serialized_end=330
  _REGISTERREQUEST._serialized_start=332
  _REGISTERREQUEST._serialized_end=400
  _REGISTERRESPONSE._serialized_start=402
  _REGISTERRESPONSE._serialized_end=454
  _USERSERVICE._serialized_start=457
  _USERSERVICE._serialized_end=625
# @@protoc_insertion_point(module_scope)
