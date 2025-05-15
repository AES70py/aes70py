"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaBlob import OcaBlob
from .Struct import Struct

 from ..types.OcaNetworkSystemInterfaceIDimport { OcaNetworkSystemInterfaceID as type }

OcaNetworkSystemInterfaceID = Struct(
  {
    "SystemInterfaceHandle": OcaBlob,
    "MyNetworkAddress": OcaBlob,
  },
  type
)
