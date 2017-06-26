class CurveExtents(object, IDisposable):
    """ Represents the start and end parameters for a curve segment. """
    def Dispose(self):
        """ Dispose(self: CurveExtents) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: CurveExtents, disposing: bool) """
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

    EndParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The end parameter of the curve extents.

Get: EndParameter(self: CurveExtents) -> float

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: CurveExtents) -> bool

"""

    StartParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The start parameter of the curve extents.

Get: StartParameter(self: CurveExtents) -> float

"""


