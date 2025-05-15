"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaModelDescription:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Name of manufacturer.
    Manufacturer: str
    # Name of this model (whatever the manufacturer wants to call it).
    Name: str
    # Text name for the version of this model, e.g. "1.2.1a".
    Version: str


class OcaModelDescription(IOcaModelDescription):
    """
    # Friendly description of this particular product model.
    @class OcaModelDescription
    """
    def __init__(self, Manufacturer: str, Name: str, Version: str):
        # Name of manufacturer.
        self.Manufacturer: str = Manufacturer
        # Name of this model (whatever the manufacturer wants to call it).
        self.Name: str = Name
        # Text name for the version of this model, e.g. "1.2.1a".
        self.Version: str = Version