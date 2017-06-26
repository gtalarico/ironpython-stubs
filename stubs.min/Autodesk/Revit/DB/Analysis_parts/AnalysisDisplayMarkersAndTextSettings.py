class AnalysisDisplayMarkersAndTextSettings(object, IDisposable):
    """
    Contains markers and text settings for analysis display style element.
    
    AnalysisDisplayMarkersAndTextSettings()
    AnalysisDisplayMarkersAndTextSettings(other: AnalysisDisplayMarkersAndTextSettings)
    """
    def Dispose(self):
        """ Dispose(self: AnalysisDisplayMarkersAndTextSettings) """
        pass

    def IsEqual(self, other):
        """
        IsEqual(self: AnalysisDisplayMarkersAndTextSettings, other: AnalysisDisplayMarkersAndTextSettings) -> bool
        
            Compares two colored surface settings objects.
        
            other: Markers and text settings object to compare with.
            Returns: True if objects are equal, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AnalysisDisplayMarkersAndTextSettings, disposing: bool) """
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
        __new__(cls: type, other: AnalysisDisplayMarkersAndTextSettings)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: AnalysisDisplayMarkersAndTextSettings) -> bool

"""

    MarkerSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Size of marker.

Get: MarkerSize(self: AnalysisDisplayMarkersAndTextSettings) -> float

Set: MarkerSize(self: AnalysisDisplayMarkersAndTextSettings) = value
"""

    MarkerType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of marker.

Get: MarkerType(self: AnalysisDisplayMarkersAndTextSettings) -> AnalysisDisplayStyleMarkerType

Set: MarkerType(self: AnalysisDisplayMarkersAndTextSettings) = value
"""

    Rounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Increment to which numeric values of analysis results are rounded in markers.

Get: Rounding(self: AnalysisDisplayMarkersAndTextSettings) -> float

Set: Rounding(self: AnalysisDisplayMarkersAndTextSettings) = value
"""

    TextLabelType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of diagram text label visualization.

Get: TextLabelType(self: AnalysisDisplayMarkersAndTextSettings) -> AnalysisDisplayStyleMarkerTextLabelType

Set: TextLabelType(self: AnalysisDisplayMarkersAndTextSettings) = value
"""

    TextTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Element id of text associated with the settings.

Get: TextTypeId(self: AnalysisDisplayMarkersAndTextSettings) -> ElementId

Set: TextTypeId(self: AnalysisDisplayMarkersAndTextSettings) = value
"""


