"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaManagerDescriptor:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Object number of this manager instance.
    ObjectNumber: int
    # Name of the manager instance.
    Name: str
    # ClassID of the class from which the manager instance was created.
    ClassID: str
    # Version number of the class from which this instance was created.
    ClassVersion: int


class OcaManagerDescriptor(IOcaManagerDescriptor):
    """
    # Structure that describes a manager instance.
    @class OcaManagerDescriptor
    """
    def __init__(self, ObjectNumber: int, Name: str, ClassID: str, ClassVersion: int):
        # Object number of this manager instance.
        self.ObjectNumber: int = ObjectNumber
        # Name of the manager instance.
        self.Name: str = Name
        # ClassID of the class from which the manager instance was created.
        self.ClassID: str = ClassID
        # Version number of the class from which this instance was created.
        self.ClassVersion: int = ClassVersion