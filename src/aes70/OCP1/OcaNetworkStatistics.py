"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaUint32 import OcaUint32
from .Struct import Struct

 from ..types.OcaNetworkStatisticsimport { OcaNetworkStatistics as type }

OcaNetworkStatistics = Struct(
  {
    "rxPacketErrors": OcaUint32,
    "txPacketErrors": OcaUint32,
  },
  type
)
