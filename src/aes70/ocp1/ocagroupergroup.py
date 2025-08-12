"""
This file is part of aes70py.
This file has been generated.
"""
from .ocastring import OcaString
from .ocauint16 import OcaUint16
from .ocauint32 import OcaUint32
from .struct import Struct

from ..types.ocagroupergroup import OcaGrouperGroup as type

OcaGrouperGroup = Struct(
  {
    "Index": OcaUint16,
    "Name": OcaString,
    "ProxyONo": OcaUint32,
  },
  type
)
