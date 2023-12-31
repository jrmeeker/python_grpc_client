# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RfmxNrCompCarriers.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import RfmxNrBwp_pb2 as RfmxNrBwp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18RfmxNrCompCarriers.proto\x12\x10multi_site_instr\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x0fRfmxNrBwp.proto\"\xac\r\n\x0eNrCompCarriers\x12\x46\n\tAllocated\x18\x01 \x01(\x0e\x32\x33.multi_site_instr.RFmxNRMXComponentCarrierAllocated\x12/\n\tBandwidth\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12+\n\x06\x43\x65llID\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x46\n\x11\x44ownlinkTestModel\x18\x04 \x01(\x0e\x32+.multi_site_instr.RFmxNRMXDownlinkTestModel\x12^\n\x1d\x44ownlinkTestModelDuplexScheme\x18\x05 \x01(\x0e\x32\x37.multi_site_instr.RFmxNRMXDownlinkTestModelDuplexScheme\x12\x62\n\x1f\x44ownlinkTestModelModulationType\x18\x06 \x01(\x0e\x32\x39.multi_site_instr.RFmxNRMXDownlinkTestModelModulationType\x12/\n\tFrequency\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12;\n\x16NumberOfBandwidthParts\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x33\n\rPbchDmrsPower\x18\t \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12/\n\tPbchPower\x18\n \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12.\n\x08PssPower\x18\x0b \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12R\n\x0fRadioAccessType\x18\x0c \x01(\x0e\x32\x39.multi_site_instr.RFmxNRMXComponentCarrierRadioAccessType\x12/\n\tRatedEirp\x18\r \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12.\n\x08RatedTrp\x18\x0e \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x36\n\x11ReferenceGridSize\x18\x0f \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x37\n\x12ReferenceGridStart\x18\x10 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x44\n\x1eReferenceGridSubcarrierSpacing\x18\x11 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x35\n\x0fSsbActiveBlocks\x18\x12 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0cSsbCrbOffset\x18\x13 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x38\n\nSsbEnabled\x18\x14 \x01(\x0e\x32$.multi_site_instr.RFmxNRMXSsbEnabled\x12\x30\n\x0bSsbGridSize\x18\x15 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x31\n\x0cSsbGridStart\x18\x16 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x30\n\x0bSsbHrfIndex\x18\x17 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x38\n\nSsbPattern\x18\x18 \x01(\x0e\x32$.multi_site_instr.RFmxNRMXSsbPattern\x12\x34\n\x0eSsbPeriodicity\x18\x19 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x38\n\x13SsbSubcarrierOffset\x18\x1a \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12.\n\x08SssPower\x18\x1b \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12=\n\x17SubcarrierSpacingCommon\x18\x1c \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12$\n\x03\x42wp\x18\x1d \x03(\x0b\x32\x17.multi_site_instr.NrBwp*U\n!RFmxNRMXComponentCarrierAllocated\x12\x11\n\rFalse_010jduk\x10\x00\x12\x10\n\x0cTrue_010gkcl\x10\x01\x12\x0b\n\x06\x65\x66\x62ilo\x10\xf4\x03*\xe4\x01\n\x19RFmxNRMXDownlinkTestModel\x12\x11\n\rTM1_1_010hjxc\x10\x00\x12\x11\n\rTM1_2_010dqkq\x10\x01\x12\x0f\n\x0bTM2_010jwno\x10\x02\x12\x10\n\x0cTM2a_010odqw\x10\x03\x12\x11\n\rTM3_1_010fwfr\x10\x04\x12\x12\n\x0eTM3_1a_010awkl\x10\x05\x12\x11\n\rTM3_2_010pwgx\x10\x06\x12\x11\n\rTM3_3_010sbed\x10\x07\x12\x10\n\x0cTM2b_010uvlq\x10\x08\x12\x12\n\x0eTM3_1b_010mlyo\x10\t\x12\x0b\n\x06\x66tuywr\x10\xf4\x03*V\n%RFmxNRMXDownlinkTestModelDuplexScheme\x12\x0f\n\x0b\x46\x64\x64_010vyvh\x10\x00\x12\x0f\n\x0bTdd_010zect\x10\x01\x12\x0b\n\x06nkymmh\x10\xf4\x03*\x84\x01\n\'RFmxNRMXDownlinkTestModelModulationType\x12\x14\n\x10Standard_010jnyh\x10\x00\x12\x10\n\x0cQpsk_010sjut\x10\x01\x12\x11\n\rQam16_010szku\x10\x02\x12\x11\n\rQam64_010yrlh\x10\x03\x12\x0b\n\x06\x63mpxah\x10\xf4\x03*Y\n\'RFmxNRMXComponentCarrierRadioAccessType\x12\x0e\n\nNR_010bkbz\x10\x00\x12\x11\n\rEutra_010baha\x10\x01\x12\x0b\n\x06sayqes\x10\xf4\x03*F\n\x12RFmxNRMXSsbEnabled\x12\x11\n\rFalse_010vmfm\x10\x00\x12\x10\n\x0cTrue_010xbgw\x10\x01\x12\x0b\n\x06xfglhg\x10\xf4\x03*\xef\x01\n\x12RFmxNRMXSsbPattern\x12\x19\n\x15\x43\x61seAUpTo3GHz_010ilwp\x10\x00\x12\x1b\n\x17\x43\x61seA3GHzTo6GHz_010hbln\x10\x01\x12\x19\n\x15\x43\x61seBUpTo3GHz_010ftit\x10\x02\x12\x1b\n\x17\x43\x61seB3GHzTo6GHz_010mrhj\x10\x03\x12\x19\n\x15\x43\x61seCUpTo3GHz_010whmt\x10\x04\x12\x1b\n\x17\x43\x61seC3GHzTo6GHz_010lphc\x10\x05\x12\x11\n\rCaseD_010aybf\x10\x06\x12\x11\n\rCaseE_010mvsp\x10\x07\x12\x0b\n\x06sasgdi\x10\xf4\x03\x42\x12\xaa\x02\x0fOranAptRuClientb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RfmxNrCompCarriers_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\017OranAptRuClient'
  _RFMXNRMXCOMPONENTCARRIERALLOCATED._serialized_start=1806
  _RFMXNRMXCOMPONENTCARRIERALLOCATED._serialized_end=1891
  _RFMXNRMXDOWNLINKTESTMODEL._serialized_start=1894
  _RFMXNRMXDOWNLINKTESTMODEL._serialized_end=2122
  _RFMXNRMXDOWNLINKTESTMODELDUPLEXSCHEME._serialized_start=2124
  _RFMXNRMXDOWNLINKTESTMODELDUPLEXSCHEME._serialized_end=2210
  _RFMXNRMXDOWNLINKTESTMODELMODULATIONTYPE._serialized_start=2213
  _RFMXNRMXDOWNLINKTESTMODELMODULATIONTYPE._serialized_end=2345
  _RFMXNRMXCOMPONENTCARRIERRADIOACCESSTYPE._serialized_start=2347
  _RFMXNRMXCOMPONENTCARRIERRADIOACCESSTYPE._serialized_end=2436
  _RFMXNRMXSSBENABLED._serialized_start=2438
  _RFMXNRMXSSBENABLED._serialized_end=2508
  _RFMXNRMXSSBPATTERN._serialized_start=2511
  _RFMXNRMXSSBPATTERN._serialized_end=2750
  _NRCOMPCARRIERS._serialized_start=96
  _NRCOMPCARRIERS._serialized_end=1804
# @@protoc_insertion_point(module_scope)
