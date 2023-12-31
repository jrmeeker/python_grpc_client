# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RfmxNr.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import RfmxPolicy_pb2 as RfmxPolicy__pb2
import RfmxInst_pb2 as RfmxInst__pb2
import RfmxNrSubBlock_pb2 as RfmxNrSubBlock__pb2
import RfmxNrChp_pb2 as RfmxNrChp__pb2
import RfmxNrAcp_pb2 as RfmxNrAcp__pb2
import RfmxNrModAcc_pb2 as RfmxNrModAcc__pb2
import RfmxNrObw_pb2 as RfmxNrObw__pb2
import RfmxNrSem_pb2 as RfmxNrSem__pb2
import RfmxNrTxp_pb2 as RfmxNrTxp__pb2
import RfmxNrPvt_pb2 as RfmxNrPvt__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cRfmxNr.proto\x12\x10multi_site_instr\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x10RfmxPolicy.proto\x1a\x0eRfmxInst.proto\x1a\x14RfmxNrSubBlock.proto\x1a\x0fRfmxNrChp.proto\x1a\x0fRfmxNrAcp.proto\x1a\x12RfmxNrModAcc.proto\x1a\x0fRfmxNrObw.proto\x1a\x0fRfmxNrSem.proto\x1a\x0fRfmxNrTxp.proto\x1a\x0fRfmxNrPvt.proto\"\xdc\x16\n\x02Nr\x12r\n\'AcquisitionBandwidthOptimizationEnabled\x18\x01 \x01(\x0e\x32\x41.multi_site_instr.RFmxNRMXAcquisitionBandwidthOptimizationEnabled\x12X\n\x1a\x41utoCellIDDetectionEnabled\x18\x02 \x01(\x0e\x32\x34.multi_site_instr.RFmxNRMXAutoCellIDDetectionEnabled\x12X\n\x1a\x41utoIncrementCellIDEnabled\x18\x03 \x01(\x0e\x32\x34.multi_site_instr.RFmxNRMXAutoIncrementCellIDEnabled\x12\x66\n!AutoResourceBlockDetectionEnabled\x18\x04 \x01(\x0e\x32;.multi_site_instr.RFmxNRMXAutoResourceBlockDetectionEnabled\x12\x35\n\x0f\x43\x65nterFrequency\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12P\n\x16\x44igitalEdgeTriggerEdge\x18\x06 \x01(\x0e\x32\x30.multi_site_instr.RFmxNRMXDigitalEdgeTriggerEdge\x12>\n\x18\x44igitalEdgeTriggerSource\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x64\n DownlinkChannelConfigurationMode\x18\x08 \x01(\x0e\x32:.multi_site_instr.RFmxNRMXDownlinkChannelConfigurationMode\x12Z\n\x1b\x44ownlinkTestModelCellIDMode\x18\t \x01(\x0e\x32\x35.multi_site_instr.RFmxNRMXDownlinkTestModelCellIDMode\x12\x39\n\x13\x45xternalAttenuation\x18\n \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12@\n\x0egNodeBCategory\x18\x0b \x01(\x0e\x32(.multi_site_instr.RFmxNRMXgNodeBCategory\x12\x38\n\ngNodeBType\x18\x0c \x01(\x0e\x32$.multi_site_instr.RFmxNRMXgNodeBType\x12<\n\x0cGridSizeMode\x18\r \x01(\x0e\x32&.multi_site_instr.RFmxNRMXGridSizeMode\x12=\n\x17IQPowerEdgeTriggerLevel\x18\x0e \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12Z\n\x1bIQPowerEdgeTriggerLevelType\x18\x0f \x01(\x0e\x32\x35.multi_site_instr.RFmxNRMXIQPowerEdgeTriggerLevelType\x12R\n\x17IQPowerEdgeTriggerSlope\x18\x10 \x01(\x0e\x32\x31.multi_site_instr.RFmxNRMXIQPowerEdgeTriggerSlope\x12>\n\x18IQPowerEdgeTriggerSource\x18\x11 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12X\n\x1aLimitedConfigurationChange\x18\x12 \x01(\x0e\x32\x34.multi_site_instr.RFmxNRMXLimitedConfigurationChange\x12>\n\rLinkDirection\x18\x13 \x01(\x0e\x32\'.multi_site_instr.RFmxNRMXLinkDirection\x12\x36\n\x11NumberOfSubblocks\x18\x14 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x46\n\x11PhaseCompensation\x18\x15 \x01(\x0e\x32+.multi_site_instr.RFmxNRMXPhaseCompensation\x12X\n\x1aPiBy2BpskPowerBoostEnabled\x18\x16 \x01(\x0e\x32\x34.multi_site_instr.RFmxNRMXPiBy2BpskPowerBoostEnabled\x12/\n\nPowerClass\x18\x17 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12X\n\x1aReferenceGridAlignmentMode\x18\x18 \x01(\x0e\x32\x34.multi_site_instr.RFmxNRMXReferenceGridAlignmentMode\x12\x34\n\x0eReferenceLevel\x18\x19 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12<\n\x16ReferenceLevelHeadroom\x18\x1a \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x38\n\x12ResultFetchTimeout\x18\x1b \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x33\n\rSelectedPorts\x18\x1c \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12=\n\x18TransmitAntennaToAnalyze\x18\x1d \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12R\n\x17TransmitterArchitecture\x18\x1e \x01(\x0e\x32\x31.multi_site_instr.RFmxNRMXTransmitterArchitecture\x12\x32\n\x0cTriggerDelay\x18\x1f \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x45\n\x1fTriggerMinimumQuietTimeDuration\x18  \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12Z\n\x1bTriggerMinimumQuietTimeMode\x18! \x01(\x0e\x32\x35.multi_site_instr.RFmxNRMXTriggerMinimumQuietTimeMode\x12:\n\x0bTriggerType\x18\" \x01(\x0e\x32%.multi_site_instr.RFmxNRMXTriggerType\x12(\n\x06Policy\x18# \x01(\x0b\x32\x18.multi_site_instr.Policy\x12%\n\x05Instr\x18$ \x01(\x0b\x32\x16.multi_site_instr.Inst\x12.\n\x08SubBlock\x18% \x03(\x0b\x32\x1c.multi_site_instr.NrSubBlock\x12$\n\x03\x43hp\x18& \x01(\x0b\x32\x17.multi_site_instr.NrChp\x12$\n\x03\x41\x63p\x18\' \x01(\x0b\x32\x17.multi_site_instr.NrAcp\x12*\n\x06ModAcc\x18( \x01(\x0b\x32\x1a.multi_site_instr.NrModAcc\x12$\n\x03Obw\x18) \x01(\x0b\x32\x17.multi_site_instr.NrObw\x12$\n\x03Sem\x18* \x01(\x0b\x32\x17.multi_site_instr.NrSem\x12$\n\x03Txp\x18+ \x01(\x0b\x32\x17.multi_site_instr.NrTxp\x12$\n\x03Pvt\x18, \x01(\x0b\x32\x17.multi_site_instr.NrPvt*c\n/RFmxNRMXAcquisitionBandwidthOptimizationEnabled\x12\x11\n\rFalse_010qymm\x10\x00\x12\x10\n\x0cTrue_010fwzb\x10\x01\x12\x0b\n\x06rqciko\x10\xf4\x03*V\n\"RFmxNRMXAutoCellIDDetectionEnabled\x12\x11\n\rFalse_010lnpq\x10\x00\x12\x10\n\x0cTrue_010drls\x10\x01\x12\x0b\n\x06rplbuq\x10\xf4\x03*V\n\"RFmxNRMXAutoIncrementCellIDEnabled\x12\x11\n\rFalse_010teth\x10\x00\x12\x10\n\x0cTrue_010nmat\x10\x01\x12\x0b\n\x06nvxfaa\x10\xf4\x03*]\n)RFmxNRMXAutoResourceBlockDetectionEnabled\x12\x11\n\rFalse_010tdxa\x10\x00\x12\x10\n\x0cTrue_010cvbt\x10\x01\x12\x0b\n\x06\x64mltox\x10\xf4\x03*V\n\x1eRFmxNRMXDigitalEdgeTriggerEdge\x12\x12\n\x0eRising_010gxad\x10\x00\x12\x13\n\x0f\x46\x61lling_010ciin\x10\x01\x12\x0b\n\x06xuvxnr\x10\xf4\x03*s\n(RFmxNRMXDownlinkChannelConfigurationMode\x12\n\n\x06ztsxql\x10\x00\x12\x17\n\x13UserDefined_010zorl\x10\x01\x12\x15\n\x11TestModel_010zyoz\x10\x02\x12\x0b\n\x06\x61gvtyc\x10\xf4\x03*X\n#RFmxNRMXDownlinkTestModelCellIDMode\x12\x10\n\x0c\x41uto_010nqvt\x10\x00\x12\x12\n\x0eManual_010drrf\x10\x01\x12\x0b\n\x06\x66\x63\x66\x66ik\x10\xf4\x03*\xab\x02\n\x16RFmxNRMXgNodeBCategory\x12(\n$WideAreaBaseStationCategoryA_010tktn\x10\x00\x12/\n+WideAreaBaseStationCategoryBOption1_010cdys\x10\x01\x12/\n+WideAreaBaseStationCategoryBOption2_010fped\x10\x02\x12 \n\x1cLocalAreaBaseStation_010timr\x10\x03\x12\"\n\x1eMediumRangeBaseStation_010zbzl\x10\x05\x12\x18\n\x14\x46R2CategoryA_010ejxy\x10\x06\x12\x18\n\x14\x46R2CategoryB_010uztt\x10\x07\x12\x0b\n\x06ipfuqe\x10\xf4\x03*q\n\x12RFmxNRMXgNodeBType\x12\x12\n\x0eType1C_010gqmh\x10\x00\x12\x12\n\x0eType1H_010rvev\x10\x01\x12\x12\n\x0eType1O_010lgpz\x10\x02\x12\x12\n\x0eType2O_010xjso\x10\x03\x12\x0b\n\x06\x64\x64\x66xfk\x10\xf4\x03*I\n\x14RFmxNRMXGridSizeMode\x12\x12\n\x0eManual_010mutd\x10\x00\x12\x10\n\x0c\x41uto_010jejq\x10\x01\x12\x0b\n\x06jknpcw\x10\xf4\x03*^\n#RFmxNRMXIQPowerEdgeTriggerLevelType\x12\x14\n\x10Relative_010eskd\x10\x00\x12\x14\n\x10\x41\x62solute_010gjyr\x10\x01\x12\x0b\n\x06jvbkau\x10\xf4\x03*W\n\x1fRFmxNRMXIQPowerEdgeTriggerSlope\x12\x12\n\x0eRising_010lcot\x10\x00\x12\x13\n\x0f\x46\x61lling_010zwer\x10\x01\x12\x0b\n\x06onlzmu\x10\xf4\x03*\xed\x01\n\"RFmxNRMXLimitedConfigurationChange\x12\x14\n\x10\x44isabled_010xfli\x10\x00\x12\x14\n\x10NoChange_010hwjl\x10\x01\x12\x15\n\x11\x46requency_010scqw\x10\x02\x12\x1a\n\x16ReferenceLevel_010lvly\x10\x03\x12&\n\"FrequencyAndReferenceLevel_010czeo\x10\x04\x12\x33\n/SelectedPortsFrequencyAndReferenceLevel_010egvu\x10\x05\x12\x0b\n\x06qfsmdx\x10\xf4\x03*N\n\x15RFmxNRMXLinkDirection\x12\x14\n\x10\x44ownlink_010shxd\x10\x00\x12\x12\n\x0eUplink_010tejs\x10\x01\x12\x0b\n\x06\x63\x64lakm\x10\xf4\x03*i\n\x19RFmxNRMXPhaseCompensation\x12\x14\n\x10\x44isabled_010cckj\x10\x00\x12\x10\n\x0c\x41uto_010gqlm\x10\x01\x12\x17\n\x13UserDefined_010vxqq\x10\x02\x12\x0b\n\x06jrsbew\x10\xf4\x03*V\n\"RFmxNRMXPiBy2BpskPowerBoostEnabled\x12\x11\n\rFalse_010hvjj\x10\x00\x12\x10\n\x0cTrue_010zhbh\x10\x01\x12\x0b\n\x06ojwacd\x10\xf4\x03*W\n\"RFmxNRMXReferenceGridAlignmentMode\x12\x12\n\x0eManual_010wjrn\x10\x00\x12\x10\n\x0c\x41uto_010vjgn\x10\x01\x12\x0b\n\x06lfmznc\x10\xf4\x03*l\n\x1fRFmxNRMXTransmitterArchitecture\x12!\n\x1dLOPerComponentCarrier_010urzb\x10\x00\x12\x19\n\x15LOPerSubblock_010zptp\x10\x01\x12\x0b\n\x06\x63tddhy\x10\xf4\x03*X\n#RFmxNRMXTriggerMinimumQuietTimeMode\x12\x12\n\x0eManual_010bbqu\x10\x00\x12\x10\n\x0c\x41uto_010umua\x10\x01\x12\x0b\n\x06\x61\x66gvpt\x10\xf4\x03*|\n\x13RFmxNRMXTriggerType\x12\x10\n\x0cNone_010jewa\x10\x00\x12\x17\n\x13\x44igitalEdge_010uymx\x10\x01\x12\x17\n\x13IQPowerEdge_010juan\x10\x02\x12\x14\n\x10Software_010khgx\x10\x03\x12\x0b\n\x06krbhmk\x10\xf4\x03\x42\x12\xaa\x02\x0fOranAptRuClientb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RfmxNr_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\017OranAptRuClient'
  _RFMXNRMXACQUISITIONBANDWIDTHOPTIMIZATIONENABLED._serialized_start=3155
  _RFMXNRMXACQUISITIONBANDWIDTHOPTIMIZATIONENABLED._serialized_end=3254
  _RFMXNRMXAUTOCELLIDDETECTIONENABLED._serialized_start=3256
  _RFMXNRMXAUTOCELLIDDETECTIONENABLED._serialized_end=3342
  _RFMXNRMXAUTOINCREMENTCELLIDENABLED._serialized_start=3344
  _RFMXNRMXAUTOINCREMENTCELLIDENABLED._serialized_end=3430
  _RFMXNRMXAUTORESOURCEBLOCKDETECTIONENABLED._serialized_start=3432
  _RFMXNRMXAUTORESOURCEBLOCKDETECTIONENABLED._serialized_end=3525
  _RFMXNRMXDIGITALEDGETRIGGEREDGE._serialized_start=3527
  _RFMXNRMXDIGITALEDGETRIGGEREDGE._serialized_end=3613
  _RFMXNRMXDOWNLINKCHANNELCONFIGURATIONMODE._serialized_start=3615
  _RFMXNRMXDOWNLINKCHANNELCONFIGURATIONMODE._serialized_end=3730
  _RFMXNRMXDOWNLINKTESTMODELCELLIDMODE._serialized_start=3732
  _RFMXNRMXDOWNLINKTESTMODELCELLIDMODE._serialized_end=3820
  _RFMXNRMXGNODEBCATEGORY._serialized_start=3823
  _RFMXNRMXGNODEBCATEGORY._serialized_end=4122
  _RFMXNRMXGNODEBTYPE._serialized_start=4124
  _RFMXNRMXGNODEBTYPE._serialized_end=4237
  _RFMXNRMXGRIDSIZEMODE._serialized_start=4239
  _RFMXNRMXGRIDSIZEMODE._serialized_end=4312
  _RFMXNRMXIQPOWEREDGETRIGGERLEVELTYPE._serialized_start=4314
  _RFMXNRMXIQPOWEREDGETRIGGERLEVELTYPE._serialized_end=4408
  _RFMXNRMXIQPOWEREDGETRIGGERSLOPE._serialized_start=4410
  _RFMXNRMXIQPOWEREDGETRIGGERSLOPE._serialized_end=4497
  _RFMXNRMXLIMITEDCONFIGURATIONCHANGE._serialized_start=4500
  _RFMXNRMXLIMITEDCONFIGURATIONCHANGE._serialized_end=4737
  _RFMXNRMXLINKDIRECTION._serialized_start=4739
  _RFMXNRMXLINKDIRECTION._serialized_end=4817
  _RFMXNRMXPHASECOMPENSATION._serialized_start=4819
  _RFMXNRMXPHASECOMPENSATION._serialized_end=4924
  _RFMXNRMXPIBY2BPSKPOWERBOOSTENABLED._serialized_start=4926
  _RFMXNRMXPIBY2BPSKPOWERBOOSTENABLED._serialized_end=5012
  _RFMXNRMXREFERENCEGRIDALIGNMENTMODE._serialized_start=5014
  _RFMXNRMXREFERENCEGRIDALIGNMENTMODE._serialized_end=5101
  _RFMXNRMXTRANSMITTERARCHITECTURE._serialized_start=5103
  _RFMXNRMXTRANSMITTERARCHITECTURE._serialized_end=5211
  _RFMXNRMXTRIGGERMINIMUMQUIETTIMEMODE._serialized_start=5213
  _RFMXNRMXTRIGGERMINIMUMQUIETTIMEMODE._serialized_end=5301
  _RFMXNRMXTRIGGERTYPE._serialized_start=5303
  _RFMXNRMXTRIGGERTYPE._serialized_end=5427
  _NR._serialized_start=245
  _NR._serialized_end=3153
# @@protoc_insertion_point(module_scope)
