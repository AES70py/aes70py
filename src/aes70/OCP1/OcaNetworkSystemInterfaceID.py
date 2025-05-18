"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaBlob import OcaBlob
from .Struct import Struct

from ..types.OcaNetworkSystemInterfaceID import OcaNetworkSystemInterfaceID as type

OcaNetworkSystemInterfaceID = Struct(
  {
    "SystemInterfaceHandle": OcaBlob,
    "MyNetworkAddress": OcaBlob,
  },
  type
)
