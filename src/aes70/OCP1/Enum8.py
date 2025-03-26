from .OcaUint8 import OcaUint8
from .Enum import Enum
from .createType import Type

def Enum8(datatype: Type):
    return Enum(datatype, OcaUint8)