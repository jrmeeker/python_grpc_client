# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RfmxNrSemSubBlock.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import RfmxNrSemOffsets_pb2 as RfmxNrSemOffsets__pb2
import RfmxNrSemCompCarriers_pb2 as RfmxNrSemCompCarriers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17RfmxNrSemSubBlock.proto\x12\x10multi_site_instr\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x16RfmxNrSemOffsets.proto\x1a\x1bRfmxNrSemCompCarriers.proto\"\xc5\x02\n\rNrSemSubBlock\x12H\n\"SubblockAggregatedChannelBandwidth\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x42\n\x1cSubblockIntegrationBandwidth\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x34\n\x0fNumberOfOffsets\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x32\n\nSemOffsets\x18\x04 \x03(\x0b\x32\x1e.multi_site_instr.NrSemOffsets\x12<\n\x0fSemCompCarriers\x18\x05 \x03(\x0b\x32#.multi_site_instr.NrSemCompCarriersB\x12\xaa\x02\x0fOranAptRuClientb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RfmxNrSemSubBlock_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\017OranAptRuClient'
  _NRSEMSUBBLOCK._serialized_start=131
  _NRSEMSUBBLOCK._serialized_end=456
# @@protoc_insertion_point(module_scope)
