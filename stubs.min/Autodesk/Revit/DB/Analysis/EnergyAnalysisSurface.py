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


