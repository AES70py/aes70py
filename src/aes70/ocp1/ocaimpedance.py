"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaFloat32 import OcaFloat32
from .Struct import Struct

from ..types.OcaImpedance import OcaImpedance as type

OcaImpedance = Struct(
  {
    "Magnitude": OcaFloat32,
    "Phase": OcaFloat32,
  },
  type
)
