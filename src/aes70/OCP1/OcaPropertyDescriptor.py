"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaBaseDataType import OcaBaseDataType
from .OcaMethodID import OcaMethodID
from .OcaPropertyID import OcaPropertyID
from .Struct import Struct

 from ..types.OcaPropertyDescriptorimport { OcaPropertyDescriptor as type }

OcaPropertyDescriptor = Struct(
  {
    "PropertyID": OcaPropertyID,
    "BaseDataType": OcaBaseDataType,
    "GetterMethodID": OcaMethodID,
    "SetterMethodID": OcaMethodID,
  },
  type
)
