"""
This file is part of aes70py.
This file has been generated.
"""
from .String16 import String16
from .ocastring import OcaString
from .ocauint16 import OcaUint16
from .ocauint32 import OcaUint32
from .struct import Struct

from ..types.ocamanagerdescriptor import OcaManagerDescriptor as type

OcaManagerDescriptor = Struct(
  {
    "ObjectNumber": OcaUint32,
    "Name": OcaString,
    "ClassID": String16,
    "ClassVersion": OcaUint16,
  },
  type
)
