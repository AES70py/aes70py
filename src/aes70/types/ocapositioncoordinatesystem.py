"""
This file is part of aes70py.
This file has been generated.
"""
from aes70.types.enum import Enum

# Enumeration that designates the type of position coordinate system used. For
# details, see the AES70-1 description of the **OcaPhysicalPosition** class.
# @class OcaPositionCoordinateSystem
OcaPositionCoordinateSystem = Enum({
    'Robotic': 1,
    'ItuAudioObjectBasedPolar': 2,
    'ItuAudioObjectBasedCartesian': 3,
    'ItuAudioSceneBasedPolar': 4,
    'ItuAudioSceneBasedCartesian': 5,
    'NAV': 6,
    'ProprietaryBase': 128,
})
