"""
This file is part of aes70py.
This file has been generated.
"""
from .ocamediaconnectorelement import OcaMediaConnectorElement
from .ocamediasourceconnector import OcaMediaSourceConnector
from .ocapropertychangetype import OcaPropertyChangeType
from .struct import Struct

from ..types.ocamediasourceconnectorchangedeventdata import OcaMediaSourceConnectorChangedEventData as type

OcaMediaSourceConnectorChangedEventData = Struct(
  {
    "SourceConnector": OcaMediaSourceConnector,
    "ChangeType": OcaPropertyChangeType,
    "ChangedElement": OcaMediaConnectorElement,
  },
  type
)
