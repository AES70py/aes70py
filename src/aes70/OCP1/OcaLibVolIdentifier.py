"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaUint32 import OcaUint32
from .Struct import Struct

 from ..types.OcaLibVolIdentifierimport { OcaLibVolIdentifier as type }

OcaLibVolIdentifier = Struct(
  {
    "Library": OcaUint32,
    "ID": OcaUint32,
  },
  type
)
