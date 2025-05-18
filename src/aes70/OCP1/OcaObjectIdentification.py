"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaClassIdentification import OcaClassIdentification
from .OcaUint32 import OcaUint32
from .Struct import Struct

from ..types.OcaObjectIdentification import OcaObjectIdentification as type

OcaObjectIdentification = Struct(
  {
    "ONo": OcaUint32,
    "ClassIdentification": OcaClassIdentification,
  },
  type
)
