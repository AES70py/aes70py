"""
This file is part of aes70py.
This file has been generated.
"""
from .string16 import String16
from .ocauint16 import OcaUint16
from .struct import Struct

from ..types.ocaclassidentification import OcaClassIdentification as type

OcaClassIdentification = Struct(
  {
    "ClassID": String16,
    "ClassVersion": OcaUint16,
  },
  type
)
