# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RfmxNrBwp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import RfmxNrUser_pb2 as RfmxNrUser__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fRfmxNrBwp.proto\x12\x10multi_site_instr\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x10RfmxNrUser.proto\"\xde\t\n\x05NrBwp\x12^\n\x1d\x42\x61ndwidthPartCyclicPrefixMode\x18\x01 \x01(\x0e\x32\x37.multi_site_instr.RFmxNRMXBandwidthPartCyclicPrefixMode\x12H\n#BandwidthPartNumberOfResourceBlocks\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x45\n BandwidthPartResourceBlockOffset\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x44\n\x1e\x42\x61ndwidthPartSubcarrierSpacing\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12X\n\x1a\x43oresetCceToRegMappingType\x18\x05 \x01(\x0e\x32\x34.multi_site_instr.RFmxNRMXCoresetCceToRegMappingType\x12;\n\x16\x43oresetInterleaverSize\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12I\n$CoresetNumberOfResourceBlockClusters\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x42\n\x1d\x43oresetNumberOfResourceBlocks\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12;\n\x16\x43oresetNumberOfSymbols\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12Z\n\x1b\x43oresetPrecodingGranularity\x18\n \x01(\x0e\x32\x35.multi_site_instr.RFmxNRMXCoresetPrecodingGranularity\x12\x39\n\x14\x43oresetRegBundleSize\x18\x0b \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x36\n\x11\x43oresetShiftIndex\x18\x0c \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x38\n\x13\x43oresetSymbolOffset\x18\r \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12-\n\x08GridSize\x18\x0e \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12.\n\tGridStart\x18\x0f \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x35\n\x10NumberOfCoresets\x18\x10 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12@\n\x1bNumberOfPdcchConfigurations\x18\x11 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x32\n\rNumberOfUsers\x18\x12 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12&\n\x04User\x18\x13 \x03(\x0b\x32\x18.multi_site_instr.NrUser*^\n%RFmxNRMXBandwidthPartCyclicPrefixMode\x12\x12\n\x0eNormal_010yhot\x10\x00\x12\x14\n\x10\x45xtended_010ykzt\x10\x01\x12\x0b\n\x06nqbzuy\x10\xf4\x03*f\n\"RFmxNRMXCoresetCceToRegMappingType\x12\x1a\n\x16NonInterleaved_010xphs\x10\x00\x12\x17\n\x13Interleaved_010yjik\x10\x01\x12\x0b\n\x06\x61\x66vvgj\x10\xf4\x03*x\n#RFmxNRMXCoresetPrecodingGranularity\x12\x1b\n\x17SameAsRegBundle_010jwgf\x10\x00\x12\'\n#AllContiguousResourceBlocks_010mfjt\x10\x01\x12\x0b\n\x06zknbeq\x10\xf4\x03\x42\x12\xaa\x02\x0fOranAptRuClientb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RfmxNrBwp_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\017OranAptRuClient'
  _RFMXNRMXBANDWIDTHPARTCYCLICPREFIXMODE._serialized_start=1336
  _RFMXNRMXBANDWIDTHPARTCYCLICPREFIXMODE._serialized_end=1430
  _RFMXNRMXCORESETCCETOREGMAPPINGTYPE._serialized_start=1432
  _RFMXNRMXCORESETCCETOREGMAPPINGTYPE._serialized_end=1534
  _RFMXNRMXCORESETPRECODINGGRANULARITY._serialized_start=1536
  _RFMXNRMXCORESETPRECODINGGRANULARITY._serialized_end=1656
  _NRBWP._serialized_start=88
  _NRBWP._serialized_end=1334
# @@protoc_insertion_point(module_scope)