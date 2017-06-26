class LineSegment(object, IDisposable):
    """ An output node that represents a tessellated line segment. """
    def Dispose(self):
        """ Dispose(self: LineSegment) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LineSegment, disposing: bool) """
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
    """Parameter associated with the end point.

Get: EndParameter(self: LineSegment) -> float

"""

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """End point of the line segment.

Get: EndPoint(self: LineSegment) -> XYZ

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: LineSegment) -> bool

"""

    LineProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Access to the line (pen) properties of the line

Get: LineProperties(self: LineSegment) -> LineProperties

"""

    StartParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Parameter associated with the start point.

Get: StartParameter(self: LineSegment) -> float

"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Start point of the line segment.

Get: StartPoint(self: LineSegment) -> XYZ

"""


