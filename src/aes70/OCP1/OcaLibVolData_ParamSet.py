"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaBlob import OcaBlob
from .OcaUint32 import OcaUint32
from .Struct import Struct

 from ..types.OcaLibVolData_ParamSetimport { OcaLibVolData_ParamSet as type }

OcaLibVolData_ParamSet = Struct(
  {
    "TargetBlockType": OcaUint32,
    "ParData": OcaBlob,
  },
  type
)
