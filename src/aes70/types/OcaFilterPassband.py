"""
This file is part of aes70py.
This file has been generated.
"""
from aes70.types.Enum import Enum

# Enumeration of passband types that can be used by OCA objects.
# @class OcaFilterPassband
OcaFilterPassband = Enum({
    'HiPass': 1,
    'LowPass': 2,
    'BandPass': 3,
    'BandReject': 4,
    'AllPass': 5,
})
