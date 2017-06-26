class ResourceDictionary(object, IDictionary, ICollection, IEnumerable, ISupportInitialize, IUriContext, INameScope):
    """
    Provides a hash table / dictionary implementation that contains WPF resources used by components and other elements of a WPF�application.
    
    ResourceDictionary()
    """
    def Add(self, key, value):
        """
        Add(self: ResourceDictionary, key: object, value: object)
            Adds a resource by key to this System.Windows.ResourceDictionary.
        
            key: The name of the key to add.
            value: The value of the resource to add.
        """
        pass

    def BeginInit(self):
        """
        BeginInit(self: ResourceDictionary)
            Begins the initialization phase for this System.Windows.ResourceDictionary.
        """
        pass

    def Clear(self):
        """
        Clear(self: ResourceDictionary)
            Clears all keys (and values) in the base System.Windows.ResourceDictionary. This does not clear any merged dictionary items.
        """
        pass

    def Contains(self, key):
        """
        Contains(self: ResourceDictionary, key: object) -> bool
        
            Determines whether the System.Windows.ResourceDictionary contains an element with the specified key.
        
            key: The key to locate in the System.Windows.ResourceDictionary.
            Returns: true if System.Windows.ResourceDictionary contains a key-value pair with the specified key; otherwise, false.
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """
        CopyTo(self: ResourceDictionary, array: Array[DictionaryEntry], arrayIndex: int)
            Copies the System.Windows.ResourceDictionary elements to a one-dimensional System.Collections.DictionaryEntry at the specified index.
        
            array: The one-dimensional array that is the destination of the System.Collections.DictionaryEntry objects copied from the System.Windows.ResourceDictionary instance. The array must have zero-based indexing.
            arrayIndex: The zero-based index of array where copying begins.
        """
        pass

    def EndInit(self):
        """
        EndInit(self: ResourceDictionary)
            Ends the initialization phase, and invalidates the previous tree such that all changes made to keys during the initialization phase can be accounted for.
        """
        pass

    def FindName(self, name):
        """
        FindName(self: ResourceDictionary, name: str) -> object
        
            Not supported by this Dictionary implementation.
        
            name: The name identifier for the object being requested.
            Returns: Always returns null.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ResourceDictionary) -> IDictionaryEnumerator
        
            Returns an System.Collections.IDictionaryEnumerator that can be used to iterate through the System.Windows.ResourceDictionary.
            Returns: A specialized enumerator for the System.Windows.ResourceDictionary.
        """
        pass

    def OnGettingValue(self, *args): #cannot find CLR method
        """ OnGettingValue(self: ResourceDictionary, key: object, value: object) -> (object, bool) """
        pass

    def RegisterName(self, name, scopedElement):
        """
        RegisterName(self: ResourceDictionary, name: str, scopedElement: object)
            Not supported by this Dictionary implementation.
        
            name: See Remarks.
            scopedElement: See Remarks.
        """
        pass

    def Remove(self, key):
        """
        Remove(self: ResourceDictionary, key: object)
            Removes the entry with the specified key from the base dictionary.
        
            key: Key of the entry to remove.
        """
        pass

    def UnregisterName(self, name):
        """
        UnregisterName(self: ResourceDictionary, name: str)
            Not supported by this Dictionary implementation.
        
            name: See Remarks
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        Contains(self: IDictionary, key: object) -> bool
        
            Determines whether the System.Collections.IDictionary object contains an element with the specified key.
        
            key: The key to locate in the System.Collections.IDictionary object.
            Returns: true if the System.Collections.IDictionary contains an element with the key; otherwise, false.
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
    """Gets the number of entries in the base System.Windows.ResourceDictionary.

Get: Count(self: ResourceDictionary) -> int

"""

    DeferrableContent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the deferrable content for this resource dictionary.

Get: DeferrableContent(self: ResourceDictionary) -> DeferrableContent

Set: DeferrableContent(self: ResourceDictionary) = value
"""

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether this System.Windows.ResourceDictionary is fixed-size.

Get: IsFixedSize(self: ResourceDictionary) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether this System.Windows.ResourceDictionary is read-only.

Get: IsReadOnly(self: ResourceDictionary) -> bool

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of all keys contained in this System.Windows.ResourceDictionary.

Get: Keys(self: ResourceDictionary) -> ICollection

"""

    MergedDictionaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of the System.Windows.ResourceDictionary dictionaries that constitute the various resource dictionaries in the merged dictionaries.

Get: MergedDictionaries(self: ResourceDictionary) -> Collection[ResourceDictionary]

"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the uniform resource identifier (URI) to load resources from.

Get: Source(self: ResourceDictionary) -> Uri

Set: Source(self: ResourceDictionary) = value
"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of all values associated with keys contained in this System.Windows.ResourceDictionary.

Get: Values(self: ResourceDictionary) -> ICollection

"""


