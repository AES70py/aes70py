"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaComponent import OcaComponent
from .OcaUint32 import OcaUint32
from .Struct import Struct

 from ..types.OcaVersionimport { OcaVersion as type }

OcaVersion = Struct(
  {
    "Major": OcaUint32,
    "Minor": OcaUint32,
    "Build": OcaUint32,
    "Component": OcaComponent,
  },
  type
)
