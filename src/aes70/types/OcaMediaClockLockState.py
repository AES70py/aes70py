"""
This file is part of aes70py.
This file has been generated.
"""
from aes70.types.Enum import Enum

# Lock states of media clocks.
# @class OcaMediaClockLockState
OcaMediaClockLockState = Enum({
    'Undefined': 0,
    'Locked': 1,
    'Synchronizing': 2,
    'FreeRun': 3,
    'Stopped': 4,
})
