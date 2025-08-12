"""
This file is part of aes70py.
This file has been generated.
"""
from aes70.types.enum import Enum

# Network states.
# @class OcaApplicationNetworkState
OcaApplicationNetworkState = Enum({
    'Unknown': 0,
    'NotReady': 1,
    'Readying': 2,
    'Ready': 3,
    'Running': 4,
    'Paused': 5,
    'Stopping': 6,
    'Stopped': 7,
    'Fault': 8,
})
