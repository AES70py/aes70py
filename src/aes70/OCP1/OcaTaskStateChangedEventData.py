"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaLibVolIdentifier import OcaLibVolIdentifier
from .OcaTaskStatus import OcaTaskStatus
from .OcaUint32 import OcaUint32
from .Struct import Struct

 from ..types.OcaTaskStateChangedEventDataimport { OcaTaskStateChangedEventData as type }

OcaTaskStateChangedEventData = Struct(
  {
    "TaskID": OcaUint32,
    "ProgramID": OcaLibVolIdentifier,
    "Status": OcaTaskStatus,
  },
  type
)
