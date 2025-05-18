"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaFloat64 import OcaFloat64
from .OcaList import OcaList
from .Struct import Struct

from ..types.OcaObservationListEventData import OcaObservationListEventData as type

OcaObservationListEventData = Struct(
  {
    "Reading": OcaList(OcaFloat64),
  },
  type
)
