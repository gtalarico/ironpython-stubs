class SortDescriptionCollection(Collection[SortDescription], IList[SortDescription], ICollection[SortDescription], IEnumerable[SortDescription], IEnumerable, IList, ICollection, IReadOnlyList[SortDescription], IReadOnlyCollection[SortDescription], INotifyCollectionChanged):
    """
    Represents a collection of System.ComponentModel.SortDescription objects.
    
    SortDescriptionCollection()
    """
    def add_CollectionChanged(self, *args): #cannot find CLR method
        """ add_CollectionChanged(self: SortDescriptionCollection, value: NotifyCollectionChangedEventHandler) """
        pass

    def ClearItems(self, *args): #cannot find CLR method
        """
        ClearItems(self: SortDescriptionCollection)
            Removes all items from the collection.
        """
        pass

    def InsertItem(self, *args): #cannot find CLR method
        """
        InsertItem(self: SortDescriptionCollection, index: int, item: SortDescription)
            Inserts an item into the collection at the specified index.
        
            index: The zero-based index where the item is inserted.
            item: The object to insert.
        """
        pass

    def RemoveItem(self, *args): #cannot find CLR method
        """
        RemoveItem(self: SortDescriptionCollection, index: int)
            Removes the item at the specified index in the collection.
        
            index: The zero-based index of the element to remove.
        """
        pass

    def remove_CollectionChanged(self, *args): #cannot find CLR method
        """ remove_CollectionChanged(self: SortDescriptionCollection, value: NotifyCollectionChangedEventHandler) """
        pass

    def SetItem(self, *args): #cannot find CLR method
        """
        SetItem(self: SortDescriptionCollection, index: int, item: SortDescription)
            Replaces the element at the specified index.
        
            index: The zero-based index of the element to replace.
            item: The new value for the element at the specified index.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection.

"""


    Empty = None

