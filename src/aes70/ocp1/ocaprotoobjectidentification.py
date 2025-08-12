"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaClassIdentification import OcaClassIdentification
from .OcaUint32 import OcaUint32
from .Struct import Struct

from ..types.OcaProtoObjectIdentification import OcaProtoObjectIdentification as type

OcaProtoObjectIdentification = Struct(
  {
    "POno": OcaUint32,
    "ClassIdentification": OcaClassIdentification,
  },
  type
)
