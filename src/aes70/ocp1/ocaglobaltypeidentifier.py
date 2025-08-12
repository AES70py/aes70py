"""
This file is part of aes70py.
This file has been generated.
"""
from .ocablobfixedlen import OcaBlobFixedLen
from .ocauint32 import OcaUint32
from .struct import Struct

from ..types.ocaglobaltypeidentifier import OcaGlobalTypeIdentifier as type

OcaGlobalTypeIdentifier = Struct(
  {
    "Authority": OcaBlobFixedLen(3),
    "ID": OcaUint32,
  },
  type
)
