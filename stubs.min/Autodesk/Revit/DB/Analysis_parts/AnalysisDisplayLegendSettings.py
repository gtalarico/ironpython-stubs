class AnalysisDisplayLegendSettings(object, IDisposable):
    """
    Contains legend settings for analysis display style element.
    
    AnalysisDisplayLegendSettings()
    AnalysisDisplayLegendSettings(other: AnalysisDisplayLegendSettings)
    """
    def Dispose(self):
        """ Dispose(self: AnalysisDisplayLegendSettings) """
        pass

    def IsEqual(self, other):
        """
        IsEqual(self: AnalysisDisplayLegendSettings, other: AnalysisDisplayLegendSettings) -> bool
        
            Compares two legend settings objects.
        
            other: Legend settings object to compare to.
            Returns: True if objects are equal, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AnalysisDisplayLegendSettings, disposing: bool) """
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
        __new__(cls: type, other: AnalysisDisplayLegendSettings)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ColorRangeHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Height of color range (for Colored Surface, Markers and Text, and Vector display). Measured in paperspace units.

Get: ColorRangeHeight(self: AnalysisDisplayLegendSettings) -> int

Set: ColorRangeHeight(self: AnalysisDisplayLegendSettings) = value
"""

    ColorRangeWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Width of color range (for Colored Surface, Markers and Text, and Vector display). Measured in paperspace units.

Get: ColorRangeWidth(self: AnalysisDisplayLegendSettings) -> int

Set: ColorRangeWidth(self: AnalysisDisplayLegendSettings) = value
"""

    HeadingTextTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Element id of text associated with legend heading.

Get: HeadingTextTypeId(self: AnalysisDisplayLegendSettings) -> ElementId

Set: HeadingTextTypeId(self: AnalysisDisplayLegendSettings) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: AnalysisDisplayLegendSettings) -> bool

"""

    NumberForScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A fixed value to display on the legend scale (0 by default; 0 means width of legend scale is calculated dynamically).

Get: NumberForScale(self: AnalysisDisplayLegendSettings) -> float

Set: NumberForScale(self: AnalysisDisplayLegendSettings) = value
"""

    NumberOfSteps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of steps (values between minimum and maximum) to be shown in legend.

Get: NumberOfSteps(self: AnalysisDisplayLegendSettings) -> int

Set: NumberOfSteps(self: AnalysisDisplayLegendSettings) = value
"""

    Rounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Rounding increment for numeric values of analysis results.

Get: Rounding(self: AnalysisDisplayLegendSettings) -> float

Set: Rounding(self: AnalysisDisplayLegendSettings) = value
"""

    ScaleHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Height of scale (for Diagram display). Measured in paperspace units.

Get: ScaleHeight(self: AnalysisDisplayLegendSettings) -> int

Set: ScaleHeight(self: AnalysisDisplayLegendSettings) = value
"""

    ShowDataDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true, data description is shown in the legend.

Get: ShowDataDescription(self: AnalysisDisplayLegendSettings) -> bool

Set: ShowDataDescription(self: AnalysisDisplayLegendSettings) = value
"""

    ShowDataName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true, data name is shown in the legend.

Get: ShowDataName(self: AnalysisDisplayLegendSettings) -> bool

Set: ShowDataName(self: AnalysisDisplayLegendSettings) = value
"""

    ShowLegend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true, legend is shown in the view.

Get: ShowLegend(self: AnalysisDisplayLegendSettings) -> bool

Set: ShowLegend(self: AnalysisDisplayLegendSettings) = value
"""

    ShowUnits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true, units are shown in the legend.

Get: ShowUnits(self: AnalysisDisplayLegendSettings) -> bool

Set: ShowUnits(self: AnalysisDisplayLegendSettings) = value
"""

    TextTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Element id of text associated with legend body.

Get: TextTypeId(self: AnalysisDisplayLegendSettings) -> ElementId

Set: TextTypeId(self: AnalysisDisplayLegendSettings) = value
"""


