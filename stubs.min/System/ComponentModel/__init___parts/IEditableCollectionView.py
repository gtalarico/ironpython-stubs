class IEditableCollectionView:
    """ Defines methods and properties that a System.Windows.Data.CollectionView implements to provide editing capabilities to a collection. """
    def AddNew(self):
        """
        AddNew(self: IEditableCollectionView) -> object
        
            Adds a new item to the collection.
            Returns: The new item that is added to the collection.
        """
        pass

    def CancelEdit(self):
        """
        CancelEdit(self: IEditableCollectionView)
            Ends the edit transaction and, if possible, restores the original value to the item.
        """
        pass

    def CancelNew(self):
        """
        CancelNew(self: IEditableCollectionView)
            Ends the add transaction and discards the pending new item.
        """
        pass

    def CommitEdit(self):
        """
        CommitEdit(self: IEditableCollectionView)
            Ends the edit transaction and saves the pending changes.
        """
        pass

    def CommitNew(self):
        """
        CommitNew(self: IEditableCollectionView)
            Ends the add transaction and saves the pending new item.
        """
        pass

    def EditItem(self, item):
        """
        EditItem(self: IEditableCollectionView, item: object)
            Begins an edit transaction of the specified item.
        
            item: The item to edit.
        """
        pass

    def Remove(self, item):
        """
        Remove(self: IEditableCollectionView, item: object)
            Removes the specified item from the collection.
        
            item: The item to remove.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: IEditableCollectionView, index: int)
            Removes the item at the specified position from the collection.
        
            index: The position of the item to remove.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CanAddNew = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a new item can be added to the collection.

Get: CanAddNew(self: IEditableCollectionView) -> bool

"""

    CanCancelEdit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the collection view can discard pending changes and restore the original values of an edited object.

Get: CanCancelEdit(self: IEditableCollectionView) -> bool

"""

    CanRemove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether an item can be removed from the collection.

Get: CanRemove(self: IEditableCollectionView) -> bool

"""

    CurrentAddItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the item that is being added during the current add transaction.

Get: CurrentAddItem(self: IEditableCollectionView) -> object

"""

    CurrentEditItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the item in the collection that is being edited.

Get: CurrentEditItem(self: IEditableCollectionView) -> object

"""

    IsAddingNew = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether an add transaction is in progress.

Get: IsAddingNew(self: IEditableCollectionView) -> bool

"""

    IsEditingItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether an edit transaction is in progress.

Get: IsEditingItem(self: IEditableCollectionView) -> bool

"""

    NewItemPlaceholderPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the position of the new item placeholder in the collection view.

Get: NewItemPlaceholderPosition(self: IEditableCollectionView) -> NewItemPlaceholderPosition

Set: NewItemPlaceholderPosition(self: IEditableCollectionView) = value
"""


