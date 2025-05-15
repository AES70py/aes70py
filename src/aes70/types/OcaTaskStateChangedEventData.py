"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaLibVolIdentifier import IOcaLibVolIdentifier, OcaLibVolIdentifier
from .OcaTaskStatus import IOcaTaskStatus, OcaTaskStatus


class IOcaTaskStateChangedEventData:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # ID of Task
    TaskID: int
    # Library volume identifier of Program running in the task at the time of
    # the change, or null
    ProgramID: IOcaLibVolIdentifier
    # New task status
    Status: IOcaTaskStatus


class OcaTaskStateChangedEventData(IOcaTaskStateChangedEventData):
    """
    #
    @class OcaTaskStateChangedEventData
    """
    def __init__(self, TaskID: int, ProgramID: OcaLibVolIdentifier, Status: OcaTaskStatus):
        # ID of Task
        self.TaskID: int = TaskID
        # Library volume identifier of Program running in the task at the time
        # of the change, or null
        self.ProgramID: OcaLibVolIdentifier = ProgramID
        # New task status
        self.Status: OcaTaskStatus = Status