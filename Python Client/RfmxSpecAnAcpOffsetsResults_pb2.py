# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RfmxSpecAnAcpOffsetsResults.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import ResultWrappers_pb2 as ResultWrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!RfmxSpecAnAcpOffsetsResults.proto\x12\x10multi_site_instr\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x14ResultWrappers.proto\"\xdb\x06\n\x17SpecAnAcpOffsetsResults\x12@\n\x18LowerOffsetAbsolutePower\x18\x01 \x01(\x0b\x32\x1e.multi_site_instr.DoubleResult\x12<\n\x14LowerOffsetFrequency\x18\x02 \x01(\x0b\x32\x1e.multi_site_instr.DoubleResult\x12K\n$LowerOffsetFrequencyReferenceCarrier\x18\x03 \x01(\x0b\x32\x1d.multi_site_instr.Int32Result\x12G\n\x1fLowerOffsetIntegrationBandwidth\x18\x04 \x01(\x0b\x32\x1e.multi_site_instr.DoubleResult\x12G\n LowerOffsetPowerReferenceCarrier\x18\x05 \x01(\x0b\x32\x1d.multi_site_instr.Int32Result\x12@\n\x18LowerOffsetRelativePower\x18\x06 \x01(\x0b\x32\x1e.multi_site_instr.DoubleResult\x12@\n\x18UpperOffsetAbsolutePower\x18\x07 \x01(\x0b\x32\x1e.multi_site_instr.DoubleResult\x12<\n\x14UpperOffsetFrequency\x18\x08 \x01(\x0b\x32\x1e.multi_site_instr.DoubleResult\x12K\n$UpperOffsetFrequencyReferenceCarrier\x18\t \x01(\x0b\x32\x1d.multi_site_instr.Int32Result\x12G\n\x1fUpperOffsetIntegrationBandwidth\x18\n \x01(\x0b\x32\x1e.multi_site_instr.DoubleResult\x12G\n UpperOffsetPowerReferenceCarrier\x18\x0b \x01(\x0b\x32\x1d.multi_site_instr.Int32Result\x12@\n\x18UpperOffsetRelativePower\x18\x0c \x01(\x0b\x32\x1e.multi_site_instr.DoubleResultB\x12\xaa\x02\x0fOranAptRuClientb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RfmxSpecAnAcpOffsetsResults_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\017OranAptRuClient'
  _SPECANACPOFFSETSRESULTS._serialized_start=110
  _SPECANACPOFFSETSRESULTS._serialized_end=969
# @@protoc_insertion_point(module_scope)
