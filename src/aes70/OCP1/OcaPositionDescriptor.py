"""
This file is part of aes70py.
This file has been generated.
"""
from .FixedLengthArray import FixedLengthArray
from .OcaFloat32 import OcaFloat32
from .OcaPositionCoordinateSystem import OcaPositionCoordinateSystem
from .OcaPositionDescriptorFieldFlags import OcaPositionDescriptorFieldFlags
from .Struct import Struct

from ..types.OcaPositionDescriptor import OcaPositionDescriptor as type

OcaPositionDescriptor = Struct(
  {
    "CoordinateSystem": OcaPositionCoordinateSystem,
    "FieldFlags": OcaPositionDescriptorFieldFlags,
    "Values": FixedLengthArray(OcaFloat32, 6),
  },
  type
)
