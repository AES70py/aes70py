"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaImpedance:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Impedance magnitude in ohms.
    Magnitude: int
    # Impedance phase in radians.
    Phase: int


class OcaImpedance(IOcaImpedance):
    """
    # Complex impedance. Expressed as a magnitude and phase.
    @class OcaImpedance
    """
    def __init__(self, Magnitude: int, Phase: int):
        # Impedance magnitude in ohms.
        self.Magnitude: int = Magnitude
        # Impedance phase in radians.
        self.Phase: int = Phase