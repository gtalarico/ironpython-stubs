class NameScope(object, INameScopeDictionary, INameScope, IDictionary[str, object], ICollection[KeyValuePair[str, object]], IEnumerable[KeyValuePair[str, object]], IEnumerable):
    """
    Implements base WPF support for the System.Windows.Markup.INameScope methods that store or retrieve name-object mappings into a particular XAML namescope. Adds attached property support to make it simpler to get or set XAML namescope names dynamically at the element level..
    
    NameScope()
    """
    def Add(self, *__args):
        """
        Add(self: NameScope, key: str, value: object)
            Adds an item to the collection.
        
            key: The string key, which is the name of the XAML namescope mapping to add.
            value: The object value, which is the object reference of the XAML namescope mapping to add.
        Add(self: NameScope, item: KeyValuePair[str, object])
        """
        pass

    def Clear(self):
        """
        Clear(self: NameScope)
            Removes all items from the collection.
        """
        pass

    def Contains(self, item):
        """ Contains(self: NameScope, item: KeyValuePair[str, object]) -> bool """
        pass

    def ContainsKey(self, key):
        """
        ContainsKey(self: NameScope, key: str) -> bool
        
            Returns whether a provided name already exists in this System.Windows.NameScope.
        
            key: The string key to find.
            Returns: true if the specified key identifies a name for an existing mapping in this System.Windows.NameScope. false if the specified key does not exist in the current System.Windows.NameScope.
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: NameScope, array: Array[KeyValuePair[str, object]], arrayIndex: int) """
        pass

    def FindName(self, name):
        """
        FindName(self: NameScope, name: str) -> object
        
            Returns the corresponding object in the XAML namescope maintained by this System.Windows.NameScope, based on a provided name string.
        
            name: Name portion of an existing mapping to retrieve the object portion for.
            Returns: The requested object that is mapped with name. Can return null if name was provided as null or empty string, or if no matching object was found.
        """
        pass

    @staticmethod
    def GetNameScope(dependencyObject):
        """
        GetNameScope(dependencyObject: DependencyObject) -> INameScope
        
            Provides the attached property get accessor for the System.Windows.NameScope.NameScope attached property.
        
            dependencyObject: The object to get the XAML namescope from.
            Returns: A XAML namescope, as an System.Windows.Markup.INameScope instance.
        """
        pass

    def RegisterName(self, name, scopedElement):
        """
        RegisterName(self: NameScope, name: str, scopedElement: object)
            Registers a new name-object pair into the current XAML namescope.
        
            name: The name to use for mapping the given object.
            scopedElement: The object to be mapped to the provided name.
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: NameScope, key: str) -> bool
        
            Removes a mapping for a specified name from the collection.
        
            key: The string key, which is the name of the XAML namescope mapping to remove.
            Returns: true if item was successfully removed from the collection, otherwise false. Also returns false if the item was not found in the collection.
        Remove(self: NameScope, item: KeyValuePair[str, object]) -> bool
        """
        pass

    @staticmethod
    def SetNameScope(dependencyObject, value):
        """
        SetNameScope(dependencyObject: DependencyObject, value: INameScope)
            Provides the attached property set accessor for the System.Windows.NameScope.NameScope attached property.
        
            dependencyObject: Object to change XAML namescope for.
            value: The new XAML namescope, using an interface cast.
        """
        pass

    def TryGetValue(self, key, value):
        """
        TryGetValue(self: NameScope, key: str) -> (bool, object)
        
            Gets the value associated with the specified key.
        
            key: The key of the value to get.
            Returns: true if the System.Windows.NameScope contains a mapping for the name provided as key. Otherwise, false.
        """
        pass

    def UnregisterName(self, name):
        """
        UnregisterName(self: NameScope, name: str)
            Removes a name-object mapping from the XAML namescope.
        
            name: The name of the mapping to remove.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary[str, object], key: str) -> bool """
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
    """Returns the number of items in the collection of mapped names in this System.Windows.NameScope.

Get: Count(self: NameScope) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the collection is read-only.

Get: IsReadOnly(self: NameScope) -> bool

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of the keys in the System.Windows.NameScope dictionary.

Get: Keys(self: NameScope) -> ICollection[str]

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of the values in the System.Windows.NameScope dictionary.

Get: Values(self: NameScope) -> ICollection[object]

"""


    NameScopeProperty = None

