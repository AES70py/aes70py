"""
This file is part of aes70py.
This file has been generated.
"""
from .ocauint16 import OcaUint16
from .struct import Struct

from ..types.ocagrouperenrollment import OcaGrouperEnrollment as type

OcaGrouperEnrollment = Struct(
  {
    "GroupIndex": OcaUint16,
    "CitizenIndex": OcaUint16,
  },
  type
)
