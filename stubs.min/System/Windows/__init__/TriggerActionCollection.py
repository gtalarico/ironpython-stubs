class TriggerActionCollection(object, IList, ICollection, IEnumerable, IList[TriggerAction], ICollection[TriggerAction], IEnumerable[TriggerAction]):
    """
    Represents a collection of System.Windows.TriggerAction objects.
    
    TriggerActionCollection()
    TriggerActionCollection(initialSize: int)
    """
    def Add(self, value):
        """
        Add(self: TriggerActionCollection, value: TriggerAction)
            Adds an item to the collection.
        
            value: The System.Windows.TriggerAction object to add.
        """
        pass

    def Clear(self):
        """
        Clear(self: TriggerActionCollection)
            Removes all items from the collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: TriggerActionCollection, value: TriggerAction) -> bool
        
            Returns a value that indicates whether the collection contains the specified System.Windows.TriggerAction object.
        
            value: The System.Windows.TriggerAction object to locate in the collection.
            Returns: true if the System.Windows.TriggerAction object is found in the collection; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: TriggerActionCollection, array: Array[TriggerAction], index: int)
            Begins at the specified index and copies the collection items to the specified array.
        
            array: The one-dimensional array that is the destination of the items that are copied from the collection. The array must use zero-based indexing.
            index: The zero-based index in the array where copying starts.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: TriggerActionCollection) -> IEnumerator[TriggerAction]
        
            Returns an enumerator that iterates through the collection.
            Returns: An System.Collections.IEnumerator object that can be used to iterate through the collection.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: TriggerActionCollection, value: TriggerAction) -> int
        
            Returns the index of the specified item in the collection.
        
            value: The System.Windows.TriggerAction object to locate in the collection.
            Returns: The index of value if the System.Windows.TriggerAction object is found in the collection; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: TriggerActionCollection, index: int, value: TriggerAction)
            Inserts the specified item into the collection at the specified index.
        
            index: The zero-based index where the value must be inserted.
            value: The System.Windows.TriggerAction object to insert into the collection.
        """
        pass

    def Remove(self, value):
        """
        Remove(self: TriggerActionCollection, value: TriggerAction) -> bool
        
            Removes the first occurrence of the specified object from the collection.
        
            value: The System.Windows.TriggerAction object to remove from the collection.
            Returns: true if item is successfully removed; otherwise, false. This method also returns false if item was not found in the System.Windows.TriggerActionCollection.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: TriggerActionCollection, index: int)
            Removes from the collection the item that is located at the specified index.
        
            index: The zero-based index of the item to remove.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[TriggerAction], item: TriggerAction) -> bool
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

    @staticmethod # known case of __new__
    def __new__(self, initialSize=None):
        """
        __new__(cls: type)
        __new__(cls: type, initialSize: int)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of items in the collection.

Get: Count(self: TriggerActionCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the collection is read-only.

Get: IsReadOnly(self: TriggerActionCollection) -> bool

"""


