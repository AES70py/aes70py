"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaUint16 import OcaUint16
from .String16 import String16
from .Struct import Struct

from ..types.OcaClassIdentification import OcaClassIdentification as type

OcaClassIdentification = Struct(
  {
    "ClassID": String16,
    "ClassVersion": OcaUint16,
  },
  type
)
