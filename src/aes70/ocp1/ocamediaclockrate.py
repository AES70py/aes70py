"""
This file is part of aes70py.
This file has been generated.
"""
from .ocafloat32 import OcaFloat32
from .struct import Struct

from ..types.ocamediaclockrate import OcaMediaClockRate as type

OcaMediaClockRate = Struct(
  {
    "NominalRate": OcaFloat32,
    "PullRange": OcaFloat32,
    "Accuracy": OcaFloat32,
    "JitterMax": OcaFloat32,
  },
  type
)
