"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaGrouperStatusChangeType import OcaGrouperStatusChangeType
from .OcaUint16 import OcaUint16
from .Struct import Struct

 from ..types.OcaGrouperStatusChangeEventDataimport { OcaGrouperStatusChangeEventData as type }

OcaGrouperStatusChangeEventData = Struct(
  {
    "groupIndex": OcaUint16,
    "citizenIndex": OcaUint16,
    "changeType": OcaGrouperStatusChangeType,
  },
  type
)
