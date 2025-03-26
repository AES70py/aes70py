from aes70.OCP1.OcaUint32 import OcaUint32
from aes70.OCP1.OcaClassIdentification import OcaClassIdentification
from .struct import Struct
from ..types.OcaObjectIdentification import OcaObjectIdentification as type

OcaObjectIdentification = Struct(
    {
        "ONo": OcaUint32,
        "ClassIdentification": OcaClassIdentification,
    },
    type
)