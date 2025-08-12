"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaGrouperGroup:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Index of group in Grouper
    Index: int
    # Name of the group.
    Name: str
    # Object number of the group's proxy. The proxy's class is the same as the
    # Grouper's citizen class.
    ProxyONo: int


class OcaGrouperGroup(IOcaGrouperGroup):
    """
    # Describes a group in a grouper.
    @class OcaGrouperGroup
    """
    def __init__(self, Index: int, Name: str, ProxyONo: int):
        # Index of group in Grouper
        self.Index: int = Index
        # Name of the group.
        self.Name: str = Name
        # Object number of the group's proxy. The proxy's class is the same as
        # the Grouper's citizen class.
        self.ProxyONo: int = ProxyONo