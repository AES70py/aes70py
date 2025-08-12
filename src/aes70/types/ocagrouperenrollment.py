"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaGrouperEnrollment:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Grouper's index of group in which the citizen identified by CitizenIndex
    # is enrolled.
    GroupIndex: int
    # Grouper's index of a citizen enrolled in the group identified by
    # GroupIndex.
    CitizenIndex: int


class OcaGrouperEnrollment(IOcaGrouperEnrollment):
    """
    # Describes the enrollment of a citizen into a group.
    @class OcaGrouperEnrollment
    """
    def __init__(self, GroupIndex: int, CitizenIndex: int):
        # Grouper's index of group in which the citizen identified by
        # CitizenIndex is enrolled.
        self.GroupIndex: int = GroupIndex
        # Grouper's index of a citizen enrolled in the group identified by
        # GroupIndex.
        self.CitizenIndex: int = CitizenIndex