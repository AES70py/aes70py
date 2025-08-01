"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaEventID:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Level in tree of class which defines this event (1=root)
    DefLevel: int
    # Index of the event (in the class description).
    EventIndex: int


class OcaEventID(IOcaEventID):
    """
    # Representation of an OCA event ID. A class may define at most 255 events
    # of its own. Additional events may be inherited, so the total number may
    # exceed 255.
    @class OcaEventID
    """
    def __init__(self, DefLevel: int, EventIndex: int):
        # Level in tree of class which defines this event (1=root)
        self.DefLevel: int = DefLevel
        # Index of the event (in the class description).
        self.EventIndex: int = EventIndex