"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaPositionDescriptor:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Type of position coordinate system - see AES70-1, section 5.5.9.
    CoordinateSystem: int
    # Which fields of the Values[] array contain valid values.
    FieldFlags: int
    # The coordinates
    Values: list[int]


class OcaPositionDescriptor(IOcaPositionDescriptor):
    """
    # A six-axis c1,c2,c3,c4,c5,c6) coordinate. For mechanical systems, these
    # axes shall be interpreted as follows:
    #
    #  - c1 = X; axial (fore-and-aft) position
    #
    #  - c2 = Y; lateral (side-to-side) position
    #
    #  - c3 = Z; vertical position
    #
    #  - c4 = rX; rotation around the X-axis, also known as *Roll*
    #
    #  - c5 = rY; rotation around the Y-axis, also known as *Pitch*
    #
    #  - c6 = rZ; rotation around the Z-axis. also known as *Yaw*
    #
    #
    # Rotation angles are measured according to the *right-hand rule:* if the
    # right hand "holds" an axis with the thumb pointing in the direction of
    # ascending coordinate values, then the fingers point in the direction of
    # ascending angle values. For GPS systems, these axes shall be interpreted
    # as follows:
    #
    #  - c1 = longitude
    #
    #  - c2 = latitude
    #
    #  - c3 = altitude
    #
    #  - c4 : not used
    #
    #  - c5 : not used
    #
    #  - c6 : not used
    #
    #
    @class OcaPositionDescriptor
    """
    def __init__(self, CoordinateSystem: int, FieldFlags: int, Values: list[int]):
        # Type of position coordinate system - see AES70-1, section 5.5.9.
        self.CoordinateSystem: int = CoordinateSystem
        # Which fields of the Values[] array contain valid values.
        self.FieldFlags: int = FieldFlags
        # The coordinates
        self.Values: list[int] = Values