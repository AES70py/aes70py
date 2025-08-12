"""
This file is part of aes70py.
This file has been generated.
"""
from .ocaclassidentification import OcaClassIdentification
from .ocalist import OcaList
from .ocastring import OcaString
from .ocauint32 import OcaUint32
from .struct import Struct

from ..types.ocaobjectsearchresult import OcaObjectSearchResult as type

OcaObjectSearchResult = Struct(
  {
    "ONo": OcaUint32,
    "ClassIdentification": OcaClassIdentification,
    "ContainerPath": OcaList(OcaUint32),
    "Role": OcaString,
    "Label": OcaString,
  },
  type
)
