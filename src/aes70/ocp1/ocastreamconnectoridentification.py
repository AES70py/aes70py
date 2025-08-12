"""
This file is part of aes70py.
This file has been generated.
"""
from .ocablob import OcaBlob
from .struct import Struct

from ..types.ocastreamconnectoridentification import OcaStreamConnectorIdentification as type

OcaStreamConnectorIdentification = Struct(
  {
    "HostID": OcaBlob,
    "NetworkAddress": OcaBlob,
    "NodeID": OcaBlob,
    "StreamConnectorID": OcaBlob,
  },
  type
)
