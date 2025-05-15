"""
This file is part of aes70py.
This file has been generated.
"""
from aes70.types.Enum import Enum

# Enumeration of reasons for device reset.
# @class OcaResetCause
OcaResetCause = Enum({
    'PowerOn': 0,
    'InternalError': 1,
    'Upgrade': 2,
    'ExternalRequest': 3,
})
