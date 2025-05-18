"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaMediaConnectorState import OcaMediaConnectorState
from .OcaUint16 import OcaUint16
from .Struct import Struct

from ..types.OcaMediaConnectorStatus import OcaMediaConnectorStatus as type

OcaMediaConnectorStatus = Struct(
  {
    "ConnectorID": OcaUint16,
    "State": OcaMediaConnectorState,
    "ErrorCode": OcaUint16,
  },
  type
)
