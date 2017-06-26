class ParameterMap(APIObject, IDisposable, IEnumerable):
    """
    A map that can contain a mapping of a parameter name (a String) to a parameter.
    
    ParameterMap()
    """
    def Clear(self):
        """
        Clear(self: ParameterMap)
            Removes every item from the map, rendering it empty.
        """
        pass

    def Contains(self, key):
        """
        Contains(self: ParameterMap, key: str) -> bool
        
            Tests for the existence of a key within the map.
        
            key: The key to be searched for.
            Returns: The Contains method returns True if the key is within the map, otherwise False.
        """
        pass

    def Dispose(self):
        """ Dispose(self: ParameterMap, A_0: bool) """
        pass

    def Erase(self, key):
        """
        Erase(self: ParameterMap, key: str) -> int
        
            Removes a object with the specified key from the map.
        
            key: The key of the item to be erased.
            Returns: The number of items that were erased from the map.
        """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: ParameterMap) -> ParameterMapIterator
        
            Retrieve a forward moving iterator to the map.
            Returns: Returns a forward moving iterator to the map.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ParameterMap) -> IEnumerator
        
            Retrieve a forward moving iterator to the map.
            Returns: Returns a forward moving iterator to the map.
        """
        pass

    def Insert(self, key, item):
        """
        Insert(self: ParameterMap, key: str, item: Parameter) -> bool
        
            Insert the specified item with the specified key into the map.
        
            key: The key to be used for inserting the item into the map.
            item: The item to be inserted into the map.
            Returns: Returns whether the item was inserted into the map.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ParameterMap) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: ParameterMap) -> ParameterMapIterator
        
            Retrieve a backward moving iterator to the map.
            Returns: Returns a backward moving iterator to the map.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
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

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Test to see if the map is empty.

Get: IsEmpty(self: ParameterMap) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of objects that are in the map.

Get: Size(self: ParameterMap) -> int

"""


