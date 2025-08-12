"""
This file is part of aes70py.
This file has been generated.
"""
from .ocaportid import OcaPortID
from .ocastring import OcaString
from .ocauint32 import OcaUint32
from .struct import Struct

from ..types.ocaport import OcaPort as type

OcaPort = Struct(
  {
    "Owner": OcaUint32,
    "ID": OcaPortID,
    "Name": OcaString,
  },
  type
)
