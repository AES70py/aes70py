"""
This file is part of aes70py.
This file has been generated.
"""
from .ocaclassidentification import OcaClassIdentification
from .ocauint32 import OcaUint32
from .struct import Struct

from ..types.ocaobjectidentification import OcaObjectIdentification as type

OcaObjectIdentification = Struct(
  {
    "ONo": OcaUint32,
    "ClassIdentification": OcaClassIdentification,
  },
  type
)
