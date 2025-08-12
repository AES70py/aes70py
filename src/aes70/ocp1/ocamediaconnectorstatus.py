"""
This file is part of aes70py.
This file has been generated.
"""
from .ocamediaconnectorstate import OcaMediaConnectorState
from .ocauint16 import OcaUint16
from .struct import Struct

from ..types.ocamediaconnectorstatus import OcaMediaConnectorStatus as type

OcaMediaConnectorStatus = Struct(
  {
    "ConnectorID": OcaUint16,
    "State": OcaMediaConnectorState,
    "ErrorCode": OcaUint16,
  },
  type
)
