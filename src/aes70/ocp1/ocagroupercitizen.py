"""
This file is part of aes70py.
This file has been generated.
"""
from .ocaboolean import OcaBoolean
from .ocaopath import OcaOPath
from .ocauint16 import OcaUint16
from .struct import Struct

from ..types.ocagroupercitizen import OcaGrouperCitizen as type

OcaGrouperCitizen = Struct(
  {
    "Index": OcaUint16,
    "ObjectPath": OcaOPath,
    "Online": OcaBoolean,
  },
  type
)
