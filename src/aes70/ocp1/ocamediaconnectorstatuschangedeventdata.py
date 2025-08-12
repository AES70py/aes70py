"""
This file is part of aes70py.
This file has been generated.
"""
from .ocamediaconnectorstatus import OcaMediaConnectorStatus
from .struct import Struct

from ..types.ocamediaconnectorstatuschangedeventdata import OcaMediaConnectorStatusChangedEventData as type

OcaMediaConnectorStatusChangedEventData = Struct(
  {
    "ConnectorStatus": OcaMediaConnectorStatus,
  },
  type
)
