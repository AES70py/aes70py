"""
This file is part of aes70py.
This file has been generated.
"""
from .ocafloat32 import OcaFloat32
from .struct import Struct

from ..types.ocadbr import OcaDBr as type

OcaDBr = Struct(
  {
    "Value": OcaFloat32,
    "Ref": OcaFloat32,
  },
  type
)
