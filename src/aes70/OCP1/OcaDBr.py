"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaFloat32 import OcaFloat32
from .Struct import Struct

 from ..types.OcaDBrimport { OcaDBr as type }

OcaDBr = Struct(
  {
    "Value": OcaFloat32,
    "Ref": OcaFloat32,
  },
  type
)
