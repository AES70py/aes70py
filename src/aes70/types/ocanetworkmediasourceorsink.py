"""
This file is part of aes70py.
This file has been generated.
"""
from aes70.types.enum import Enum

# enum that describes whether a port is a source (= sends program into the
# network; "talker") or sink (=receives program from the network; "listener")
# @class OcaNetworkMediaSourceOrSink
OcaNetworkMediaSourceOrSink = Enum({
    'None': 0,
    'Source': 1,
    'Sink': 2,
})
