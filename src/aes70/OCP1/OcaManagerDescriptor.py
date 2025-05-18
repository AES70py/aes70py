"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaString import OcaString
from .OcaUint16 import OcaUint16
from .OcaUint32 import OcaUint32
from .String16 import String16
from .Struct import Struct

from ..types.OcaManagerDescriptor import OcaManagerDescriptor as type

OcaManagerDescriptor = Struct(
  {
    "ObjectNumber": OcaUint32,
    "Name": OcaString,
    "ClassID": String16,
    "ClassVersion": OcaUint16,
  },
  type
)
