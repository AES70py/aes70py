"""
This file is part of aes70py.
This file has been generated.
"""
from .ocaeventid import OcaEventID
from .ocauint32 import OcaUint32
from .struct import Struct

from ..types.ocaevent import OcaEvent as type

OcaEvent = Struct(
  {
    "EmitterONo": OcaUint32,
    "EventID": OcaEventID,
  },
  type
)
