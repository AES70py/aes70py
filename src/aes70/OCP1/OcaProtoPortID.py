"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaPortMode import OcaPortMode
from .OcaUint16 import OcaUint16
from .Struct import Struct

from ..types.OcaProtoPortID import OcaProtoPortID as type

OcaProtoPortID = Struct(
  {
    "Mode": OcaPortMode,
    "Index": OcaUint16,
  },
  type
)
