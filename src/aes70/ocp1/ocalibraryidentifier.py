"""
This file is part of aes70py.
This file has been generated.
"""
from .ocalibvoltype import OcaLibVolType
from .ocauint32 import OcaUint32
from .struct import Struct

from ..types.ocalibraryidentifier import OcaLibraryIdentifier as type

OcaLibraryIdentifier = Struct(
  {
    "Type": OcaLibVolType,
    "ONo": OcaUint32,
  },
  type
)
