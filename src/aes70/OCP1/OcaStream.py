"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaBlob import OcaBlob
from .OcaBoolean import OcaBoolean
from .OcaStreamConnectorIdentification import OcaStreamConnectorIdentification
from .OcaStreamStatus import OcaStreamStatus
from .OcaStreamType import OcaStreamType
from .OcaString import OcaString
from .OcaUint16 import OcaUint16
from .OcaUint32 import OcaUint32
from .Struct import Struct

from ..types.OcaStream import OcaStream as type

OcaStream = Struct(
  {
    "ErrorNumber": OcaUint16,
    "IDAdvertised": OcaBlob,
    "Index": OcaUint16,
    "Label": OcaString,
    "LocalConnectorONo": OcaUint32,
    "Priority": OcaUint16,
    "RemoteConnectorIdentification": OcaStreamConnectorIdentification,
    "Secure": OcaBoolean,
    "Status": OcaStreamStatus,
    "StreamParameters": OcaBlob,
    "StreamType": OcaStreamType,
  },
  type
)
