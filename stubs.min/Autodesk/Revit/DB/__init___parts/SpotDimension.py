class SpotDimension(Dimension, IDisposable):
    """ An object that represents a spot dimension within the Revit project. """
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

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get a location point object. This is the location of the spot dimension.

Get: Location(self: SpotDimension) -> Location

"""

    SpotDimensionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The dimension style of this dimension.

Get: SpotDimensionType(self: SpotDimension) -> SpotDimensionType

Set: SpotDimensionType(self: SpotDimension) = value
"""


