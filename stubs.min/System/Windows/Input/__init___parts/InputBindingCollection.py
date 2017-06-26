class InputBindingCollection(object, IList, ICollection, IEnumerable):
    """
    Represents an ordered collection of System.Windows.Input.InputBinding objects.
    
    InputBindingCollection()
    InputBindingCollection(inputBindings: IList)
    """
    def Add(self, inputBinding):
        """
        Add(self: InputBindingCollection, inputBinding: InputBinding) -> int
        
            Adds the specified System.Windows.Input.InputBinding to this System.Windows.Input.InputBindingCollection.
        
            inputBinding: The binding to add to the collection.
            Returns: Always returns 0. This deviates from the standard System.Collections.IList implementation for Add, which should return the index where the new item was added to the collection.
        """
        pass

    def AddRange(self, collection):
        """
        AddRange(self: InputBindingCollection, collection: ICollection)
            Adds the items of the specified System.Collections.ICollection to the end of this System.Windows.Input.InputBindingCollection
        
            collection: The collection of items to add to the end of this System.Windows.Input.InputBindingCollection.
        """
        pass

    def Clear(self):
        """
        Clear(self: InputBindingCollection)
            Removes all items from this System.Windows.Input.InputBindingCollection.
        """
        pass

    def Contains(self, key):
        """
        Contains(self: InputBindingCollection, key: InputBinding) -> bool
        
            Determines whether the specified System.Windows.Input.InputBinding is in this System.Windows.Input.InputBindingCollection
        
            key: The binding to locate in the collection.
            Returns: true if the specified System.Windows.Input.InputBinding is in the collection; otherwise, false.
        """
        pass

    def CopyTo(self, inputBindings, index):
        """
        CopyTo(self: InputBindingCollection, inputBindings: Array[InputBinding], index: int)
            Copies all of the items in the System.Windows.Input.InputBindingCollection to the specified one-dimensional array, starting at the specified index of the target array.
        
            inputBindings: The array into which the collection is copied.
            index: The index position in inputBindings at which copying starts.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: InputBindingCollection) -> IEnumerator
        
            Gets an enumerator that iterates through this System.Windows.Input.InputBindingCollection.
            Returns: The enumerator for this collection.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: InputBindingCollection, value: InputBinding) -> int
        
            Searches for the first occurrence of the specified System.Windows.Input.InputBinding in his System.Windows.Input.InputBindingCollection.
        
            value: The object to locate in the collection.
                """
        pass

    def Insert(self, index, inputBinding):
        """
        Insert(self: InputBindingCollection, index: int, inputBinding: InputBinding)
            Inserts the specified System.Windows.Input.InputBinding into this System.Windows.Input.InputBindingCollection at the specified index.
        
            index: The zero-based index at which to insert inputBinding.
            inputBinding: The binding to insert.
        """
        pass

    def Remove(self, inputBinding):
        """
        Remove(self: InputBindingCollection, inputBinding: InputBinding)
            Removes the first occurrence of the specified System.Windows.Input.InputBinding from this System.Windows.Input.InputBindingCollection.
        
            inputBinding: The binding to remove.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: InputBindingCollection, index: int)
            Removes the specified System.Windows.Input.InputBinding at the specified index of this System.Windows.Input.InputBindingCollection.
        
            index: The zero-based index of the System.Windows.Input.InputBinding to remove.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
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
    def __new__(self, inputBindings=None):
        """
        __new__(cls: type)
        __new__(cls: type, inputBindings: IList)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of System.Windows.Input.InputBinding items in this collection.

Get: Count(self: InputBindingCollection) -> int

"""

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this System.Windows.Input.InputBindingCollection has a fixed size.

Get: IsFixedSize(self: InputBindingCollection) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this System.Windows.Input.InputBindingCollection is read-only.

Get: IsReadOnly(self: InputBindingCollection) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether access to this System.Windows.Input.InputBindingCollection is synchronized (thread-safe).

Get: IsSynchronized(self: InputBindingCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that can be used to synchronize access to the System.Windows.Input.InputBindingCollection.

Get: SyncRoot(self: InputBindingCollection) -> object

"""


