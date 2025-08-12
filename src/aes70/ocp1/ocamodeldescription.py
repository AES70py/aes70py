"""
This file is part of aes70py.
This file has been generated.
"""
from .ocastring import OcaString
from .struct import Struct

from ..types.ocamodeldescription import OcaModelDescription as type

OcaModelDescription = Struct(
  {
    "Manufacturer": OcaString,
    "Name": OcaString,
    "Version": OcaString,
  },
  type
)
