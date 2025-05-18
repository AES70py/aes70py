"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaUint16 import OcaUint16
from .Struct import Struct

from ..types.OcaEventID import OcaEventID as type

OcaEventID = Struct(
  {
    "DefLevel": OcaUint16,
    "EventIndex": OcaUint16,
  },
  type
)
