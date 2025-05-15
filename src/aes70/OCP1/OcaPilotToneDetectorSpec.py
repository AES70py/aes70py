"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaDBr import OcaDBr
from .OcaFloat32 import OcaFloat32
from .OcaUint32 import OcaUint32
from .Struct import Struct

 from ..types.OcaPilotToneDetectorSpecimport { OcaPilotToneDetectorSpec as type }

OcaPilotToneDetectorSpec = Struct(
  {
    "Threshold": OcaDBr,
    "Frequency": OcaFloat32,
    "PollInterval": OcaUint32,
  },
  type
)
