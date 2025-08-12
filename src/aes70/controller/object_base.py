from ..ocp1.commandrrq import CommandRrq

"""
Base class for all client-side control classes.
"""
class ObjectBase:
    def __init__(self, ObjectNumber, device):
        self.ono = ObjectNumber
        self.device = device

    # The ObjectNumber of this object.
    @property
    def ObjectNumber(self):
        return self.ono

    # The ClassVersion of this object. This is a local property.
    @property
    def ClassVersion(self):
        return self.__class__.ClassVersion

    # The ClassVersion of this object. This is a local property.
    @property
    def ClassID(self):
        return self.__class__.ClassID

    # The name of the class of this object. This is a local property.
    @property
    def ClassName(self):
        return self.__class__.ClassName

    def sendCommandRrq(self, method_level, method_index, param_count, parameters, rs):
        cmd = CommandRrq(
            self.ono,
            method_level,
            method_index,
            param_count,
            parameters
        )
        return self.device.send_command(cmd, rs)

    """
    Get the name of a given OcaPropertyID.
    @param {Types/OcaPropertyID} id
    @return {string}
    """
    def GetPropertyName(self, id):
        return self.get_properties().find_name(id)

    """
    Get the OcaPropertyID for a given name.
    @param {String} name
    @return {OcaPropertyID}
    """
    def GetPropertyID(self, name):
        p = self.get_properties().find_property(name)
        if p:
            return p.GetPropertyID()

    # @staticmethod
    # def get_properties():
    #     return None

    """
    Returns an instance of :class:`Properties` for this remote object.
    """
    def get_properties(self):
        return None
        #return self.__class__.get_properties()

    @property
    def __oca_properties__(self):
        return self.get_properties()

    """
    Returns an instance of :class:`PropertySync` for this remote object.
    """
    def GetPropertySync(self):
        p = self.__class__.GetPropertySync()
        return p(self)

    def Dispose(self):
        pass
