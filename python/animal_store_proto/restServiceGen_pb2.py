# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: animal_store_proto/restServiceGen.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_swagger.options import annotations_pb2 as protoc__gen__swagger_dot_options_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from animal_store_proto import animal_pb2 as animal__store__proto_dot_animal__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='animal_store_proto/restServiceGen.proto',
  package='animal_store_proto',
  syntax='proto3',
  serialized_pb=_b('\n\'animal_store_proto/restServiceGen.proto\x12\x12\x61nimal_store_proto\x1a\x1cgoogle/api/annotations.proto\x1a,protoc-gen-swagger/options/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1f\x61nimal_store_proto/animal.proto2\xce\x01\n\x12\x41nimalStoreService\x12\xb7\x01\n\tGetAnimal\x12\x1d.animal_store_proto.AnimalReq\x1a\x1d.animal_store_proto.AnimalRsp\"l\x92\x41G*\x06\x41nimalJ=\n\x07\x64\x65\x66\x61ult\x12\x32\n\x0e\x45rror response\x12 \n\x1e\x1a\x1c.animal_store_proto.ErrorRsp\x82\xd3\xe4\x93\x02\x1c\x12\x1a/animal-store/v1/getAnimalB\x16Z\x14./animal_store_protob\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,protoc__gen__swagger_dot_options_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,animal__store__proto_dot_animal__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\024./animal_store_proto'))

_ANIMALSTORESERVICE = _descriptor.ServiceDescriptor(
  name='AnimalStoreService',
  full_name='animal_store_proto.AnimalStoreService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=202,
  serialized_end=408,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAnimal',
    full_name='animal_store_proto.AnimalStoreService.GetAnimal',
    index=0,
    containing_service=None,
    input_type=animal__store__proto_dot_animal__pb2._ANIMALREQ,
    output_type=animal__store__proto_dot_animal__pb2._ANIMALRSP,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\222AG*\006AnimalJ=\n\007default\0222\n\016Error response\022 \n\036\032\034.animal_store_proto.ErrorRsp\202\323\344\223\002\034\022\032/animal-store/v1/getAnimal')),
  ),
])
_sym_db.RegisterServiceDescriptor(_ANIMALSTORESERVICE)

DESCRIPTOR.services_by_name['AnimalStoreService'] = _ANIMALSTORESERVICE

# @@protoc_insertion_point(module_scope)