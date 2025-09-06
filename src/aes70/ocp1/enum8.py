from .ocauint8 import OcaUint8
from .enum import Enum
from .createtype import Type

def Enum8(datatype: Type):
    return Enum(datatype, OcaUint8)
