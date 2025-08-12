"""
This file is part of aes70py.
This file has been generated.
"""
from .ocablobfixedlen import OcaBlobFixedLen
from .struct import Struct

from ..types.ocamodelguid import OcaModelGUID as type

OcaModelGUID = Struct(
  {
    "Reserved": OcaBlobFixedLen(1),
    "MfrCode": OcaBlobFixedLen(3),
    "ModelCode": OcaBlobFixedLen(4),
  },
  type
)
