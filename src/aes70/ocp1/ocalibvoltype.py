"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaBlobFixedLen import OcaBlobFixedLen
from .OcaUint32 import OcaUint32
from .Struct import Struct

from ..types.OcaLibVolType import OcaLibVolType as type

OcaLibVolType = Struct(
  {
    "Authority": OcaBlobFixedLen(3),
    "ID": OcaUint32,
  },
  type
)
