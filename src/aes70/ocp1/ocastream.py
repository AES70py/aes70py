"""
This file is part of aes70py.
This file has been generated.
"""
from .ocablob import OcaBlob
from .ocaboolean import OcaBoolean
from .ocastreamconnectoridentification import OcaStreamConnectorIdentification
from .ocastreamstatus import OcaStreamStatus
from .ocastreamtype import OcaStreamType
from .ocastring import OcaString
from .ocauint16 import OcaUint16
from .ocauint32 import OcaUint32
from .struct import Struct

from ..types.ocastream import OcaStream as type

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
