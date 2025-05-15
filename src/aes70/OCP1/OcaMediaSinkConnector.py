"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaFloat32 import OcaFloat32
from .OcaList import OcaList
from .OcaMediaCoding import OcaMediaCoding
from .OcaMediaConnection import OcaMediaConnection
from .OcaMultiMap import OcaMultiMap
from .OcaPortID import OcaPortID
from .OcaString import OcaString
from .OcaUint16 import OcaUint16
from .Struct import Struct

 from ..types.OcaMediaSinkConnectorimport { OcaMediaSinkConnector as type }

OcaMediaSinkConnector = Struct(
  {
    "IDInternal": OcaUint16,
    "IDExternal": OcaString,
    "Connection": OcaMediaConnection,
    "AvailableCodings": OcaList(OcaMediaCoding),
    "PinCount": OcaUint16,
    "ChannelPinMap": OcaMultiMap(OcaUint16, OcaPortID),
    "AlignmentLevel": OcaFloat32,
    "AlignmentGain": OcaFloat32,
    "CurrentCoding": OcaMediaCoding,
  },
  type
)
