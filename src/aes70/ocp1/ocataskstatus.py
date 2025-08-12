"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaTaskState import OcaTaskState
from .OcaUint16 import OcaUint16
from .OcaUint32 import OcaUint32
from .Struct import Struct

from ..types.OcaTaskStatus import OcaTaskStatus as type

OcaTaskStatus = Struct(
  {
    "ID": OcaUint32,
    "State": OcaTaskState,
    "ErrorCode": OcaUint16,
  },
  type
)
