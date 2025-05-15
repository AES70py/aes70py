"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaPort import OcaPort
from .Struct import Struct

 from ..types.OcaSignalPathimport { OcaSignalPath as type }

OcaSignalPath = Struct(
  {
    "SourcePort": OcaPort,
    "SinkPort": OcaPort,
  },
  type
)
