"""
This file is part of aes70py.
This file has been generated.
"""
from .ocacomponent import OcaComponent
from .ocauint32 import OcaUint32
from .struct import Struct

from ..types.ocaversion import OcaVersion as type

OcaVersion = Struct(
  {
    "Major": OcaUint32,
    "Minor": OcaUint32,
    "Build": OcaUint32,
    "Component": OcaComponent,
  },
  type
)
