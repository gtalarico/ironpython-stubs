class FamilyTypefaceCollection(object, IList[FamilyTypeface], ICollection[FamilyTypeface], IEnumerable[FamilyTypeface], IEnumerable, IList, ICollection):
    """ Represents a collection of System.Windows.Media.FamilyTypeface instances. """
    def Add(self, item):
        """
        Add(self: FamilyTypefaceCollection, item: FamilyTypeface)
            Inserts the specified System.Windows.Media.FamilyTypeface object into the collection.
        
            item: The System.Windows.Media.FamilyTypeface object to insert.
        """
        pass

    def Clear(self):
        """
        Clear(self: FamilyTypefaceCollection)
            Removes all System.Windows.Media.FamilyTypeface objects from the System.Windows.Media.FamilyTypefaceCollection.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: FamilyTypefaceCollection, item: FamilyTypeface) -> bool
        
            Determines if the collection contains the specified System.Windows.Media.FamilyTypeface.
        
            item: The System.Windows.Media.FamilyTypeface object to locate.
            Returns: true if item is in the collection; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: FamilyTypefaceCollection, array: Array[FamilyTypeface], index: int)
            Copies the System.Windows.Media.FamilyTypeface objects in the collection into an array of System.Windows.Media.FamilyTypefaceCollection, starting at the specified index position.
        
            array: The destination array.
            index: The zero-based index position where copying begins.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: FamilyTypefaceCollection) -> IEnumerator[FamilyTypeface]
        
            Returns an enumerator that can iterate through the collection.
            Returns: An enumerator that can iterate through the collection.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: FamilyTypefaceCollection, item: FamilyTypeface) -> int
        
            Returns the index of the specified System.Windows.Media.FamilyTypeface object within the collection.
        
            item: The System.Windows.Media.FamilyTypeface object to locate.
            Returns: The zero-based index of item, if found; otherwise -1;
        """
        pass

    def Insert(self, index, item):
        """
        Insert(self: FamilyTypefaceCollection, index: int, item: FamilyTypeface)
            Inserts the specified System.Windows.Media.FamilyTypeface object at the specified index position in the collection.
        
            index: The zero-based index position to insert the object.
            item: The System.Windows.Media.FamilyTypeface object to insert.
        """
        pass

    def Remove(self, item):
        """
        Remove(self: FamilyTypefaceCollection, item: FamilyTypeface) -> bool
        
            Removes the specified System.Windows.Media.FamilyTypeface object from the collection.
        
            item: The System.Windows.Media.FamilyTypeface object to remove.
            Returns: true if item was successfully deleted; otherwise false.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: FamilyTypefaceCollection, index: int)
            Removes the specified System.Windows.Media.FamilyTypeface object from the collection at the specified index.
        
            index: The zero-based index position from where to delete the object.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[FamilyTypeface], item: FamilyTypeface) -> bool
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

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of System.Windows.Media.FamilyTypeface objects in the System.Windows.Media.FamilyTypefaceCollection.

Get: Count(self: FamilyTypefaceCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Windows.Media.FamilyTypefaceCollection is read-only.

Get: IsReadOnly(self: FamilyTypefaceCollection) -> bool

"""


