class RelinquishedItems(object, IDisposable):
    """ List of elements and worksets that were relinquished by the current user. """
    def Dispose(self):
        """ Dispose(self: RelinquishedItems) """
        pass

    def GetRelinquishedElements(self):
        """
        GetRelinquishedElements(self: RelinquishedItems) -> ICollection[ElementId]
        
            The elements that were relinquished by the current user.
        """
        pass

    def GetRelinquishedWorksets(self):
        """
        GetRelinquishedWorksets(self: RelinquishedItems) -> ICollection[WorksetId]
        
            The elements that were relinquished by the current user.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RelinquishedItems, disposing: bool) """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RelinquishedItems) -> bool

"""


