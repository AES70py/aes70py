"""
This file is part of aes70py.
This file has been generated.
"""
from aes70.types.enum import Enum

# Enumeration of classicalr filter types that can be used by OCA objects.
# @class OcaClassicalFilterShape
OcaClassicalFilterShape = Enum({
    'Butterworth': 1,
    'Bessel': 2,
    'Chebyshev': 3,
    'LinkwitzRiley': 4,
})
