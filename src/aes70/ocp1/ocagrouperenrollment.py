"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaUint16 import OcaUint16
from .Struct import Struct

from ..types.OcaGrouperEnrollment import OcaGrouperEnrollment as type

OcaGrouperEnrollment = Struct(
  {
    "GroupIndex": OcaUint16,
    "CitizenIndex": OcaUint16,
  },
  type
)
