"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaDBr import IOcaDBr, OcaDBr


class IOcaPilotToneDetectorSpec:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Tone level threshold in dB.
    Threshold: IOcaDBr
    # Frequency of the measured tone (in Hz).
    Frequency: int
    # Poll interval in milliseconds.
    PollInterval: int


class OcaPilotToneDetectorSpec(IOcaPilotToneDetectorSpec):
    """
    # Multifield descriptor for a pilot tone detector element.
    @class OcaPilotToneDetectorSpec
    """
    def __init__(self, Threshold: OcaDBr, Frequency: int, PollInterval: int):
        # Tone level threshold in dB.
        self.Threshold: OcaDBr = Threshold
        # Frequency of the measured tone (in Hz).
        self.Frequency: int = Frequency
        # Poll interval in milliseconds.
        self.PollInterval: int = PollInterval