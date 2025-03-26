from aes70.types.OcaModelGUID import OcaModelGUID as OCAModelGUIDType
from aes70.OCP1.OcaBlobFixedLen import OcaBlobFixedLen
from .struct import Struct

type = OCAModelGUIDType

# Definition of OcaModelGUID (exported constant)
OcaModelGUID = Struct(
    {
        "Reserved": OcaBlobFixedLen(1),
        "MfrCode": OcaBlobFixedLen(3),
        "ModelCode": OcaBlobFixedLen(4),
    },
    type
)
