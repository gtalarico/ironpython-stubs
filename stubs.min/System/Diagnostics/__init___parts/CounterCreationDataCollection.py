class CounterCreationDataCollection(CollectionBase, IList, ICollection, IEnumerable):
    """
    Provides a strongly typed collection of System.Diagnostics.CounterCreationData objects.
    
    CounterCreationDataCollection()
    CounterCreationDataCollection(value: CounterCreationDataCollection)
    CounterCreationDataCollection(value: Array[CounterCreationData])
    """
    def Add(self, value):
        """
        Add(self: CounterCreationDataCollection, value: CounterCreationData) -> int
        
            Adds an instance of the System.Diagnostics.CounterCreationData class to the collection.
        
            value: A System.Diagnostics.CounterCreationData object to append to the existing collection.
            Returns: The index of the new System.Diagnostics.CounterCreationData object.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: CounterCreationDataCollection, value: CounterCreationDataCollection)
            Adds the specified collection of System.Diagnostics.CounterCreationData instances to the collection.
        
            value: A collection of System.Diagnostics.CounterCreationData instances to append to the existing collection.
        AddRange(self: CounterCreationDataCollection, value: Array[CounterCreationData])
            Adds the specified array of System.Diagnostics.CounterCreationData instances to the collection.
        
            value: An array of System.Diagnostics.CounterCreationData instances to append to the existing collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: CounterCreationDataCollection, value: CounterCreationData) -> bool
        
            Determines whether a System.Diagnostics.CounterCreationData instance exists in the collection.
        
            value: The System.Diagnostics.CounterCreationData object to find in the collection.
            Returns: true if the specified System.Diagnostics.CounterCreationData object exists in the collection; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: CounterCreationDataCollection, array: Array[CounterCreationData], index: int)
            Copies the elements of the System.Diagnostics.CounterCreationData to an array, starting at the specified index of the array.
        
            array: An array of System.Diagnostics.CounterCreationData instances to add to the collection.
            index: The location at which to add the new instances.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: CounterCreationDataCollection, value: CounterCreationData) -> int
        
            Returns the index of a System.Diagnostics.CounterCreationData object in the collection.
        
            value: The System.Diagnostics.CounterCreationData object to locate in the collection.
            Returns: The zero-based index of the specified System.Diagnostics.CounterCreationData, if it is found, in the collection; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: CounterCreationDataCollection, index: int, value: CounterCreationData)
            Inserts a System.Diagnostics.CounterCreationData object into the collection, at the specified index.
        
            index: The zero-based index of the location at which the System.Diagnostics.CounterCreationData is to be inserted.
            value: The System.Diagnostics.CounterCreationData to insert into the collection.
        """
        pass

    def OnClear(self, *args): #cannot find CLR method
        """
        OnClear(self: CollectionBase)
            Performs additional custom processes when clearing the contents of the System.Collections.CollectionBase instance.
        """
        pass

    def OnClearComplete(self, *args): #cannot find CLR method
        """
        OnClearComplete(self: CollectionBase)
            Performs additional custom processes after clearing the contents of the System.Collections.CollectionBase instance.
        """
        pass

    def OnInsert(self, *args): #cannot find CLR method
        """
        OnInsert(self: CollectionBase, index: int, value: object)
            Performs additional custom processes before inserting a new element into the System.Collections.CollectionBase instance.
        
            index: The zero-based index at which to insert value.
            value: The new value of the element at index.
        """
        pass

    def OnInsertComplete(self, *args): #cannot find CLR method
        """
        OnInsertComplete(self: CollectionBase, index: int, value: object)
            Performs additional custom processes after inserting a new element into the System.Collections.CollectionBase instance.
        
            index: The zero-based index at which to insert value.
            value: The new value of the element at index.
        """
        pass

    def OnRemove(self, *args): #cannot find CLR method
        """
        OnRemove(self: CollectionBase, index: int, value: object)
            Performs additional custom processes when removing an element from the System.Collections.CollectionBase instance.
        
            index: The zero-based index at which value can be found.
            value: The value of the element to remove from index.
        """
        pass

    def OnRemoveComplete(self, *args): #cannot find CLR method
        """
        OnRemoveComplete(self: CollectionBase, index: int, value: object)
            Performs additional custom processes after removing an element from the System.Collections.CollectionBase instance.
        
            index: The zero-based index at which value can be found.
            value: The value of the element to remove from index.
        """
        pass

    def OnSet(self, *args): #cannot find CLR method
        """
        OnSet(self: CollectionBase, index: int, oldValue: object, newValue: object)
            Performs additional custom processes before setting a value in the System.Collections.CollectionBase instance.
        
            index: The zero-based index at which oldValue can be found.
            oldValue: The value to replace with newValue.
            newValue: The new value of the element at index.
        """
        pass

    def OnSetComplete(self, *args): #cannot find CLR method
        """
        OnSetComplete(self: CollectionBase, index: int, oldValue: object, newValue: object)
            Performs additional custom processes after setting a value in the System.Collections.CollectionBase instance.
        
            index: The zero-based index at which oldValue can be found.
            oldValue: The value to replace with newValue.
            newValue: The new value of the element at index.
        """
        pass

    def OnValidate(self, *args): #cannot find CLR method
        """
        OnValidate(self: CounterCreationDataCollection, value: object)
            Checks the specified object to determine whether it is a valid System.Diagnostics.CounterCreationData type.
        
            value: The object that will be validated.
        """
        pass

    def Remove(self, value):
        """
        Remove(self: CounterCreationDataCollection, value: CounterCreationData)
            Removes a System.Diagnostics.CounterCreationData object from the collection.
        
            value: The System.Diagnostics.CounterCreationData to remove from the collection.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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

    @staticmethod # known case of __new__
    def __new__(self, value=None):
        """
        __new__(cls: type)
        __new__(cls: type, value: CounterCreationDataCollection)
        __new__(cls: type, value: Array[CounterCreationData])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""


