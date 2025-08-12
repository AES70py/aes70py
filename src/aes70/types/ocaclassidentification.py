"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaClassIdentification:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    #
    ClassID: str
    # Version number of the class.
    ClassVersion: int


class OcaClassIdentification(IOcaClassIdentification):
    """
    #
    @class OcaClassIdentification
    """
    def __init__(self, ClassID: str, ClassVersion: int):
        #
        self.ClassID: str = ClassID
        # Version number of the class.
        self.ClassVersion: int = ClassVersion