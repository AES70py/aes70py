# This file has been generated.
from .OcaPortMode import OcaPortMode
from .OcaUint16 import OcaUint16
from .struct import Struct

from ..types.OcaPortId import OcaPortID as type

OcaPortID = Struct(
  {
    "Mode": OcaPortMode,
    "Index": OcaUint16,
  },
  type
)
