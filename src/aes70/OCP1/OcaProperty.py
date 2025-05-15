"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaPropertyDescriptor import OcaPropertyDescriptor
from .OcaUint32 import OcaUint32
from .Struct import Struct

 from ..types.OcaPropertyimport { OcaProperty as type }

OcaProperty = Struct(
  {
    "ONo": OcaUint32,
    "Descriptor": OcaPropertyDescriptor,
  },
  type
)
