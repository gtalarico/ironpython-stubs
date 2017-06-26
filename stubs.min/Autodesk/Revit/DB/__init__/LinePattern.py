class LinePattern(object, IDisposable):
    """
    Represents a line pattern definition.
    
    LinePattern(name: str)
    LinePattern()
    """
    def Dispose(self):
        """ Dispose(self: LinePattern) """
        pass

    def GetSegments(self):
        """
        GetSegments(self: LinePattern) -> IList[LinePatternSegment]
        
            Gets the sequence of segments that defines this line pattern.
            Returns: The sequence of segments.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LinePattern, disposing: bool) """
        pass

    def SetSegments(self, lineSegs):
        """ SetSegments(self: LinePattern, lineSegs: IList[LinePatternSegment]) """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: LinePattern) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Line pattern name.

Get: Name(self: LinePattern) -> str

Set: Name(self: LinePattern) = value
"""


