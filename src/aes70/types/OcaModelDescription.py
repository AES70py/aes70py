
class OcaModelDescription:
    """
    /**
     * Friendly description of this particular product model.
     * @class OcaModelDescription
     */
    """
    def __init__(self, Manufacturer: str, Name: str, Version: str):
        """
         * Name of manufacturer.
         * @type string
         """
        self.Manufacturer = Manufacturer
        """
         * Name of this model (whatever the manufacturer wants to call it).
         * @type string
         """
        self.Name = Name
        """
         * Text name for the version of this model, e.g. "1.2.1a".
         * @type string
         """
        self.Version = Version
