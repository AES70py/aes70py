"""
This file is part of aes70py.
This file has been generated.
"""
from aes70.types.Enum import Enum

# Enumeration of waveform types that can be used by OCA objects.
# @class OcaWaveformType
OcaWaveformType = Enum({
    'None': 0,
    'DC': 1,
    'Sine': 2,
    'Square': 3,
    'Impulse': 4,
    'NoisePink': 5,
    'NoiseWhite': 6,
    'PolarityTest': 7,
})
