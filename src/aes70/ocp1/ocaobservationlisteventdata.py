"""
This file is part of aes70py.
This file has been generated.
"""
from .ocafloat64 import OcaFloat64
from .ocalist import OcaList
from .struct import Struct

from ..types.ocaobservationlisteventdata import OcaObservationListEventData as type

OcaObservationListEventData = Struct(
  {
    "Reading": OcaList(OcaFloat64),
  },
  type
)
