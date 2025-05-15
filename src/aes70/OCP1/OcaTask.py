"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaBlob import OcaBlob
from .OcaLibVolIdentifier import OcaLibVolIdentifier
from .OcaString import OcaString
from .OcaTimeMode import OcaTimeMode
from .OcaTimePTP import OcaTimePTP
from .OcaUint16 import OcaUint16
from .OcaUint32 import OcaUint32
from .Struct import Struct

 from ..types.OcaTaskimport { OcaTask as type }

OcaTask = Struct(
  {
    "ID": OcaUint32,
    "Label": OcaString,
    "ProgramID": OcaLibVolIdentifier,
    "GroupID": OcaUint16,
    "TimeMode": OcaTimeMode,
    "TimeSourceONo": OcaUint32,
    "StartTime": OcaTimePTP,
    "Duration": OcaTimePTP,
    "ApplicationSpecificParameters": OcaBlob,
  },
  type
)
