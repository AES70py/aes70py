"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaBoolean import OcaBoolean
from .OcaUint32 import OcaUint32
from .OcaUint64 import OcaUint64
from .Struct import Struct

from ..types.OcaTimePTP import OcaTimePTP as type

OcaTimePTP = Struct(
  {
    "Negative": OcaBoolean,
    "Seconds": OcaUint64,
    "Nanoseconds": OcaUint32,
  },
  type
)
