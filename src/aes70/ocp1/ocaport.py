"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaPortID import OcaPortID
from .OcaString import OcaString
from .OcaUint32 import OcaUint32
from .Struct import Struct

from ..types.OcaPort import OcaPort as type

OcaPort = Struct(
  {
    "Owner": OcaUint32,
    "ID": OcaPortID,
    "Name": OcaString,
  },
  type
)
