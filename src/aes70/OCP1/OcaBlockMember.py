
from ..types.OcaObjectIdentification import OcaObjectIdentification
from ..OCP1.OcaUint32 import OcaUint32
from ..OCP1.struct import Struct
from ..types.OcaBlockMember import OcaBlockMember as type

OcaBlockMember = Struct(
  {
    "MemberObjectIdentification": OcaObjectIdentification,
    "ContainerObjectNumber": OcaUint32,
  },
  type
)
