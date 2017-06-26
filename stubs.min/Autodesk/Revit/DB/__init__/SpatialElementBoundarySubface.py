class SpatialElementBoundarySubface(object, IDisposable):
    """ SpatialElementBoundarySubface represents the geometry boundary information of spatial element. """
    def Dispose(self):
        """ Dispose(self: SpatialElementBoundarySubface) """
        pass

    def GetBoundingElementFace(self):
        """
        GetBoundingElementFace(self: SpatialElementBoundarySubface) -> Face
        
            Returns the face of the bounding element.
            Returns: The face of the bounding element.
        """
        pass

    def GetSpatialElementFace(self):
        """
        GetSpatialElementFace(self: SpatialElementBoundarySubface) -> Face
        
            Returns the face of the spatial element's 3D geometry.
            Returns: The face of the spatial element's 3D geometry.
        """
        pass

    def GetSubface(self):
        """
        GetSubface(self: SpatialElementBoundarySubface) -> Face
        
            Returns a face that represents the portion of the room face bounded by the 
             boundary element.
        
            Returns: The sub-face.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: SpatialElementBoundarySubface, disposing: bool) """
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

Get: IsValidObject(self: SpatialElementBoundarySubface) -> bool

"""

    SpatialBoundaryElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Element that gave rise to this room face.

Get: SpatialBoundaryElement(self: SpatialElementBoundarySubface) -> LinkElementId

"""

    SubfaceArisesFromElementFace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the subface is coincident with a portion of a (possibly offset) face of the element.

Get: SubfaceArisesFromElementFace(self: SpatialElementBoundarySubface) -> bool

"""

    SubfaceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of the subface.

Get: SubfaceType(self: SpatialElementBoundarySubface) -> SubfaceType

"""

    Valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the subface instance is valid and can be used.

Get: Valid(self: SpatialElementBoundarySubface) -> bool

"""


