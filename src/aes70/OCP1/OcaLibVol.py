"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaBlob import OcaBlob
from .OcaLibVolMetadata import OcaLibVolMetadata
from .Struct import Struct

from ..types.OcaLibVol import OcaLibVol as type

OcaLibVol = Struct(
  {
    "Metadata": OcaLibVolMetadata,
    "Data": OcaBlob,
  },
  type
)
