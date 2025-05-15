"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaMediaClockRate:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Nominal clock rate, in hertz.
    NominalRate: int
    # Pull range in hertz. Not all clock types will specify this. Use IEEE NaN
    # for unspecified value (OcaFrequency is IEEE floating-point).
    PullRange: int
    # Accuracy in ppm. Not all clock types will specify this. Use IEEE NaN for
    # unspecified value.
    Accuracy: int
    # Maximum jitter in ppm. Not all clock types will specify this. Use IEEE NaN
    # for unspecified value.
    JitterMax: int


class OcaMediaClockRate(IOcaMediaClockRate):
    """
    # Media clock nominal rate and associated parameters.
    @class OcaMediaClockRate
    """
    def __init__(self, NominalRate: int, PullRange: int, Accuracy: int, JitterMax: int):
        # Nominal clock rate, in hertz.
        self.NominalRate: int = NominalRate
        # Pull range in hertz. Not all clock types will specify this. Use IEEE
        # NaN for unspecified value (OcaFrequency is IEEE floating-point).
        self.PullRange: int = PullRange
        # Accuracy in ppm. Not all clock types will specify this. Use IEEE NaN
        # for unspecified value.
        self.Accuracy: int = Accuracy
        # Maximum jitter in ppm. Not all clock types will specify this. Use IEEE
        # NaN for unspecified value.
        self.JitterMax: int = JitterMax