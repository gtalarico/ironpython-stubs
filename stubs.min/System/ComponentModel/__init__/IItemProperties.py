class IItemProperties:
    """ Defines a property that provides information about an object's properties. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ItemProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection that contains information about the properties that are available on the items in a collection.

Get: ItemProperties(self: IItemProperties) -> ReadOnlyCollection[ItemPropertyInfo]

"""


