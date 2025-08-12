"""
This file is part of aes70py.
This file has been generated.
"""
from .ocaboolean import OcaBoolean
from .ocauint32 import OcaUint32
from .ocauint64 import OcaUint64
from .struct import Struct

from ..types.ocatimeptp import OcaTimePTP as type

OcaTimePTP = Struct(
  {
    "Negative": OcaBoolean,
    "Seconds": OcaUint64,
    "Nanoseconds": OcaUint32,
  },
  type
)
