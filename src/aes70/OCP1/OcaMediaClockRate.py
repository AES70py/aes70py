"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaFloat32 import OcaFloat32
from .Struct import Struct

 from ..types.OcaMediaClockRateimport { OcaMediaClockRate as type }

OcaMediaClockRate = Struct(
  {
    "NominalRate": OcaFloat32,
    "PullRange": OcaFloat32,
    "Accuracy": OcaFloat32,
    "JitterMax": OcaFloat32,
  },
  type
)
