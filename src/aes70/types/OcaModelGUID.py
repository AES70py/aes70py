# No external dependencies are required for this translation.

class OcaModelGUID:
    """
     * 64 bit device type GUID.
     * @class OcaModelGUID
    """
    def __init__(self, Reserved, MfrCode, ModelCode):
        """
         * 8 reserved bits.
         * @type Uint8Array
        """
        self.Reserved = Reserved
        """
         * IEEE Manufacturer code. Unique worldwide.
         * @type Uint8Array
        """
        self.MfrCode = MfrCode
        """
         * Model code. Unique within the given manufacturer's products. May be set
         * freely by the manufacturer.
         * @type Uint8Array
        """
        self.ModelCode = ModelCode
