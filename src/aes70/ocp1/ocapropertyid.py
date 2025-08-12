"""
This file is part of aes70py.
This file has been generated.
"""
from .ocauint16 import OcaUint16
from .struct import Struct

from ..types.ocapropertyid import OcaPropertyID as type

OcaPropertyID = Struct(
  {
    "DefLevel": OcaUint16,
    "PropertyIndex": OcaUint16,
  },
  type
)
