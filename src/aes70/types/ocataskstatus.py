"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaTaskStatus:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # ID of the task to which this state descriptor applies.
    ID: int
    # State of the task - running, stopped, etc.
    State: int
    # Error code. Value is application-specific.
    ErrorCode: int


class OcaTaskStatus(IOcaTaskStatus):
    """
    # Status of an OcaTask: task state plus a nonspecific blob named Parameter
    # which the application can use, or not.
    #
    #  - The initial value of Parameter is null.
    #
    #  - The controller sets the value of Parameter via the Control() method.
    #
    #  - If the task's state changes due to an internal event (examples: task
    #    duration value reached; or failure due to an error), Parameter is not
    #    changed.
    #
    #
    @class OcaTaskStatus
    """
    def __init__(self, ID: int, State: int, ErrorCode: int):
        # ID of the task to which this state descriptor applies.
        self.ID: int = ID
        # State of the task - running, stopped, etc.
        self.State: int = State
        # Error code. Value is application-specific.
        self.ErrorCode: int = ErrorCode