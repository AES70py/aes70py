"""
This file is part of aes70py.
This file has been generated.
"""
from .ocamethodid import OcaMethodID
from .ocauint32 import OcaUint32
from .struct import Struct

from ..types.ocamethod import OcaMethod as type

OcaMethod = Struct(
  {
    "ONo": OcaUint32,
    "MethodID": OcaMethodID,
  },
  type
)
