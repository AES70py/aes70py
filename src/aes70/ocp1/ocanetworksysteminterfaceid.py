"""
This file is part of aes70py.
This file has been generated.
"""
from .ocablob import OcaBlob
from .struct import Struct

from ..types.ocanetworksysteminterfaceid import OcaNetworkSystemInterfaceID as type

OcaNetworkSystemInterfaceID = Struct(
  {
    "SystemInterfaceHandle": OcaBlob,
    "MyNetworkAddress": OcaBlob,
  },
  type
)
