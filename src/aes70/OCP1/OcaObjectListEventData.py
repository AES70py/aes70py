"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaList import OcaList
from .OcaUint32 import OcaUint32
from .Struct import Struct

from ..types.OcaObjectListEventData import OcaObjectListEventData as type

OcaObjectListEventData = Struct(
  {
    "objectList": OcaList(OcaUint32),
  },
  type
)
