class WireSet(APIObject, IDisposable, IEnumerable):
    """
    A set that can contain any type of object.
    
    WireSet()
    """
    def Clear(self):
        """
        Clear(self: WireSet)
            Removes every item from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """ Contains(self: WireSet, item: Wire) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: WireSet, A_0: bool) """
        pass

    def Erase(self, item):
        """ Erase(self: WireSet, item: Wire) -> int """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: WireSet) -> WireSetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: WireSet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """ Insert(self: WireSet, item: Wire) -> bool """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: WireSet) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: WireSet) -> WireSetIterator
        
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

Get: IsEmpty(self: WireSet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of objects that are in the set.

Get: Size(self: WireSet) -> int

"""


