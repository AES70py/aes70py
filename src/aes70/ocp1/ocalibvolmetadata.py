"""
This file is part of aes70py.
This file has been generated.
"""
from .ocalibaccess import OcaLibAccess
from .ocalibvoltype import OcaLibVolType
from .ocastring import OcaString
from .ocatimeptp import OcaTimePTP
from .ocauint32 import OcaUint32
from .struct import Struct

from ..types.ocalibvolmetadata import OcaLibVolMetadata as type

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
