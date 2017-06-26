class CommandBindingCollection(object, IList, ICollection, IEnumerable):
    """
    Represents a collection of System.Windows.Input.CommandBinding objects.
    
    CommandBindingCollection()
    CommandBindingCollection(commandBindings: IList)
    """
    def Add(self, commandBinding):
        """
        Add(self: CommandBindingCollection, commandBinding: CommandBinding) -> int
        
            Adds the specified System.Windows.Input.CommandBinding to this System.Windows.Input.CommandBindingCollection.
        
            commandBinding: The binding to add to the collection.
            Returns: 0, if the operation was successful (note that this is not the index of the added item).
        """
        pass

    def AddRange(self, collection):
        """
        AddRange(self: CommandBindingCollection, collection: ICollection)
            Adds the items of the specified System.Collections.ICollection to the end of this System.Windows.Input.CommandBindingCollection.
        
            collection: The collection of items to add to the end of this System.Windows.Input.CommandBindingCollection.
        """
        pass

    def Clear(self):
        """
        Clear(self: CommandBindingCollection)
            Removes all items from this System.Windows.Input.CommandBindingCollection.
        """
        pass

    def Contains(self, commandBinding):
        """
        Contains(self: CommandBindingCollection, commandBinding: CommandBinding) -> bool
        
            Determines whether the specified System.Windows.Input.CommandBinding is in this System.Windows.Input.CommandBindingCollection.
        
            commandBinding: The binding to locate in the collection.
            Returns: true if the specified System.Windows.Input.CommandBinding is in the collection; otherwise, false.
        """
        pass

    def CopyTo(self, commandBindings, index):
        """
        CopyTo(self: CommandBindingCollection, commandBindings: Array[CommandBinding], index: int)
            Copies all of the items in the System.Windows.Input.CommandBindingCollection to the specified one-dimensional array, starting at the specified index of the target array.
        
            commandBindings: The array into which the collection is copied.
            index: The index position in commandBindings at which copying starts.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: CommandBindingCollection) -> IEnumerator
        
            Gets an enumerator that iterates through this System.Windows.Input.CommandBindingCollection.
            Returns: The enumerator for this collection.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: CommandBindingCollection, value: CommandBinding) -> int
        
            Searches for the first occurrence of the specified System.Windows.Input.CommandBinding in this System.Windows.Input.CommandBindingCollection.
        
            value: The binding to locate in the collection.
            Returns: The index of the first occurrence of value, if found; otherwise, -1.
        """
        pass

    def Insert(self, index, commandBinding):
        """
        Insert(self: CommandBindingCollection, index: int, commandBinding: CommandBinding)
            Inserts the specified System.Windows.Input.CommandBinding into this System.Windows.Input.CommandBindingCollection at the specified index.
        
            index: The zero-based index at which to insert commandBinding
            commandBinding: The binding to insert.
        """
        pass

    def Remove(self, commandBinding):
        """
        Remove(self: CommandBindingCollection, commandBinding: CommandBinding)
            Removes the first occurrence of the specified System.Windows.Input.CommandBinding from this System.Windows.Input.CommandBindingCollection.
        
            commandBinding: The binding to remove.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: CommandBindingCollection, index: int)
            Removes the specified System.Windows.Input.CommandBinding at the specified index of this System.Windows.Input.CommandBindingCollection.
        
            index: The zero-based index of the System.Windows.Input.CommandBinding to remove.
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
    def __new__(self, commandBindings=None):
        """
        __new__(cls: type)
        __new__(cls: type, commandBindings: IList)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of System.Windows.Input.CommandBinding items in this System.Windows.Input.CommandBindingCollection.

Get: Count(self: CommandBindingCollection) -> int

"""

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this System.Windows.Input.CommandBindingCollection has a fixed size.

Get: IsFixedSize(self: CommandBindingCollection) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this System.Windows.Input.CommandBindingCollection is read-only.

Get: IsReadOnly(self: CommandBindingCollection) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether access to this System.Windows.Input.CommandBindingCollection is synchronized (thread-safe).

Get: IsSynchronized(self: CommandBindingCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that can be used to synchronize access to the System.Windows.Input.CommandBindingCollection.

Get: SyncRoot(self: CommandBindingCollection) -> object

"""


