"""
This file is part of aes70py.
This file has been generated.
"""
from .ocaobjectidentification import OcaObjectIdentification
from .ocauint32 import OcaUint32
from .struct import Struct

from ..types.ocablockmember import OcaBlockMember as type

OcaBlockMember = Struct(
  {
    "MemberObjectIdentification": OcaObjectIdentification,
    "ContainerObjectNumber": OcaUint32,
  },
  type
)
