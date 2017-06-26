class DefaultDivideSettings(Element, IDisposable):
    """ Provides access to project-wide divide settings. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetDefaultDivideSettings(cda):
        """
        GetDefaultDivideSettings(cda: Document) -> DefaultDivideSettings
        
            Obtains the DefaultDivideSettings object for the specified document.
        
            cda: A document.
            Returns: The DefaultDivideSettings object.
        """
        pass

    def GetSurfaceDistance(self, gridlines):
        """
        GetSurfaceDistance(self: DefaultDivideSettings, gridlines: UVGridlineType) -> float
        
            Gets the default Divided Surface distance for a fixed, minimum, or maximum 
             distance layout for U or V gridlines.
        
        
            gridlines: U-gridlines or V-gridlines.
            Returns: The default distance for the layout.
        """
        pass

    def GetSurfaceLayout(self, gridlines):
        """
        GetSurfaceLayout(self: DefaultDivideSettings, gridlines: UVGridlineType) -> SpacingRuleLayout
        
            Gets the default Divided Surface layout for U or V gridlines.
        
            gridlines: U-gridlines or V-gridlines.
            Returns: The layout spacing rule.
        """
        pass

    def GetSurfaceNumber(self, gridlines):
        """
        GetSurfaceNumber(self: DefaultDivideSettings, gridlines: UVGridlineType) -> int
        
            Gets the default Divided Surface number for a fixed number layout for U or V 
             gridlines.
        
        
            gridlines: U-gridlines or V-gridlines.
            Returns: The default number for a fixed number layout.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetSurfaceDistance(self, gridlines, distance):
        """
        SetSurfaceDistance(self: DefaultDivideSettings, gridlines: UVGridlineType, distance: float)
            Sets the default Divided Surface distance for a fixed, minimum, or maximum 
             distance layout for U or V gridlines.
        
        
            gridlines: U-gridlines or V-gridlines.
            distance: A default distance for a layout.
        """
        pass

    def SetSurfaceLayout(self, gridlines, layout):
        """
        SetSurfaceLayout(self: DefaultDivideSettings, gridlines: UVGridlineType, layout: SpacingRuleLayout)
            Sets the default Divided Surface layout for U or V gridlines.
        
            gridlines: U-gridlines or V-gridlines.
            layout: A layout spacing rule.
        """
        pass

    def SetSurfaceNumber(self, gridlines, number):
        """
        SetSurfaceNumber(self: DefaultDivideSettings, gridlines: UVGridlineType, number: int)
            Sets the default Divided Surface number for a fixed number layout for U or V 
             gridlines.
        
        
            gridlines: U-gridlines or V-gridlines.
            number: A default number for a fixed number layout.
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

    PathDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A default Divided Path distance for a fixed, minimum, or maximum distance layout.

Get: PathDistance(self: DefaultDivideSettings) -> float

Set: PathDistance(self: DefaultDivideSettings) = value
"""

    PathLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A default Divided Path layout.

Get: PathLayout(self: DefaultDivideSettings) -> SpacingRuleLayout

Set: PathLayout(self: DefaultDivideSettings) = value
"""

    PathMeasurementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A default Divided Path measurement type for distance layouts.

Get: PathMeasurementType(self: DefaultDivideSettings) -> DividedPathMeasurementType

Set: PathMeasurementType(self: DefaultDivideSettings) = value
"""

    PathNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A default Divided Path number for a fixed number layout.

Get: PathNumber(self: DefaultDivideSettings) -> int

Set: PathNumber(self: DefaultDivideSettings) = value
"""


