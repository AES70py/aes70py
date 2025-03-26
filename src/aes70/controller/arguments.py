class Arguments:
    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return "aes70.controller.arguments< " + (self.values).__repr__() + " >"

    def item(self, n):
        """
        Returns an item.
        :param n: Index of the item.
        :type n: int
        """
        return self.values[n]

    @property
    def length(self):
        """
        The number of elements.
        """
        return len(self.values)



