"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaLibAccess import OcaLibAccess
from .OcaLibVolType import OcaLibVolType
from .OcaString import OcaString
from .OcaTimePTP import OcaTimePTP
from .OcaUint32 import OcaUint32
from .Struct import Struct

from ..types.OcaLibVolMetadata import OcaLibVolMetadata as type

OcaLibVolMetadata = Struct(
  {
    "Name": OcaString,
    "VolType": OcaLibVolType,
    "Access": OcaLibAccess,
    "Version": OcaUint32,
    "Creator": OcaString,
    "UpDate": OcaTimePTP,
  },
  type
)
