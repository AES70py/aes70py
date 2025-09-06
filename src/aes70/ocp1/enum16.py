from .ocauint16 import OcaUint16
from .enum import Enum
from .createtype import Type

def Enum16(datatype: Type):
    return Enum(datatype, OcaUint16)
