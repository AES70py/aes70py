"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaProtoPortID import OcaProtoPortID
from .OcaString import OcaString
from .OcaUint32 import OcaUint32
from .Struct import Struct

 from ..types.OcaProtoPortimport { OcaProtoPort as type }

OcaProtoPort = Struct(
  {
    "Owner": OcaUint32,
    "ProtoID": OcaProtoPortID,
    "Name": OcaString,
  },
  type
)
