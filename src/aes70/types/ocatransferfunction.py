"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaTransferFunction:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Frequencies
    Frequency: list[int]
    # Amplitude (not in dB)
    Amplitude: list[int]
    # Phase in radians.
    Phase: list[int]


class OcaTransferFunction(IOcaTransferFunction):
    """
    # A complex (i.e. magnitude + phase) transfer function.
    @class OcaTransferFunction
    """
    def __init__(self, Frequency: list[int], Amplitude: list[int], Phase: list[int]):
        # Frequencies
        self.Frequency: list[int] = Frequency
        # Amplitude (not in dB)
        self.Amplitude: list[int] = Amplitude
        # Phase in radians.
        self.Phase: list[int] = Phase