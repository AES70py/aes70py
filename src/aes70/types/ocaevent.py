"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaEventID import IOcaEventID, OcaEventID


class IOcaEvent:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Object number of the emitter.
    EmitterONo: int
    # Event ID of the subscribed event.
    EventID: IOcaEventID


class OcaEvent(IOcaEvent):
    """
    # Representation of an OCA event, i.e. the unique combination of emitter ONo
    # and the EventID.
    @class OcaEvent
    """
    def __init__(self, EmitterONo: int, EventID: OcaEventID):
        # Object number of the emitter.
        self.EmitterONo: int = EmitterONo
        # Event ID of the subscribed event.
        self.EventID: OcaEventID = EventID