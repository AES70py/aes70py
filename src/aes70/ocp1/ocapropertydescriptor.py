"""
This file is part of aes70py.
This file has been generated.
"""
from .ocabasedatatype import OcaBaseDataType
from .ocamethodid import OcaMethodID
from .ocapropertyid import OcaPropertyID
from .struct import Struct

from ..types.ocapropertydescriptor import OcaPropertyDescriptor as type

OcaPropertyDescriptor = Struct(
  {
    "PropertyID": OcaPropertyID,
    "BaseDataType": OcaBaseDataType,
    "GetterMethodID": OcaMethodID,
    "SetterMethodID": OcaMethodID,
  },
  type
)
