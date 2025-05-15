"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaTimePTP:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # TRUE if and only if time value is negative. Absolute times are always
    # positive.
    Negative: bool
    # 48 bits of seconds
    Seconds: int
    # 32 bits of nano seconds
    Nanoseconds: int


class OcaTimePTP(IOcaTimePTP):
    """
    # An absolute or relative PTP time. Format is standard PTP format: - 48 bit
    # integer seconds - 32 bit integer nanoseconds PLUS a boolean sign
    # (positive=TRUE) field. Absolute times are always positive. Relative times
    # may be positive or negative.
    @class OcaTimePTP
    """
    def __init__(self, Negative: bool, Seconds: int, Nanoseconds: int):
        # TRUE if and only if time value is negative. Absolute times are always
        # positive.
        self.Negative: bool = Negative
        # 48 bits of seconds
        self.Seconds: int = Seconds
        # 32 bits of nano seconds
        self.Nanoseconds: int = Nanoseconds