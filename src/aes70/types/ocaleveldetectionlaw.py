"""
This file is part of aes70py.
This file has been generated.
"""
from aes70.types.enum import Enum

# Enumeration of the types of level detector characteristics. Used in dynamics
# classes and for sensors.
# @class OcaLevelDetectionLaw
OcaLevelDetectionLaw = Enum({
    'None': 0,
    'RMS': 1,
    'Peak': 2,
})
