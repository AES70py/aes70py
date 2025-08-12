"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaLibVolType import OcaLibVolType
from .OcaUint32 import OcaUint32
from .Struct import Struct

from ..types.OcaLibraryIdentifier import OcaLibraryIdentifier as type

OcaLibraryIdentifier = Struct(
  {
    "Type": OcaLibVolType,
    "ONo": OcaUint32,
  },
  type
)
