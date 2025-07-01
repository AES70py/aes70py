from .OcaUint16 import OcaUint16
from .Enum import Enum
from .createType import Type

def Enum16(datatype: Type):
    return Enum(datatype, OcaUint16)
