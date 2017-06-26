class TableRowGroupCollection(object, IList[TableRowGroup], ICollection[TableRowGroup], IEnumerable[TableRowGroup], IEnumerable, IList, ICollection):
    """ Provides standard facilities for creating and managing a type-safe, ordered collection of System.Windows.Documents.TableRowGroup objects. """
    def Add(self, item):
        """
        Add(self: TableRowGroupCollection, item: TableRowGroup)
            Appends a specified item to the collection.
        
            item: An item to append to the collection.
        """
        pass

    def Clear(self):
        """
        Clear(self: TableRowGroupCollection)
            Clears all items from the collection.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: TableRowGroupCollection, item: TableRowGroup) -> bool
        
            Queries for the presence of a specified item in the collection.
        
            item: An item to query for the presence of in the collection.
            Returns: true if the specified item is present in the collection; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: TableRowGroupCollection, array: Array[TableRowGroup], index: int)
            Copies the contents of the collection and inserts them into a specified System.Windows.Documents.TableRowGroup array of starting at a specified index position in the array.
        
            array: A one-dimensional System.Windows.Documents.TableRowGroup array to which the collection contents will be copied.  This array must use zero-based indexing.
            index: A zero-based index in array specifying the position at which to begin inserting the copied collection objects.
        CopyTo(self: TableRowGroupCollection, array: Array, index: int)
            Copies the contents of the collection and inserts them into a specified array starting at a specified index position in the array.
        
            array: A one-dimensional array to which the collection contents will be copied.  This array must use zero-based indexing.
            index: A zero-based index in array specifying the position at which to begin inserting the copied collection objects.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: TableRowGroupCollection, item: TableRowGroup) -> int
        
            Returns the zero-based index of specified collection item.
        
            item: A collection item to return the index of.
            Returns: The zero-based index of the specified collection item, or -1 if the specified item is not a member of the collection.
        """
        pass

    def Insert(self, index, item):
        """
        Insert(self: TableRowGroupCollection, index: int, item: TableRowGroup)
            Inserts a specified item in the collection at a specified index position.
        
            index: A zero-based index that specifies the position in the collection at which to insert item.
            item: An item to insert into the collection.
        """
        pass

    def Remove(self, item):
        """
        Remove(self: TableRowGroupCollection, item: TableRowGroup) -> bool
        
            Removes a specified item from the collection.
        
            item: An item to remove from the collection.
            Returns: true if the specified item was found and removed; otherwise, false.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: TableRowGroupCollection, index: int)
            Removes an item, specified by index, from the collection.
        
            index: A zero-based index that specifies the collection item to remove.
        """
        pass

    def RemoveRange(self, index, count):
        """
        RemoveRange(self: TableRowGroupCollection, index: int, count: int)
            Removes a range of items, specified by beginning index and count, from the collection.
        
            index: A zero-based index indicating the beginning of a range of items to remove.
            count: The number of items to remove, beginning form the position specified by index.
        """
        pass

    def TrimToSize(self):
        """
        TrimToSize(self: TableRowGroupCollection)
            Optimizes memory consumption for the collection by setting the underlying collection System.Windows.Documents.TableRowGroupCollection.Capacity equal to the 
             System.Windows.Documents.TableRowGroupCollection.Count of items currently in the collection.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[TableRowGroup], item: TableRowGroup) -> bool
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: true if the System.Object is found in the System.Collections.IList; otherwise, false.
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the pre-allocated collection item capacity for this collection.

Get: Capacity(self: TableRowGroupCollection) -> int

Set: Capacity(self: TableRowGroupCollection) = value
"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of items currently contained by the collection.

Get: Count(self: TableRowGroupCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This type or member supports the Windows Presentation Foundation (WPF) infrastructure and is not intended to be used directly from your code.

Get: IsReadOnly(self: TableRowGroupCollection) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This type or member supports the Windows Presentation Foundation (WPF) infrastructure and is not intended to be used directly from your code.

Get: IsSynchronized(self: TableRowGroupCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This type or member supports the Windows Presentation Foundation (WPF) infrastructure and is not intended to be used directly from your code.

Get: SyncRoot(self: TableRowGroupCollection) -> object

"""


