from ..types.OcaPropertyId import OcaPropertyID

# /**
#  * Class representing the collection of all properties in a remote object.
#  * Returned by the {@link ObjectBase#get_properties} method inside of all remote control
#  * classes.
#  */
class Properties:
    def __init__(self, properties, level, parent):
        N = {}  # Using a dict to mimic JavaScript's Map
        P = []  # Using a list to mimic JavaScript's Array
        self.by_name = N
        self.parent = parent
        self.properties = P
        self.level = level

        for i in range(len(properties)):
            p = properties[i]
            N[p.name] = p
            # Ensure the list is long enough for the index assignment
            while len(P) <= p.index:
                P.append(None)
            P[p.index] = p

            if hasattr(p, 'aliases') and p.aliases:
                aliases = p.aliases
                for j in range(len(aliases)):
                    N[aliases[j]] = p

    # /**
    #  * Find a property.
    #  *
    #  * @param {String|OcaPropertyID} id The property identifier. Either a name
    #  *    or a :class:`OcaPropertyID`.
    #  */
    def find_property(self, id):
        if isinstance(id, OcaPropertyID):
            if id.DefLevel == self.level:
                return self.properties[id.PropertyIndex]
            elif self.parent:
                return self.parent.find_property(id)
        elif isinstance(id, str):
            p = self.by_name.get(id)
            if p:
                return p
            if self.parent:
                return self.parent.find_property(id)
        else:
            raise Exception('Expected PropertyID')

    def find_name(self, id):
        p = self.find_property(id)
        if p:
            return p.name

    # /**
    #  * Iterate all properties.
    #  *
    #  * @param {Function} callback
    #  *    Function to be called with each
    #  *    :class:`Property` as only argument.
    #  * @param {Object} [ctx]
    #  *    Optional context to call function in.
    #  */
    def forEach(self, cb, ctx=None):
        ret = self.parent.forEach(cb, ctx) if self.parent else []

        P = self.properties

        for i in range(len(P)):
            p = P[i]
            if p is not None:
                if ctx is not None:
                    # Bind the callback to the context using __get__ to simulate Function.prototype.call(ctx, p)
                    ret.append(cb.__get__(ctx)(p))
                else:
                    ret.append(cb(p))
        return ret
