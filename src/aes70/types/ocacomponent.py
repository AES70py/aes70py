"""
This file is part of aes70py.
This file has been generated.
"""
from aes70.types.Enum import Enum

# Enumeration (16-bit) for of software & firmware components in the device.
# Except for the boot loader, all other values of this enum are device-specific
# and will be specified by subclassing this class.
# @class OcaComponent
OcaComponent = Enum({
    'BootLoader': 0,
})
