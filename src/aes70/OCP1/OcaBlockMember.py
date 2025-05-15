"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaObjectIdentification import OcaObjectIdentification
from .OcaUint32 import OcaUint32
from .Struct import Struct

 from ..types.OcaBlockMemberimport { OcaBlockMember as type }

OcaBlockMember = Struct(
  {
    "MemberObjectIdentification": OcaObjectIdentification,
    "ContainerObjectNumber": OcaUint32,
  },
  type
)
