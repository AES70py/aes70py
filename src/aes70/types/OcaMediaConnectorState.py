"""
This file is part of aes70py.
This file has been generated.
"""
from aes70.types.Enum import Enum

# Status options for a stream connector.
# @class OcaMediaConnectorState
OcaMediaConnectorState = Enum({
    'Stopped': 0,
    'SettingUp': 1,
    'Running': 2,
    'Paused': 3,
    'Fault': 4,
})
