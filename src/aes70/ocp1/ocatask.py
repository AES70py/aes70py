"""
This file is part of aes70py.
This file has been generated.
"""
from .ocablob import OcaBlob
from .ocalibvolidentifier import OcaLibVolIdentifier
from .ocastring import OcaString
from .ocatimemode import OcaTimeMode
from .ocatimeptp import OcaTimePTP
from .ocauint16 import OcaUint16
from .ocauint32 import OcaUint32
from .struct import Struct

from ..types.ocatask import OcaTask as type

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
