"""
This file is part of aes70py.
This file has been generated.
"""
from .ocaprotoportid import OcaProtoPortID
from .ocastring import OcaString
from .ocauint32 import OcaUint32
from .struct import Struct

from ..types.ocaprotoport import OcaProtoPort as type

OcaProtoPort = Struct(
  {
    "Owner": OcaUint32,
    "ProtoID": OcaProtoPortID,
    "Name": OcaString,
  },
  type
)
