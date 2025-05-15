"""
This file is part of aes70py.
This file has been generated.
"""
from aes70.types.Enum import Enum

# Enumeration defining the power states that OCA devices can be in. The state is
# returned by the device's Power Manager on request.
# @class OcaPowerState
OcaPowerState = Enum({
    'None': 0,
    'Working': 1,
    'Standby': 2,
    'Off': 3,
})
