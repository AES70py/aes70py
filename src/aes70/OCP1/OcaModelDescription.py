from aes70.types.OcaModelDescription import OcaModelDescription as OcaModelDescriptionType
from aes70.OCP1.OcaString import OcaString
from .struct import Struct

type = OcaModelDescriptionType

OcaModelDescription = Struct(
    {
        "Manufacturer": OcaString,
        "Name": OcaString,
        "Version": OcaString,
    },
    type
)