"""
This file is part of aes70py.
This file has been generated.
"""
from aes70.types.enum import Enum

# Type of string comparison.
# @class OcaStringComparisonType
OcaStringComparisonType = Enum({
    'Exact': 0,
    'Substring': 1,
    'Contains': 2,
    'ExactCaseInsensitive': 3,
    'SubstringCaseInsensitive': 4,
    'ContainsCaseInsensitive': 5,
})
