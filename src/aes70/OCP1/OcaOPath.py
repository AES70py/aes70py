"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaBlob import OcaBlob
from .OcaUint32 import OcaUint32
from .Struct import Struct

 from ..types.OcaOPathimport { OcaOPath as type }

OcaOPath = Struct(
  {
    "HostID": OcaBlob,
    "ONo": OcaUint32,
  },
  type
)
