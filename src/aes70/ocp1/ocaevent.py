"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaEventID import OcaEventID
from .OcaUint32 import OcaUint32
from .Struct import Struct

from ..types.OcaEvent import OcaEvent as type

OcaEvent = Struct(
  {
    "EmitterONo": OcaUint32,
    "EventID": OcaEventID,
  },
  type
)
