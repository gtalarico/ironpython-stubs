class FontFamilyMapCollection(object, IList[FontFamilyMap], ICollection[FontFamilyMap], IEnumerable[FontFamilyMap], IEnumerable, IList, ICollection):
    """ Represents an ordered collection of System.Windows.Media.FontFamilyMap objects. """
    def Add(self, item):
        """
        Add(self: FontFamilyMapCollection, item: FontFamilyMap)
            Inserts the specified System.Windows.Media.FontFamilyMap object into the collection.
        
            item: The object to insert.
        """
        pass

    def Clear(self):
        """
        Clear(self: FontFamilyMapCollection)
            Removes all System.Windows.Media.FontFamilyMap objects from the System.Windows.Media.FontFamilyMapCollection.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: FontFamilyMapCollection, item: FontFamilyMap) -> bool
        
            Indicates whether the System.Windows.Media.FontFamilyMapCollection contains the specified System.Windows.Media.FontFamilyMap object.
        
            item: The object to locate.
            Returns: true if the collection contains item; otherwise false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: FontFamilyMapCollection, array: Array[FontFamilyMap], index: int)
            Copies the System.Windows.Media.FontFamilyMap objects in the collection into an array of FontFamilyMaps, starting at the specified index position.
        
            array: The destination array.
            index: The zero-based index position where copying begins.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: FontFamilyMapCollection) -> IEnumerator[FontFamilyMap]
        
            Returns an enumerator that can iterate through the collection.
            Returns: An enumerator that can iterate through the collection.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: FontFamilyMapCollection, item: FontFamilyMap) -> int
        
            Returns the index of the specified System.Windows.Media.FontFamilyMap object within the collection.
        
            item: The object to locate.
            Returns: The zero-based index of item, if found; otherwise -1;
        """
        pass

    def Insert(self, index, item):
        """
        Insert(self: FontFamilyMapCollection, index: int, item: FontFamilyMap)
            Inserts the specified System.Windows.Media.FontFamilyMap object at the specified index position in the collection.
        
            index: The zero-based index position to insert the object.
            item: The object to insert.
        """
        pass

    def Remove(self, item):
        """
        Remove(self: FontFamilyMapCollection, item: FontFamilyMap) -> bool
        
            Removes the specified System.Windows.Media.FontFamilyMap object from the collection.
        
            item: The object to remove.
            Returns: true if item was successfully deleted; otherwise false.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: FontFamilyMapCollection, index: int)
            Deletes a System.Windows.Media.FontFamilyMap object from the System.Windows.Media.FontFamilyMapCollection.
        
            index: The zero-based index position to remove the object.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[FontFamilyMap], item: FontFamilyMap) -> bool
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
    """Gets the number of System.Windows.Media.FontFamilyMap objects in the System.Windows.Media.FontFamilyMapCollection.

Get: Count(self: FontFamilyMapCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates if a System.Windows.Media.FontFamilyMapCollection is read only.

Get: IsReadOnly(self: FontFamilyMapCollection) -> bool

"""


