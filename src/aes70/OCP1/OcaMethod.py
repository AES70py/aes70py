"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaMethodID import OcaMethodID
from .OcaUint32 import OcaUint32
from .Struct import Struct

from ..types.OcaMethod import OcaMethod as type

OcaMethod = Struct(
  {
    "ONo": OcaUint32,
    "MethodID": OcaMethodID,
  },
  type
)
