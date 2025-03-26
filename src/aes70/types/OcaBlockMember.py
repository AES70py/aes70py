# /*
#  * This file has been generated.
#  */
from .OcaObjectIdentification import IOcaObjectIdentification, OcaObjectIdentification


class IOcaBlockMember:
    """
    Object identification of a block member.
    @type OcaObjectIdentification: IOcaObjectIdentification

    Object number of the block that contains the member.
    @type number: int
    """
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    MemberObjectIdentification: IOcaObjectIdentification
    ContainerObjectNumber: int


class OcaBlockMember(IOcaBlockMember):
    """
    Describes an object that is a member of a block.
    @class OcaBlockMember
    """

    def __init__(self, MemberObjectIdentification: OcaObjectIdentification, ContainerObjectNumber: int):
        # Object identification of a block member.
        # @type OcaObjectIdentification
        self.MemberObjectIdentification: OcaObjectIdentification = MemberObjectIdentification

        # Object number of the block that contains the member.
        # @type number
        self.ContainerObjectNumber: int = ContainerObjectNumber
