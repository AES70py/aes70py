"""
This file is part of aes70py.
This file has been generated.
"""
from .ocadbr import OcaDBr
from .ocafloat32 import OcaFloat32
from .ocauint32 import OcaUint32
from .struct import Struct

from ..types.ocapilottonedetectorspec import OcaPilotToneDetectorSpec as type

OcaPilotToneDetectorSpec = Struct(
  {
    "Threshold": OcaDBr,
    "Frequency": OcaFloat32,
    "PollInterval": OcaUint32,
  },
  type
)
