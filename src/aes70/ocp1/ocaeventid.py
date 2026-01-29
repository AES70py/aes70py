"""
This file is part of aes70py.
This file has been generated.
"""
from .ocauint16 import OcaUint16
from .struct import Struct

from ..types.ocaeventid import OcaEventID as type

OcaEventID =Struct(
  {
    "DefLevel": OcaUint16,
    "EventIndex": OcaUint16,
  },
  type
)
