"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaString import OcaString
from .OcaUint16 import OcaUint16
from .OcaUint32 import OcaUint32
from .Struct import Struct

 from ..types.OcaGrouperGroupimport { OcaGrouperGroup as type }

OcaGrouperGroup = Struct(
  {
    "Index": OcaUint16,
    "Name": OcaString,
    "ProxyONo": OcaUint32,
  },
  type
)
