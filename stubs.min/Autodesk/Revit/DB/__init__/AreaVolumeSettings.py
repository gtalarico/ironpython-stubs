class AreaVolumeSettings(Element, IDisposable):
    """ This class provides access to settings related to volume and area computations. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    @staticmethod
    def GetAreaVolumeSettings(aDoc):
        """
        GetAreaVolumeSettings(aDoc: Document) -> AreaVolumeSettings
        
            Get the area and volume settings of the project.
        
            aDoc: The document.
            Returns: The area and volume settings of the project.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetSpatialElementBoundaryLocation(self, spType):
        """
        GetSpatialElementBoundaryLocation(self: AreaVolumeSettings, spType: SpatialElementType) -> SpatialElementBoundaryLocation
        
            Gets the spatial element boundary location based on spatial element type.
        
            spType: The spatial element type.
            Returns: The boundary location.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetSpatialElementBoundaryLocation(self, spatialElementBoundaryLocation, spType):
        """
        SetSpatialElementBoundaryLocation(self: AreaVolumeSettings, spatialElementBoundaryLocation: SpatialElementBoundaryLocation, spType: SpatialElementType)
            Sets the spatial element boundary location of a spatial element type.
        
            spatialElementBoundaryLocation: The boundary location.
            spType: The spatial element type.
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

    ComputeVolumes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True to enable volume computation.  False to disable it.

Get: ComputeVolumes(self: AreaVolumeSettings) -> bool

Set: ComputeVolumes(self: AreaVolumeSettings) = value
"""


