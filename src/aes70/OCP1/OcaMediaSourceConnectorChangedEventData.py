"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaMediaConnectorElement import OcaMediaConnectorElement
from .OcaMediaSourceConnector import OcaMediaSourceConnector
from .OcaPropertyChangeType import OcaPropertyChangeType
from .Struct import Struct

 from ..types.OcaMediaSourceConnectorChangedEventDataimport { OcaMediaSourceConnectorChangedEventData as type }

OcaMediaSourceConnectorChangedEventData = Struct(
  {
    "SourceConnector": OcaMediaSourceConnector,
    "ChangeType": OcaPropertyChangeType,
    "ChangedElement": OcaMediaConnectorElement,
  },
  type
)
