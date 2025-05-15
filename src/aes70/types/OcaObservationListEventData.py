"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaObservationListEventData:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # The list of observed values that the event is reporting.
    Reading: list[int]


class OcaObservationListEventData(IOcaObservationListEventData):
    """
    # Event data for event **OcaNumericObserverList.Observation**. Note: due to
    # an error in AES70-2015, this class was not made a subclass of
    # **OcaEventData**. Therefore, this class explicitly defines the **Event**
    # property explicitly, rather than inheriting it from **OcaEventData,** as
    # other event data classes do. However, the effect is the same as for all
    # event data classes: the first property in the data structure is an
    # **OcaEvent** value.
    @class OcaObservationListEventData
    """
    def __init__(self, Reading: list[int]):
        # The list of observed values that the event is reporting.
        self.Reading: list[int] = Reading