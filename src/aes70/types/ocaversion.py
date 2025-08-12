"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaVersion:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # The major version number.
    Major: int
    # The minor version number.
    Minor: int
    # The build number. May be 0 if it is not used (e.g. for a hardware
    # component).
    Build: int
    # The component.
    Component: int


class OcaVersion(IOcaVersion):
    """
    # Representation of a version number of a (hardware/software) component of a
    # device in the form of Major.Minor.Build (e.g. 1.0.123).
    @class OcaVersion
    """
    def __init__(self, Major: int, Minor: int, Build: int, Component: int):
        # The major version number.
        self.Major: int = Major
        # The minor version number.
        self.Minor: int = Minor
        # The build number. May be 0 if it is not used (e.g. for a hardware
        # component).
        self.Build: int = Build
        # The component.
        self.Component: int = Component