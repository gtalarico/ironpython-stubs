class SpatialElement(Element, IDisposable):
    """
    Represents an enclosed area or volume in the Revit model.  This is the parent class for 
    rooms, spaces and areas.
    """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GetBoundarySegments(self, options):
        """
        GetBoundarySegments(self: SpatialElement, options: SpatialElementBoundaryOptions) -> IList[IList[BoundarySegment]]
        
            Returns the boundary segments.
        
            options: The SpatialElementBoundaryOptions.
        """
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

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The area.

Get: Area(self: SpatialElement) -> float

"""

    Level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the level of the room.

Get: Level(self: SpatialElement) -> Level

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The location of the element.

Get: Location(self: SpatialElement) -> Location

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A human readable name for the Element.

Set: Name(self: SpatialElement) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number.

Get: Number(self: SpatialElement) -> str

Set: Number(self: SpatialElement) = value
"""

    Perimeter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The perimeter.

Get: Perimeter(self: SpatialElement) -> float

"""


