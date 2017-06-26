class ReferencePlane(DatumPlane, IDisposable):
    """ Represents a reference plane of Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def Flip(self):
        """
        Flip(self: ReferencePlane)
            Flips the orientation of the reference plane.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetPlane(self):
        """
        GetPlane(self: ReferencePlane) -> Plane
        
            Returns the geometry plane to which the reference plane is assigned.
            Returns: The geometry plane to which the reference plane is assigned.
        """
        pass

    def GetReference(self):
        """
        GetReference(self: ReferencePlane) -> Reference
        
            Returns the geometry reference of the reference plane.
            Returns: The geometry reference of the reference plane.
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

    BubbleEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The bubble end of the reference plane.

Get: BubbleEnd(self: ReferencePlane) -> XYZ

Set: BubbleEnd(self: ReferencePlane) = value
"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The direction of the reference plane.

Get: Direction(self: ReferencePlane) -> XYZ

Set: Direction(self: ReferencePlane) = value
"""

    FreeEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The free end of the reference plane.

Get: FreeEnd(self: ReferencePlane) -> XYZ

Set: FreeEnd(self: ReferencePlane) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name property of the reference plane.

Get: Name(self: ReferencePlane) -> str

Set: Name(self: ReferencePlane) = value
"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The normal vector of the reference plane.

Get: Normal(self: ReferencePlane) -> XYZ

"""


