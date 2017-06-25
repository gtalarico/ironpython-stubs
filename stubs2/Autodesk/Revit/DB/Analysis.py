# encoding: utf-8
# module Autodesk.Revit.DB.Analysis calls itself Analysis
# from RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

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



class AnalysisDisplayColorSettings(object, IDisposable):
    """
    Contains color settings for analysis display style element.
    
    AnalysisDisplayColorSettings()
    AnalysisDisplayColorSettings(other: AnalysisDisplayColorSettings)
    """
    def AreIntermediateColorsValid(self, map):
        """ AreIntermediateColorsValid(self: AnalysisDisplayColorSettings, map: IList[AnalysisDisplayColorEntry]) -> bool """
        pass

    def Colors(self):
        """
        Colors(self: AnalysisDisplayColorSettings) -> int
        
            Get number of colors, including min, max and intermediate.
            Returns: Number of colors, including min, max and intermediate.
        """
        pass

    def Dispose(self):
        """ Dispose(self: AnalysisDisplayColorSettings) """
        pass

    def GetIntermediateColors(self):
        """
        GetIntermediateColors(self: AnalysisDisplayColorSettings) -> IList[AnalysisDisplayColorEntry]
        
            Get intermediate color entries (other than the minimum and maximum settings).
            Returns: Array of intermediate color entries.
        """
        pass

    def IsEqual(self, other):
        """
        IsEqual(self: AnalysisDisplayColorSettings, other: AnalysisDisplayColorSettings) -> bool
        
            Compares two color settings objects.
        
            other: Color settings object to compare to.
            Returns: True if objects are equal, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AnalysisDisplayColorSettings, disposing: bool) """
        pass

    def SetIntermediateColors(self, map):
        """ SetIntermediateColors(self: AnalysisDisplayColorSettings, map: IList[AnalysisDisplayColorEntry]) """
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
        __new__(cls: type, other: AnalysisDisplayColorSettings)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ColorSettingsType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Stores type of color settings

Get: ColorSettingsType(self: AnalysisDisplayColorSettings) -> AnalysisDisplayStyleColorSettingsType

Set: ColorSettingsType(self: AnalysisDisplayColorSettings) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: AnalysisDisplayColorSettings) -> bool

"""

    MaxColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Color assigned to the maximum value.

Get: MaxColor(self: AnalysisDisplayColorSettings) -> Color

Set: MaxColor(self: AnalysisDisplayColorSettings) = value
"""

    MinColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Color assigned to the minimum value.

Get: MinColor(self: AnalysisDisplayColorSettings) -> Color

Set: MinColor(self: AnalysisDisplayColorSettings) = value
"""



class AnalysisDisplayDeformedShapeSettings(object, IDisposable):
    """
    Contains deformed shape settings for analysis display style element.
    
    AnalysisDisplayDeformedShapeSettings()
    AnalysisDisplayDeformedShapeSettings(other: AnalysisDisplayDeformedShapeSettings)
    """
    def Dispose(self):
        """ Dispose(self: AnalysisDisplayDeformedShapeSettings) """
        pass

    def IsEqual(self, other):
        """
        IsEqual(self: AnalysisDisplayDeformedShapeSettings, other: AnalysisDisplayDeformedShapeSettings) -> bool
        
            Compares two deformed shape settings objects.
        
            other: Deformed shape settings object to compare with.
            Returns: True if objects are equal, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AnalysisDisplayDeformedShapeSettings, disposing: bool) """
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
        __new__(cls: type, other: AnalysisDisplayDeformedShapeSettings)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    GridColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Color of grid lines.

Get: GridColor(self: AnalysisDisplayDeformedShapeSettings) -> Color

Set: GridColor(self: AnalysisDisplayDeformedShapeSettings) = value
"""

    GridLineWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Line weight of grid lines.

Get: GridLineWeight(self: AnalysisDisplayDeformedShapeSettings) -> int

Set: GridLineWeight(self: AnalysisDisplayDeformedShapeSettings) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: AnalysisDisplayDeformedShapeSettings) -> bool

"""

    Rounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Increment to which numeric values of analysis results are rounded in deformed shape.

Get: Rounding(self: AnalysisDisplayDeformedShapeSettings) -> float

Set: Rounding(self: AnalysisDisplayDeformedShapeSettings) = value
"""

    ShowContourLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true, show contour lines in the analysis display.

Get: ShowContourLines(self: AnalysisDisplayDeformedShapeSettings) -> bool

Set: ShowContourLines(self: AnalysisDisplayDeformedShapeSettings) = value
"""

    ShowGridLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true, show grid lines in the analysis display.

Get: ShowGridLines(self: AnalysisDisplayDeformedShapeSettings) -> bool

Set: ShowGridLines(self: AnalysisDisplayDeformedShapeSettings) = value
"""

    TextLabelType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of deformed shape text visualization.

Get: TextLabelType(self: AnalysisDisplayDeformedShapeSettings) -> AnalysisDisplayStyleDeformedShapeTextLabelType

Set: TextLabelType(self: AnalysisDisplayDeformedShapeSettings) = value
"""

    TextTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Element id of text associated with the settings.

Get: TextTypeId(self: AnalysisDisplayDeformedShapeSettings) -> ElementId

Set: TextTypeId(self: AnalysisDisplayDeformedShapeSettings) = value
"""

    Transparency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Transparency percentage of deformed shape color fill on surfaces

Get: Transparency(self: AnalysisDisplayDeformedShapeSettings) -> int

Set: Transparency(self: AnalysisDisplayDeformedShapeSettings) = value
"""



class AnalysisDisplayDiagramSettings(object, IDisposable):
    """
    Contains diagram settings for analysis display style element.
    
    AnalysisDisplayDiagramSettings()
    AnalysisDisplayDiagramSettings(other: AnalysisDisplayDiagramSettings)
    """
    def Dispose(self):
        """ Dispose(self: AnalysisDisplayDiagramSettings) """
        pass

    def IsEqual(self, other):
        """
        IsEqual(self: AnalysisDisplayDiagramSettings, other: AnalysisDisplayDiagramSettings) -> bool
        
            Compares two diagram settings objects.
        
            other: Diagram settings object to compare with.
            Returns: True if objects are equal, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AnalysisDisplayDiagramSettings, disposing: bool) """
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
        __new__(cls: type, other: AnalysisDisplayDiagramSettings)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    FenceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of diagram fence visualization.

Get: FenceType(self: AnalysisDisplayDiagramSettings) -> AnalysisDisplayStyleDiagramFenceType

Set: FenceType(self: AnalysisDisplayDiagramSettings) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: AnalysisDisplayDiagramSettings) -> bool

"""

    OutlineColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Color of outline and fence lines in the diagram.

Get: OutlineColor(self: AnalysisDisplayDiagramSettings) -> Color

Set: OutlineColor(self: AnalysisDisplayDiagramSettings) = value
"""

    OutlineLineWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Line weight of outline and fence lines in the diagram.

Get: OutlineLineWeight(self: AnalysisDisplayDiagramSettings) -> int

Set: OutlineLineWeight(self: AnalysisDisplayDiagramSettings) = value
"""

    Rounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Increment to which numeric values of analysis results are rounded in diagram.

Get: Rounding(self: AnalysisDisplayDiagramSettings) -> float

Set: Rounding(self: AnalysisDisplayDiagramSettings) = value
"""

    TextLabelType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of diagram text label visualization.

Get: TextLabelType(self: AnalysisDisplayDiagramSettings) -> AnalysisDisplayStyleDiagramTextLabelType

Set: TextLabelType(self: AnalysisDisplayDiagramSettings) = value
"""

    TextTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Element id of text associated with the settings.

Get: TextTypeId(self: AnalysisDisplayDiagramSettings) -> ElementId

Set: TextTypeId(self: AnalysisDisplayDiagramSettings) = value
"""

    Transparency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Transparency percentage of diagram color fill

Get: Transparency(self: AnalysisDisplayDiagramSettings) -> int

Set: Transparency(self: AnalysisDisplayDiagramSettings) = value
"""



class AnalysisDisplayLegend(Element, IDisposable):
    """ The legend that describes an Analysis Visualization. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The height, in sheet size, of the legend's rectangle

Get: Height(self: AnalysisDisplayLegend) -> float

Set: Height(self: AnalysisDisplayLegend) = value
"""



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



class AnalysisDisplayStyle(Element, IDisposable):
    """ Exposes API for manipulation of analysis display style. """
    @staticmethod
    def CreateAnalysisDisplayStyle(document, name, *__args):
        """
        CreateAnalysisDisplayStyle(document: Document, name: str, markersAndTextSettings: AnalysisDisplayMarkersAndTextSettings, colorSettings: AnalysisDisplayColorSettings, legendSettings: AnalysisDisplayLegendSettings) -> AnalysisDisplayStyle
        
            Factory method - creates analysis display style object of type Markers and Text 
             for the given document.
        
        
            document: Document for which analysis display style object is created.
            name: Name of the analysis display style within the %document%.
            markersAndTextSettings: Markers and text settings for the style.
            colorSettings: Color settings for the style.
            legendSettings: Legend settings for the style.
            Returns: New analysis display style object.
        CreateAnalysisDisplayStyle(document: Document, name: str, coloredSurfaceSettings: AnalysisDisplayColoredSurfaceSettings, colorSettings: AnalysisDisplayColorSettings, legendSettings: AnalysisDisplayLegendSettings) -> AnalysisDisplayStyle
        
            Factory method - creates analysis display style object of type Colored Surface 
             for the given document.
        
        
            document: Document for which analysis display style object is created.
            name: Name of the analysis display style within the %document%.
            coloredSurfaceSettings: Colored surface settings for the style.
            colorSettings: Color settings for the style.
            legendSettings: Legend settings for the style.
            Returns: New analysis display style object.
        CreateAnalysisDisplayStyle(document: Document, name: str, diagramSettings: AnalysisDisplayDiagramSettings, colorSettings: AnalysisDisplayColorSettings, legendSettings: AnalysisDisplayLegendSettings) -> AnalysisDisplayStyle
        
            Factory method - creates analysis display style object of type Diagram for the 
             given document.
        
        
            document: Document for which analysis display style object is created.
            name: Name of the analysis display style within the %document%.
            diagramSettings: Diagram settings for the style.
            colorSettings: Color settings for the style.
            legendSettings: Legend settings for the style.
            Returns: New analysis display style object.
        CreateAnalysisDisplayStyle(document: Document, name: str, deformedShapeSettings: AnalysisDisplayDeformedShapeSettings, colorSettings: AnalysisDisplayColorSettings, legendSettings: AnalysisDisplayLegendSettings) -> AnalysisDisplayStyle
        
            Factory method - creates analysis display style object of type Deformed Shape 
             for the given document.
        
        
            document: Document for which analysis display style object is created.
            name: Name of the analysis display style within the %document%.
            deformedShapeSettings: Deformed Shape settings for the style.
            colorSettings: Color settings for the style.
            legendSettings: Legend settings for the style.
            Returns: New analysis display style object.
        CreateAnalysisDisplayStyle(document: Document, name: str, vectorSettings: AnalysisDisplayVectorSettings, colorSettings: AnalysisDisplayColorSettings, legendSettings: AnalysisDisplayLegendSettings) -> AnalysisDisplayStyle
        
            Factory method - creates analysis display style object of type Vectors for the 
             given document.
        
        
            document: Document for which analysis display style object is created.
            name: Name of the analysis display style within the %document%.
            vectorSettings: Vector settings for the style.
            colorSettings: Color settings for the style.
            legendSettings: Legend settings for the style.
            Returns: New analysis display style object.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    @staticmethod
    def FindByName(document, name):
        """
        FindByName(document: Document, name: str) -> ElementId
        
            Finds analysis display style by name.
        
            document: Document in which to look for analysis display style element.
            name: Name of analysis display style to look for.
            Returns: Element id of the found analysis display style, invalidElementId if not found.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetColoredSurfaceSettings(self):
        """
        GetColoredSurfaceSettings(self: AnalysisDisplayStyle) -> AnalysisDisplayColoredSurfaceSettings
        
            Get colored surface settings object from the style.
        """
        pass

    def GetColorSettings(self):
        """
        GetColorSettings(self: AnalysisDisplayStyle) -> AnalysisDisplayColorSettings
        
            Get color settings object from the style.
        """
        pass

    def GetDeformedShapeSettings(self):
        """
        GetDeformedShapeSettings(self: AnalysisDisplayStyle) -> AnalysisDisplayDeformedShapeSettings
        
            Get deformed shape settings object from the style.
        """
        pass

    def GetDiagramSettings(self):
        """
        GetDiagramSettings(self: AnalysisDisplayStyle) -> AnalysisDisplayDiagramSettings
        
            Get diagram settings object from the style.
        """
        pass

    @staticmethod
    def GetElements(document):
        """
        GetElements(document: Document) -> ICollection[ElementId]
        
            Returns set of all analysis display styles elements in the given document.
        
            document: Document from which analysis display style elements are retrieved.
            Returns: All analysis display style elements existing in the document.
        """
        pass

    def GetLegendSettings(self):
        """
        GetLegendSettings(self: AnalysisDisplayStyle) -> AnalysisDisplayLegendSettings
        
            Get legend settings object from the style.
        """
        pass

    def GetMarkersAndTextSettings(self):
        """
        GetMarkersAndTextSettings(self: AnalysisDisplayStyle) -> AnalysisDisplayMarkersAndTextSettings
        
            Get markers and text settings object from the style.
        """
        pass

    def GetVectorSettings(self):
        """
        GetVectorSettings(self: AnalysisDisplayStyle) -> AnalysisDisplayVectorSettings
        
            Get vector settings object from the style.
        """
        pass

    def HasColoredSurfaceSettings(self):
        """
        HasColoredSurfaceSettings(self: AnalysisDisplayStyle) -> bool
        
            If true style has colored surface settings.
        """
        pass

    def HasDeformedShapeSettings(self):
        """
        HasDeformedShapeSettings(self: AnalysisDisplayStyle) -> bool
        
            If true style has deformed shape settings.
        """
        pass

    def HasDiagramSettings(self):
        """
        HasDiagramSettings(self: AnalysisDisplayStyle) -> bool
        
            If true style has diagram settings.
        """
        pass

    def HasMarkersAndTextSettings(self):
        """
        HasMarkersAndTextSettings(self: AnalysisDisplayStyle) -> bool
        
            If true style has markers and text settings.
        """
        pass

    def HasVectorSettings(self):
        """
        HasVectorSettings(self: AnalysisDisplayStyle) -> bool
        
            If true style has vector settings.
        """
        pass

    @staticmethod
    def IsNameUnique(document, name, excludedElement):
        """
        IsNameUnique(document: Document, name: str, excludedElement: AnalysisDisplayStyle) -> bool
        
            Verify the uniqueness of the name among all analysis display style elements of 
             the document.
        
        
            document: Document in which name uniqueness is verified.
            name: Name to verify uniqueness of.
            excludedElement: Element to be excluded from uniqueness verification (for renaming of an 
             existing element).
        
            Returns: True if name is unique, false otherwise.
        """
        pass

    @staticmethod
    def IsTextTypeIdValid(textTypeId, doc):
        """
        IsTextTypeIdValid(textTypeId: ElementId, doc: Document) -> bool
        
            Verify if text type id is valid.
        
            textTypeId: Text type id to be validated.
            doc: Document for which %textTypeId% is validated.
            Returns: True if text type id is valid, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def SetColoredSurfaceSettings(self, coloredSurfaceSettings):
        """
        SetColoredSurfaceSettings(self: AnalysisDisplayStyle, coloredSurfaceSettings: AnalysisDisplayColoredSurfaceSettings)
            Set colored surface settings object for the style.
        """
        pass

    def SetColorSettings(self, colorSettings):
        """
        SetColorSettings(self: AnalysisDisplayStyle, colorSettings: AnalysisDisplayColorSettings)
            Set color settings object for the style.
        """
        pass

    def SetDeformedShapeSettings(self, deformedShapeSettings):
        """
        SetDeformedShapeSettings(self: AnalysisDisplayStyle, deformedShapeSettings: AnalysisDisplayDeformedShapeSettings)
            Set deformed shape settings object for the style.
        """
        pass

    def SetDiagramSettings(self, diagramSettings):
        """
        SetDiagramSettings(self: AnalysisDisplayStyle, diagramSettings: AnalysisDisplayDiagramSettings)
            Set diagram settings object for the style.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetLegendSettings(self, legendSettings):
        """
        SetLegendSettings(self: AnalysisDisplayStyle, legendSettings: AnalysisDisplayLegendSettings)
            Set legend settings object for the style.
        """
        pass

    def SetMarkersAndTextSettings(self, markersAndTextSettings):
        """
        SetMarkersAndTextSettings(self: AnalysisDisplayStyle, markersAndTextSettings: AnalysisDisplayMarkersAndTextSettings)
            Set markers and text settings object for the style.
        """
        pass

    def SetName(self, name):
        """
        SetName(self: AnalysisDisplayStyle, name: str)
            Set name of analysis display style element.
        
            name: Analysis display style element name to be set.
        """
        pass

    def SetVectorSettings(self, vectorSettings):
        """
        SetVectorSettings(self: AnalysisDisplayStyle, vectorSettings: AnalysisDisplayVectorSettings)
            Set vector settings object for the style.
        """
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


class AnalysisDisplayStyleColorSettingsType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines types for color settings of analysis display style.
    
    enum AnalysisDisplayStyleColorSettingsType, values: GradientColor (0), SolidColorRanges (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    GradientColor = None
    SolidColorRanges = None
    value__ = None


class AnalysisDisplayStyleDeformedShapeTextLabelType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines text visualization types for deformed shape settings of analysis display style.
    
    enum AnalysisDisplayStyleDeformedShapeTextLabelType, values: ShowAll (0), ShowNone (1), ShowPredefined (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ShowAll = None
    ShowNone = None
    ShowPredefined = None
    value__ = None


class AnalysisDisplayStyleDiagramFenceType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines fence visualization types for diagram settings of analysis display style.
    
    enum AnalysisDisplayStyleDiagramFenceType, values: ShowAll (0), ShowNone (1), ShowPredefined (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ShowAll = None
    ShowNone = None
    ShowPredefined = None
    value__ = None


class AnalysisDisplayStyleDiagramTextLabelType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines text label visualization types for diagram settings of analysis display style.
    
    enum AnalysisDisplayStyleDiagramTextLabelType, values: ShowAll (0), ShowNone (1), ShowPredefined (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ShowAll = None
    ShowNone = None
    ShowPredefined = None
    value__ = None


class AnalysisDisplayStyleMarkerTextLabelType(Enum, IComparable, IFormattable, IConvertible):
    """
    Text label visualization types for Markers and Text settings of analysis display style.
    
    enum AnalysisDisplayStyleMarkerTextLabelType, values: ShowAll (0), ShowNone (1), ShowPredefined (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ShowAll = None
    ShowNone = None
    ShowPredefined = None
    value__ = None


class AnalysisDisplayStyleMarkerType(Enum, IComparable, IFormattable, IConvertible):
    """
    Marker types for Markers and Text settings of analysis display style.
    
    enum AnalysisDisplayStyleMarkerType, values: Circle (0), Square (1), Triangle (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Circle = None
    Square = None
    Triangle = None
    value__ = None


class AnalysisDisplayStyleVectorArrowheadScale(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines arrow head scaling for vector settings of analysis display style.
    
    enum AnalysisDisplayStyleVectorArrowheadScale, values: Length10Percent (2), Length15Percent (3), Length20Percent (4), Length5Percent (1), NoScaling (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Length10Percent = None
    Length15Percent = None
    Length20Percent = None
    Length5Percent = None
    NoScaling = None
    value__ = None


class AnalysisDisplayStyleVectorOrientation(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines vector orientation for vector settings of analysis display style.
    
    enum AnalysisDisplayStyleVectorOrientation, values: ArcAroundVectorAxis (1), Linear (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ArcAroundVectorAxis = None
    Linear = None
    value__ = None


class AnalysisDisplayStyleVectorPosition(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines vector position for vector settings of analysis display style.
    
    enum AnalysisDisplayStyleVectorPosition, values: FromDataPoint (1), ToDataPoint (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FromDataPoint = None
    ToDataPoint = None
    value__ = None


class AnalysisDisplayStyleVectorTextType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines text visualization types for vector settings of analysis display style.
    
    enum AnalysisDisplayStyleVectorTextType, values: ShowAll (0), ShowNone (1), ShowPredefined (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ShowAll = None
    ShowNone = None
    ShowPredefined = None
    value__ = None


class AnalysisDisplayVectorSettings(object, IDisposable):
    """
    Contains vector settings for analysis display style element.
    
    AnalysisDisplayVectorSettings()
    AnalysisDisplayVectorSettings(other: AnalysisDisplayVectorSettings)
    """
    def Dispose(self):
        """ Dispose(self: AnalysisDisplayVectorSettings) """
        pass

    def IsEqual(self, other):
        """
        IsEqual(self: AnalysisDisplayVectorSettings, other: AnalysisDisplayVectorSettings) -> bool
        
            Compares two vector settings objects.
        
            other: Vector settings object to compare with.
            Returns: True if objects are equal, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AnalysisDisplayVectorSettings, disposing: bool) """
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
        __new__(cls: type, other: AnalysisDisplayVectorSettings)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ArrowheadScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of arrow head scaling.

Get: ArrowheadScale(self: AnalysisDisplayVectorSettings) -> AnalysisDisplayStyleVectorArrowheadScale

Set: ArrowheadScale(self: AnalysisDisplayVectorSettings) = value
"""

    ArrowLineWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Line weight assigned to arrow lines for vectors.

Get: ArrowLineWeight(self: AnalysisDisplayVectorSettings) -> int

Set: ArrowLineWeight(self: AnalysisDisplayVectorSettings) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: AnalysisDisplayVectorSettings) -> bool

"""

    Rounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Increment to which numeric values of analysis results are rounded in vectors.

Get: Rounding(self: AnalysisDisplayVectorSettings) -> float

Set: Rounding(self: AnalysisDisplayVectorSettings) = value
"""

    TextTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Element id of text associated with the settings.

Get: TextTypeId(self: AnalysisDisplayVectorSettings) -> ElementId

Set: TextTypeId(self: AnalysisDisplayVectorSettings) = value
"""

    VectorOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Vector orientation.

Get: VectorOrientation(self: AnalysisDisplayVectorSettings) -> AnalysisDisplayStyleVectorOrientation

Set: VectorOrientation(self: AnalysisDisplayVectorSettings) = value
"""

    VectorPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Vector position.

Get: VectorPosition(self: AnalysisDisplayVectorSettings) -> AnalysisDisplayStyleVectorPosition

Set: VectorPosition(self: AnalysisDisplayVectorSettings) = value
"""

    VectorTextType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of vector text visualization.

Get: VectorTextType(self: AnalysisDisplayVectorSettings) -> AnalysisDisplayStyleVectorTextType

Set: VectorTextType(self: AnalysisDisplayVectorSettings) = value
"""



class AnalysisMode(Enum, IComparable, IFormattable, IConvertible):
    """
    This enum is used to define the Energy Analysis Model.
    
    enum AnalysisMode, values: BuildingElements (0), ConceptualMasses (1), ConceptualMassesAndBuildingElements (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BuildingElements = None
    ConceptualMasses = None
    ConceptualMassesAndBuildingElements = None
    value__ = None


class AnalysisResultSchema(object, IDisposable):
    """
    Contains all information about one analysis result. Each result may contain several measurements.
    
    AnalysisResultSchema(name: str, description: str)
    AnalysisResultSchema(other: AnalysisResultSchema)
    """
    def Dispose(self):
        """ Dispose(self: AnalysisResultSchema) """
        pass

    def GetNumberOfUnits(self):
        """
        GetNumberOfUnits(self: AnalysisResultSchema) -> int
        
            returns number of possible units
        """
        pass

    def GetUnitsMultiplier(self, index):
        """
        GetUnitsMultiplier(self: AnalysisResultSchema, index: int) -> float
        
            returns units multiplier by index
        
            index: index of unit in the list
        """
        pass

    def GetUnitsName(self, index):
        """
        GetUnitsName(self: AnalysisResultSchema, index: int) -> str
        
            returns units name by index
        
            index: index of unit in the list
        """
        pass

    def IsEqual(self, other):
        """
        IsEqual(self: AnalysisResultSchema, other: AnalysisResultSchema) -> bool
        
            Determines if the input object is equivalent to this AnalysisResultSchema.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AnalysisResultSchema, disposing: bool) """
        pass

    def SetUnits(self, names, multipliers):
        """ SetUnits(self: AnalysisResultSchema, names: IList[str], multipliers: IList[float]) """
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
    def __new__(self, *__args):
        """
        __new__(cls: type, name: str, description: str)
        __new__(cls: type, other: AnalysisResultSchema)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AnalysisDisplayStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ElementId of analysis display style overriding the style set for view; -1 if the style is not overridden

Get: AnalysisDisplayStyleId(self: AnalysisResultSchema) -> ElementId

Set: AnalysisDisplayStyleId(self: AnalysisResultSchema) = value
"""

    CurrentUnits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Stores the index in the array of applicable units

Get: CurrentUnits(self: AnalysisResultSchema) -> int

Set: CurrentUnits(self: AnalysisResultSchema) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Description of analysis result in view

Get: Description(self: AnalysisResultSchema) -> str

Set: Description(self: AnalysisResultSchema) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: AnalysisResultSchema) -> bool

"""

    IsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true analysis result is visible in view

Get: IsVisible(self: AnalysisResultSchema) -> bool

Set: IsVisible(self: AnalysisResultSchema) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of analysis result in view

Get: Name(self: AnalysisResultSchema) -> str

Set: Name(self: AnalysisResultSchema) = value
"""

    Scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Multiplier used for displaying diagram or vector values in view.

Get: Scale(self: AnalysisResultSchema) -> float

Set: Scale(self: AnalysisResultSchema) = value
"""



class BuildingEnvelopeAnalyzer(object, IDisposable):
    """ Analyzes which elements are part of the building envelope, the building elements exposed to the outside. """
    @staticmethod
    def Create(document, options):
        """
        Create(document: Document, options: BuildingEnvelopeAnalyzerOptions) -> BuildingEnvelopeAnalyzer
        
            Creates a new analyzer.
        
            document: The document that contains the physical model of the building.
            options: Options for the method analyzing the building elements for the building 
             envelope.
        
            Returns: The created analyzer.
        """
        pass

    def Dispose(self):
        """ Dispose(self: BuildingEnvelopeAnalyzer) """
        pass

    def GetBoundingElements(self):
        """
        GetBoundingElements(self: BuildingEnvelopeAnalyzer) -> IList[LinkElementId]
        
            Returns the collection of building elements exposed to the outside forming the 
             building envelope.
        
            Returns: The ids of the building elements in the envelope.
        """
        pass

    def GetBoundingElementsForSpaceVolume(self, spaceVolume):
        """
        GetBoundingElementsForSpaceVolume(self: BuildingEnvelopeAnalyzer, spaceVolume: int) -> IList[LinkElementId]
        
            Returns the collection of bounding building elements for an enclosed space 
             volume.
        
            Returns: The ids of the bounding building elements for the enclosed space volume.
        """
        pass

    def GetCenterPointsForConnectedGridCellsInSpaceVolume(self, spaceVolume):
        """
        GetCenterPointsForConnectedGridCellsInSpaceVolume(self: BuildingEnvelopeAnalyzer, spaceVolume: int) -> IList[XYZ]
        
            Returns the collection of connected cells in an enclosed space volume.
            Returns: The center points for the connected analytical grid cells in the enclosed space 
             volume.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: BuildingEnvelopeAnalyzer, disposing: bool) """
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

Get: IsValidObject(self: BuildingEnvelopeAnalyzer) -> bool

"""



class BuildingEnvelopeAnalyzerOptions(object, IDisposable):
    """
    Specific options for the method analyzing the building elements for the building envelope.
    
    BuildingEnvelopeAnalyzerOptions()
    """
    def Dispose(self):
        """ Dispose(self: BuildingEnvelopeAnalyzerOptions) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: BuildingEnvelopeAnalyzerOptions, disposing: bool) """
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

    AnalyzeEnclosedSpaceVolumes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether or not to analyze interior connected regions inside the building forming enclosed space volumes.

Get: AnalyzeEnclosedSpaceVolumes(self: BuildingEnvelopeAnalyzerOptions) -> bool

Set: AnalyzeEnclosedSpaceVolumes(self: BuildingEnvelopeAnalyzerOptions) = value
"""

    GridCellSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The cell size for the uniform cubical grid used when analyzing the building envelope.

Get: GridCellSize(self: BuildingEnvelopeAnalyzerOptions) -> float

Set: GridCellSize(self: BuildingEnvelopeAnalyzerOptions) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: BuildingEnvelopeAnalyzerOptions) -> bool

"""

    OptimizeGridCellSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether or not to use the exact value for the cell size or let the analyzer optimize the cell size based on the specified grid size

Get: OptimizeGridCellSize(self: BuildingEnvelopeAnalyzerOptions) -> bool

Set: OptimizeGridCellSize(self: BuildingEnvelopeAnalyzerOptions) = value
"""



class ConceptualConstructionFloorSlabType(Enum, IComparable, IFormattable, IConvertible):
    """
    ConceptualConstructionType values for Floors.
    
    enum ConceptualConstructionFloorSlabType, values: HighMassConstructionColdClimateSlabInsulation (5), HighMassConstructionFrigidClimateSlabInsulation (4), HighMassConstructionTypicalNoInsulation (6), InvalidFloorSlabTypeConstruction (-1), LightweightConstructionHighInsulation (0), LightweightConstructionLowInsulation (2), LightweightConstructionNoInsulationInterior (3), LightweightConstructionTypicalInsulation (1), NumFloorSlabTypeConstruction (7)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    HighMassConstructionColdClimateSlabInsulation = None
    HighMassConstructionFrigidClimateSlabInsulation = None
    HighMassConstructionTypicalNoInsulation = None
    InvalidFloorSlabTypeConstruction = None
    LightweightConstructionHighInsulation = None
    LightweightConstructionLowInsulation = None
    LightweightConstructionNoInsulationInterior = None
    LightweightConstructionTypicalInsulation = None
    NumFloorSlabTypeConstruction = None
    value__ = None


class ConceptualConstructionOpeningType(Enum, IComparable, IFormattable, IConvertible):
    """
    ConceptualConstructionType values for Openings.
    
    enum ConceptualConstructionOpeningType, values: Air (0), InvalidOpeningTypeConstruction (-1), NumOpeningTypeConstruction (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Air = None
    InvalidOpeningTypeConstruction = None
    NumOpeningTypeConstruction = None
    value__ = None


class ConceptualConstructionRoofType(Enum, IComparable, IFormattable, IConvertible):
    """
    ConceptualConstructionType values for Roofs.
    
    enum ConceptualConstructionRoofType, values: HighInsulationCoolRoof (0), HighInsulationDarkRoof (1), InvalidRoofTypeConstruction (-1), LowInsulationCoolRoof (4), LowInsulationDarkRoof (5), NoInsulationDarkRoof (6), NumRoofTypeConstruction (7), TypicalInsulationCoolRoof (2), TypicalInsulationDarkRoof (3)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    HighInsulationCoolRoof = None
    HighInsulationDarkRoof = None
    InvalidRoofTypeConstruction = None
    LowInsulationCoolRoof = None
    LowInsulationDarkRoof = None
    NoInsulationDarkRoof = None
    NumRoofTypeConstruction = None
    TypicalInsulationCoolRoof = None
    TypicalInsulationDarkRoof = None
    value__ = None


class ConceptualConstructionShadeType(Enum, IComparable, IFormattable, IConvertible):
    """
    ConceptualConstructionType values for Shades.
    
    enum ConceptualConstructionShadeType, values: BasicShade (0), InvalidShadeTypeConstruction (-1), NumShadeTypeConstruction (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BasicShade = None
    InvalidShadeTypeConstruction = None
    NumShadeTypeConstruction = None
    value__ = None


class ConceptualConstructionType(ElementType, IDisposable):
    """
    This element is used to describe the conceptual physical, construction, and energy properties in a manner
       that can be understood by both the Revit BIM model and Green Building Studio/Green Building XML.
       For serialization
    """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    @staticmethod
    def GetAllConceptualConstructionsForCategory(ccda, massSubCategoryId):
        """
        GetAllConceptualConstructionsForCategory(ccda: Document, massSubCategoryId: ElementId) -> ICollection[ElementId]
        
            Get all the ids of constructions applicable to the input massSubCategory
        
            ccda: The document.
            massSubCategoryId: The ElementId of the mass subcategory.
            Returns: Returns a set of ElementIds that for the ConceptualConstructionTypes that are 
             appropriate for the subcategory.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetFloorOrSlabConstructionType(ccda, typeEnum):
        """
        GetFloorOrSlabConstructionType(ccda: Document, typeEnum: ConceptualConstructionFloorSlabType) -> ElementId
        
            Get a Floor or Slab ConceptualConstructionType by its 
             ConceptualConstructionFloorSlabType.
        
        
            ccda: The Document.
            typeEnum: The ConceptualConstructionFloorSlabType to get the ConceptualConstructionType 
             for.
        
            Returns: Returns ElementId of a ConceptualConstructionType.
        """
        pass

    def GetGBSId(self, massSurfaceSubCategoryId):
        """
        GetGBSId(self: ConceptualConstructionType, massSurfaceSubCategoryId: ElementId) -> int
        
            Gets the Green Building Studio identifier associated with the construction.
        
            massSurfaceSubCategoryId: The ElementId of a valid Mass subcategory of a MassSurfaceData.
            Returns: Returns the integer id used to represent the ConceptualConstructionType.
        """
        pass

    @staticmethod
    def GetOpeningConstructionType(ccda, typeEnum):
        """
        GetOpeningConstructionType(ccda: Document, typeEnum: ConceptualConstructionOpeningType) -> ElementId
        
            Get an Opening ConceptualConstructionType by its 
             ConceptualConstructionOpeningType.
        
        
            ccda: The Document.
            typeEnum: The ConceptualConstructionOpeningType to get the ConceptualConstructionType for.
            Returns: Returns ElementId of a ConceptualConstructionType.
        """
        pass

    @staticmethod
    def GetRoofConstructionType(ccda, typeEnum):
        """
        GetRoofConstructionType(ccda: Document, typeEnum: ConceptualConstructionRoofType) -> ElementId
        
            Get a Roof ConceptualConstructionType by its ConceptualConstructionRoofType.
        
            ccda: The Document.
            typeEnum: The ConceptualConstructionRoofType to get the ConceptualConstructionType for.
            Returns: Returns ElementId of a ConceptualConstructionType.
        """
        pass

    @staticmethod
    def GetShadeConstructionType(ccda, typeEnum):
        """
        GetShadeConstructionType(ccda: Document, typeEnum: ConceptualConstructionShadeType) -> ElementId
        
            Get a Shade ConceptualConstructionType by its ConceptualConstructionShadeType.
        
            ccda: The Document.
            typeEnum: The ConceptualConstructionShadeType to get the ConceptualConstructionType for.
            Returns: Returns ElementId of a ConceptualConstructionType.
        """
        pass

    @staticmethod
    def GetWallConstructionType(ccda, typeEnum):
        """
        GetWallConstructionType(ccda: Document, typeEnum: ConceptualConstructionWallType) -> ElementId
        
            Get a Wall ConceptualConstructionType by its ConceptualConstructionWallType.
        
            ccda: The Document.
            typeEnum: The ConceptualConstructionWallType to get the ConceptualConstructionType for.
            Returns: Returns ElementId of a ConceptualConstructionType.
        """
        pass

    @staticmethod
    def GetWindowOrSkylightConstructionType(ccda, typeEnum):
        """
        GetWindowOrSkylightConstructionType(ccda: Document, typeEnum: ConceptualConstructionWindowSkylightType) -> ElementId
        
            Get a Window or Skylight ConceptualConstructionType by its 
             ConceptualConstructionWindowSkylightType.
        
        
            ccda: The Document.
            typeEnum: The ConceptualConstructionWindowSkylightType to get the 
             ConceptualConstructionType for.
        
            Returns: Returns ElementId of a ConceptualConstructionType.
        """
        pass

    @staticmethod
    def IsValidConceptualConstructionId(ccda, constructionTypeId):
        """
        IsValidConceptualConstructionId(ccda: Document, constructionTypeId: ElementId) -> bool
        
            Indicates if the ElementId is an id of a ConceptualConstructionType.
        
            ccda: The document.
            constructionTypeId: The ElementId of the ConceptualConstructionType.
            Returns: Returns true if is an id of a ConceptualConstructionType, false otherwise.
        """
        pass

    @staticmethod
    def IsValidConceptualConstructionIdForCategory(ccda, constructionTypeId, massSubcategoryId):
        """
        IsValidConceptualConstructionIdForCategory(ccda: Document, constructionTypeId: ElementId, massSubcategoryId: ElementId) -> bool
        
            Indicate if a ConceptualConstruction is appropriate to assign to a 
             MassSurfaceData of a particular Mass subcategory.
        
        
            ccda: The document.
            constructionTypeId: The ElementId of the ConceptualConstructionType.
            massSubcategoryId: The ElementId of the Mass subcategory.
            Returns: Returns true if valid, false otherwise
        """
        pass

    @staticmethod
    def IsValidSubcategoryForMassSurfaceDatas(massSubCategoryId):
        """
        IsValidSubcategoryForMassSurfaceDatas(massSubCategoryId: ElementId) -> bool
        
            Validate if a subcategory is appropriate for assignment to Massing surfaces 
             (MassSurfaceData).
           This is the list of acceptable values:
           
             OST_MassInteriorWallOST_MassExteriorWallOST_MassExteriorWallUndergroundOST_MassR
             oofOST_MassFloorOST_MassSlabOST_MassShadeOST_MassGlazingOST_MassSkylightsOST_Mas
             sOpening
        
        
            massSubCategoryId: The mass sub-category to be checked.
            Returns: True if the mass sub-category falls within the list, false otherwise.
        """
        pass

    def IsValidSurfaceSubcategoryForConstruction(self, massSurfaceSubcategoryId):
        """
        IsValidSurfaceSubcategoryForConstruction(self: ConceptualConstructionType, massSurfaceSubcategoryId: ElementId) -> bool
        
            Indicates if this ConceptualConstructionType is appropriate for the input 
             MassSurfaceData subcategory.
        
        
            massSurfaceSubcategoryId: The ElementId of a Mass subcategory of a MassSurfaceData.
            Returns: Returns true if appropriate for the input subcategory, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    MassSurfaceSubCategoryId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The surface type subcategory element id associated with the ConceptualConstructionType.

Get: MassSurfaceSubCategoryId(self: ConceptualConstructionType) -> ElementId

"""

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Material used for visualization of this construction.

Get: MaterialId(self: ConceptualConstructionType) -> ElementId

Set: MaterialId(self: ConceptualConstructionType) = value
"""



class ConceptualConstructionWallType(Enum, IComparable, IFormattable, IConvertible):
    """
    ConceptualConstructionType values for Walls.
    
    enum ConceptualConstructionWallType, values: HighMassConstructionHighInsulation (5), HighMassConstructionNoInsulationInterior (8), HighMassConstructionTypicalColdClimateInsulation (6), HighMassConstructionTypicalMildClimateInsulation (7), InvalidExteriorWallTypeConstruction (-1), LightweightConstructionHighInsulation (0), LightweightConstructionLowInsulation (3), LightweightConstructionNoInsulationInterior (4), LightweightConstructionTypicalColdClimateInsulation (1), LightweightConstructionTypicalMildClimateInsulation (2), NumWallTypeConstruction (9)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    HighMassConstructionHighInsulation = None
    HighMassConstructionNoInsulationInterior = None
    HighMassConstructionTypicalColdClimateInsulation = None
    HighMassConstructionTypicalMildClimateInsulation = None
    InvalidExteriorWallTypeConstruction = None
    LightweightConstructionHighInsulation = None
    LightweightConstructionLowInsulation = None
    LightweightConstructionNoInsulationInterior = None
    LightweightConstructionTypicalColdClimateInsulation = None
    LightweightConstructionTypicalMildClimateInsulation = None
    NumWallTypeConstruction = None
    value__ = None


class ConceptualConstructionWindowSkylightType(Enum, IComparable, IFormattable, IConvertible):
    """
    ConceptualConstructionType values for Windows and Skylights
    
    enum ConceptualConstructionWindowSkylightType, values: DoublePaneClearHighestPerformanceLowEHighVisTransLowSHGC (8), DoublePaneClearLowEColdClimateHighSHGC (6), DoublePaneClearLowEHotClimateLowSHGC (7), DoublePaneClearNoCoating (3), DoublePaneReflective (5), DoublePaneTinted (4), InvalidWindowSkylightTypeConstruction (-1), NumWindowSkylightTypeConstruction (11), QuadPaneClearLowEHotOrColdClimate (10), SinglePaneClearNoCoating (0), SinglePaneReflective (2), SinglePaneTinted (1), TriplePaneClearLowEHotOrColdClimate (9)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DoublePaneClearHighestPerformanceLowEHighVisTransLowSHGC = None
    DoublePaneClearLowEColdClimateHighSHGC = None
    DoublePaneClearLowEHotClimateLowSHGC = None
    DoublePaneClearNoCoating = None
    DoublePaneReflective = None
    DoublePaneTinted = None
    InvalidWindowSkylightTypeConstruction = None
    NumWindowSkylightTypeConstruction = None
    QuadPaneClearLowEHotOrColdClimate = None
    SinglePaneClearNoCoating = None
    SinglePaneReflective = None
    SinglePaneTinted = None
    TriplePaneClearLowEHotOrColdClimate = None
    value__ = None


class ConceptualSurfaceType(Element, IDisposable):
    """
    This element represents a conceptual BIM object category to assign to faces in Mass geometries.
       There is one ConceptualSurfaceType element for each of the Mass Surface Subcategories.
       for serialization
    """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    @staticmethod
    def GetAllMassSubCategoryIds():
        """
        GetAllMassSubCategoryIds() -> IList[ElementId]
        
            Get all the mass subcategory ids for which there are ConceptualSurfaceType's.
            Returns: Returns an array of element id of mass subcategories for which there are 
             ConceptualSurfaceType's.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetByMassSubCategoryId(cda, massSubCategoryId):
        """
        GetByMassSubCategoryId(cda: Document, massSubCategoryId: ElementId) -> ConceptualSurfaceType
        
            Get the ConceptualSurfaceType by its mass subcategory id.
        
            cda: The document.
            massSubCategoryId: The mass subcategory id to get the ConceptualSurfaceType for.
            Returns: Returns ConceptualSurfaceType associated with input id or NULL.
        """
        pass

    def GetConstructionTypeIds(self):
        """
        GetConstructionTypeIds(self: ConceptualSurfaceType) -> ICollection[ElementId]
        
            The element ids of the ConceptualConstructionType's associated with this 
             ConceptualSurfaceType.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    DefaultConstructionTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id of the user specified ConceptualConstructionType to be used by default on creation for mass faces of this mass subcategory.

Get: DefaultConstructionTypeId(self: ConceptualSurfaceType) -> ElementId

Set: DefaultConstructionTypeId(self: ConceptualSurfaceType) = value
"""

    MassSubCategoryId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The mass subcategory id of the ConceptualSurfaceType.

Get: MassSubCategoryId(self: ConceptualSurfaceType) -> ElementId

"""



class ConstructionType(Enum, IComparable, IFormattable, IConvertible):
    """
    This enumeration specifies the available analytical construction types
       like external walls, windows etc. for use in the detailed analytical
       energy model.
    
    enum ConstructionType, values: Ceiling (4), Door (6), ExteriorWall (0), ExteriorWindow (7), Floor (5), InteriorWall (1), InteriorWindow (8), Roof (3), Skylight (9), Slab (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Ceiling = None
    Door = None
    ExteriorWall = None
    ExteriorWindow = None
    Floor = None
    InteriorWall = None
    InteriorWindow = None
    Roof = None
    Skylight = None
    Slab = None
    value__ = None


class EnergyAnalysisDetailModel(Element, IDisposable):
    """ Manage the analytical thermal model. """
    @staticmethod
    def Create(document, options):
        """
        Create(document: Document, options: EnergyAnalysisDetailModelOptions) -> EnergyAnalysisDetailModel
        
            Creates a new energy analysis detailed model.
        
            document: The document that contains the physical model of the building.
            options: The options to control the calculation rules.
            Returns: The created model instance.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GetAnalyticalOpenings(self):
        """
        GetAnalyticalOpenings(self: EnergyAnalysisDetailModel) -> IList[EnergyAnalysisOpening]
        
            The collection of analytical openings.
            Returns: Returns the analytical openings after model calculation.
        """
        pass

    def GetAnalyticalShadingSurfaces(self):
        """
        GetAnalyticalShadingSurfaces(self: EnergyAnalysisDetailModel) -> IList[EnergyAnalysisSurface]
        
            The collection of analytical shading surfaces.
            Returns: Returns the analytical shading surfaces after model calculation.
        """
        pass

    def GetAnalyticalSpaces(self):
        """
        GetAnalyticalSpaces(self: EnergyAnalysisDetailModel) -> IList[EnergyAnalysisSpace]
        
            The collection of analytical spaces.
            Returns: Returns the analytical spaces after model calculation.
        """
        pass

    def GetAnalyticalSurfaces(self):
        """
        GetAnalyticalSurfaces(self: EnergyAnalysisDetailModel) -> IList[EnergyAnalysisSurface]
        
            The collection of analytical surfaces.
            Returns: Returns the analytical surfaces after model calculation.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetMainEnergyAnalysisDetailModel(document):
        """
        GetMainEnergyAnalysisDetailModel(document: Document) -> EnergyAnalysisDetailModel
        
            Gets the EnergyAnalysisDetailModel in given document.
        
            document: The document that contains the physical model of the building.
            Returns: Returns the EnergyAnalysisDetailModel contained in the document, if it exists. 
             If it does not exist, this returns ll.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def TransformModel(self):
        """
        TransformModel(self: EnergyAnalysisDetailModel)
            Transforms all surfaces in the model according to the document's active
           
             ground plane, shared coordinates and true north.
        """
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

    ExportCategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Export elements of this category in energy analysis.

Get: ExportCategory(self: EnergyAnalysisDetailModel) -> ElementId

Set: ExportCategory(self: EnergyAnalysisDetailModel) = value
"""

    ExportMullions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if to specify the setting for exporting mullions.

Get: ExportMullions(self: EnergyAnalysisDetailModel) -> bool

"""

    IncludeShadingSurfaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if to set and get the setting for if shading surfaces should be included.

Get: IncludeShadingSurfaces(self: EnergyAnalysisDetailModel) -> bool

"""

    SimplifyCurtainSystems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if to specify the setting for simplified curtain systems.

Get: SimplifyCurtainSystems(self: EnergyAnalysisDetailModel) -> bool

"""

    Tier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Level of computation for energy analysis model.

Get: Tier(self: EnergyAnalysisDetailModel) -> EnergyAnalysisDetailModelTier

"""



class EnergyAnalysisDetailModelOptions(object, IDisposable):
    """
    Options that govern the calculations for the generation of the energy analysis detail model.
    
    EnergyAnalysisDetailModelOptions()
    """
    def Dispose(self):
        """ Dispose(self: EnergyAnalysisDetailModelOptions) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: EnergyAnalysisDetailModelOptions, disposing: bool) """
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

    EnergyModelType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """It indicates whether the energy model is based on rooms/spaces or building elements.

Get: EnergyModelType(self: EnergyAnalysisDetailModelOptions) -> EnergyModelType

Set: EnergyModelType(self: EnergyAnalysisDetailModelOptions) = value
"""

    ExportMullions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if to specify the setting for exporting mullions.

Get: ExportMullions(self: EnergyAnalysisDetailModelOptions) -> bool

Set: ExportMullions(self: EnergyAnalysisDetailModelOptions) = value
"""

    IncludeShadingSurfaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if to set and get the setting for if shading surfaces should be included.

Get: IncludeShadingSurfaces(self: EnergyAnalysisDetailModelOptions) -> bool

Set: IncludeShadingSurfaces(self: EnergyAnalysisDetailModelOptions) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: EnergyAnalysisDetailModelOptions) -> bool

"""

    SimplifyCurtainSystems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if to specify the setting for simplified curtain systems.

Get: SimplifyCurtainSystems(self: EnergyAnalysisDetailModelOptions) -> bool

Set: SimplifyCurtainSystems(self: EnergyAnalysisDetailModelOptions) = value
"""

    Tier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Level of computation for energy analysis model.

Get: Tier(self: EnergyAnalysisDetailModelOptions) -> EnergyAnalysisDetailModelTier

Set: Tier(self: EnergyAnalysisDetailModelOptions) = value
"""



class EnergyAnalysisDetailModelTier(Enum, IComparable, IFormattable, IConvertible):
    """
    Level of computation for energy analysis model.
    
    enum EnergyAnalysisDetailModelTier, values: Final (3), FirstLevelBoundaries (1), NotComputed (0), SecondLevelBoundaries (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Final = None
    FirstLevelBoundaries = None
    NotComputed = None
    SecondLevelBoundaries = None
    value__ = None


class EnergyAnalysisOpening(Element, IDisposable):
    """ Analytical opening. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GetAnalyticalSurface(self):
        """
        GetAnalyticalSurface(self: EnergyAnalysisOpening) -> EnergyAnalysisSurface
        
            Gets the associative analytical parent surface element.
            Returns: The associative analytical parent surface element.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetPolyloop(self):
        """
        GetPolyloop(self: EnergyAnalysisOpening) -> Polyloop
        
            Gets the planar polygon describing the opening geometry.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    CADLinkUniqueId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unique id of the originating CAD object's link (linked document) associated with this opening.

Get: CADLinkUniqueId(self: EnergyAnalysisOpening) -> str

"""

    CADObjectUniqueId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unique id of the originating CAD object (model element) associated with this opening.

Get: CADObjectUniqueId(self: EnergyAnalysisOpening) -> str

"""

    Corner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The lower-left coordinate for the analytical rectangular geometry viewed from outside.

Get: Corner(self: EnergyAnalysisOpening) -> XYZ

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The height of the analytical rectangular geometry.

Get: Height(self: EnergyAnalysisOpening) -> float

"""

    OpeningId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unique identifier for the opening.

Get: OpeningId(self: EnergyAnalysisOpening) -> str

"""

    OpeningName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unique name identifier for the opening.

Get: OpeningName(self: EnergyAnalysisOpening) -> str

"""

    OpeningType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The analytical opening type.

Get: OpeningType(self: EnergyAnalysisOpening) -> EnergyAnalysisOpeningType

"""

    OriginatingElementDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The description for the originating Revit element.

Get: OriginatingElementDescription(self: EnergyAnalysisOpening) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The gbXML opening type attribute.

Get: Type(self: EnergyAnalysisOpening) -> gbXMLOpeningType

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The width of the analytical rectangular geometry.

Get: Width(self: EnergyAnalysisOpening) -> float

"""



class EnergyAnalysisOpeningType(Enum, IComparable, IFormattable, IConvertible):
    """
    Analytical opening types.
    
    enum EnergyAnalysisOpeningType, values: Air (3), Door (0), Skylight (2), Window (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Air = None
    Door = None
    Skylight = None
    value__ = None
    Window = None


class EnergyAnalysisSpace(Element, IDisposable):
    """ Analytical space. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GetAnalyticalSurfaces(self):
        """
        GetAnalyticalSurfaces(self: EnergyAnalysisSpace) -> IList[EnergyAnalysisSurface]
        
            Provides a way to access the collection of
           analytical surfaces for a space.
             
           Geometry data defining an analytical space volume.
           Through an 
             analytical surface you can connect a
           source element with each polygon in a 
             space.
           The analytical surfaces defines an enclosed volume
           bounded by 
             the center plane of walls
           and the top plane of roofs and floors.
        
            Returns: the collection of analytical surfaces for a space.
        """
        pass

    def GetBoundary(self):
        """
        GetBoundary(self: EnergyAnalysisSpace) -> IList[Polyloop]
        
            Gets the collection of polygons that form the 2D boundary.
           This method 
             returns a collection of polyloops (planar
           polygons) that defines an 
             enclosed area measured by
           interior bounding surfaces.
        
            Returns: The collection of polygons that form the 2D boundary.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetClosedShell(self):
        """
        GetClosedShell(self: EnergyAnalysisSpace) -> IList[Polyloop]
        
            Gets the collection of polygons that form a closed shell.
           This method 
             returns a collection of polyloops (planar
           polygons) that defines an 
             enclosed volume measured by
           interior bounding surfaces.
        
            Returns: the collection of polygons that form a closed shell.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    AnalyticalVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The volume for this space.

Get: AnalyticalVolume(self: EnergyAnalysisSpace) -> float

"""

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The area for this space.

Get: Area(self: EnergyAnalysisSpace) -> float

"""

    CADObjectUniqueId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unique id of the originating CAD object (model element) associated with this space.

Get: CADObjectUniqueId(self: EnergyAnalysisSpace) -> str

"""

    ComposedName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The composed name for this space.

Get: ComposedName(self: EnergyAnalysisSpace) -> str

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The description.

Get: Description(self: EnergyAnalysisSpace) -> str

"""

    InnerVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The analytical volume for this space.

Get: InnerVolume(self: EnergyAnalysisSpace) -> float

"""

    SpaceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name.

Get: SpaceName(self: EnergyAnalysisSpace) -> str

"""



class EnergyAnalysisSurface(Element, IDisposable):
    """
    Analytical surface.
       The collection of analytic openings belonging to this analytical parent surface
    """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GetAdjacentAnalyticalSpace(self):
        """
        GetAdjacentAnalyticalSpace(self: EnergyAnalysisSurface) -> EnergyAnalysisSpace
        
            Gets the secondary adjacent analytical space this surface is associated with.
            Returns: The secondary analytical space.
        """
        pass

    def GetAnalyticalOpenings(self):
        """
        GetAnalyticalOpenings(self: EnergyAnalysisSurface) -> IList[EnergyAnalysisOpening]
        
            Returns the analytical openings of the analytical surface.
            Returns: The collection of analytical openings.
        """
        pass

    def GetAnalyticalSpace(self):
        """
        GetAnalyticalSpace(self: EnergyAnalysisSurface) -> EnergyAnalysisSpace
        
            Gets the primary analytical space this surface is associated with.
            Returns: The primary analytical space.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetPolyloop(self):
        """
        GetPolyloop(self: EnergyAnalysisSurface) -> Polyloop
        
            Gets the planar polygon describing the opening geometry.
            Returns: The planar polygon describing the opening geometry.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    Azimuth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The azimuth angle for this surface.

Get: Azimuth(self: EnergyAnalysisSurface) -> float

"""

    CADLinkUniqueId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unique id of the originating CAD object's link (linked document) associated with this surface.

Get: CADLinkUniqueId(self: EnergyAnalysisSurface) -> str

"""

    CADObjectUniqueId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unique id of the originating CAD object (model element) associated with this surface.

Get: CADObjectUniqueId(self: EnergyAnalysisSurface) -> str

"""

    Corner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The lower-left coordinate for the analytical rectangular geometry viewed from outside.

Get: Corner(self: EnergyAnalysisSurface) -> XYZ

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The height of the analytical rectangular geometry.

Get: Height(self: EnergyAnalysisSurface) -> float

"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The outward normal for this surface.

Get: Normal(self: EnergyAnalysisSurface) -> XYZ

"""

    OriginatingElementDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The description for the originating Revit element.

Get: OriginatingElementDescription(self: EnergyAnalysisSurface) -> str

"""

    SurfaceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unique identifier for the surface.

Get: SurfaceId(self: EnergyAnalysisSurface) -> str

"""

    SurfaceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unique name identifier for this surface.

Get: SurfaceName(self: EnergyAnalysisSurface) -> str

"""

    SurfaceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The analytical surface type.

Get: SurfaceType(self: EnergyAnalysisSurface) -> EnergyAnalysisSurfaceType

"""

    Tilt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The tilt angle for this surface.

Get: Tilt(self: EnergyAnalysisSurface) -> float

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The gbXML surface type attribute.

Get: Type(self: EnergyAnalysisSurface) -> gbXMLSurfaceType

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The width of the analytical rectangular geometry.

Get: Width(self: EnergyAnalysisSurface) -> float

"""



class EnergyAnalysisSurfaceType(Enum, IComparable, IFormattable, IConvertible):
    """
    Analytical surface types.
    
    enum EnergyAnalysisSurfaceType, values: Air (7), Ceiling (3), ExteriorFloor (5), ExteriorWall (1), InteriorFloor (4), InteriorWall (2), Roof (0), Shading (6), Underground (8)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Air = None
    Ceiling = None
    ExteriorFloor = None
    ExteriorWall = None
    InteriorFloor = None
    InteriorWall = None
    Roof = None
    Shading = None
    Underground = None
    value__ = None


class EnergyDataSettings(Element, IDisposable):
    """
    This element contains settings for gbXML Export and Heating and Cooling Load Calculations
       and project level settings for Conceptual Energy Analysis.
       for serialization
    """
    @staticmethod
    def CheckAnalysisType(analysisType):
        """
        CheckAnalysisType(analysisType: AnalysisMode) -> bool
        
            Checks that the analysis type falls within an appropriate range.
        
            analysisType: The analysis type to be checked.
            Returns: True if the analysis type falls within an appropriate range, false otherwise.
        """
        pass

    @staticmethod
    def CheckBuildingConstructionClass(buildingConstructionClass):
        """
        CheckBuildingConstructionClass(buildingConstructionClass: HVACLoadConstructionClass) -> bool
        
            Checks that the building construction class falls within an appropriate range.
        
            buildingConstructionClass: The building construction class to be checked.
            Returns: True if the building construction class falls within an appropriate range, 
             false otherwise.
        """
        pass

    @staticmethod
    def CheckBuildingEnvelope(determinationMethod):
        """
        CheckBuildingEnvelope(determinationMethod: gbXMLExportBuildingEnvelope) -> bool
        
            Checks that the building envelope determination method falls within an 
             appropriate range.
        
        
            determinationMethod: The building envelope determination method to be checked.
            Returns: True if the building envelope determination method falls within an appropriate 
             range, false otherwise.
        """
        pass

    @staticmethod
    def CheckBuildingHVACSystem(buildingHVACSystem):
        """
        CheckBuildingHVACSystem(buildingHVACSystem: gbXMLBuildingHVACSystem) -> bool
        
            Checks that the building HVAC system falls within an appropriate range.
        
            buildingHVACSystem: The building HVAC system to be checked.
            Returns: True if the building HVAC system falls within an appropriate range, false 
             otherwise.
        """
        pass

    @staticmethod
    def CheckBuildingOperatingSchedule(buildingOperatingSchedule):
        """
        CheckBuildingOperatingSchedule(buildingOperatingSchedule: gbXMLBuildingOperatingSchedule) -> bool
        
            Checks that the building operating schedule falls within an appropriate range.
        
            buildingOperatingSchedule: The building operating schedule to be checked.
            Returns: True if the building operating schedule falls within an appropriate range, 
             false otherwise.
        """
        pass

    @staticmethod
    def CheckBuildingType(buildingType):
        """
        CheckBuildingType(buildingType: gbXMLBuildingType) -> bool
        
            Checks that the building type falls within an appropriate range.
        
            buildingType: The building type to be checked.
            Returns: True if the building type falls within an appropriate range, false otherwise.
        """
        pass

    def CheckConstructionSetElement(self, constructionSetElementId):
        """
        CheckConstructionSetElement(self: EnergyDataSettings, constructionSetElementId: ElementId) -> bool
        
            Checks that the construction set ElementId is acceptable.
        
            constructionSetElementId: The construction set ElementId to be checked.
            Returns: True if the construction set ElementId is a valid construction set element, 
             false otherwise.
        """
        pass

    @staticmethod
    def CheckExportCategory(exportCategoryId):
        """
        CheckExportCategory(exportCategoryId: ElementId) -> bool
        
            Checks whether the export category falls within the list:
           
             OST_RoomsOST_MEPSpaces
        
        
            exportCategoryId: The export category to be checked.
            Returns: True if the export category falls within the list, false otherwise.
        """
        pass

    @staticmethod
    def CheckExportComplexity(exportComplexity):
        """
        CheckExportComplexity(exportComplexity: gbXMLExportComplexity) -> bool
        
            Checks that the export complexity falls within an appropriate range.
        
            exportComplexity: The export complexity to be checked.
            Returns: True if the export complexity falls within an appropriate range, false 
             otherwise.
        """
        pass

    @staticmethod
    def CheckGroundPlane(*__args):
        """
        CheckGroundPlane(self: EnergyDataSettings, groundPlaneId: ElementId) -> bool
        
            The ground plane should be an Element of type Level.  This method checks to 
             confirm that an ElementId is for a Level element.
        
        
            groundPlaneId: The element id to be checked to confirm that it is suitable to be a ground 
             plane (i.e., that it is a level) or
           that it is invalidElementId.  Setting 
             ground plane with invalidElementId will lead to the ground plane being "reset".
        
            Returns: True if the input element is a level or invalidElementId, false otherwise.
        CheckGroundPlane(ccda: Document, groundPlaneId: ElementId) -> bool
        
            The ground plane should be an Element of type Level.  This method checks to 
             confirm that an ElementId is for a Level element.
        
        
            ccda: The Document.
            groundPlaneId: The element id to be checked to confirm that it is suitable to be a ground 
             plane (i.e., that it is a level) or
           that it is invalidElementId.  Setting 
             ground plane with invalidElementId will lead to the ground plane being "reset".
        
            Returns: True if the input element is a level or invalidElementId, false otherwise.
        """
        pass

    def CheckProjectPhase(self, projectPhaseId):
        """
        CheckProjectPhase(self: EnergyDataSettings, projectPhaseId: ElementId) -> bool
        
            Checks that the input element is a project phase.
        
            projectPhaseId: The element to be checked.
            Returns: True if the input element is a project phase, false otherwise.
        """
        pass

    @staticmethod
    def CheckProjectReportType(projectReportType):
        """
        CheckProjectReportType(projectReportType: HVACLoadLoadsReportType) -> bool
        
            Checks that the project report type falls within an appropriate range.
        
            projectReportType: The project report type to be checked.
            Returns: True if the project report type falls within an appropriate range, false 
             otherwise.
        """
        pass

    @staticmethod
    def CheckRangeOfMassZoneCoreOffset(massZoneCoreOffset):
        """
        CheckRangeOfMassZoneCoreOffset(massZoneCoreOffset: float) -> bool
        
            Checks that the mass zone core offset is greater than or equal to zero.
        
            massZoneCoreOffset: The mass zone core offset to be checked.  Should be greater than or equal to 
             zero.
        
            Returns: True if the mass zone core offset is greater than or equal to zero, false 
             otherwise.
        """
        pass

    @staticmethod
    def CheckRangeOfPercentageGlazing(percentageGlazing):
        """
        CheckRangeOfPercentageGlazing(percentageGlazing: float) -> bool
        
            Checks that the percentage glazing value is between 0.00 and 0.95.
        
            percentageGlazing: The percentage glazing to be checked.
            Returns: True if the percentage glazing value is between 0.00 and 0.95, false otherwise.
        """
        pass

    @staticmethod
    def CheckRangeOfPercentageSkylights(percentageSkylights):
        """
        CheckRangeOfPercentageSkylights(percentageSkylights: float) -> bool
        
            Checks that the percentage skylights value is between 0.00 and 0.95.
        
            percentageSkylights: The percentage skylights to be checked.
            Returns: True if the percentage skylights value is between 0.00 and 0.95, false 
             otherwise.
        """
        pass

    @staticmethod
    def CheckRangeOfShadeDepth(shadeDepth):
        """
        CheckRangeOfShadeDepth(shadeDepth: float) -> bool
        
            Checks that the shade depth is greater than or equal to zero.
        
            shadeDepth: The shade depth to be checked.
            Returns: True if the shade depth is greater than or equal to zero, false otherwise.
        """
        pass

    @staticmethod
    def CheckRangeOfSillHeight(sillHeight):
        """
        CheckRangeOfSillHeight(sillHeight: float) -> bool
        
            Checks that the sill height is greater than or equal to zero.
        
            sillHeight: The sill height to be checked.
            Returns: True if the sill height falls is greater than or equal to zero, false otherwise.
        """
        pass

    @staticmethod
    def CheckRangeOfSkylightWidth(skylightWidth):
        """
        CheckRangeOfSkylightWidth(skylightWidth: float) -> bool
        
            Checks that the skylight width is greater than or equal to eight inches.
        
            skylightWidth: The skylight width to be checked.  Should be greater than or equal to eight 
             inches.
        
            Returns: True if the skylight width is greater than or equal to eight inches, false 
             otherwise.
        """
        pass

    @staticmethod
    def CheckRangeOfSliverSpaceTolerance(silverSpaceTolerance):
        """
        CheckRangeOfSliverSpaceTolerance(silverSpaceTolerance: float) -> bool
        
            Checks that the sliver space tolerance is greater than or equal to zero.
        
            silverSpaceTolerance: The sliver space tolerance to be checked.
            Returns: Returns true if the sliver space tolerance is greater than or equal to zero, 
             false otherwise.
        """
        pass

    @staticmethod
    def CheckServiceType(serviceType):
        """
        CheckServiceType(serviceType: gbXMLServiceType) -> bool
        
            Checks that the service type falls within an appropriate range.
        
            serviceType: The service type to be checked.
            Returns: True if the service type falls within an appropriate range, false otherwise.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    @staticmethod
    def EnableConceptualEnergyAnalyticalModel():
        """
        EnableConceptualEnergyAnalyticalModel() -> bool
        
            Turns on functionality related to conceptual energy analysis.
            Returns: Returns true if the Conceptual Energy Analytical model is turned on, false 
             otherwise.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetBuildingConstructionSetElementId(ccda):
        """
        GetBuildingConstructionSetElementId(ccda: Document) -> ElementId
        
            Id of the building construction set.
            Returns: Returns the id of the building construction set.
        """
        pass

    @staticmethod
    def GetFromDocument(cda):
        """
        GetFromDocument(cda: Document) -> EnergyDataSettings
        
            Every project document has a EnergyDataSettings element.
           Family documents 
             do not have EnergyDataSettings elements.
        
        
            cda: The document.
            Returns: Returns the EnergyDataSettings element or NULL.
        """
        pass

    @staticmethod
    def IsDocumentUsingEnergyDataAnalyticalModel(ccda):
        """
        IsDocumentUsingEnergyDataAnalyticalModel(ccda: Document) -> bool
        
            Get EnergyDataSettings element and if it exists, return result from 
             getCreateAnalyticalModel.
        
        
            ccda: The document.
            Returns: Returns true if the Conceptual Energy Analytical Model is enabled, false 
             otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def SetCreateAnalyticalModel(self, createAnalyticalModel):
        """
        SetCreateAnalyticalModel(self: EnergyDataSettings, createAnalyticalModel: bool)
            If this is true, data, features, and geometry related to the Energy Analytical 
             Model
           will be created, allowing the energy performance to be analyzed 
             through GreenBuilidingXML.
        
        
            createAnalyticalModel: True to enable the Energy Analytical Model otherwise.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    AnalysisType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of analysis mode.

Get: AnalysisType(self: EnergyDataSettings) -> AnalysisMode

Set: AnalysisType(self: EnergyDataSettings) = value
"""

    AnalyticalGridCellSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The cell size for the uniform cubical grid used when computing the building envelope

Get: AnalyticalGridCellSize(self: EnergyDataSettings) -> float

Set: AnalyticalGridCellSize(self: EnergyDataSettings) = value
"""

    BuildingConstructionClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Used for both the detailed and conceptual energy model
   Construction class of building as defined by:
   loose, medium, tight, or none.

Get: BuildingConstructionClass(self: EnergyDataSettings) -> HVACLoadConstructionClass

Set: BuildingConstructionClass(self: EnergyDataSettings) = value
"""

    BuildingEnvelopeDeterminationMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if an analysis should be perform to find the model elements that are part of the building envelope

Get: BuildingEnvelopeDeterminationMethod(self: EnergyDataSettings) -> gbXMLExportBuildingEnvelope

Set: BuildingEnvelopeDeterminationMethod(self: EnergyDataSettings) = value
"""

    BuildingHVACSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of HVAC system used by the building for conceptual model energy calculations.

Get: BuildingHVACSystem(self: EnergyDataSettings) -> gbXMLBuildingHVACSystem

Set: BuildingHVACSystem(self: EnergyDataSettings) = value
"""

    BuildingOperatingSchedule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The operating schedule of the building used for conceptual model energy calculations.

Get: BuildingOperatingSchedule(self: EnergyDataSettings) -> gbXMLBuildingOperatingSchedule

Set: BuildingOperatingSchedule(self: EnergyDataSettings) = value
"""

    BuildingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of building.

Get: BuildingType(self: EnergyDataSettings) -> gbXMLBuildingType

Set: BuildingType(self: EnergyDataSettings) = value
"""

    CoreOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The default offset used to determine the outer perimeter to be divided into zones.

Get: CoreOffset(self: EnergyDataSettings) -> float

Set: CoreOffset(self: EnergyDataSettings) = value
"""

    CreateAnalyticalModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If this is true, data, features, and geometry related to the Energy Analytical Model
   will be created, allowing the energy performance to be analyzed through GreenBuilidingXML.

Get: CreateAnalyticalModel(self: EnergyDataSettings) -> bool

"""

    DividePerimeter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If this is true, zones with exterior boundaries on each floor of the building will be divided based on geometric criteria.

Get: DividePerimeter(self: EnergyDataSettings) -> bool

Set: DividePerimeter(self: EnergyDataSettings) = value
"""

    EnergyModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """if this is on there should be an energy model dependent on the current AnalysisType
   if it is off the conceptual energy model should be turned off
   but setting this datum does not do the work, just reflects the state.

Get: EnergyModel(self: EnergyDataSettings) -> bool

Set: EnergyModel(self: EnergyDataSettings) = value
"""

    ExportCategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Value is a category indicating which discipline model will be used for GreenBuildingXML export.

Get: ExportCategory(self: EnergyDataSettings) -> ElementId

Set: ExportCategory(self: EnergyDataSettings) = value
"""

    ExportComplexity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Value determines Export Complexity for GreenBuildingXML detailed model export.

Get: ExportComplexity(self: EnergyDataSettings) -> gbXMLExportComplexity

Set: ExportComplexity(self: EnergyDataSettings) = value
"""

    ExportDefaults = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Use for detailed model GreenBuildingXML export.
   When this setting is true, all building and space defaults, schedules, and constructions will be exported to GreenBuildingXML.
   When this setting is false, only values that are specified on the zone or space will be exported to GreenBuildingXML.

Get: ExportDefaults(self: EnergyDataSettings) -> bool

Set: ExportDefaults(self: EnergyDataSettings) = value
"""

    GroundPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of level which represents ground level.

Get: GroundPlane(self: EnergyDataSettings) -> ElementId

Set: GroundPlane(self: EnergyDataSettings) = value
"""

    IncludeThermalProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if thermal information from model assemblies and components is included in GreenBuildingXML export of the detailed model.

Get: IncludeThermalProperties(self: EnergyDataSettings) -> bool

Set: IncludeThermalProperties(self: EnergyDataSettings) = value
"""

    IsExportMullionsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if mullions are included in GreenBuildingXML export of the detailed model.

Get: IsExportMullionsEnabled(self: EnergyDataSettings) -> bool

"""

    IsExportShadingSurfacesEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if "shading surfaces" are included in GreenBuildingXML export of the detailed model.

Get: IsExportShadingSurfacesEnabled(self: EnergyDataSettings) -> bool

"""

    IsExportSimplifiedCurtainSystemsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if curtain system geometry is being simplified for GreenBuildingXML export of the detailed model.

Get: IsExportSimplifiedCurtainSystemsEnabled(self: EnergyDataSettings) -> bool

"""

    IsGlazingShaded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If this is true, glazing/windows that are auto-created on exterior walls will automatically
   have a shading device created on their top edge.

Get: IsGlazingShaded(self: EnergyDataSettings) -> bool

Set: IsGlazingShaded(self: EnergyDataSettings) = value
"""

    MassZoneCoreOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """It defines the default behavior for the automatic generation of Mass Zones
   for each Mass Floor in the Project.  Specifying a value here will offset the
   outside perimeter of a Mass Zone to create the core.

Get: MassZoneCoreOffset(self: EnergyDataSettings) -> float

Set: MassZoneCoreOffset(self: EnergyDataSettings) = value
"""

    MassZoneDividePerimeter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If this is true, outward facing zones on each floor of the building will be divided based on the four compass directions.

Get: MassZoneDividePerimeter(self: EnergyDataSettings) -> bool

Set: MassZoneDividePerimeter(self: EnergyDataSettings) = value
"""

    OutsideAirChangesRatePerHour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of times the volume of air interchanges in the room in one hour.

Get: OutsideAirChangesRatePerHour(self: EnergyDataSettings) -> float

Set: OutsideAirChangesRatePerHour(self: EnergyDataSettings) = value
"""

    OutsideAirPerArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The rate of flow of outside air available per unit area.

Get: OutsideAirPerArea(self: EnergyDataSettings) -> float

Set: OutsideAirPerArea(self: EnergyDataSettings) = value
"""

    OutsideAirPerPerson = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The rate of flow of outside air available per person.

Get: OutsideAirPerPerson(self: EnergyDataSettings) -> float

Set: OutsideAirPerPerson(self: EnergyDataSettings) = value
"""

    PercentageGlazing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Used for the conceptual energy model.
   The approximate percentage of the building exterior wall surfaces
   which are covered by windows or other glazing.

Get: PercentageGlazing(self: EnergyDataSettings) -> float

Set: PercentageGlazing(self: EnergyDataSettings) = value
"""

    PercentageSkylights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Used for the conceptual energy model.
   The approximate percentage of the building roof surfaces in
   massing instances for the Conceptual Energy Analytical Model.

Get: PercentageSkylights(self: EnergyDataSettings) -> float

Set: PercentageSkylights(self: EnergyDataSettings) = value
"""

    ProjectPhase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The project phase of the EnergyData information.

Get: ProjectPhase(self: EnergyDataSettings) -> ElementId

Set: ProjectPhase(self: EnergyDataSettings) = value
"""

    ProjectReportType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Report type: None, simple, standard, detailed

Get: ProjectReportType(self: EnergyDataSettings) -> HVACLoadLoadsReportType

Set: ProjectReportType(self: EnergyDataSettings) = value
"""

    ServiceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of heating or cooling system.

Get: ServiceType(self: EnergyDataSettings) -> gbXMLServiceType

Set: ServiceType(self: EnergyDataSettings) = value
"""

    ShadeDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Used for the conceptual energy model.
   Amount that auto-generated shading will extend from auto-generated windows.

Get: ShadeDepth(self: EnergyDataSettings) -> float

Set: ShadeDepth(self: EnergyDataSettings) = value
"""

    SillHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Used for the conceptual energy model.
   The height from the nearest lower level used for auto-glazing created
   on walls.

Get: SillHeight(self: EnergyDataSettings) -> float

Set: SillHeight(self: EnergyDataSettings) = value
"""

    SkylightWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Used for the conceptual energy model.  The approximate width used for the skylights in
   massing instances when the Energy Analytical model is being created.

Get: SkylightWidth(self: EnergyDataSettings) -> float

Set: SkylightWidth(self: EnergyDataSettings) = value
"""

    SliverSpaceTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Used for Detailed GreenBuildingXML export.
   This value is used to identify sliver spaces, i.e. spaces bounded by parallel surfaces belonging to different rooms.

Get: SliverSpaceTolerance(self: EnergyDataSettings) -> float

Set: SliverSpaceTolerance(self: EnergyDataSettings) = value
"""

    UseAirChangesPerHour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if user is specifying air changes per hour, false otherwise.

Get: UseAirChangesPerHour(self: EnergyDataSettings) -> bool

Set: UseAirChangesPerHour(self: EnergyDataSettings) = value
"""

    UseHeatingCredits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true, Revit will use heating credits in the final load sum calculations.
   If false, Revit will ignore heating credits in the final load sum calculations.

Get: UseHeatingCredits(self: EnergyDataSettings) -> bool

Set: UseHeatingCredits(self: EnergyDataSettings) = value
"""

    UseOutsideAirPerArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True is user is specifying outside air per area, false otherwise.

Get: UseOutsideAirPerArea(self: EnergyDataSettings) -> bool

Set: UseOutsideAirPerArea(self: EnergyDataSettings) = value
"""

    UseOutsideAirPerPerson = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if user is specifying outside air per person, false otherwise.

Get: UseOutsideAirPerPerson(self: EnergyDataSettings) -> bool

Set: UseOutsideAirPerPerson(self: EnergyDataSettings) = value
"""



class EnergyModelType(Enum, IComparable, IFormattable, IConvertible):
    """
    This enum is used to define if the energy model is based on rooms/spaces or building elements.
    
    enum EnergyModelType, values: BuildingElement (1), SpatialElement (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BuildingElement = None
    SpatialElement = None
    value__ = None


class FieldDomainPoints(object, IDisposable):
    """ Abstract base class for various classes of field domain points """
    def Dispose(self):
        """ Dispose(self: FieldDomainPoints) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FieldDomainPoints, disposing: bool) """
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

Get: IsValidObject(self: FieldDomainPoints) -> bool

"""



class FieldDomainPointsByParameter(FieldDomainPoints, IDisposable):
    """
    Represents a set of one-dimensional point coordinates (defined usually on curve)
    
    FieldDomainPointsByParameter(points: IList[float])
    """
    def Dispose(self):
        """ Dispose(self: FieldDomainPoints, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FieldDomainPoints, disposing: bool) """
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
    def __new__(self, points):
        """ __new__(cls: type, points: IList[float]) """
        pass


class FieldDomainPointsByUV(FieldDomainPoints, IDisposable):
    """
    Represents a set of two-dimensional point coordinates (defined usually on surface)
    
    FieldDomainPointsByUV(points: IList[UV], uCoordinates: ICollection[float], vCoordinates: ICollection[float])
    FieldDomainPointsByUV(points: IList[UV])
    """
    def Dispose(self):
        """ Dispose(self: FieldDomainPoints, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FieldDomainPoints, disposing: bool) """
        pass

    def SetGridCoordinates(self, uCoordinates, vCoordinates):
        """ SetGridCoordinates(self: FieldDomainPointsByUV, uCoordinates: ICollection[float], vCoordinates: ICollection[float]) """
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
    def __new__(self, points, uCoordinates=None, vCoordinates=None):
        """
        __new__(cls: type, points: IList[UV], uCoordinates: ICollection[float], vCoordinates: ICollection[float])
        __new__(cls: type, points: IList[UV])
        """
        pass


class FieldDomainPointsByXYZ(FieldDomainPoints, IDisposable):
    """
    Represents a set of three-dimensional point coordinates
    
    FieldDomainPointsByXYZ(points: IList[XYZ])
    """
    def Dispose(self):
        """ Dispose(self: FieldDomainPoints, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FieldDomainPoints, disposing: bool) """
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
    def __new__(self, points):
        """ __new__(cls: type, points: IList[XYZ]) """
        pass


class FieldValues(object, IDisposable):
    """
    Contains values corresponding to domain points.
       Each domain point may have an array of values, each corresponding to a separate "measurement" for which this value was calculated.
    
    FieldValues(otherObject: FieldValues)
    FieldValues(vectorAtPoint: IList[VectorAtPoint])
    FieldValues(valueAtPoint: IList[ValueAtPoint], unitDirection: XYZ)
    FieldValues(valueAtPoint: IList[ValueAtPoint])
    """
    def Dispose(self):
        """ Dispose(self: FieldValues) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FieldValues, disposing: bool) """
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
    def __new__(self, *__args):
        """
        __new__(cls: type, otherObject: FieldValues)
        __new__(cls: type, vectorAtPoint: IList[VectorAtPoint])
        __new__(cls: type, valueAtPoint: IList[ValueAtPoint], unitDirection: XYZ)
        __new__(cls: type, valueAtPoint: IList[ValueAtPoint])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FieldValues) -> bool

"""



class gbXMLBuildingHVACSystem(Enum, IComparable, IFormattable, IConvertible):
    """
    Enumerations for gbXML (Green Building XML) format, used for energy
       analysis, schema version 0.34.
    
    enum gbXMLBuildingHVACSystem, values: CentralVAVElectricResistanceHeatChillerFivePointNinetySixCOP (4), CentralVAVHWHeatChillerFivePointNinetySixCOPBoilersEightyFourPoint5Eff (2), ElevenPointThreeEERPackagedVAVEightyFourPointFourPercentBoilerHeating (1), FourPipeFanCoilSystemChillerFivePointNinetySixCOPBoilersEightFourPointFiveEff (3), NoOfHVACSystemEnums (12), ResidentialFourteenSEEREightPointThreeHSPFSplitPackagedHeatPump (11), ResidentialFourteenSEERPointNineAFUESplitPackagedGasLessThanFivePointFiveTon (10), ResidentialSeventeenSEERNinePointSixHSPFSplitHPLessThanFivePointFiveTon (8), TwelveSEEREightPointThreeHSPFPackagedTerminalHeatPumpPTAC (7), TwelveSEERSevenPointSevenHSPFSplitPackagedHeatPump (5), TwelveSEERSPointNineAFUESplitPackagedGasFiveToElevenTon (0), TwoPipeFanCoilSystemChillerFivePointNinetySixCOPBoilersEightyFourPointFiveEff (6), UnderfloorAirDistribution (9)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CentralVAVElectricResistanceHeatChillerFivePointNinetySixCOP = None
    CentralVAVHWHeatChillerFivePointNinetySixCOPBoilersEightyFourPoint5Eff = None
    ElevenPointThreeEERPackagedVAVEightyFourPointFourPercentBoilerHeating = None
    FourPipeFanCoilSystemChillerFivePointNinetySixCOPBoilersEightFourPointFiveEff = None
    NoOfHVACSystemEnums = None
    ResidentialFourteenSEEREightPointThreeHSPFSplitPackagedHeatPump = None
    ResidentialFourteenSEERPointNineAFUESplitPackagedGasLessThanFivePointFiveTon = None
    ResidentialSeventeenSEERNinePointSixHSPFSplitHPLessThanFivePointFiveTon = None
    TwelveSEEREightPointThreeHSPFPackagedTerminalHeatPumpPTAC = None
    TwelveSEERSevenPointSevenHSPFSplitPackagedHeatPump = None
    TwelveSEERSPointNineAFUESplitPackagedGasFiveToElevenTon = None
    TwoPipeFanCoilSystemChillerFivePointNinetySixCOPBoilersEightyFourPointFiveEff = None
    UnderfloorAirDistribution = None
    value__ = None


class gbXMLBuildingOperatingSchedule(Enum, IComparable, IFormattable, IConvertible):
    """
    Enumerations for gbXML (Green Building XML) format, used for energy
       analysis, schema version 0.34.
    
    enum gbXMLBuildingOperatingSchedule, values: DefaultOperatingSchedule (0), KindergartenThruTwelveGradeSchool (7), NoOfOperatingScheduleEnums (11), TheaterPerformingArts (9), TwelveHourFiveDayFacility (6), TwelveHourSevenDayFacility (4), TwelveHourSixDayFacility (5), TwentyFourHourHourFiveDayFacility (3), TwentyFourHourHourSixDayFacility (2), TwentyFourHourSevenDayFacility (1), Worship (10), YearRoundSchool (8)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DefaultOperatingSchedule = None
    KindergartenThruTwelveGradeSchool = None
    NoOfOperatingScheduleEnums = None
    TheaterPerformingArts = None
    TwelveHourFiveDayFacility = None
    TwelveHourSevenDayFacility = None
    TwelveHourSixDayFacility = None
    TwentyFourHourHourFiveDayFacility = None
    TwentyFourHourHourSixDayFacility = None
    TwentyFourHourSevenDayFacility = None
    value__ = None
    Worship = None
    YearRoundSchool = None


class gbXMLBuildingType(Enum, IComparable, IFormattable, IConvertible):
    """
    This enumeration corresponds to the buildingType attribute in gbXML and
       is used to specify the most predominant building use type.
    
    enum gbXMLBuildingType, values: AutomotiveFacility (0), ConventionCenter (1), Courthouse (2), DiningBarLoungeOrLeisure (3), DiningCafeteriaFastFood (4), DiningFamily (5), Dormitory (6), ExerciseCenter (7), FireStation (8), Gymnasium (9), HospitalOrHealthcare (10), Hotel (11), Library (12), Manufacturing (13), Motel (14), MotionPictureTheatre (15), MultiFamily (16), Museum (17), NoBuildingType (-1), NoOfBuildingTypes (33), Office (18), ParkingGarage (19), Penitentiary (20), PerformingArtsTheater (21), PoliceStation (22), PostOffice (23), ReligiousBuilding (24), Retail (25), SchoolOrUniversity (26), SingleFamily (27), SportsArena (28), TownHall (29), Transportation (30), Warehouse (31), Workshop (32)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AutomotiveFacility = None
    ConventionCenter = None
    Courthouse = None
    DiningBarLoungeOrLeisure = None
    DiningCafeteriaFastFood = None
    DiningFamily = None
    Dormitory = None
    ExerciseCenter = None
    FireStation = None
    Gymnasium = None
    HospitalOrHealthcare = None
    Hotel = None
    Library = None
    Manufacturing = None
    Motel = None
    MotionPictureTheatre = None
    MultiFamily = None
    Museum = None
    NoBuildingType = None
    NoOfBuildingTypes = None
    Office = None
    ParkingGarage = None
    Penitentiary = None
    PerformingArtsTheater = None
    PoliceStation = None
    PostOffice = None
    ReligiousBuilding = None
    Retail = None
    SchoolOrUniversity = None
    SingleFamily = None
    SportsArena = None
    TownHall = None
    Transportation = None
    value__ = None
    Warehouse = None
    Workshop = None


class gbXMLConditionType(Enum, IComparable, IFormattable, IConvertible):
    """
    This enumeration corresponds to the conditionType attribute in gbXML.
       The enumerated attribute identifies the type of heating, cooling,
       or ventilation the space has.
    
    enum gbXMLConditionType, values: Cooled (1), Heated (0), HeatedAndCooled (2), NaturallyVentedOnly (5), NoConditionType (-1), NoOfConditionTypes (6), Unconditioned (3), Vented (4)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Cooled = None
    Heated = None
    HeatedAndCooled = None
    NaturallyVentedOnly = None
    NoConditionType = None
    NoOfConditionTypes = None
    Unconditioned = None
    value__ = None
    Vented = None


class gbXMLExportBuildingEnvelope(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates the determination method for the building envelope
    
    enum gbXMLExportBuildingEnvelope, values: IdentifyExteriorElements (1), UseFunctionParameter (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IdentifyExteriorElements = None
    UseFunctionParameter = None
    value__ = None


class gbXMLExportComplexity(Enum, IComparable, IFormattable, IConvertible):
    """
    This enumeration specifies the level of detail of the exported analytical energy model in gbXML.
       Complex means that Curtain Walls and Curtain Systems are exported as several openings, panel by panel;
       a curtain wall with 50 panels gets exported as 50 openings. Simple means that one "huge" opening with
       the total opening area equal to the 50 panels is exported. This is more appropriate for most energy analysis.
       Mullions mean that Mullions in Curtain Walls and Systems are exported as shading surfaces. A "simplified"
       analytical shading surface is produced from a mullion based on its centerline, thickness and offset.
    
    enum gbXMLExportComplexity, values: Complex (2), ComplexWithMullionsAndShadingSurfaces (4), ComplexWithShadingSurfaces (3), Simple (0), SimpleWithShadingSurfaces (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Complex = None
    ComplexWithMullionsAndShadingSurfaces = None
    ComplexWithShadingSurfaces = None
    Simple = None
    SimpleWithShadingSurfaces = None
    value__ = None


class gbXMLOpeningType(Enum, IComparable, IFormattable, IConvertible):
    """
    This enumeration corresponds to the openingType attribute in gbXML
       and identifies the type of opening defined.
    
    enum gbXMLOpeningType, values: FixedSkylight (2), FixedWindow (0), NonSlidingDoor (5), NoOfOpeningTypes (7), OpeningAir (6), OperableSkylight (3), OperableWindow (1), SlidingDoor (4)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FixedSkylight = None
    FixedWindow = None
    NonSlidingDoor = None
    NoOfOpeningTypes = None
    OpeningAir = None
    OperableSkylight = None
    OperableWindow = None
    SlidingDoor = None
    value__ = None


class gbXMLServiceType(Enum, IComparable, IFormattable, IConvertible):
    """
    This enumeration corresponds to the systemType attribute in gbXML
       and is used for specifying the service for the building or space.
    
    enum gbXMLServiceType, values: ActiveChilledBeams (22), CentralHeatingConvectors (1), CentralHeatingHotAir (3), CentralHeatingRadiantFloor (2), CentralHeatingRadiators (0), ConstantVolumeDualDuct (20), ConstantVolumeFixedOA (16), ConstantVolumeTerminalReheat (18), ConstantVolumeVariableOA (17), FanCoilSystem (14), ForcedConvectionHeaterFlue (8), ForcedConvectionHeaterNoFlue (9), InductionSystem (15), MultizoneHotDeckColdDeck (19), NoOfServiceTypes (28), NoServiceType (-1), OtherRoomHeater (4), RadiantCooledCeilings (21), RadiantHeaterFlue (5), RadiantHeaterMultiburner (7), RadiantHeaterNoFlue (6), SplitSystemsWithMechanicalVentilation (26), SplitSystemsWithMechanicalVentilationWithCooling (27), SplitSystemsWithNaturalVentilation (25), VariableRefrigerantFlow (24), VAVDualDuct (11), VAVIndoorPackagedCabinet (12), VAVSingleDuct (10), VAVTerminalReheat (13), WaterLoopHeatPump (23)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ActiveChilledBeams = None
    CentralHeatingConvectors = None
    CentralHeatingHotAir = None
    CentralHeatingRadiantFloor = None
    CentralHeatingRadiators = None
    ConstantVolumeDualDuct = None
    ConstantVolumeFixedOA = None
    ConstantVolumeTerminalReheat = None
    ConstantVolumeVariableOA = None
    FanCoilSystem = None
    ForcedConvectionHeaterFlue = None
    ForcedConvectionHeaterNoFlue = None
    InductionSystem = None
    MultizoneHotDeckColdDeck = None
    NoOfServiceTypes = None
    NoServiceType = None
    OtherRoomHeater = None
    RadiantCooledCeilings = None
    RadiantHeaterFlue = None
    RadiantHeaterMultiburner = None
    RadiantHeaterNoFlue = None
    SplitSystemsWithMechanicalVentilation = None
    SplitSystemsWithMechanicalVentilationWithCooling = None
    SplitSystemsWithNaturalVentilation = None
    value__ = None
    VariableRefrigerantFlow = None
    VAVDualDuct = None
    VAVIndoorPackagedCabinet = None
    VAVSingleDuct = None
    VAVTerminalReheat = None
    WaterLoopHeatPump = None


class gbXMLSpaceType(Enum, IComparable, IFormattable, IConvertible):
    """
    This enumeration corresponds to the spaceType attribute in gbXML.
       The enumerated attribute identifies the type of space defined and
       allows to better approximate the actual internal loads and schedules
       associated with the defined space type.
    
    enum gbXMLSpaceType, values: ActiveStorage (0), ActiveStorageHospitalOrHealthcare (1), AirOrTrainOrBusBaggageArea (2), AirportConcourse (3), AtriumEachAdditionalFloor (4), AtriumFirstThreeFloors (5), AudienceOrSeatingAreaAuditorium (16), AudienceOrSeatingAreaConventionCenter (10), AudienceOrSeatingAreaCourtHouse (15), AudienceOrSeatingAreaExerciseCenter (7), AudienceOrSeatingAreaGymnasium (8), AudienceOrSeatingAreaMotionPictureTheatre (11), AudienceOrSeatingAreaPenitentiary (6), AudienceOrSeatingAreaPerformingArtsTheatre (12), AudienceOrSeatingAreaPoliceOrFireStations (14), AudienceOrSeatingAreaReligious (13), AudienceOrSeatingAreaSportsArena (9), BankCustomerArea (17), BankingActivityAreaOffice (18), BarberAndBeautyParlor (19), CardFileAndCataloguingLibrary (20), ClassroomOrLectureOrTraining (22), ClassroomOrLectureOrTrainingPenitentiary (21), ComfinementCellsCourtHouse (24), ComfinementCellsPenitentiary (23), ConferenceMeetingOrMultipurpose (25), CorridorOrTransition (26), CorridorOrTransitionManufacturingFacility (27), CorridorsWithPatientWaitingExamHospitalOrHealthcare (28), CourtroomCourtHouse (30), CourtSportsAreaSportsArena (29), DepartmentStoreSalesAreaRetail (31), DetailedManufacturingFacility (32), DiningArea (33), DiningAreaCivilServices (40), DiningAreaFamilyDining (35), DiningAreaHotel (34), DiningAreaLoungeOrLeisureDining (36), DiningAreaMotel (37), DiningAreaPenitentiary (39), DiningAreaTransportation (38), DormitoryBedroom (41), DormitoryStudyHall (42), DressingOrLockerOrFittingRoomAuditorium (46), DressingOrLockerOrFittingRoomCourtHouse (44), DressingOrLockerOrFittingRoomExerciseCenter (47), DressingOrLockerOrFittingRoomGymnasium (43), DressingOrLockerOrFittingRoomPerformingArtsTheatre (45), ElectricalOrMechanical (48), ElevatorLobbies (49), EmergencyHospitalOrHealthcare (50), EquipmentRoomManufacturingFacility (51), ExamOrTreatmentHospitalOrHealthcare (52), ExerciseAreaExerciseCenter (53), ExerciseAreaGymnasium (54), ExhibitSpaceConventionCenter (55), FellowshipHallReligiousBuildings (56), FineMaterialWarehouse (57), FineMerchandiseSalesAreaRetail (58), FireStationEngineRoomPoliceOrFireStation (59), FoodPreparation (60), GarageServiceOrRepairAutomotiveFacility (61), GeneralExhibitionMuseum (64), GeneralHighBayManufacturingFacility (62), GeneralLowBayManufacturingFacility (63), HospitalNurseryHospitalOrHealthcare (65), HospitalOrMedicalSuppliesHospitalOrHealthcare (66), HospitalOrRadiologyHospitalOrHealthcare (67), HotelOrConferenceCenterConferenceOrMeeting (68), InactiveStorage (69), JudgesChambersCourtHouse (70), LaboratoryOffice (71), LaundryIroningAndSorting (72), LaundryWashingHospitalOrHealthcare (73), LibraryAudioVisualLibraryAudioVisual (74), LivingQuartersDormitory (75), LivingQuartersHotel (77), LivingQuartersMotel (76), Lobby (78), LobbyAuditorium (81), LobbyHotel (84), LobbyMotionPictureTheatre (80), LobbyPerformingArtsTheatre (82), LobbyPostOffice (83), LobbyReligiousBuildings (79), LoungeOrRecreation (85), MallConcourseSalesAreaRetail (86), MassMerchandisingSalesAreaRetail (87), MediumOrBulkyMaterialWarehouse (88), MerchandisingSalesAreaRetail (89), MuseumAndGalleryStorage (90), NoOfSpaceTypes (125), NoSpaceType (-1), NurseStationHospitalOrHealthcare (91), OfficeCommonActivityAreasInactiveStorage (94), OfficeEnclosed (92), OfficeOpenPlan (93), OperatingRoomHospitalOrHealthcare (95), OtherTelevisedPlayingAreaSportsArena (96), ParkingAreaAttendantOnlyParkingGarage (97), ParkingAreaPedestrianParkingGarage (98), PatientRoomHospitalOrHealthcare (99), PersonalServicesSalesAreaRetail (100), PharmacyHospitalOrHealthcare (101), PhysicalTherapyHospitalOrHealthcare (102), PlayingAreaGymnasium (103), Plenum (104), PoliceStationLaboratoryPoliceOrFireStations (105), PublicAndStaffLoungeHospitalOrHealthcare (106), ReadingAreaLibrary (107), ReceptionOrWaitingHotel (110), ReceptionOrWaitingMotel (109), ReceptionOrWaitingTransportation (108), RecoveryHospitalOrHealthcare (111), RestorationMuseum (112), Restrooms (113), RingSportsAreaSportsArena (114), SleepingQuartersPoliceOrFireStation (115), SortingAreaPostOffice (116), SpecialtyStoreSalesAreaRetail (117), StacksLibrary (118), StairsInactive (119), Stairway (120), SupermarketSalesAreaRetail (121), TerminalTicketCounterTransportation (122), WorkshopWorkshop (123), WorshipPulpitChoirReligious (124)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ActiveStorage = None
    ActiveStorageHospitalOrHealthcare = None
    AirOrTrainOrBusBaggageArea = None
    AirportConcourse = None
    AtriumEachAdditionalFloor = None
    AtriumFirstThreeFloors = None
    AudienceOrSeatingAreaAuditorium = None
    AudienceOrSeatingAreaConventionCenter = None
    AudienceOrSeatingAreaCourtHouse = None
    AudienceOrSeatingAreaExerciseCenter = None
    AudienceOrSeatingAreaGymnasium = None
    AudienceOrSeatingAreaMotionPictureTheatre = None
    AudienceOrSeatingAreaPenitentiary = None
    AudienceOrSeatingAreaPerformingArtsTheatre = None
    AudienceOrSeatingAreaPoliceOrFireStations = None
    AudienceOrSeatingAreaReligious = None
    AudienceOrSeatingAreaSportsArena = None
    BankCustomerArea = None
    BankingActivityAreaOffice = None
    BarberAndBeautyParlor = None
    CardFileAndCataloguingLibrary = None
    ClassroomOrLectureOrTraining = None
    ClassroomOrLectureOrTrainingPenitentiary = None
    ComfinementCellsCourtHouse = None
    ComfinementCellsPenitentiary = None
    ConferenceMeetingOrMultipurpose = None
    CorridorOrTransition = None
    CorridorOrTransitionManufacturingFacility = None
    CorridorsWithPatientWaitingExamHospitalOrHealthcare = None
    CourtroomCourtHouse = None
    CourtSportsAreaSportsArena = None
    DepartmentStoreSalesAreaRetail = None
    DetailedManufacturingFacility = None
    DiningArea = None
    DiningAreaCivilServices = None
    DiningAreaFamilyDining = None
    DiningAreaHotel = None
    DiningAreaLoungeOrLeisureDining = None
    DiningAreaMotel = None
    DiningAreaPenitentiary = None
    DiningAreaTransportation = None
    DormitoryBedroom = None
    DormitoryStudyHall = None
    DressingOrLockerOrFittingRoomAuditorium = None
    DressingOrLockerOrFittingRoomCourtHouse = None
    DressingOrLockerOrFittingRoomExerciseCenter = None
    DressingOrLockerOrFittingRoomGymnasium = None
    DressingOrLockerOrFittingRoomPerformingArtsTheatre = None
    ElectricalOrMechanical = None
    ElevatorLobbies = None
    EmergencyHospitalOrHealthcare = None
    EquipmentRoomManufacturingFacility = None
    ExamOrTreatmentHospitalOrHealthcare = None
    ExerciseAreaExerciseCenter = None
    ExerciseAreaGymnasium = None
    ExhibitSpaceConventionCenter = None
    FellowshipHallReligiousBuildings = None
    FineMaterialWarehouse = None
    FineMerchandiseSalesAreaRetail = None
    FireStationEngineRoomPoliceOrFireStation = None
    FoodPreparation = None
    GarageServiceOrRepairAutomotiveFacility = None
    GeneralExhibitionMuseum = None
    GeneralHighBayManufacturingFacility = None
    GeneralLowBayManufacturingFacility = None
    HospitalNurseryHospitalOrHealthcare = None
    HospitalOrMedicalSuppliesHospitalOrHealthcare = None
    HospitalOrRadiologyHospitalOrHealthcare = None
    HotelOrConferenceCenterConferenceOrMeeting = None
    InactiveStorage = None
    JudgesChambersCourtHouse = None
    LaboratoryOffice = None
    LaundryIroningAndSorting = None
    LaundryWashingHospitalOrHealthcare = None
    LibraryAudioVisualLibraryAudioVisual = None
    LivingQuartersDormitory = None
    LivingQuartersHotel = None
    LivingQuartersMotel = None
    Lobby = None
    LobbyAuditorium = None
    LobbyHotel = None
    LobbyMotionPictureTheatre = None
    LobbyPerformingArtsTheatre = None
    LobbyPostOffice = None
    LobbyReligiousBuildings = None
    LoungeOrRecreation = None
    MallConcourseSalesAreaRetail = None
    MassMerchandisingSalesAreaRetail = None
    MediumOrBulkyMaterialWarehouse = None
    MerchandisingSalesAreaRetail = None
    MuseumAndGalleryStorage = None
    NoOfSpaceTypes = None
    NoSpaceType = None
    NurseStationHospitalOrHealthcare = None
    OfficeCommonActivityAreasInactiveStorage = None
    OfficeEnclosed = None
    OfficeOpenPlan = None
    OperatingRoomHospitalOrHealthcare = None
    OtherTelevisedPlayingAreaSportsArena = None
    ParkingAreaAttendantOnlyParkingGarage = None
    ParkingAreaPedestrianParkingGarage = None
    PatientRoomHospitalOrHealthcare = None
    PersonalServicesSalesAreaRetail = None
    PharmacyHospitalOrHealthcare = None
    PhysicalTherapyHospitalOrHealthcare = None
    PlayingAreaGymnasium = None
    Plenum = None
    PoliceStationLaboratoryPoliceOrFireStations = None
    PublicAndStaffLoungeHospitalOrHealthcare = None
    ReadingAreaLibrary = None
    ReceptionOrWaitingHotel = None
    ReceptionOrWaitingMotel = None
    ReceptionOrWaitingTransportation = None
    RecoveryHospitalOrHealthcare = None
    RestorationMuseum = None
    Restrooms = None
    RingSportsAreaSportsArena = None
    SleepingQuartersPoliceOrFireStation = None
    SortingAreaPostOffice = None
    SpecialtyStoreSalesAreaRetail = None
    StacksLibrary = None
    StairsInactive = None
    Stairway = None
    SupermarketSalesAreaRetail = None
    TerminalTicketCounterTransportation = None
    value__ = None
    WorkshopWorkshop = None
    WorshipPulpitChoirReligious = None


class gbXMLSurfaceType(Enum, IComparable, IFormattable, IConvertible):
    """
    This enumeration corresponds to the surfaceType attribute in gbXML
       and identifies the type of surface defined.
    
    enum gbXMLSurfaceType, values: Ceiling (7), ExteriorWall (1), InteriorFloor (3), InteriorWall (0), NoOfSurfaceTypes (12), RaisedFloor (10), Roof (2), Shade (4), SlabOnGrade (11), SurfaceAir (8), UndergroundCeiling (9), UndergroundSlab (6), UndergroundWall (5)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Ceiling = None
    ExteriorWall = None
    InteriorFloor = None
    InteriorWall = None
    NoOfSurfaceTypes = None
    RaisedFloor = None
    Roof = None
    Shade = None
    SlabOnGrade = None
    SurfaceAir = None
    UndergroundCeiling = None
    UndergroundSlab = None
    UndergroundWall = None
    value__ = None


class HVACLoadConstructionClass(Enum, IComparable, IFormattable, IConvertible):
    """
    Enumerated type listing options for construction class for HVAC analysis.
    
    enum HVACLoadConstructionClass, values: LooseConstruction (0), MediumConstruction (1), NoneConstruction (3), TightConstruction (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    LooseConstruction = None
    MediumConstruction = None
    NoneConstruction = None
    TightConstruction = None
    value__ = None


class HVACLoadLoadsReportType(Enum, IComparable, IFormattable, IConvertible):
    """
    Enumerated type listing possible types of reports generated for HVAC loads.
    
    enum HVACLoadLoadsReportType, values: DetailedReport (3), NoReport (0), SimpleReport (1), StandardReport (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DetailedReport = None
    NoReport = None
    SimpleReport = None
    StandardReport = None
    value__ = None


class MassEnergyAnalyticalModel(Element, IDisposable):
    """ This class associates a mass instance with an energy analytical model data and geometry. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetCoincidentEnergyAnalyticalModelFaceReference(document, referenceToFace):
        """
        GetCoincidentEnergyAnalyticalModelFaceReference(document: Document, referenceToFace: Reference) -> Reference
        
            Returns a Reference to a Face from the same or a different 
             MassEnergyAnalyticalModel
           that is coincident with the input Face.
        
        
            document: The Document.
            referenceToFace: A Reference to a Face of a MassEnergyAnalyticalModel.
        """
        pass

    @staticmethod
    def GetCoincidentMassZoneFaceReferences(document, referenceToFace):
        """
        GetCoincidentMassZoneFaceReferences(document: Document, referenceToFace: Reference) -> IList[Reference]
        
            Returns References to Faces from MassZones coincident with an input Face from a
             
           MassEnergyAnalyticalModel.
        
        
            document: The Document.
            referenceToFace: A Reference to a Face of a MassEnergyAnalyticalModel.
            Returns: Returns References to Faces from MassZones coincident with an input Face from a
             
           MassEnergyAnalyticalModel.
        """
        pass

    def GetJoinedMassEnergyAnalyticalModelElementIds(self):
        """
        GetJoinedMassEnergyAnalyticalModelElementIds(self: MassEnergyAnalyticalModel) -> ICollection[ElementId]
        
            The ElementIds of other MassEnergyAnalyticalModels that are "joined" to this 
             one.
        
            Returns: ElementIds of other MassEnergyAnalyticalModels that are joined to this one.
        """
        pass

    @staticmethod
    def GetMassEnergyAnalyticalModelIdForMassInstance(document, massInstanceId):
        """
        GetMassEnergyAnalyticalModelIdForMassInstance(document: Document, massInstanceId: ElementId) -> ElementId
        
            Get the ElementId of the MassEnergyAnalyticalModel for a mass instance.
        
            document: The Document.
            massInstanceId: ElementId of a mass instance.
            Returns: ElementId of a MassEnergyAnalyticalModel.
        """
        pass

    def GetMassSurfaceDataIdForReference(self, reference):
        """
        GetMassSurfaceDataIdForReference(self: MassEnergyAnalyticalModel, reference: Reference) -> ElementId
        
            Get the ElementId of the MassSurfaceData corresponding to the Reference.
        
            reference: A Reference to a face of this MassEnergyAnalyticalModel.
            Returns: ElementId of a MassSurfaceData.
        """
        pass

    def GetMassZoneIds(self):
        """
        GetMassZoneIds(self: MassEnergyAnalyticalModel) -> ICollection[ElementId]
        
            Get the MassZone ElementIds that are created from this 
             MassEnergyAnalyticalModel.
        
            Returns: Returns the ElementIds of MassZones.
        """
        pass

    def GetReferencesToAllFaces(self):
        """
        GetReferencesToAllFaces(self: MassEnergyAnalyticalModel) -> IList[Reference]
        
            Get References to all Faces which are meaningful for the 
             MassEnergyAnalyticalModel.
           Array of References to Faces of the 
             MassEnergyAnalyticalModel.
        """
        pass

    def GetReferencesToAllShadingFaces(self):
        """
        GetReferencesToAllShadingFaces(self: MassEnergyAnalyticalModel) -> IList[Reference]
        
            Get References to all Faces of the MassEnergyAnalyticalModel which are of Mass 
             Shade subcategory.
        
            Returns: Array of Reference to Faces that represent Mass Shades.
        """
        pass

    def GetValidSurfaceCategoryIdsForReference(self, reference, recommendedDefaultSubcategoryId):
        """
        GetValidSurfaceCategoryIdsForReference(self: MassEnergyAnalyticalModel, reference: Reference) -> (IList[ElementId], ElementId)
        
            The Mass surface subcategory ids that are appropriate values for the input 
             Reference.
        
        
            reference: A Reference to a Face of this MassEnergyAnalyticalModel.
            Returns: Returns the ElementIds of appropriate values for input Reference.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    MassId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ElementId of the mass instance the MassEnergyAnalyticalModel is associated with.

Get: MassId(self: MassEnergyAnalyticalModel) -> ElementId

"""

    MassZoneCoreOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If this value is greater than 0.0, in the MassEnergyAnalytical model a building "core" geometry
   will be created for each solid geometry of the mass instance.

Get: MassZoneCoreOffset(self: MassEnergyAnalyticalModel) -> float

Set: MassZoneCoreOffset(self: MassEnergyAnalyticalModel) = value
"""



class MassGBXMLExportOptions(object, IDisposable):
    """
    Options used when exporting a gbXML file from a mass model document.
    
    MassGBXMLExportOptions(massZoneIds: IList[ElementId])
    MassGBXMLExportOptions(massZoneIds: IList[ElementId], massIds: IList[ElementId])
    """
    def Dispose(self):
        """ Dispose(self: MassGBXMLExportOptions) """
        pass

    def GetMassIds(self):
        """
        GetMassIds(self: MassGBXMLExportOptions) -> IList[ElementId]
        
            Gets a list of masses to use as shading surfaces in the exported gbXML--these 
             masses must not have mass floors or mass zones so as not to end up with 
             duplicate surface information in the gbXML output.
        
            Returns: The ids of the masses.
        """
        pass

    def GetMassZoneIds(self):
        """
        GetMassZoneIds(self: MassGBXMLExportOptions) -> IList[ElementId]
        
            Gets a list of mass zones to analyze in the exported gbXML.
            Returns: The ids of the mass zone.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: MassGBXMLExportOptions, disposing: bool) """
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
    def __new__(self, massZoneIds, massIds=None):
        """
        __new__(cls: type, massZoneIds: IList[ElementId])
        __new__(cls: type, massZoneIds: IList[ElementId], massIds: IList[ElementId])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: MassGBXMLExportOptions) -> bool

"""



class MassLevelData(Element, IDisposable):
    """
    MassLevelData is a conceptual representation of an occupiable floor (Mass Floor) in a conceptual building model.
       It is defined by associating a particular level with a particular mass element in a Revit project.
    """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def IsEmpty(self):
        """
        IsEmpty(self: MassLevelData) -> bool
        
            Indicates if the MassLevelData (Mass Floor) has a geometrical representation.  
             May not
           if the level does not intersect the mass geometry.
        
            Returns: Returns True if MassLevelData is dimensionless, False otherwise.
        """
        pass

    @staticmethod
    def IsMassFamilyInstance(document, id):
        """
        IsMassFamilyInstance(document: Document, id: ElementId) -> bool
        
            Checks if the ElementId is a mass family instance.
        
            document: The document.
            id: The ElementId to be checked.
            Returns: True if the ElementId is a mass family instance, false otherwise.
        """
        pass

    def IsValidConceptualConstructionTypeElement(self, id):
        """
        IsValidConceptualConstructionTypeElement(self: MassLevelData, id: ElementId) -> bool
        
            Checks if the ElementId is an acceptable conceptual construction type ElementId 
             for the MassLevelData (Mass Floor).
        
        
            id: The ElementId to be checked.
            Returns: True if the ElementId is an acceptable conceptual construction type ElementId, 
             false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    ConceptualConstructionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ElementId of the conceptual construction associated with the MassLevelData (Mass Floor).

Get: ConceptualConstructionId(self: MassLevelData) -> ElementId

Set: ConceptualConstructionId(self: MassLevelData) = value
"""

    ConceptualConstructionIsByEnergyData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the ConceptualConstructionType of the MassLevelData (Mass Floor) is synchronized
   with the EnergyDataSettings or if it overrides those settings.

Get: ConceptualConstructionIsByEnergyData(self: MassLevelData) -> bool

Set: ConceptualConstructionIsByEnergyData(self: MassLevelData) = value
"""

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ElementId of the visualization material used for the MassLevelData (Mass Floor)

Get: MaterialId(self: MassLevelData) -> ElementId

Set: MaterialId(self: MassLevelData) = value
"""

    MaterialType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the material used for the graphical appearance is by category or a specific material, or
   if the material to be used should be taken from the ConceptualConstructionType of the MassLevelData.

Get: MaterialType(self: MassLevelData) -> MassSurfaceDataMaterialType

Set: MaterialType(self: MassLevelData) = value
"""

    NExteriorSurfaceArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The exterior surface area of the volume of the mass between the level of this MassLevelData (Mass Floor) to the next in the mass.

Get: NExteriorSurfaceArea(self: MassLevelData) -> float

"""

    NLevelFafArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The surface area of the intersection of the MassLevelData's level with the mass geometry.

Get: NLevelFafArea(self: MassLevelData) -> float

"""

    NLevelPerimeter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The perimeter of the intersection of the MassLevelData's level with the mass geometry.

Get: NLevelPerimeter(self: MassLevelData) -> float

"""

    NVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The volume of from the level of this MassLevelData (Mass Floor) to the next in the mass.

Get: NVolume(self: MassLevelData) -> float

"""

    OwningMassId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ElementId of the mass that the MassLevelData (Mass Floor) is associated with.

Get: OwningMassId(self: MassLevelData) -> ElementId

"""

    StrUsage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A String which describes the usage or occupancy type of the level of the MassLevelData.

Get: StrUsage(self: MassLevelData) -> str

Set: StrUsage(self: MassLevelData) = value
"""



class MassSurfaceData(Element, IDisposable):
    """ Holds properties and other data about a face in the MassEnergyAnalyticalModel element. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetFaceReferences(self):
        """
        GetFaceReferences(self: MassSurfaceData) -> IList[Reference]
        
            Gets References to the faces that the MassSurfaceData provides properties for.
            Returns: Returns an array of References to Faces that the MassSurfaceData provides 
             properties for.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Area of the references that the MassSurfaceData provides properties for.

Get: Area(self: MassSurfaceData) -> float

"""

    CategoryIdForConceptualSurfaceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the mass subcategory ElementId used for ConceptualSurfaceType for this MassSurfaceData.

Get: CategoryIdForConceptualSurfaceType(self: MassSurfaceData) -> ElementId

"""

    ConceptualConstructionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the conceptual construction associated with the reference surface.

Get: ConceptualConstructionId(self: MassSurfaceData) -> ElementId

Set: ConceptualConstructionId(self: MassSurfaceData) = value
"""

    IsConceptualConstructionByEnergyData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True when the ConceptualConstructionType id is synchronized to the EnergyDataSettings.
   False when the ConceptualConstructionType id is overridden for this MassSurfaceData.

Get: IsConceptualConstructionByEnergyData(self: MassSurfaceData) -> bool

Set: IsConceptualConstructionByEnergyData(self: MassSurfaceData) = value
"""

    IsGlazingShaded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if shade geometry is auto-generated on the top edge of auto-generated glazing.

Get: IsGlazingShaded(self: MassSurfaceData) -> bool

Set: IsGlazingShaded(self: MassSurfaceData) = value
"""

    IsSlab = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if a floor is a slab.

Get: IsSlab(self: MassSurfaceData) -> bool

"""

    IsUnderground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the roof, floor, slab, or wall surface reference is underground.

Get: IsUnderground(self: MassSurfaceData) -> bool

Set: IsUnderground(self: MassSurfaceData) = value
"""

    MassLevelDataId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The MassLevelData used when the surface is horizontal, planar, and at the same height as a MassLevelData
   related to the same mass as the referenced face.

Get: MassLevelDataId(self: MassSurfaceData) -> ElementId

"""

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The visualization material used for the surface for displaying the energy analytical model.

Get: MaterialId(self: MassSurfaceData) -> ElementId

Set: MaterialId(self: MassSurfaceData) = value
"""

    MaterialType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """material type of mass zone

Get: MaterialType(self: MassSurfaceData) -> MassSurfaceDataMaterialType

Set: MaterialType(self: MassSurfaceData) = value
"""

    PercentageGlazing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The target percentage of the reference wall surface that is to
   be covered with automatically generated windows. Revit will use this number when
   determining the size, shape, and location of automatically generated windows.

Get: PercentageGlazing(self: MassSurfaceData) -> float

Set: PercentageGlazing(self: MassSurfaceData) = value
"""

    PercentageSkylights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The target percentage of the reference roof surface that is to
   be covered with automatically generated skylights.  Revit will use this number when
   determining the size, shape, and location of automatically generated skylights.

Get: PercentageSkylights(self: MassSurfaceData) -> float

Set: PercentageSkylights(self: MassSurfaceData) = value
"""

    ReferenceElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ElementId of the element whose face the MassSurfaceData primarily refers to.

Get: ReferenceElementId(self: MassSurfaceData) -> ElementId

"""

    ShadeDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How far any auto-generated shades should extend from the wall surface.

Get: ShadeDepth(self: MassSurfaceData) -> float

Set: ShadeDepth(self: MassSurfaceData) = value
"""

    SillHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The height above the level where the bottoms of auto-generated windows will be located.

Get: SillHeight(self: MassSurfaceData) -> float

Set: SillHeight(self: MassSurfaceData) = value
"""

    SkylightWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The length dimension to be used for the sides of each individual square skylight
   produced in the grid of auto-generated skylights.

Get: SkylightWidth(self: MassSurfaceData) -> float

Set: SkylightWidth(self: MassSurfaceData) = value
"""

    SurfaceDataSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether the MassSurfaceData properties are driven by the EnergyDataSettings
   of the Document or are overridden for the surface.

Get: SurfaceDataSource(self: MassSurfaceData) -> MassSurfaceDataSource

Set: SurfaceDataSource(self: MassSurfaceData) = value
"""



class MassSurfaceDataMaterialType(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates how the visualization material for the MassSurfaceData is calculated.
    
    enum MassSurfaceDataMaterialType, values: MaterialByConstruction (-2), NormalMaterial (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    MaterialByConstruction = None
    NormalMaterial = None
    value__ = None


class MassSurfaceDataSource(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates whether values for the properties of the MassSurfaceData
       are synchronized with the EnergyDataSettings of the
       document or instead, serve as overrides of those settings.
    
    enum MassSurfaceDataSource, values: EnergyData (0), Invalid (-1), Surface (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    EnergyData = None
    Invalid = None
    Surface = None
    value__ = None


class MassZone(Element, IDisposable):
    """ MassZones are created from the MassEnergyAnalyticalModel.  They are conceptual representations of individually heated and cooled sub-volumes of a building. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetCoincidentReferenceFromAdjacentZone(self, referenceToZoneFace):
        """
        GetCoincidentReferenceFromAdjacentZone(self: MassZone, referenceToZoneFace: Reference) -> Reference
        
            This method is used to get a Reference from an adjacent MassZone that is 
             coincident to a Reference of this MassZone.
        
        
            referenceToZoneFace: Reference to face of MassZone.
            Returns: Reference to coincident face of adjacent MassZone or ll if there is no adjacent 
             MassZone face Reference.
        """
        pass

    def GetEquivalentReferenceFromMassOrLevel(self, referenceToZoneFace):
        """
        GetEquivalentReferenceFromMassOrLevel(self: MassZone, referenceToZoneFace: Reference) -> Reference
        
            Returns a Reference to a face of a MassEnergyAnalyticalModel element or
           an 
             element Reference to a MassLevelData element.
           This Reference represents 
             what the MassZone face was "cut from" when making the MassZone for the level.
        
        
            referenceToZoneFace: Reference to a face of the zone to get an equivalent reference for.
            Returns: Reference to MassEnergyAnalyticalModel or MassLevelData.  Should only be ll if 
             there is an error
           in the MassEnergyAnalyticalModel data or the input is not 
             a
        """
        pass

    def GetMassDataElementIdForZoneFaceReference(self, referenceOfZone):
        """
        GetMassDataElementIdForZoneFaceReference(self: MassZone, referenceOfZone: Reference) -> ElementId
        
            MassZone faces come from faces of MassEnergyAnalyticalModel, and those faces 
             have MassSurfaceData
           or MassLevelData elements associated with them.
        
        
            referenceOfZone: Reference to face of the MassZone to get data element for.
            Returns: Id of MassSurfaceData or MassLevelData element.
        """
        pass

    def GetReferencesToEnergyAnalysisFaces(self):
        """
        GetReferencesToEnergyAnalysisFaces(self: MassZone) -> IList[Reference]
        
            Used to get References to all the faces of the MassZone that are used for 
             Energy Analysis.
        
            Returns: Array of References to faces of MassZone.
        """
        pass

    def IsEmpty(self):
        """
        IsEmpty(self: MassZone) -> bool
        
            Indicates if MassZone has no geometry.  Such zones should not be shown to the 
             user.
        
            Returns: Returns True if MassZone has no geometry.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    ConditionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The gbXMLConditionType of the MassZone.

Get: ConditionType(self: MassZone) -> gbXMLConditionType

Set: ConditionType(self: MassZone) = value
"""

    CutByLowerLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates the relationship between the MassZone and its lower level.

Get: CutByLowerLevel(self: MassZone) -> MassZoneLevelCutState

"""

    CutByUpperLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates the relationship between the MassZone and its upper level.

Get: CutByUpperLevel(self: MassZone) -> MassZoneLevelCutState

"""

    FloorArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The floor area of the MassZone.

Get: FloorArea(self: MassZone) -> float

"""

    IsZoneOccupiable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A MassZone must have a level as its bottom to be occupiable;
   If it does not, it is still a MassZone, but it is not occupiable

Get: IsZoneOccupiable(self: MassZone) -> bool

"""

    LowerLevelId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The bottom level defining the MassZone.

Get: LowerLevelId(self: MassZone) -> ElementId

"""

    MassEnergyAnalyticalModelId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ElementId of the MassEnergyAnalyticalModel that the MassZone is derived from.

Get: MassEnergyAnalyticalModelId(self: MassZone) -> ElementId

"""

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The visualization material for the MassZone.
   Will be InvalidElementId if material is by category or the material type is by MassZoneMaterialTypeMaterialBySurfaceType.

Get: MaterialId(self: MassZone) -> ElementId

Set: MaterialId(self: MassZone) = value
"""

    MaterialType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates how the material of MassZone faces is determined.

Get: MaterialType(self: MassZone) -> MassZoneMaterialType

Set: MaterialType(self: MassZone) = value
"""

    SpaceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The gbXMLSpaceType of the MassZone.

Get: SpaceType(self: MassZone) -> gbXMLSpaceType

Set: SpaceType(self: MassZone) = value
"""

    UpperLevelId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The upper level defining the MassZone.

Get: UpperLevelId(self: MassZone) -> ElementId

"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The volume of the MassZone.

Get: Volume(self: MassZone) -> float

"""



class MassZoneLevelCutState(Enum, IComparable, IFormattable, IConvertible):
    """
    The relationship between lower level or upper level and the MassZone.
       The MassZone is not intersected by this level, this level just happens to be the nearest upper or lower level.
       The MassZone was created by cutting its source geometry with this level.  The level cuts through the MassZone geometry.
       One or more faces of the MassZone are coincident with this level and the level does not otherwise cut through or intersect
       the MassZone geometry.
    
    enum MassZoneLevelCutState, values: Cut (1), NotCut (0), NotCutButCoincident (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Cut = None
    NotCut = None
    NotCutButCoincident = None
    value__ = None


class MassZoneMaterialType(Enum, IComparable, IFormattable, IConvertible):
    """
    MassZone material type.
    
    enum MassZoneMaterialType, values: MaterialBySurfaceType (-2), NormalMaterial (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    MaterialBySurfaceType = None
    NormalMaterial = None
    value__ = None


class Polyloop(object, IDisposable):
    """ A Polyloop represent a planar polygon with ordered points. """
    def ComputeArea(self):
        """
        ComputeArea(self: Polyloop) -> float
        
            Gets the area for this polygon.
            Returns: The area for this polygon.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Polyloop) """
        pass

    def GetPoints(self):
        """
        GetPoints(self: Polyloop) -> IList[XYZ]
        
            Gets the array of points in the polygon
            Returns: The array of points in the polygon
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Polyloop, disposing: bool) """
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

    Centroid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The polygon centroid.

Get: Centroid(self: Polyloop) -> XYZ

"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The direction for the outward normal for this polygon.

Get: Direction(self: Polyloop) -> XYZ

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: Polyloop) -> bool

"""



class SpatialFieldManager(Element, IDisposable):
    """
    Exposes all API for an external analysis application.
       Its primary role is creation, deletion and modification of SpatialFieldElement elements.
    """
    def AddSpatialFieldPrimitive(self, *__args):
        """
        AddSpatialFieldPrimitive(self: SpatialFieldManager, reference: Reference) -> int
        
            Creates an empty analysis results primitive associated with a reference.
        
            reference: Reference pointing to the curve or face to be associated with the primitive
            Returns: Unique index of primitive for future references
        AddSpatialFieldPrimitive(self: SpatialFieldManager) -> int
        
            Creates empty analysis results primitive not associated with any geometry 
             element
        
            Returns: Unique index of primitive for future references
        AddSpatialFieldPrimitive(self: SpatialFieldManager, reference: Reference, hidingMode: SpatialFieldPrimitiveHideMode) -> int
        
            Creates an empty analysis results primitive associated with a reference, with 
             the option to control how the reference element is hidden.
        
        
            reference: Reference pointing to the curve or face to be associated with the primitive
            hidingMode: The mode used to hide the original model element
            Returns: Unique index of primitive for future references
        AddSpatialFieldPrimitive(self: SpatialFieldManager, curve: Curve, trf: Transform) -> int
        
            Creates empty analysis results primitive associated with a curve and a 
             transform.
        
        
            curve: Curve to be associated with the primitive.
           %curve% does NOT correspond to 
             actual Revit geometry, i.e. it cannot be associated with reference;
           
             otherwise the other overload of the method must be used (taking "reference" as 
             the input)
        
            trf: Conformal Transform to be applied to %curve%.
            Returns: Unique index of primitive for future references
        AddSpatialFieldPrimitive(self: SpatialFieldManager, face: Face, trf: Transform) -> int
        
            Creates empty analysis results primitive associated with a face and a transform.
        
            face: Face to be associated with the primitive
            trf: Conformal Transform to be applied to %face%
            Returns: Unique index of primitive for future references
        """
        pass

    def Clear(self):
        """
        Clear(self: SpatialFieldManager)
            Clear all analysis results managed by this manager object
        """
        pass

    @staticmethod
    def CreateSpatialFieldManager(view, numberOfMeasurements):
        """
        CreateSpatialFieldManager(view: View, numberOfMeasurements: int) -> SpatialFieldManager
        
            Factory method - creates manager object for the given view
        
            view: View for which manager object is created or retrieved
            numberOfMeasurements: Total number of measurements in the calculated results.
           This number defines 
             the length of value arrays in ValueAtPoint objects
        
            Returns: Manager object for the view passed in the argument
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetLegend(self):
        """
        GetLegend(self: SpatialFieldManager) -> AnalysisDisplayLegend
        
            Returns legend element or NULL
            Returns: The legend element or NULL
        """
        pass

    def GetMaximum(self, resultIndex, rawValue):
        """
        GetMaximum(self: SpatialFieldManager, resultIndex: int, rawValue: bool) -> float
        
            Calculates the maximum value for all primitives
        
            resultIndex: Index of result schema
            rawValue: If true returned value is NOT multiplied by the current result's units 
             multiplier, otherwise it IS
        
            Returns: Resulting maximum value
        """
        pass

    def GetMinimum(self, resultIndex, rawValue):
        """
        GetMinimum(self: SpatialFieldManager, resultIndex: int, rawValue: bool) -> float
        
            Calculates the minimum value for all primitives
        
            resultIndex: Index of result schema
            rawValue: If true returned value is NOT multiplied by the current result's units 
             multiplier, otherwise it IS
        
            Returns: Resulting minimum value
        """
        pass

    def GetRegisteredResults(self):
        """
        GetRegisteredResults(self: SpatialFieldManager) -> IList[int]
        
            Returns an array of indices of all registered results
        """
        pass

    def GetResultSchema(self, idx):
        """
        GetResultSchema(self: SpatialFieldManager, idx: int) -> AnalysisResultSchema
        
            Returns result schema by index
        
            idx: Index of registered result schema
        """
        pass

    @staticmethod
    def GetSpatialFieldManager(view):
        """
        GetSpatialFieldManager(view: View) -> SpatialFieldManager
        
            Retrieves manager object for the given view or returns NULL
        
            view: View for which manager object is retrieved
            Returns: Manager object for the view passed in the argument
        """
        pass

    def IsResultSchemaNameUnique(self, name, resultIndexToSkip):
        """
        IsResultSchemaNameUnique(self: SpatialFieldManager, name: str, resultIndexToSkip: int) -> bool
        
            Verify the uniqueness of the name among all registered result schemas.
        
            name: Name to verify uniqueness of.
            resultIndexToSkip: Index of result (e.g. to be replaced) which names should not count for 
             uniqueness; negative number means nothing is excluded from comparison.
        
            Returns: True if name is unique, false otherwise.
        """
        pass

    @staticmethod
    def IsTextTypeIdValid(textTypeId, doc):
        """
        IsTextTypeIdValid(textTypeId: ElementId, doc: Document) -> bool
        
            Verify if text type id is valid.
        
            textTypeId: Text type id to be validated.
            doc: Document for which %textTypeId% is validated.
            Returns: True if text type id is valid, false otherwise.
        """
        pass

    def RegisterResult(self, resultSchema):
        """
        RegisterResult(self: SpatialFieldManager, resultSchema: AnalysisResultSchema) -> int
        
            Registers result and assigns it a unique result index
        
            resultSchema: Result schema to be registered
            Returns: Unique index assigned to the result
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveSpatialFieldPrimitive(self, idx):
        """
        RemoveSpatialFieldPrimitive(self: SpatialFieldManager, idx: int)
            Removes analysis results primitive identified by the unique index
        
            idx: Unique index identifying the primitive
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetMeasurementDescriptions(self, measurementDescriptions):
        """ SetMeasurementDescriptions(self: SpatialFieldManager, measurementDescriptions: IList[str]) """
        pass

    def SetMeasurementNames(self, measurementNames):
        """ SetMeasurementNames(self: SpatialFieldManager, measurementNames: IList[str]) """
        pass

    def SetResultSchema(self, idx, resultSchema):
        """
        SetResultSchema(self: SpatialFieldManager, idx: int, resultSchema: AnalysisResultSchema)
            Sets a new value for an existing result schema in the result registry
        
            idx: Index of registered result schema
            resultSchema: Result schema replacing the existent one
        """
        pass

    def UpdateSpatialFieldPrimitive(self, idx, fieldDomainPoints, fieldValues, resultIndex):
        """
        UpdateSpatialFieldPrimitive(self: SpatialFieldManager, idx: int, fieldDomainPoints: FieldDomainPoints, fieldValues: FieldValues, resultIndex: int)
            Populates analysis results data (or replaces the existing data) in the existing 
             primitive identified by the unique index
        
        
            idx: Unique index identifying the primitive
            fieldDomainPoints: Set of domain points.
           If the new set of domain points is supplied, all 
             previously supplied domain points and field values for all results are removed 
             from the primitive.
           If %fieldDomainPoints% is ll only fieldValues are 
             updated
        
            fieldValues: Set of data values.
           Number of values in fieldValues must coincide with the 
             number of points in fieldDomainPoints
        
            resultIndex: Unique index identifying the result schema
        """
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

    CurrentMeasurement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Stores the currently displayed measurement

Get: CurrentMeasurement(self: SpatialFieldManager) -> int

Set: CurrentMeasurement(self: SpatialFieldManager) = value
"""

    LegendPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Stores current position of analysis results legend element in view

Get: LegendPosition(self: SpatialFieldManager) -> XYZ

Set: LegendPosition(self: SpatialFieldManager) = value
"""

    LegendShowConfigurationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true legend contains analysis configuration name.

Get: LegendShowConfigurationName(self: SpatialFieldManager) -> bool

Set: LegendShowConfigurationName(self: SpatialFieldManager) = value
"""

    LegendShowDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true legend contains analysis description.

Get: LegendShowDescription(self: SpatialFieldManager) -> bool

Set: LegendShowDescription(self: SpatialFieldManager) = value
"""

    LegendTextTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Stores element id of text associated with common (result-independent) part of legend in view.

Get: LegendTextTypeId(self: SpatialFieldManager) -> ElementId

Set: LegendTextTypeId(self: SpatialFieldManager) = value
"""

    NumberOfMeasurements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Stores the total number of measurements

Get: NumberOfMeasurements(self: SpatialFieldManager) -> int

"""

    ResultsVisibleInView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enables analysis results visibility in the view.

Get: ResultsVisibleInView(self: SpatialFieldManager) -> bool

Set: ResultsVisibleInView(self: SpatialFieldManager) = value
"""

    UseRangeForAllMeasurements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Governs how minimum and maximum values (the data range) are calculated.

Get: UseRangeForAllMeasurements(self: SpatialFieldManager) -> bool

Set: UseRangeForAllMeasurements(self: SpatialFieldManager) = value
"""



class SpatialFieldPrimitiveHideMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines modes which can be used by a SpatialFieldPrimitive to hide the original referenced element.
    
    enum SpatialFieldPrimitiveHideMode, values: Default (0), HideNone (1), HideOnlyReference (2), HideWholeElement (3)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Default = None
    HideNone = None
    HideOnlyReference = None
    HideWholeElement = None
    value__ = None


class ValueAtPoint(ValueAtPointBase, IDisposable):
    """
    Stores values at one domain point.
       Each value corresponds to a "measurement" for which this value was calculated.
    
    ValueAtPoint(otherObject: ValueAtPoint)
    ValueAtPoint(values: IList[float])
    """
    def Dispose(self):
        """ Dispose(self: ValueAtPointBase, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ValueAtPointBase, disposing: bool) """
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
    def __new__(self, *__args):
        """
        __new__(cls: type, otherObject: ValueAtPoint)
        __new__(cls: type, values: IList[float])
        """
        pass


class VectorAtPoint(ValueAtPointBase, IDisposable):
    """
    Stores vectors at one domain point.
       Each vector corresponds to a "measurement" for which this vector was calculated.
    
    VectorAtPoint(otherObject: VectorAtPoint)
    VectorAtPoint(vectors: IList[XYZ])
    """
    def Dispose(self):
        """ Dispose(self: ValueAtPointBase, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ValueAtPointBase, disposing: bool) """
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
    def __new__(self, *__args):
        """
        __new__(cls: type, otherObject: VectorAtPoint)
        __new__(cls: type, vectors: IList[XYZ])
        """
        pass


