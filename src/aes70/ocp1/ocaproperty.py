"""
This file is part of aes70py.
This file has been generated.
"""
from .ocapropertydescriptor import OcaPropertyDescriptor
from .ocauint32 import OcaUint32
from .struct import Struct

from ..types.ocaproperty import OcaProperty as type

OcaProperty = Struct(
  {
    "ONo": OcaUint32,
    "Descriptor": OcaPropertyDescriptor,
  },
  type
)
