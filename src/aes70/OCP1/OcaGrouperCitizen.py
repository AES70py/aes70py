"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaBoolean import OcaBoolean
from .OcaOPath import OcaOPath
from .OcaUint16 import OcaUint16
from .Struct import Struct

from ..types.OcaGrouperCitizen import OcaGrouperCitizen as type

OcaGrouperCitizen = Struct(
  {
    "Index": OcaUint16,
    "ObjectPath": OcaOPath,
    "Online": OcaBoolean,
  },
  type
)
