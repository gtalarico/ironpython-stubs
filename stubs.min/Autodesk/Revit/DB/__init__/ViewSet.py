class ViewSet(APIObject, IDisposable, IEnumerable):
    """
    A set that contains views.
    
    ViewSet()
    """
    def Clear(self):
        """
        Clear(self: ViewSet)
            Removes every view from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: ViewSet, item: View) -> bool
        
            Tests for the existence of a view within the set.
        
            item: The view to be searched for.
            Returns: The Contains method returns True if the view is within the set, otherwise False.
        """
        pass

    def Dispose(self):
        """ Dispose(self: ViewSet, A_0: bool) """
        pass

    def Erase(self, item):
        """
        Erase(self: ViewSet, item: View) -> int
        
            Removes a specified view from the set.
        
            item: The view to be erased.
            Returns: The number of views that were erased from the set.
        """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: ViewSet) -> ViewSetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ViewSet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """
        Insert(self: ViewSet, item: View) -> bool
        
            Insert the specified view into the set.
        
            item: The view to be inserted into the set.
            Returns: Returns whether the view was inserted into the set.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: ViewSet) -> ViewSetIterator
        
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

Get: IsEmpty(self: ViewSet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of views that are in the set.

Get: Size(self: ViewSet) -> int

"""


