"""
This file is part of aes70py.
This file has been generated.
"""
from .ocablob import OcaBlob
from .struct import Struct

from ..types.ocanetworksysteminterfacedescriptor import OcaNetworkSystemInterfaceDescriptor as type

OcaNetworkSystemInterfaceDescriptor = Struct(
  {
    "SystemInterfaceParameters": OcaBlob,
    "MyNetworkAddress": OcaBlob,
  },
  type
)
