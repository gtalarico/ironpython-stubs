class Boolean(int):
    """ Represents a Boolean value. """
    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: object, o: object) -> bool
        __new__(cls: object) -> object
        """
        pass

