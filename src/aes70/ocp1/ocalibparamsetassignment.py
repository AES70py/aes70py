"""
This file is part of aes70py.
This file has been generated.
"""
from .ocalibvolidentifier import OcaLibVolIdentifier
from .ocauint32 import OcaUint32
from .struct import Struct

from ..types.ocalibparamsetassignment import OcaLibParamSetAssignment as type

OcaLibParamSetAssignment = Struct(
  {
    "ParamSetIdentifier": OcaLibVolIdentifier,
    "TargetBlockONo": OcaUint32,
  },
  type
)
