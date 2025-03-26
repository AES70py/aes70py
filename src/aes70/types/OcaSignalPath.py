# /*
#  * This file has been generated.
#  */
from typing import Protocol
from OcaPort import IOcaPort, OcaPort

# export declare interface IOcaSignalPath {
class IOcaSignalPath(Protocol):
    """
    /**
     * Source port (i.e. output port) of the signal path.
     * @type OcaPort
     */
    """
    SourcePort: IOcaPort

    """
    /**
     * Sink port (i.e. input port) of the signal path.
     * @type OcaPort
     */
    """
    SinkPort: IOcaPort

# export declare class OcaSignalPath implements IOcaSignalPath {
class OcaSignalPath(IOcaSignalPath):
    """
    /**
     * Signal path between two object ports in the same device.
     * @class OcaSignalPath
     */
    """

    def __init__(self, SourcePort: OcaPort, SinkPort: OcaPort):
        # constructor(SourcePort: OcaPort, SinkPort: OcaPort);
        self.SourcePort: OcaPort = SourcePort
        self.SinkPort: OcaPort = SinkPort

    # /**
    #  * Source port (i.e. output port) of the signal path.
    #  * @type OcaPort
    #  */
    SourcePort: OcaPort

    # /**
    #  * Sink port (i.e. input port) of the signal path.
    #  * @type OcaPort
    #  */
    SinkPort: OcaPort
