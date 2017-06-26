class SpatialElementGeometryResults(object, IDisposable):
    """ The results of spatial element geometry calculation. """
    def Dispose(self):
        """ Dispose(self: SpatialElementGeometryResults) """
        pass

    def GetBoundaryFaceInfo(self, face):
        """
        GetBoundaryFaceInfo(self: SpatialElementGeometryResults, face: Face) -> IList[SpatialElementBoundarySubface]
        
            Query the spatial element boundary face information with the given face.
        
            face: The face from the spatial element's geometry.
            Returns: Sub-faces related to the room bounding elements that define the spatial element 
             face. Returns ll if there is no corresponding boundary information with the 
             given face.
        """
        pass

    def GetGeometry(self):
        """
        GetGeometry(self: SpatialElementGeometryResults) -> Solid
        
            The solid from the spatial element.
            Returns: Requested solid.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: SpatialElementGeometryResults, disposing: bool) """
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

Get: IsValidObject(self: SpatialElementGeometryResults) -> bool

"""


