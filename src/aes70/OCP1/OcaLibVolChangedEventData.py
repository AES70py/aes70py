"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaPropertyChangeType import OcaPropertyChangeType
from .OcaUint32 import OcaUint32
from .Struct import Struct

from ..types.OcaLibVolChangedEventData import OcaLibVolChangedEventData as type

OcaLibVolChangedEventData = Struct(
  {
    "VolumeID": OcaUint32,
    "ChangeType": OcaPropertyChangeType,
  },
  type
)
