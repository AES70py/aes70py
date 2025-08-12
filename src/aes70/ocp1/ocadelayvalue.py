"""
This file is part of aes70py.
This file has been generated.
"""
from .ocadelayunit import OcaDelayUnit
from .ocafloat32 import OcaFloat32
from .struct import Struct

from ..types.ocadelayvalue import OcaDelayValue as type

OcaDelayValue = Struct(
  {
    "DelayValue": OcaFloat32,
    "DelayUnit": OcaDelayUnit,
  },
  type
)
