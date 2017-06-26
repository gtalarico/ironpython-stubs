class ExportPatternTableIterator(object, IEnumerator[KeyValuePair[ExportPatternKey, ExportPatternInfo]], IDisposable, IEnumerator):
    """ An iterator to a set of Pattern table. """
    def Dispose(self):
        """ Dispose(self: ExportPatternTableIterator) """
        pass

    def IsDone(self):
        """
        IsDone(self: ExportPatternTableIterator) -> bool
        
            Identifies if the iteration has completed.
            Returns: True if the iteration has no more items.  False if there are more items to be 
             iterated.
        """
        pass

    def MoveNext(self):
        """
        MoveNext(self: ExportPatternTableIterator) -> bool
        
            Increments the iterator to the next item.
            Returns: True if there is a next available item in this iterator.
           False if the 
             iterator has completed all available items.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ExportPatternTableIterator, disposing: bool) """
        pass

    def Reset(self):
        """
        Reset(self: ExportPatternTableIterator)
            Resets the iterator to the initial state.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[KeyValuePair[ExportPatternKey, ExportPatternInfo]](enumerator: IEnumerator[KeyValuePair[ExportPatternKey, ExportPatternInfo]], value: KeyValuePair[ExportPatternKey, ExportPatternInfo]) -> bool """
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

Get: Current(self: ExportPatternTableIterator) -> KeyValuePair[ExportPatternKey, ExportPatternInfo]

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ExportPatternTableIterator) -> bool

"""


