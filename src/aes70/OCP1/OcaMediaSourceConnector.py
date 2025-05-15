"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaFloat32 import OcaFloat32
from .OcaList import OcaList
from .OcaMap import OcaMap
from .OcaMediaCoding import OcaMediaCoding
from .OcaMediaConnection import OcaMediaConnection
from .OcaPortID import OcaPortID
from .OcaString import OcaString
from .OcaUint16 import OcaUint16
from .Struct import Struct

 from ..types.OcaMediaSourceConnectorimport { OcaMediaSourceConnector as type }

OcaMediaSourceConnector = Struct(
  {
    "IDInternal": OcaUint16,
    "IDExternal": OcaString,
    "Connection": OcaMediaConnection,
    "AvailableCodings": OcaList(OcaMediaCoding),
    "PinCount": OcaUint16,
    "ChannelPinMap": OcaMap(OcaUint16, OcaPortID),
    "AlignmentLevel": OcaFloat32,
    "CurrentCoding": OcaMediaCoding,
  },
  type
)
