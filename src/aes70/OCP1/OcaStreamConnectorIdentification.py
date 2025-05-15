"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaBlob import OcaBlob
from .Struct import Struct

 from ..types.OcaStreamConnectorIdentificationimport { OcaStreamConnectorIdentification as type }

OcaStreamConnectorIdentification = Struct(
  {
    "HostID": OcaBlob,
    "NetworkAddress": OcaBlob,
    "NodeID": OcaBlob,
    "StreamConnectorID": OcaBlob,
  },
  type
)
