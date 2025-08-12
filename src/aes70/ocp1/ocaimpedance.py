"""
This file is part of aes70py.
This file has been generated.
"""
from .ocafloat32 import OcaFloat32
from .struct import Struct

from ..types.ocaimpedance import OcaImpedance as type

OcaImpedance = Struct(
  {
    "Magnitude": OcaFloat32,
    "Phase": OcaFloat32,
  },
  type
)
