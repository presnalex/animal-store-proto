# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: animal_store_proto/common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='animal_store_proto/common.proto',
  package='animal_store_proto',
  syntax='proto3',
  serialized_pb=_b('\n\x1f\x61nimal_store_proto/common.proto\x12\x12\x61nimal_store_proto\x1a\x1egoogle/protobuf/wrappers.proto\";\n\x08\x45rrorRsp\x12/\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x19.animal_store_proto.ErrorR\x05\x65rror\"_\n\x05\x45rror\x12\x12\n\x04\x63ode\x18\x01 \x01(\tR\x04\x63ode\x12\x14\n\x05title\x18\x02 \x01(\tR\x05title\x12\x12\n\x04uuid\x18\x03 \x01(\tR\x04uuid\x12\x18\n\x07\x64\x65tails\x18\x04 \x01(\tR\x07\x64\x65tailsB\x16Z\x14./animal_store_protob\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_ERRORRSP = _descriptor.Descriptor(
  name='ErrorRsp',
  full_name='animal_store_proto.ErrorRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='animal_store_proto.ErrorRsp.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='error', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=146,
)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='animal_store_proto.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='animal_store_proto.Error.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='code', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='animal_store_proto.Error.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='title', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='animal_store_proto.Error.uuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='uuid', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='details', full_name='animal_store_proto.Error.details', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='details', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=243,
)

_ERRORRSP.fields_by_name['error'].message_type = _ERROR
DESCRIPTOR.message_types_by_name['ErrorRsp'] = _ERRORRSP
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ErrorRsp = _reflection.GeneratedProtocolMessageType('ErrorRsp', (_message.Message,), dict(
  DESCRIPTOR = _ERRORRSP,
  __module__ = 'animal_store_proto.common_pb2'
  # @@protoc_insertion_point(class_scope:animal_store_proto.ErrorRsp)
  ))
_sym_db.RegisterMessage(ErrorRsp)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), dict(
  DESCRIPTOR = _ERROR,
  __module__ = 'animal_store_proto.common_pb2'
  # @@protoc_insertion_point(class_scope:animal_store_proto.Error)
  ))
_sym_db.RegisterMessage(Error)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\024./animal_store_proto'))
# @@protoc_insertion_point(module_scope)
