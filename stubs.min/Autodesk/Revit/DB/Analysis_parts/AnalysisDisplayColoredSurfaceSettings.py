class AnalysisDisplayColoredSurfaceSettings(object, IDisposable):
    """
    Contains colored surface settings for analysis display style element.
    
    AnalysisDisplayColoredSurfaceSettings()
    AnalysisDisplayColoredSurfaceSettings(other: AnalysisDisplayColoredSurfaceSettings)
    """
    def Dispose(self):
        """ Dispose(self: AnalysisDisplayColoredSurfaceSettings) """
        pass

    def IsEqual(self, other):
        """
        IsEqual(self: AnalysisDisplayColoredSurfaceSettings, other: AnalysisDisplayColoredSurfaceSettings) -> bool
        
            Compares two colored surface settings objects.
        
            other: Colored surface settings object to compare with.
            Returns: True if objects are equal, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AnalysisDisplayColoredSurfaceSettings, disposing: bool) """
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
    def __new__(self, other=None):
        """
        __new__(cls: type)
        __new__(cls: type, other: AnalysisDisplayColoredSurfaceSettings)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    GridColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Color of grid lines.

Get: GridColor(self: AnalysisDisplayColoredSurfaceSettings) -> Color

Set: GridColor(self: AnalysisDisplayColoredSurfaceSettings) = value
"""

    GridLineWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Line weight of grid lines.

Get: GridLineWeight(self: AnalysisDisplayColoredSurfaceSettings) -> int

Set: GridLineWeight(self: AnalysisDisplayColoredSurfaceSettings) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: AnalysisDisplayColoredSurfaceSettings) -> bool

"""

    ShowContourLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true, show contour lines in the analysis display.

Get: ShowContourLines(self: AnalysisDisplayColoredSurfaceSettings) -> bool

Set: ShowContourLines(self: AnalysisDisplayColoredSurfaceSettings) = value
"""

    ShowGridLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true, show grid lines in the analysis display.

Get: ShowGridLines(self: AnalysisDisplayColoredSurfaceSettings) -> bool

Set: ShowGridLines(self: AnalysisDisplayColoredSurfaceSettings) = value
"""


