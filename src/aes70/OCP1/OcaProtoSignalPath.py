"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaProtoPort import OcaProtoPort
from .Struct import Struct

 from ..types.OcaProtoSignalPathimport { OcaProtoSignalPath as type }

OcaProtoSignalPath = Struct(
  {
    "SourceProtoPort": OcaProtoPort,
    "SinkProtoPort": OcaProtoPort,
  },
  type
)
