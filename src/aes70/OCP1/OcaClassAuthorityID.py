"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaBlobFixedLen import OcaBlobFixedLen
from .OcaUint16 import OcaUint16
from .OcaUint8 import OcaUint8
from .Struct import Struct

from ..types.OcaClassAuthorityID import OcaClassAuthorityID as type

OcaClassAuthorityID = Struct(
  {
    "Sentinel": OcaUint16,
    "Reserved": OcaUint8,
    "OrganizationID": OcaBlobFixedLen(3),
  },
  type
)
