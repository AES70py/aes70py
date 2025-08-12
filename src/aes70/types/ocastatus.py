"""
This file is part of aes70py.
This file has been generated.
"""
from aes70.types.Enum import Enum

# Standard status codes returned from method calls.
# @class OcaStatus
OcaStatus = Enum({
    'OK': 0,
    'ProtocolVersionError': 1,
    'DeviceError': 2,
    'Locked': 3,
    'BadFormat': 4,
    'BadONo': 5,
    'ParameterError': 6,
    'ParameterOutOfRange': 7,
    'NotImplemented': 8,
    'InvalidRequest': 9,
    'ProcessingFailed': 10,
    'BadMethod': 11,
    'PartiallySucceeded': 12,
    'Timeout': 13,
    'BufferOverflow': 14,
})
