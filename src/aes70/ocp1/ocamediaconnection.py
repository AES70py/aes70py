"""
This file is part of aes70py.
This file has been generated.
"""
from .ocablob import OcaBlob
from .ocaboolean import OcaBoolean
from .ocamediastreamcastmode import OcaMediaStreamCastMode
from .ocauint16 import OcaUint16
from .struct import Struct

from ..types.ocamediaconnection import OcaMediaConnection as type

OcaMediaConnection = Struct(
  {
    "Secure": OcaBoolean,
    "StreamParameters": OcaBlob,
    "StreamCastMode": OcaMediaStreamCastMode,
    "StreamChannelCount": OcaUint16,
  },
  type
)
