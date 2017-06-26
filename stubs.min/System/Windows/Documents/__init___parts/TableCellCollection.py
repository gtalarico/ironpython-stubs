class TableCellCollection(object, IList[TableCell], ICollection[TableCell], IEnumerable[TableCell], IEnumerable, IList, ICollection):
    """ Provides standard facilities for creating and managing a type-safe, ordered collection of System.Windows.Documents.TableCell objects. """
    def Add(self, item):
        """
        Add(self: TableCellCollection, item: TableCell)
            Appends a specified System.Windows.Documents.TableCell to the collection of table cells.
        
            item: The System.Windows.Documents.TableCell to append to the collection of table cells.
        """
        pass

    def Clear(self):
        """
        Clear(self: TableCellCollection)
            Clears all items from the collection.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: TableCellCollection, item: TableCell) -> bool
        
            Queries for the presence of a specified item in the collection.
        
            item: An item to query for the presence of in the collection.
            Returns: true if the specified item is present in the collection; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: TableCellCollection, array: Array[TableCell], index: int)
            Copies the contents of the collection and inserts them into a specified System.Windows.Documents.TableCell array of starting at a specified index position in the array.
        
            array: A one-dimensional System.Windows.Documents.TableCell array to which the collection contents will be copied. This array must use zero-based indexing.
            index: A zero-based index in array that specifies the position at which to begin inserting the copied collection objects.
        CopyTo(self: TableCellCollection, array: Array, index: int)
            Copies the contents of the collection and inserts them into a specified array starting at a specified index position in the array.
        
            array: A one-dimensional array to which the collection contents will be copied. This array must use zero-based indexing.
            index: A zero-based index in array specifying the position at which to begin inserting the copied collection objects.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: TableCellCollection, item: TableCell) -> int
        
            Returns the zero-based index of specified collection item.
        
            item: A collection item to return the index of.
            Returns: The zero-based index of the specified collection item, or -1 if the specified item is not a member of the collection.
        """
        pass

    def Insert(self, index, item):
        """
        Insert(self: TableCellCollection, index: int, item: TableCell)
            Inserts a specified item in the collection at a specified index position.
        
            index: A zero-based index that specifies the position in the collection at which to insert item.
            item: An item to insert into the collection.
        """
        pass

    def Remove(self, item):
        """
        Remove(self: TableCellCollection, item: TableCell) -> bool
        
            Removes a specified item from the collection.
        
            item: An item to remove from the collection.
            Returns: true if the specified item was found and removed; otherwise, false.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: TableCellCollection, index: int)
            Removes an item, specified by index, from the collection.
        
            index: A zero-based index that specifies the collection item to remove.
        """
        pass

    def RemoveRange(self, index, count):
        """
        RemoveRange(self: TableCellCollection, index: int, count: int)
            Removes a range of items, specified by beginning index and count, from the collection.
        
            index: A zero-based index that indicates the beginning of a range of items to remove.
            count: The number of items to remove, beginning from the position specified by index.
        """
        pass

    def TrimToSize(self):
        """
        TrimToSize(self: TableCellCollection)
            Optimizes memory consumption for the collection by setting the underlying collection System.Windows.Documents.TableCellCollection.Capacity equal to the System.Windows.Documents.TableCellCollection.Count of 
             items currently in the collection.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[TableCell], item: TableCell) -> bool
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
    """Gets or sets the preallocated collection item capacity for this collection.

Get: Capacity(self: TableCellCollection) -> int

Set: Capacity(self: TableCellCollection) = value
"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of items currently contained by the collection.

Get: Count(self: TableCellCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This type or member supports the Windows Presentation Foundation (WPF) infrastructure and is not intended to be used directly from your code.

Get: IsReadOnly(self: TableCellCollection) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This type or member supports the Windows Presentation Foundation (WPF) infrastructure and is not intended to be used directly from your code.

Get: IsSynchronized(self: TableCellCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This type or member supports the Windows Presentation Foundation (WPF) infrastructure and is not intended to be used directly from your code.

Get: SyncRoot(self: TableCellCollection) -> object

"""


