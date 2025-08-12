"""
This file is part of aes70py.
This file has been generated.
"""
from .ocablob import OcaBlob
from .ocalibvolmetadata import OcaLibVolMetadata
from .struct import Struct

from ..types.ocalibvol import OcaLibVol as type

OcaLibVol = Struct(
  {
    "Metadata": OcaLibVolMetadata,
    "Data": OcaBlob,
  },
  type
)
