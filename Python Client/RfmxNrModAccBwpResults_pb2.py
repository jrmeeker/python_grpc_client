# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RfmxNrModAccBwpResults.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import ResultWrappers_pb2 as ResultWrappers__pb2
import RfmxNrModAccUserResults_pb2 as RfmxNrModAccUserResults__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cRfmxNrModAccBwpResults.proto\x12\x10multi_site_instr\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x14ResultWrappers.proto\x1a\x1dRfmxNrModAccUserResults.proto\"\xcb\x03\n\x12NrModAccBwpResults\x12>\n\x16Pdsch1024QamRmsEvmMean\x18\x01 \x01(\x0b\x32\x1e.multi_site_instr.DoubleResult\x12<\n\x14Pdsch16QamRmsEvmMean\x18\x02 \x01(\x0b\x32\x1e.multi_site_instr.DoubleResult\x12=\n\x15Pdsch256QamRmsEvmMean\x18\x03 \x01(\x0b\x32\x1e.multi_site_instr.DoubleResult\x12<\n\x14Pdsch64QamRmsEvmMean\x18\x04 \x01(\x0b\x32\x1e.multi_site_instr.DoubleResult\x12;\n\x13Pdsch8PskRmsEvmMean\x18\x05 \x01(\x0b\x32\x1e.multi_site_instr.DoubleResult\x12;\n\x13PdschQpskRmsEvmMean\x18\x06 \x01(\x0b\x32\x1e.multi_site_instr.DoubleResult\x12@\n\x11ModAccUserResults\x18\x07 \x03(\x0b\x32%.multi_site_instr.NrModAccUserResultsB\x12\xaa\x02\x0fOranAptRuClientb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RfmxNrModAccBwpResults_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\017OranAptRuClient'
  _NRMODACCBWPRESULTS._serialized_start=136
  _NRMODACCBWPRESULTS._serialized_end=595
# @@protoc_insertion_point(module_scope)