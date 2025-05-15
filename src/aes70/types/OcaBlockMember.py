"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaObjectIdentification import IOcaObjectIdentification, OcaObjectIdentification


class IOcaBlockMember:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Object identification of a block member.
    MemberObjectIdentification: IOcaObjectIdentification
    # Object number of a the block that contains the member.
    ContainerObjectNumber: int


class OcaBlockMember(IOcaBlockMember):
    """
    # Describes an object that is a member of a block.
    @class OcaBlockMember
    """
    def __init__(self, MemberObjectIdentification: OcaObjectIdentification, ContainerObjectNumber: int):
        # Object identification of a block member.
        self.MemberObjectIdentification: OcaObjectIdentification = MemberObjectIdentification
        # Object number of a the block that contains the member.
        self.ContainerObjectNumber: int = ContainerObjectNumber