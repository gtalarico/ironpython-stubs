class LineProperties(object, IDisposable):
    """
    A structure that has access to the pen properties of lines/curves
       that are currently being drawn/exported via an export context
       during a custom export process.
    """
    def Dispose(self):
        """ Dispose(self: LineProperties) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LineProperties, disposing: bool) """
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

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current color used when drawing lines/curves.

Get: Color(self: LineProperties) -> Color

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: LineProperties) -> bool

"""

    LineWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current width (thickness) of the pen stroke when drawing lines/curves.

Get: LineWidth(self: LineProperties) -> float

"""

    PatternId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of the current Line pattern element used when drawing lines/curves.

Get: PatternId(self: LineProperties) -> ElementId

"""

    Transparency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current transparency level to be applied to the current color.

Get: Transparency(self: LineProperties) -> int

"""


