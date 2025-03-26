from aes70.OCP1.OcaUint16 import OcaUint16
from aes70.OCP1.String16 import String16
from .struct import Struct
from ..types.OcaClassIdentification import OcaClassIdentification as type

OcaClassIdentification = Struct(
  {
    'ClassID': String16,
    'ClassVersion': OcaUint16,
  },
  type
)