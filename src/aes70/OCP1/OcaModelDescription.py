"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaString import OcaString
from .Struct import Struct

 from ..types.OcaModelDescriptionimport { OcaModelDescription as type }

OcaModelDescription = Struct(
  {
    "Manufacturer": OcaString,
    "Name": OcaString,
    "Version": OcaString,
  },
  type
)
