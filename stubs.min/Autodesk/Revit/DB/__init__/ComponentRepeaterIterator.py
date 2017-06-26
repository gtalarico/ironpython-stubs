class ComponentRepeaterIterator(object, IEnumerator[ComponentRepeaterSlot], IDisposable, IEnumerator):
    """ A slot iterator for ComponentRepeater. """
    def Dispose(self):
        """ Dispose(self: ComponentRepeaterIterator) """
        pass

    def GetCurrent(self):
        """
        GetCurrent(self: ComponentRepeaterIterator) -> ComponentRepeaterSlot
        
            Returns the current repeater slot.
            Returns: The current slot.
        """
        pass

    def IsDone(self):
        """
        IsDone(self: ComponentRepeaterIterator) -> bool
        
            Identifies if the iteration has completed.
            Returns: True if the iteration has no more items.  False if there are more items to be 
             iterated.
        """
        pass

    def MoveNext(self):
        """
        MoveNext(self: ComponentRepeaterIterator) -> bool
        
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
        """ ReleaseUnmanagedResources(self: ComponentRepeaterIterator, disposing: bool) """
        pass

    def Reset(self):
        """
        Reset(self: ComponentRepeaterIterator)
            Resets the iterator to the initial state.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ComponentRepeaterSlot](enumerator: IEnumerator[ComponentRepeaterSlot], value: ComponentRepeaterSlot) -> bool """
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

Get: Current(self: ComponentRepeaterIterator) -> ComponentRepeaterSlot

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ComponentRepeaterIterator) -> bool

"""


