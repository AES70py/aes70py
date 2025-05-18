"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaUint16 import OcaUint16
from .Struct import Struct

from ..types.OcaMethodID import OcaMethodID as type

OcaMethodID = Struct(
  {
    "DefLevel": OcaUint16,
    "MethodIndex": OcaUint16,
  },
  type
)
