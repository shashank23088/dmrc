# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dmrc.proto
# Protobuf Python Version: 5.28.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    0,
    '',
    'dmrc.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndmrc.proto\x12\x10transit_realtime\"i\n\x0b\x46\x65\x65\x64Message\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.transit_realtime.FeedHeader\x12,\n\x06\x65ntity\x18\x02 \x03(\x0b\x32\x1c.transit_realtime.FeedEntity\">\n\nFeedHeader\x12\x1d\n\x15gtfs_realtime_version\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\"L\n\nFeedEntity\x12\n\n\x02id\x18\x01 \x01(\t\x12\x32\n\x07vehicle\x18\x04 \x01(\x0b\x32!.transit_realtime.VehiclePosition\"\xb8\x01\n\x0fVehiclePosition\x12.\n\x04trip\x18\x01 \x01(\x0b\x32 .transit_realtime.TripDescriptor\x12,\n\x08position\x18\x02 \x01(\x0b\x32\x1a.transit_realtime.Position\x12\x11\n\ttimestamp\x18\x05 \x01(\x04\x12\x34\n\x07vehicle\x18\x08 \x01(\x0b\x32#.transit_realtime.VehicleDescriptor\"q\n\x0eTripDescriptor\x12\x0f\n\x07trip_id\x18\x01 \x01(\t\x12\x12\n\nstart_time\x18\x02 \x01(\t\x12\x12\n\nstart_date\x18\x03 \x01(\t\x12\x14\n\x0c\x64irection_id\x18\x04 \x01(\r\x12\x10\n\x08route_id\x18\x05 \x01(\t\"@\n\x08Position\x12\x10\n\x08latitude\x18\x01 \x01(\x02\x12\x11\n\tlongitude\x18\x02 \x01(\x02\x12\x0f\n\x07\x62\x65\x61ring\x18\x05 \x01(\x02\".\n\x11VehicleDescriptor\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dmrc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FEEDMESSAGE']._serialized_start=32
  _globals['_FEEDMESSAGE']._serialized_end=137
  _globals['_FEEDHEADER']._serialized_start=139
  _globals['_FEEDHEADER']._serialized_end=201
  _globals['_FEEDENTITY']._serialized_start=203
  _globals['_FEEDENTITY']._serialized_end=279
  _globals['_VEHICLEPOSITION']._serialized_start=282
  _globals['_VEHICLEPOSITION']._serialized_end=466
  _globals['_TRIPDESCRIPTOR']._serialized_start=468
  _globals['_TRIPDESCRIPTOR']._serialized_end=581
  _globals['_POSITION']._serialized_start=583
  _globals['_POSITION']._serialized_end=647
  _globals['_VEHICLEDESCRIPTOR']._serialized_start=649
  _globals['_VEHICLEDESCRIPTOR']._serialized_end=695
# @@protoc_insertion_point(module_scope)
