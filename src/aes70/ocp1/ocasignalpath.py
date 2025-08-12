"""
This file is part of aes70py.
This file has been generated.
"""
from .ocaport import OcaPort
from .struct import Struct

from ..types.ocasignalpath import OcaSignalPath as type

OcaSignalPath = Struct(
  {
    "SourcePort": OcaPort,
    "SinkPort": OcaPort,
  },
  type
)
