"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaClassIdentification import OcaClassIdentification
from .OcaList import OcaList
from .OcaString import OcaString
from .OcaUint32 import OcaUint32
from .Struct import Struct

 from ..types.OcaObjectSearchResultimport { OcaObjectSearchResult as type }

OcaObjectSearchResult = Struct(
  {
    "ONo": OcaUint32,
    "ClassIdentification": OcaClassIdentification,
    "ContainerPath": OcaList(OcaUint32),
    "Role": OcaString,
    "Label": OcaString,
  },
  type
)
