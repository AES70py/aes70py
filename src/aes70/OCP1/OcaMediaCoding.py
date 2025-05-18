"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaString import OcaString
from .OcaUint16 import OcaUint16
from .OcaUint32 import OcaUint32
from .Struct import Struct

from ..types.OcaMediaCoding import OcaMediaCoding as type

OcaMediaCoding = Struct(
  {
    "CodingSchemeID": OcaUint16,
    "CodecParameters": OcaString,
    "ClockONo": OcaUint32,
  },
  type
)
