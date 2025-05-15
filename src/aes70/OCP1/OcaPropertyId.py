"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaUint16 import OcaUint16
from .Struct import Struct

 from ..types.OcaPropertyIDimport { OcaPropertyID as type }

OcaPropertyID = Struct(
  {
    "DefLevel": OcaUint16,
    "PropertyIndex": OcaUint16,
  },
  type
)
