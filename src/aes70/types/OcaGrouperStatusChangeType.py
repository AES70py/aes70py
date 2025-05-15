"""
This file is part of aes70py.
This file has been generated.
"""
from aes70.types.Enum import Enum

# Enum describing status change types, as used in **OcaGrouper's StatusChange**
# event.
# @class OcaGrouperStatusChangeType
OcaGrouperStatusChangeType = Enum({
    'citizenAdded': 1,
    'citizenDeleted': 2,
    'citizenConnectionLost': 3,
    'citizenConnectionReEstablished': 4,
    'citizenError': 5,
    'enrollment': 6,
    'unEnrollment': 7,
})
