# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ResultWrappers.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14ResultWrappers.proto\x12\x10multi_site_instr\x1a\x1egoogle/protobuf/wrappers.proto\"S\n\x0c\x44oubleResult\x12\x16\n\x0erequest_result\x18\x01 \x01(\x08\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\"Q\n\x0b\x46loatResult\x12\x16\n\x0erequest_result\x18\x01 \x01(\x08\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"Q\n\x0bInt32Result\x12\x16\n\x0erequest_result\x18\x01 \x01(\x08\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\"O\n\nBoolResult\x12\x16\n\x0erequest_result\x18\x01 \x01(\x08\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"S\n\x0cStringResult\x12\x16\n\x0erequest_result\x18\x01 \x01(\x08\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x10\xaa\x02\rResultWrapperb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ResultWrappers_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\rResultWrapper'
  _DOUBLERESULT._serialized_start=74
  _DOUBLERESULT._serialized_end=157
  _FLOATRESULT._serialized_start=159
  _FLOATRESULT._serialized_end=240
  _INT32RESULT._serialized_start=242
  _INT32RESULT._serialized_end=323
  _BOOLRESULT._serialized_start=325
  _BOOLRESULT._serialized_end=404
  _STRINGRESULT._serialized_start=406
  _STRINGRESULT._serialized_end=489
# @@protoc_insertion_point(module_scope)
