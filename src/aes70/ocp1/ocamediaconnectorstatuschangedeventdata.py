"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaMediaConnectorStatus import OcaMediaConnectorStatus
from .Struct import Struct

from ..types.OcaMediaConnectorStatusChangedEventData import OcaMediaConnectorStatusChangedEventData as type

OcaMediaConnectorStatusChangedEventData = Struct(
  {
    "ConnectorStatus": OcaMediaConnectorStatus,
  },
  type
)
