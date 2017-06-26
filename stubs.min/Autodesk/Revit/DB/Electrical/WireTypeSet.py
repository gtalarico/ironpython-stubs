class WireTypeSet(APIObject, IDisposable, IEnumerable):
    """
    A set that contains wire types.
    
    WireTypeSet()
    """
    def Clear(self):
        """
        Clear(self: WireTypeSet)
            Removes every wire type from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: WireTypeSet, item: WireType) -> bool
        
            Tests for the existence of a wire type within the set.
        
            item: The wire type to be searched for.
            Returns: The Contains method returns True if the wire type is within the set, otherwise 
             False.
        """
        pass

    def Dispose(self):
        """ Dispose(self: WireTypeSet, A_0: bool) """
        pass

    def Erase(self, item):
        """
        Erase(self: WireTypeSet, item: WireType) -> int
        
            Removes a specified wire type from the set.
        
            item: The wire type to be erased.
            Returns: The number of wire types that were erased from the set.
        """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: WireTypeSet) -> WireTypeSetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: WireTypeSet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """
        Insert(self: WireTypeSet, item: WireType) -> bool
        
            Insert the specified wire type into the set.
        
            item: The wire type to be inserted into the set.
            Returns: Returns whether the wire type was inserted into the set.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: WireTypeSet) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: WireTypeSet) -> WireTypeSetIterator
        
            Retrieve a backward moving iterator to the set.
            Returns: Returns a backward moving iterator to the set.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Test to see if the set is empty.

Get: IsEmpty(self: WireTypeSet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of wire types that are in the set.

Get: Size(self: WireTypeSet) -> int

"""


