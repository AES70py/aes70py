"""
This file is part of aes70py.
This file has been generated.
"""
from .ocataskstate import OcaTaskState
from .ocauint16 import OcaUint16
from .ocauint32 import OcaUint32
from .struct import Struct

from ..types.ocataskstatus import OcaTaskStatus as type

OcaTaskStatus = Struct(
  {
    "ID": OcaUint32,
    "State": OcaTaskState,
    "ErrorCode": OcaUint16,
  },
  type
)
