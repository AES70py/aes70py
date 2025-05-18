"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaMediaConnectorElement import OcaMediaConnectorElement
from .OcaMediaSinkConnector import OcaMediaSinkConnector
from .OcaPropertyChangeType import OcaPropertyChangeType
from .Struct import Struct

from ..types.OcaMediaSinkConnectorChangedEventData import OcaMediaSinkConnectorChangedEventData as type

OcaMediaSinkConnectorChangedEventData = Struct(
  {
    "SinkConnector": OcaMediaSinkConnector,
    "ChangeType": OcaPropertyChangeType,
    "ChangedElement": OcaMediaConnectorElement,
  },
  type
)
