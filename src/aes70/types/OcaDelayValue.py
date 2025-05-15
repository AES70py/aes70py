"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaDelayUnit import OcaDelayUnit


class IOcaDelayValue:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # The delay value.
    DelayValue: int
    # The unit of the delay value.
    DelayUnit: OcaDelayUnit


class OcaDelayValue(IOcaDelayValue):
    """
    # Multifield descriptor that defines a delay value element.
    @class OcaDelayValue
    """
    def __init__(self, DelayValue: int, DelayUnit: OcaDelayUnit):
        # The delay value.
        self.DelayValue: int = DelayValue
        # The unit of the delay value.
        self.DelayUnit: OcaDelayUnit = DelayUnit