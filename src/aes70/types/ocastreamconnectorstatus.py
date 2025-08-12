"""
This file is part of aes70py.
This file has been generated.
"""
from aes70.types.enum import Enum

# Status options for a stream connector.
# @class OcaStreamConnectorStatus
OcaStreamConnectorStatus = Enum({
    'NotAvailable': 0,
    'Idle': 1,
    'Connected': 2,
    'Paused': 3,
})
