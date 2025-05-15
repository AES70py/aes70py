"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaBlobFixedLen import OcaBlobFixedLen
from .Struct import Struct

 from ..types.OcaModelGUIDimport { OcaModelGUID as type }

OcaModelGUID = Struct(
  {
    "Reserved": OcaBlobFixedLen(1),
    "MfrCode": OcaBlobFixedLen(3),
    "ModelCode": OcaBlobFixedLen(4),
  },
  type
)
