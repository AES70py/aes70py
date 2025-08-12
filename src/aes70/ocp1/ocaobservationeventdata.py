"""
This file is part of aes70py.
This file has been generated.
"""
from .ocafloat64 import OcaFloat64
from .struct import Struct

from ..types.ocaobservationeventdata import OcaObservationEventData as type

OcaObservationEventData = Struct(
  {
    "Reading": OcaFloat64,
  },
  type
)
