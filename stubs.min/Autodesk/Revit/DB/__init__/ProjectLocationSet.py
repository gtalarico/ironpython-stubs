class ProjectLocationSet(APIObject, IDisposable, IEnumerable):
    """
    An set that contains project locations.
    
    ProjectLocationSet()
    """
    def Clear(self):
        """
        Clear(self: ProjectLocationSet)
            Removes every project location from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: ProjectLocationSet, item: ProjectLocation) -> bool
        
            Tests for the existence of a project location within the set.
        
            item: The project location to be searched for.
            Returns: The Contains method returns True if the project location is within the set, 
             otherwise False.
        """
        pass

    def Dispose(self):
        """ Dispose(self: ProjectLocationSet, A_0: bool) """
        pass

    def Erase(self, item):
        """
        Erase(self: ProjectLocationSet, item: ProjectLocation) -> int
        
            Removes a specified project location from the set.
        
            item: The project location to be erased.
            Returns: The number of project locations that were erased from the set.
        """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: ProjectLocationSet) -> ProjectLocationSetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ProjectLocationSet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """
        Insert(self: ProjectLocationSet, item: ProjectLocation) -> bool
        
            Insert the specified project location into the set.
        
            item: The project location to be inserted into the set.
            Returns: Returns whether the project location was inserted into the set.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ProjectLocationSet) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: ProjectLocationSet) -> ProjectLocationSetIterator
        
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

Get: IsEmpty(self: ProjectLocationSet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of project locations that are in the set.

Get: Size(self: ProjectLocationSet) -> int

"""


