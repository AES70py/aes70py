"""
This file is part of aes70py.
This file has been generated.
"""
from .ocafloat32 import OcaFloat32
from .ocalist import OcaList
from .ocamediacoding import OcaMediaCoding
from .ocamediaconnection import OcaMediaConnection
from .ocamultimap import OcaMultiMap
from .ocaportid import OcaPortID
from .ocastring import OcaString
from .ocauint16 import OcaUint16
from .struct import Struct

from ..types.ocamediasinkconnector import OcaMediaSinkConnector as type

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
