# /*
#  * This file has been generated.
#  */
from .OcaBlobFixedLen import OcaBlobFixedLen
from .OcaUint32 import OcaUint32
from .struct import Struct

from aes70.types.OcaGlobalTypeIdentifier import OcaGlobalTypeIdentifier as type

OcaGlobalTypeIdentifier = Struct(
  {
    "Authority": OcaBlobFixedLen(3),
    "ID": OcaUint32,
  },
  type
)
