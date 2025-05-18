"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaDelayUnit import OcaDelayUnit
from .OcaFloat32 import OcaFloat32
from .Struct import Struct

from ..types.OcaDelayValue import OcaDelayValue as type

OcaDelayValue = Struct(
  {
    "DelayValue": OcaFloat32,
    "DelayUnit": OcaDelayUnit,
  },
  type
)
