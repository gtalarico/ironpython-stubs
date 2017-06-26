class ComponentIndex(object):
    """ ComponentIndex(type: ComponentIndexType, index: int) """
    @staticmethod # known case of __new__
    def __new__(self, type, index):
        """
        __new__[ComponentIndex]() -> ComponentIndex
        
        __new__(cls: type, type: ComponentIndexType, index: int)
        """
        pass

    ComponentIndexType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentIndexType(self: ComponentIndex) -> ComponentIndexType

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: ComponentIndex) -> int

"""


    Unset = None

