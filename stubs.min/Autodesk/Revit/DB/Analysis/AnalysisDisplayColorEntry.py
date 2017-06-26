class AnalysisDisplayColorEntry(object, IDisposable):
    """
    Contains one entry of intermediate colors in color settings for analysis display style.
    
    AnalysisDisplayColorEntry(color: Color)
    AnalysisDisplayColorEntry(color: Color, value: float)
    AnalysisDisplayColorEntry()
    """
    def Dispose(self):
        """ Dispose(self: AnalysisDisplayColorEntry) """
        pass

    def HasValue(self):
        """
        HasValue(self: AnalysisDisplayColorEntry) -> bool
        
            Check if color entry has associated value.
            Returns: True if entry has a value associated with it, false otherwise.
        """
        pass

    def IsEqual(self, other):
        """
        IsEqual(self: AnalysisDisplayColorEntry, other: AnalysisDisplayColorEntry) -> bool
        
            Compare color entries.
        
            other: Color entry to compare to.
            Returns: True if color entries are equal, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AnalysisDisplayColorEntry, disposing: bool) """
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
    def __new__(self, color=None, value=None):
        """
        __new__(cls: type, color: Color)
        __new__(cls: type, color: Color, value: float)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Color associated with color entry.

Get: Color(self: AnalysisDisplayColorEntry) -> Color

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: AnalysisDisplayColorEntry) -> bool

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Value associated with color entry.

Get: Value(self: AnalysisDisplayColorEntry) -> float

"""


