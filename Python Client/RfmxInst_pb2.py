# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RfmxInst.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eRfmxInst.proto\x12\x10multi_site_instr\x1a\x1egoogle/protobuf/wrappers.proto\"\x84%\n\x04Inst\x12\x45\n\x1f\x41\x64vanceTriggerDigitalEdgeSource\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12H\n\"AdvanceTriggerExportOutputTerminal\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12K\n\x12\x41\x64vanceTriggerType\x18\x03 \x01(\x0e\x32/.multi_site_instr.RFmxInstrMXAdvanceTriggerType\x12\x37\n\x11\x41mplitudeSettling\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12Q\n\x15\x41utomaticSGSASharedLO\x18\x05 \x01(\x0e\x32\x32.multi_site_instr.RFmxInstrMXAutomaticSGSASharedLO\x12\x45\n\x0f\x43hannelCoupling\x18\x06 \x01(\x0e\x32,.multi_site_instr.RFmxInstrMXChannelCoupling\x12\x45\n\x0f\x43leanerSpectrum\x18\x07 \x01(\x0e\x32,.multi_site_instr.RFmxInstrMXCleanerSpectrum\x12\x35\n\x0f\x43ommonModeLevel\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12Y\n\x19\x44\x65viceSynchronizationMode\x18\t \x01(\x0e\x32\x36.multi_site_instr.RFmxInstrMXDeviceSynchronizationMode\x12S\n\x16\x44igitizerDitherEnabled\x18\n \x01(\x0e\x32\x33.multi_site_instr.RFmxInstrMXDigitizerDitherEnabled\x12=\n\x17\x44oneEventOutputTerminal\x18\x0b \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x42\n\x1c\x44ownconverterCenterFrequency\x18\x0c \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x42\n\x1c\x44ownconverterFrequencyOffset\x18\r \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x65\n\x1f\x44ownconverterPreselectorEnabled\x18\x0e \x01(\x0e\x32<.multi_site_instr.RFmxInstrMXDownconverterPreselectorEnabled\x12\x44\n\x1e\x45ndOfRecordEventOutputTerminal\x18\x0f \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08\x46\x66tWidth\x18\x10 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x39\n\x15\x46orceAllTracesEnabled\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12H\n\"FrequencyReferenceExportedTerminal\x18\x12 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x41\n\x1b\x46requencyReferenceFrequency\x18\x13 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12>\n\x18\x46requencyReferenceSource\x18\x14 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x11\x46requencySettling\x18\x15 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12S\n\x16\x46requencySettlingUnits\x18\x16 \x01(\x0e\x32\x33.multi_site_instr.RFmxInstrMXFrequencySettlingUnits\x12\x37\n\x11IFFilterBandwidth\x18\x17 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12>\n\x18IFOutputPowerLevelOffset\x18\x18 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12Q\n\x15InputIsolationEnabled\x18\x19 \x01(\x0e\x32\x32.multi_site_instr.RFmxInstrMXInputIsolationEnabled\x12\x37\n\x11IQFrequencyOffset\x18\x1a \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12G\n\x10LO2ExportEnabled\x18\x1b \x01(\x0e\x32-.multi_site_instr.RFmxInstrMXLO2ExportEnabled\x12\x33\n\x0fLOExportEnabled\x18\x1c \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x31\n\x0bLOFrequency\x18\x1d \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x39\n\x13LOFrequencyStepSize\x18\x1e \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x45\n\x0fLOInjectionSide\x18\x1f \x01(\x0e\x32,.multi_site_instr.RFmxInstrMXLOInjectionSide\x12/\n\tLOInPower\x18  \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12Y\n\x19LOLeakageAvoidanceEnabled\x18! \x01(\x0e\x32\x36.multi_site_instr.RFmxInstrMXLOLeakageAvoidanceEnabled\x12\x30\n\nLOOutPower\x18\" \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12M\n\x13LOPllFractionalMode\x18# \x01(\x0e\x32\x30.multi_site_instr.RFmxInstrMXLOPllFractionalMode\x12\x41\n\rLOSharingMode\x18$ \x01(\x0e\x32*.multi_site_instr.RFmxInstrMXLOSharingMode\x12.\n\x08LOSource\x18% \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12<\n\x16LOVcoFrequencyStepSize\x18& \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12Y\n\x19MechanicalAttenuationAuto\x18\' \x01(\x0e\x32\x36.multi_site_instr.RFmxInstrMXMechanicalAttenuationAuto\x12@\n\x1aMechanicalAttenuationValue\x18( \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x30\n\nMixerLevel\x18) \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x36\n\x10MixerLevelOffset\x18* \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12<\n\x17NumberOfLOSharingGroups\x18+ \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x63\n\x1eOptimizePathForSignalBandwidth\x18, \x01(\x0e\x32;.multi_site_instr.RFmxInstrMXOptimizePathForSignalBandwidth\x12\x45\n\x0fOspDelayEnabled\x18- \x01(\x0e\x32,.multi_site_instr.RFmxInstrMXOspDelayEnabled\x12S\n\x16OverflowErrorReporting\x18. \x01(\x0e\x32\x33.multi_site_instr.RFmxInstrMXOverflowErrorReporting\x12\x31\n\x0bPhaseOffset\x18/ \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x41\n\rPreampEnabled\x18\x30 \x01(\x0e\x32*.multi_site_instr.RFmxInstrMXPreampEnabled\x12H\n\"ReadyForAdvanceEventOutputTerminal\x18\x31 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12J\n$ReadyForReferenceEventOutputTerminal\x18\x32 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x46\n ReadyForStartEventOutputTerminal\x18\x33 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12I\n\x11RFAttenuationAuto\x18\x34 \x01(\x0e\x32..multi_site_instr.RFmxInstrMXRFAttenuationAuto\x12;\n\x15RFAttenuationStepSize\x18\x35 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x38\n\x12RFAttenuationValue\x18\x36 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12?\n\x19RFHighpassFilterFrequency\x18\x37 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12_\n\x1cSelfCalibrationValidityCheck\x18\x38 \x01(\x0e\x32\x39.multi_site_instr.RFmxInstrMXSelfCalibrationValidityCheck\x12N\n(SelfCalibrationValidityCheckTimeInterval\x18\x39 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x30\n\nSmuChannel\x18: \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0fSmuResourceName\x18; \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12U\n\x17StartTriggerDigitalEdge\x18< \x01(\x0e\x32\x34.multi_site_instr.RFmxInstrMXStartTriggerDigitalEdge\x12\x43\n\x1dStartTriggerDigitalEdgeSource\x18= \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x46\n StartTriggerExportOutputTerminal\x18> \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12G\n\x10StartTriggerType\x18? \x01(\x0e\x32-.multi_site_instr.RFmxInstrMXStartTriggerType\x12\x34\n\x0eSubSpanOverlap\x18@ \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12=\n\x17TemperatureReadInterval\x18\x41 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x44\n\x1eThermalCorrectionHeadroomRange\x18\x42 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12L\n&ThermalCorrectionTemperatureResolution\x18\x43 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x41\n\x1bTriggerExportOutputTerminal\x18\x44 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12=\n\x0bTuningSpeed\x18\x45 \x01(\x0e\x32(.multi_site_instr.RFmxInstrMXTuningSpeed*m\n\x1dRFmxInstrMXAdvanceTriggerType\x12\x10\n\x0cNone_010zpgq\x10\x00\x12\x17\n\x13\x44igitalEdge_010uifd\x10\x01\x12\x14\n\x10Software_010hzkx\x10\x03\x12\x0b\n\x06lxtfdq\x10\xf4\x03*Z\n RFmxInstrMXAutomaticSGSASharedLO\x12\x14\n\x10\x44isabled_010ezpa\x10\x00\x12\x13\n\x0f\x45nabled_010lzcn\x10\x01\x12\x0b\n\x06vdwuwj\x10\xf4\x03*W\n\x1aRFmxInstrMXChannelCoupling\x12\x15\n\x11\x41\x43\x43oupled_010iydc\x10\x00\x12\x15\n\x11\x44\x43\x43oupled_010uvsz\x10\x01\x12\x0b\n\x06\x65synrr\x10\xf4\x03*T\n\x1aRFmxInstrMXCleanerSpectrum\x12\x14\n\x10\x44isabled_010yodw\x10\x00\x12\x13\n\x0f\x45nabled_010dqiy\x10\x01\x12\x0b\n\x06\x65yehnh\x10\xf4\x03*p\n$RFmxInstrMXDeviceSynchronizationMode\x12\x1a\n\x16TriggerSharing_010mbhn\x10\x00\x12\x1f\n\x1bTClkSynchronization_010cbpn\x10\x01\x12\x0b\n\x06urkhye\x10\xf4\x03*[\n!RFmxInstrMXDigitizerDitherEnabled\x12\x14\n\x10\x44isabled_010vwcx\x10\x00\x12\x13\n\x0f\x45nabled_010hlpg\x10\x01\x12\x0b\n\x06\x61\x61rgaj\x10\xf4\x03*d\n*RFmxInstrMXDownconverterPreselectorEnabled\x12\x14\n\x10\x44isabled_010teyn\x10\x00\x12\x13\n\x0f\x45nabled_010ilnd\x10\x01\x12\x0b\n\x06llkpcl\x10\xf4\x03*{\n!RFmxInstrMXFrequencySettlingUnits\x12\x0f\n\x0bPpm_010ummv\x10\x00\x12\x1c\n\x18SecondsAfterLock_010sddh\x10\x01\x12\x1a\n\x16SecondsAfterIO_010wgzc\x10\x02\x12\x0b\n\x06sgagvw\x10\xf4\x03*Z\n RFmxInstrMXInputIsolationEnabled\x12\x14\n\x10\x44isabled_010bftp\x10\x00\x12\x13\n\x0f\x45nabled_010swzm\x10\x01\x12\x0b\n\x06rrlqns\x10\xf4\x03*U\n\x1bRFmxInstrMXLO2ExportEnabled\x12\x14\n\x10\x44isabled_010ielo\x10\x00\x12\x13\n\x0f\x45nabled_010nvnw\x10\x01\x12\x0b\n\x06gmhrng\x10\xf4\x03*T\n\x1aRFmxInstrMXLOInjectionSide\x12\x14\n\x10HighSide_010tgce\x10\x00\x12\x13\n\x0fLowSide_010pnow\x10\x01\x12\x0b\n\x06retpwf\x10\xf4\x03*X\n$RFmxInstrMXLOLeakageAvoidanceEnabled\x12\x11\n\rFalse_010mlvg\x10\x00\x12\x10\n\x0cTrue_010shto\x10\x01\x12\x0b\n\x06umtaje\x10\xf4\x03*X\n\x1eRFmxInstrMXLOPllFractionalMode\x12\x14\n\x10\x44isabled_010zhib\x10\x00\x12\x13\n\x0f\x45nabled_010jttk\x10\x01\x12\x0b\n\x06phaadl\x10\xf4\x03*\xaf\x01\n\x18RFmxInstrMXLOSharingMode\x12\x14\n\x10\x44isabled_010mguy\x10\x00\x12\x17\n\x13OnboardStar_010zhkv\x10\x01\x12\x1d\n\x19OnboardDaisyChain_010qbyg\x10\x02\x12\x18\n\x14\x45xternalStar_010mflp\x10\x03\x12\x1e\n\x1a\x45xternalDaisyChain_010lpdk\x10\x04\x12\x0b\n\x06xkwsgc\x10\xf4\x03*X\n$RFmxInstrMXMechanicalAttenuationAuto\x12\x11\n\rFalse_010mbvo\x10\x00\x12\x10\n\x0cTrue_010fseh\x10\x01\x12\x0b\n\x06\x62osuac\x10\xf4\x03*z\n)RFmxInstrMXOptimizePathForSignalBandwidth\x12\x14\n\x10\x44isabled_010tdrh\x10\x00\x12\x13\n\x0f\x45nabled_010ccgo\x10\x01\x12\x15\n\x11\x41utomatic_010zzwk\x10\x02\x12\x0b\n\x06wtnbjc\x10\xf4\x03*T\n\x1aRFmxInstrMXOspDelayEnabled\x12\x14\n\x10\x44isabled_010swuj\x10\x00\x12\x13\n\x0f\x45nabled_010zbvg\x10\x01\x12\x0b\n\x06\x63\x66\x64xxq\x10\xf4\x03*[\n!RFmxInstrMXOverflowErrorReporting\x12\x13\n\x0fWarning_010pbqt\x10\x00\x12\x14\n\x10\x44isabled_010tppd\x10\x01\x12\x0b\n\x06wxcwru\x10\xf4\x03*i\n\x18RFmxInstrMXPreampEnabled\x12\x14\n\x10\x44isabled_010wkua\x10\x00\x12\x13\n\x0f\x45nabled_010epcd\x10\x01\x12\x15\n\x11\x41utomatic_010hkep\x10\x03\x12\x0b\n\x06mwablb\x10\xf4\x03*P\n\x1cRFmxInstrMXRFAttenuationAuto\x12\x11\n\rFalse_010cfvv\x10\x00\x12\x10\n\x0cTrue_010ctiu\x10\x01\x12\x0b\n\x06moaxhd\x10\xf4\x03*\\\n\'RFmxInstrMXSelfCalibrationValidityCheck\x12\x0f\n\x0bOff_010kakr\x10\x00\x12\x13\n\x0f\x45nabled_010ldsi\x10\x01\x12\x0b\n\x06nltgpd\x10\xf4\x03*Z\n\"RFmxInstrMXStartTriggerDigitalEdge\x12\x12\n\x0eRising_010dtcv\x10\x00\x12\x13\n\x0f\x46\x61lling_010matm\x10\x01\x12\x0b\n\x06zaharj\x10\xf4\x03*k\n\x1bRFmxInstrMXStartTriggerType\x12\x10\n\x0cNone_010codk\x10\x00\x12\x17\n\x13\x44igitalEdge_010dbfl\x10\x01\x12\x14\n\x10Software_010mjqi\x10\x03\x12\x0b\n\x06iurjbw\x10\xf4\x03*_\n\x16RFmxInstrMXTuningSpeed\x12\x12\n\x0eNormal_010eert\x10\x00\x12\x12\n\x0eMedium_010lelg\x10\x01\x12\x10\n\x0c\x46\x61st_010jybj\x10\x02\x12\x0b\n\x06jkljfz\x10\xf4\x03\x42\x12\xaa\x02\x0fOranAptRuClientb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RfmxInst_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\017OranAptRuClient'
  _RFMXINSTRMXADVANCETRIGGERTYPE._serialized_start=4811
  _RFMXINSTRMXADVANCETRIGGERTYPE._serialized_end=4920
  _RFMXINSTRMXAUTOMATICSGSASHAREDLO._serialized_start=4922
  _RFMXINSTRMXAUTOMATICSGSASHAREDLO._serialized_end=5012
  _RFMXINSTRMXCHANNELCOUPLING._serialized_start=5014
  _RFMXINSTRMXCHANNELCOUPLING._serialized_end=5101
  _RFMXINSTRMXCLEANERSPECTRUM._serialized_start=5103
  _RFMXINSTRMXCLEANERSPECTRUM._serialized_end=5187
  _RFMXINSTRMXDEVICESYNCHRONIZATIONMODE._serialized_start=5189
  _RFMXINSTRMXDEVICESYNCHRONIZATIONMODE._serialized_end=5301
  _RFMXINSTRMXDIGITIZERDITHERENABLED._serialized_start=5303
  _RFMXINSTRMXDIGITIZERDITHERENABLED._serialized_end=5394
  _RFMXINSTRMXDOWNCONVERTERPRESELECTORENABLED._serialized_start=5396
  _RFMXINSTRMXDOWNCONVERTERPRESELECTORENABLED._serialized_end=5496
  _RFMXINSTRMXFREQUENCYSETTLINGUNITS._serialized_start=5498
  _RFMXINSTRMXFREQUENCYSETTLINGUNITS._serialized_end=5621
  _RFMXINSTRMXINPUTISOLATIONENABLED._serialized_start=5623
  _RFMXINSTRMXINPUTISOLATIONENABLED._serialized_end=5713
  _RFMXINSTRMXLO2EXPORTENABLED._serialized_start=5715
  _RFMXINSTRMXLO2EXPORTENABLED._serialized_end=5800
  _RFMXINSTRMXLOINJECTIONSIDE._serialized_start=5802
  _RFMXINSTRMXLOINJECTIONSIDE._serialized_end=5886
  _RFMXINSTRMXLOLEAKAGEAVOIDANCEENABLED._serialized_start=5888
  _RFMXINSTRMXLOLEAKAGEAVOIDANCEENABLED._serialized_end=5976
  _RFMXINSTRMXLOPLLFRACTIONALMODE._serialized_start=5978
  _RFMXINSTRMXLOPLLFRACTIONALMODE._serialized_end=6066
  _RFMXINSTRMXLOSHARINGMODE._serialized_start=6069
  _RFMXINSTRMXLOSHARINGMODE._serialized_end=6244
  _RFMXINSTRMXMECHANICALATTENUATIONAUTO._serialized_start=6246
  _RFMXINSTRMXMECHANICALATTENUATIONAUTO._serialized_end=6334
  _RFMXINSTRMXOPTIMIZEPATHFORSIGNALBANDWIDTH._serialized_start=6336
  _RFMXINSTRMXOPTIMIZEPATHFORSIGNALBANDWIDTH._serialized_end=6458
  _RFMXINSTRMXOSPDELAYENABLED._serialized_start=6460
  _RFMXINSTRMXOSPDELAYENABLED._serialized_end=6544
  _RFMXINSTRMXOVERFLOWERRORREPORTING._serialized_start=6546
  _RFMXINSTRMXOVERFLOWERRORREPORTING._serialized_end=6637
  _RFMXINSTRMXPREAMPENABLED._serialized_start=6639
  _RFMXINSTRMXPREAMPENABLED._serialized_end=6744
  _RFMXINSTRMXRFATTENUATIONAUTO._serialized_start=6746
  _RFMXINSTRMXRFATTENUATIONAUTO._serialized_end=6826
  _RFMXINSTRMXSELFCALIBRATIONVALIDITYCHECK._serialized_start=6828
  _RFMXINSTRMXSELFCALIBRATIONVALIDITYCHECK._serialized_end=6920
  _RFMXINSTRMXSTARTTRIGGERDIGITALEDGE._serialized_start=6922
  _RFMXINSTRMXSTARTTRIGGERDIGITALEDGE._serialized_end=7012
  _RFMXINSTRMXSTARTTRIGGERTYPE._serialized_start=7014
  _RFMXINSTRMXSTARTTRIGGERTYPE._serialized_end=7121
  _RFMXINSTRMXTUNINGSPEED._serialized_start=7123
  _RFMXINSTRMXTUNINGSPEED._serialized_end=7218
  _INST._serialized_start=69
  _INST._serialized_end=4809
# @@protoc_insertion_point(module_scope)
