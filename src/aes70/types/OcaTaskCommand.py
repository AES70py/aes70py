"""
This file is part of aes70py.
This file has been generated.
"""
from aes70.types.Enum import Enum

# Commands controllers can send to OcaTasks to change their states
# @class OcaTaskCommand
OcaTaskCommand = Enum({
    'None': 0,
    'Prepare': 1,
    'Enable': 2,
    'Start': 3,
    'Stop': 4,
    'Abort': 5,
    'Disable': 6,
    'Clear': 7,
})
