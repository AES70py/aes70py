"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaGrouperStatusChangeEventData:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Index of relevant group, or zero if event is non-group-specific.
    groupIndex: int
    # Index of citizen within given grouper, or zero if event is
    # non-citizen-specific.
    citizenIndex: int
    # Type of change.
    changeType: int


class OcaGrouperStatusChangeEventData(IOcaGrouperStatusChangeEventData):
    """
    # Class that defines the event data parameter for the **StatusChange** event
    # defined in **OcaGrouper**.
    @class OcaGrouperStatusChangeEventData
    """
    def __init__(self, groupIndex: int, citizenIndex: int, changeType: int):
        # Index of relevant group, or zero if event is non-group-specific.
        self.groupIndex: int = groupIndex
        # Index of citizen within given grouper, or zero if event is
        # non-citizen-specific.
        self.citizenIndex: int = citizenIndex
        # Type of change.
        self.changeType: int = changeType