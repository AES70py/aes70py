"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaLibVolIdentifier import OcaLibVolIdentifier
from .OcaUint32 import OcaUint32
from .Struct import Struct

 from ..types.OcaLibParamSetAssignmentimport { OcaLibParamSetAssignment as type }

OcaLibParamSetAssignment = Struct(
  {
    "ParamSetIdentifier": OcaLibVolIdentifier,
    "TargetBlockONo": OcaUint32,
  },
  type
)
