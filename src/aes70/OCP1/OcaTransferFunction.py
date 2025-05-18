"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaFloat32 import OcaFloat32
from .OcaList import OcaList
from .Struct import Struct

from ..types.OcaTransferFunction import OcaTransferFunction as type

OcaTransferFunction = Struct(
  {
    "Frequency": OcaList(OcaFloat32),
    "Amplitude": OcaList(OcaFloat32),
    "Phase": OcaList(OcaFloat32),
  },
  type
)
