"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaLibVolIdentifier import IOcaLibVolIdentifier, OcaLibVolIdentifier
from .OcaTimePTP import IOcaTimePTP, OcaTimePTP


class IOcaTask:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Task ID - assigned by OcaTaskManager
    ID: int
    #
    Label: str
    # ID of program this task was given or null if it's idle.
    ProgramID: IOcaLibVolIdentifier
    # ID of group the task is in, or zero if it isn't in a group
    GroupID: int
    # Absolute or Relative time.
    TimeMode: int
    # ONo of relevant **OcaTimeSource** object or zero to use device time (see
    # **OcaDeviceTimeManager**).
    TimeSourceONo: int
    # Time at which to start task, or zero if task will be manually started. If
    # **TimeMode=Relative**, the actual event start time equals the value of
    # **StartTime** plus the absolute time that **StartTime** was most recently
    # set. Datatype shall depend on value of **TimeUnits**: - If **TimeUnits**
    # is seconds, datatype shall be **OcaTimePTP;** - If TimeUnits is samples,
    # datatype shall be **OcaUint64**. If **TimeMode=Absolute**, the actual
    # event start time equals the value of **StartTime**
    StartTime: IOcaTimePTP
    # Duration of task execution, or zero to run until complete or explicitly
    # stopped.
    Duration: IOcaTimePTP
    # Arbitrary application-specific parameters for the Task and its Program.
    ApplicationSpecificParameters: bytes


class OcaTask(IOcaTask):
    """
    # An execution thread that runs an AES70 Program. Programs are OcaLibrary
    # volumes that contain application-specific execution instructions.
    @class OcaTask
    """
    def __init__(self, ID: int, Label: str, ProgramID: OcaLibVolIdentifier, GroupID: int, TimeMode: int, TimeSourceONo: int, StartTime: OcaTimePTP, Duration: OcaTimePTP, ApplicationSpecificParameters: bytes):
        # Task ID - assigned by OcaTaskManager
        self.ID: int = ID
        #
        self.Label: str = Label
        # ID of program this task was given or null if it's idle.
        self.ProgramID: OcaLibVolIdentifier = ProgramID
        # ID of group the task is in, or zero if it isn't in a group
        self.GroupID: int = GroupID
        # Absolute or Relative time.
        self.TimeMode: int = TimeMode
        # ONo of relevant **OcaTimeSource** object or zero to use device time
        # (see **OcaDeviceTimeManager**).
        self.TimeSourceONo: int = TimeSourceONo
        # Time at which to start task, or zero if task will be manually started.
        # If **TimeMode=Relative**, the actual event start time equals the value
        # of **StartTime** plus the absolute time that **StartTime** was most
        # recently set. Datatype shall depend on value of **TimeUnits**: - If
        # **TimeUnits** is seconds, datatype shall be **OcaTimePTP;** - If
        # TimeUnits is samples, datatype shall be **OcaUint64**. If
        # **TimeMode=Absolute**, the actual event start time equals the value of
        # **StartTime**
        self.StartTime: OcaTimePTP = StartTime
        # Duration of task execution, or zero to run until complete or
        # explicitly stopped.
        self.Duration: OcaTimePTP = Duration
        # Arbitrary application-specific parameters for the Task and its
        # Program.
        self.ApplicationSpecificParameters: bytes = ApplicationSpecificParameters