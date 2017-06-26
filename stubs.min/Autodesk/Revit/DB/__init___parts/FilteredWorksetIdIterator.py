class FilteredWorksetIdIterator(object, IEnumerator[WorksetId], IDisposable, IEnumerator):
    """ An iterator to a set of workset ids filtered by the settings of a FilteredWorksetCollector. """
    def Dispose(self):
        """ Dispose(self: FilteredWorksetIdIterator) """
        pass

    def GetCurrent(self):
        """
        GetCurrent(self: FilteredWorksetIdIterator) -> WorksetId
        
            The current workset id found by the iterator.
            Returns: The workset id.
        """
        pass

    def IsDone(self):
        """
        IsDone(self: FilteredWorksetIdIterator) -> bool
        
            Identifies if the iteration has completed.
            Returns: True if the iteration has no more matching worksets.  False if there are more 
             workset ids to be iterated.
        """
        pass

    def MoveNext(self):
        """
        MoveNext(self: FilteredWorksetIdIterator) -> bool
        
            Increments the iterator to the next workset id passing the filter.
            Returns: True if there is another available workset id passing the filter in this 
             iterator.
           False if the iterator has completed all available workset ids.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FilteredWorksetIdIterator, disposing: bool) """
        pass

    def Reset(self):
        """
        Reset(self: FilteredWorksetIdIterator)
            Resets the iterator to the beginning.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[WorksetId](enumerator: IEnumerator[WorksetId], value: WorksetId) -> bool """
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
        """ __iter__(self: IEnumerator) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the item at the current position of the iterator.

Get: Current(self: FilteredWorksetIdIterator) -> WorksetId

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FilteredWorksetIdIterator) -> bool

"""


