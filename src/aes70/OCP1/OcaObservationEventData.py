"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaFloat64 import OcaFloat64
from .Struct import Struct

 from ..types.OcaObservationEventDataimport { OcaObservationEventData as type }

OcaObservationEventData = Struct(
  {
    "Reading": OcaFloat64,
  },
  type
)
