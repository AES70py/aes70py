"""
This file is part of aes70py.
This file has been generated.
"""
from aes70.types.enum import Enum

# Enum that describes whether an **OcaSensor**'s current reading value can be
# trusted, and if not, why not.
# @class OcaSensorReadingState
OcaSensorReadingState = Enum({
    'Unknown': 0,
    'Valid': 1,
    'Underrange': 2,
    'Overrange': 3,
    'Error': 4,
})
