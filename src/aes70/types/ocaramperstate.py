"""
This file is part of aes70py.
This file has been generated.
"""
from aes70.types.Enum import Enum

# States of the ramper. Here are the rules for ramper state change:
#
#  - A freshly-constructed ramper's state is **NotInitialized**.
#
#  - A ramper becomes **Initialized** when : The ramper is **NotInitialized**;
#    AND ** TargetProperty** has been set to a valid value; AND ** Goal** has
#    been set; AND ** Duration** has been set.
#
#  - A ramper becomes **Scheduled** when It is **Initialized**; AND **Tstart**
#    and **TimeMode** have been set; AND (T :sub:`start` + **Duration**) is in
#    the future.
#
#  - A ramper becomes **Enabled** when it is **Scheduled** AND receives an
#    *Enable* command.
#
#  - A ramper becomes **Ramping** when: It is **Enabled** and the ramp start
#    time is reached; OR It is **Initialized**, **Scheduled**, or **Enabled**
#    and a *Start* command is received.
#
#  - Completion of a ramp or Receipt of a *Halt* command causes the state to
#    become: **Scheduled**, if T :sub:`start`, Time Mode have been set; AND (T
#    :sub:`start` + Duration) is in the future. Otherwise, **Initialized.**
#
#
# @class OcaRamperState
OcaRamperState = Enum({
    'NotInitialized': 1,
    'Iniitialized': 2,
    'Scheduled': 3,
    'Enabled': 4,
    'Ramping': 5,
})
