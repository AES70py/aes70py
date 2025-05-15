"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaBlob import OcaBlob
from .OcaBoolean import OcaBoolean
from .OcaMediaStreamCastMode import OcaMediaStreamCastMode
from .OcaUint16 import OcaUint16
from .Struct import Struct

 from ..types.OcaMediaConnectionimport { OcaMediaConnection as type }

OcaMediaConnection = Struct(
  {
    "Secure": OcaBoolean,
    "StreamParameters": OcaBlob,
    "StreamCastMode": OcaMediaStreamCastMode,
    "StreamChannelCount": OcaUint16,
  },
  type
)
