"""
This file is part of aes70py.
This file has been generated.
"""
from .ocauint32 import OcaUint32
from .struct import Struct

from ..types.ocanetworkstatistics import OcaNetworkStatistics as type

OcaNetworkStatistics = Struct(
  {
    "rxPacketErrors": OcaUint32,
    "txPacketErrors": OcaUint32,
  },
  type
)
