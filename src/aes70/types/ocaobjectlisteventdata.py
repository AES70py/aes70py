"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaObjectListEventData:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # List of object numbers.
    objectList: list[int]


class OcaObjectListEventData(IOcaObjectListEventData):
    """
    # Event data for events returning object lists, for example the
    # **SynchronizeState** event defined in **OcaSubscriptionManager.**
    @class OcaObjectListEventData
    """
    def __init__(self, objectList: list[int]):
        # List of object numbers.
        self.objectList: list[int] = objectList