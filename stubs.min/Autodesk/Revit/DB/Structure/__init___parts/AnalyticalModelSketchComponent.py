class AnalyticalModelSketchComponent(object, IDisposable):
    """ This is one component of an AnalyticalModelSketch, which exists to provide greater granularity over the Analytical Model than at the Element level. """
    def Dispose(self):
        """ Dispose(self: AnalyticalModelSketchComponent) """
        pass

    def EnableAutoDetect(self):
        """
        EnableAutoDetect(self: AnalyticalModelSketchComponent)
            Enables Auto-detect on Sketch Component.
        """
        pass

    def GetAnalyticalAlignmentMethod(self):
        """
        GetAnalyticalAlignmentMethod(self: AnalyticalModelSketchComponent) -> AnalyticalAlignmentMethod
        
            Retrieves Analytical Alignment Method preset for Sketch Component.
            Returns: Indicates whether Alignment Method is at Auto-Detect or Projection
        """
        pass

    def GetAnalyticalProjectionDatumPlane(self):
        """
        GetAnalyticalProjectionDatumPlane(self: AnalyticalModelSketchComponent) -> ElementId
        
            Retrieves Datum Plane ElementId for Analytical Projection
            Returns: Represents Datum used for Analytical Projection, if Analytical Projection Type 
             indicates that a
           Datum Plane is to be used.  Otherwise, invalidElementId is 
             returned.
        """
        pass

    def GetAnalyticalProjectionType(self):
        """
        GetAnalyticalProjectionType(self: AnalyticalModelSketchComponent) -> AnalyticalProjectionType
        
            Retrieves Analytical Projection Type preset for Sketch Component.
            Returns: Indicates whether Analytical Projection is at a preset, or refers to a Datum.
        """
        pass

    def GetAutoDetectMatchedElements(self):
        """
        GetAutoDetectMatchedElements(self: AnalyticalModelSketchComponent) -> ICollection[ElementId]
        
            Retrieves ElementIds that Sketch Component is Auto-detecting against.
            Returns: Set of ElementIds that Sketch Component is auto-detecting against.
        """
        pass

    def GetComponentElementId(self):
        """
        GetComponentElementId(self: AnalyticalModelSketchComponent) -> ElementId
        
            Retrieves ElementId of Sketch Component, if such an operation makes sense.
            Returns: ElementId of Sketch Component.
           If the operation does not make sense 
             (perhaps because the Sketch abstraction does not
           translate one-to-one to 
             ElementIds), then this will return invalidElementId.
        """
        pass

    def IsAutoDetectEnabled(self):
        """
        IsAutoDetectEnabled(self: AnalyticalModelSketchComponent) -> bool
        
            Indicates whether Auto-detect is enabled on the given Sketch component.
            Returns: True if Auto-detect is enabled, false otherwise.
        """
        pass

    def IsValidAnalyticalAlignmentMethod(self, alignmentMethod):
        """
        IsValidAnalyticalAlignmentMethod(self: AnalyticalModelSketchComponent, alignmentMethod: AnalyticalAlignmentMethod) -> bool
        
            Indicates whether Analytical Alignment Method is valid for Sketch Component.
        
            alignmentMethod: Analytical Alignment Method preset to test for validity.
            Returns: True means alignment method is valid, false otherwise.
        """
        pass

    def IsValidAnalyticalProjectionType(self, projectionType):
        """
        IsValidAnalyticalProjectionType(self: AnalyticalModelSketchComponent, projectionType: AnalyticalProjectionType) -> bool
        
            Indicates whether Analytical Projection Type is valid for Sketch Component.
        
            projectionType: Analytical Projection Type preset to test for validity.
            Returns: True is projection type is valid, false otherwise.
        """
        pass

    def IsValidDatumPlaneForProjection(self, datumPlaneId):
        """
        IsValidDatumPlaneForProjection(self: AnalyticalModelSketchComponent, datumPlaneId: ElementId) -> bool
        
            Indicates whether Datum Plane is valid Analytical Projection of Sketch 
             Component.
        
        
            datumPlaneId: ElementId identifying Datum Plane.
            Returns: True if Datum Plane is valid; false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AnalyticalModelSketchComponent, disposing: bool) """
        pass

    def SetAnalyticalAlignmentMethod(self, alignmentMethod):
        """
        SetAnalyticalAlignmentMethod(self: AnalyticalModelSketchComponent, alignmentMethod: AnalyticalAlignmentMethod)
            Sets the Alignment Method to the supplied Analytical Alignment Method
        
            alignmentMethod: Analytical Alignment Method which the Analytical Model should use for alignment.
        """
        pass

    def SetAnalyticalProjectionDatumPlane(self, datumPlaneId):
        """
        SetAnalyticalProjectionDatumPlane(self: AnalyticalModelSketchComponent, datumPlaneId: ElementId)
            Sets the Analytical Projection to supplied Datum Plane.
        
            datumPlaneId: Identifies Datum Plane ElementId.
        """
        pass

    def SetAnalyticalProjectionType(self, projectionType):
        """
        SetAnalyticalProjectionType(self: AnalyticalModelSketchComponent, projectionType: AnalyticalProjectionType)
            Sets the Analytical Projection to the supplied Analytical Projection Type.
        
            projectionType: Analytical Projection Type to which the Analytical Model should project.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: AnalyticalModelSketchComponent) -> bool

"""


