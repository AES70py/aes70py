"""
This file is part of aes70py.
This file has been generated.
"""
from .ocaportmode import OcaPortMode
from .ocauint16 import OcaUint16
from .struct import Struct

from ..types.ocaportid import OcaPortID as type

OcaPortID = Struct(
  {
    "Mode": OcaPortMode,
    "Index": OcaUint16,
  },
  type
)
