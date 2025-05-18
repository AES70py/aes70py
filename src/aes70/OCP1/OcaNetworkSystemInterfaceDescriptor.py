"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaBlob import OcaBlob
from .Struct import Struct

from ..types.OcaNetworkSystemInterfaceDescriptor import OcaNetworkSystemInterfaceDescriptor as type

OcaNetworkSystemInterfaceDescriptor = Struct(
  {
    "SystemInterfaceParameters": OcaBlob,
    "MyNetworkAddress": OcaBlob,
  },
  type
)
