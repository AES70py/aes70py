"""
This file is part of aes70py.
This file has been generated.
"""
from .ocalist import OcaList
from .ocauint32 import OcaUint32
from .struct import Struct

from ..types.ocaobjectlisteventdata import OcaObjectListEventData as type

OcaObjectListEventData = Struct(
  {
    "objectList": OcaList(OcaUint32),
  },
  type
)
