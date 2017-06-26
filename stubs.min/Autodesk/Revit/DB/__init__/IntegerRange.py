class IntegerRange(object, IDisposable):
    """ A class to define a range of a sequence of consecutive integer numbers """
    def Dispose(self):
        """ Dispose(self: IntegerRange) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: IntegerRange, disposing: bool) """
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

    High = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The upper limit of the range

Get: High(self: IntegerRange) -> int

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: IntegerRange) -> bool

"""

    Low = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The lower limit of the range

Get: Low(self: IntegerRange) -> int

"""


