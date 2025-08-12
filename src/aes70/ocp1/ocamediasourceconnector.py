"""
This file is part of aes70py.
This file has been generated.
"""
from .ocafloat32 import OcaFloat32
from .ocalist import OcaList
from .ocamap import OcaMap
from .ocamediacoding import OcaMediaCoding
from .ocamediaconnection import OcaMediaConnection
from .ocaportid import OcaPortID
from .ocastring import OcaString
from .ocauint16 import OcaUint16
from .struct import Struct

from ..types.ocamediasourceconnector import OcaMediaSourceConnector as type

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
