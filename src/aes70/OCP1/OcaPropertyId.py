
from .OcaUint16 import OcaUint16
from .struct import Struct
from ..types.OcaPropertyId import OcaPropertyID as type

OcaPropertyID = Struct(
  {
    'DefLevel': OcaUint16,
    'PropertyIndex': OcaUint16,
  },
  type
)
