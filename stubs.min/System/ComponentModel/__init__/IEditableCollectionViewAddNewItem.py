class IEditableCollectionViewAddNewItem(IEditableCollectionView):
    """ Defines methods and properties that a System.Windows.Data.CollectionView implements to enable specifying adding items of a specific type. """
    def AddNewItem(self, newItem):
        """
        AddNewItem(self: IEditableCollectionViewAddNewItem, newItem: object) -> object
        
            Adds the specified object to the collection.
        
            newItem: The object to add to the collection.
            Returns: The object that is added to the collection.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CanAddNewItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a specified object can be added to the collection.

Get: CanAddNewItem(self: IEditableCollectionViewAddNewItem) -> bool

"""


