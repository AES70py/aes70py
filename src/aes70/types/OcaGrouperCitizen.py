"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaOPath import IOcaOPath, OcaOPath


class IOcaGrouperCitizen:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Index of citizen in Grouper
    Index: int
    # Object path (= hostname + object number) of the worker object that is the
    # citizen of the grouper.
    ObjectPath: IOcaOPath
    # True iff connection from grouper to citizen is healthy.
    Online: bool


class OcaGrouperCitizen(IOcaGrouperCitizen):
    """
    # Describes a citizen of a grouper. Refers to a specific worker object
    # somewhere in the media network.
    @class OcaGrouperCitizen
    """
    def __init__(self, Index: int, ObjectPath: OcaOPath, Online: bool):
        # Index of citizen in Grouper
        self.Index: int = Index
        # Object path (= hostname + object number) of the worker object that is
        # the citizen of the grouper.
        self.ObjectPath: OcaOPath = ObjectPath
        # True iff connection from grouper to citizen is healthy.
        self.Online: bool = Online