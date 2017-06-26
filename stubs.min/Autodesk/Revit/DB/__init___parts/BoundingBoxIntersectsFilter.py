class BoundingBoxIntersectsFilter(ElementQuickFilter, IDisposable):
    """
    A filter used to match elements with a bounding box that intersects the given Outline.
    
    BoundingBoxIntersectsFilter(outline: Outline, tolerance: float, inverted: bool)
    BoundingBoxIntersectsFilter(outline: Outline, tolerance: float)
    BoundingBoxIntersectsFilter(outline: Outline, inverted: bool)
    BoundingBoxIntersectsFilter(outline: Outline)
    """
    def Dispose(self):
        """ Dispose(self: ElementFilter, A_0: bool) """
        pass

    def GetBoundingBox(self):
        """
        GetBoundingBox(self: BoundingBoxIntersectsFilter) -> Outline
        
            Gets the outline being used for this filter.
            Returns: The outline being used for this filter.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ElementFilter, disposing: bool) """
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
    def __new__(self, outline, *__args):
        """
        __new__(cls: type, outline: Outline, tolerance: float, inverted: bool)
        __new__(cls: type, outline: Outline, tolerance: float)
        __new__(cls: type, outline: Outline, inverted: bool)
        __new__(cls: type, outline: Outline)
        """
        pass

    Tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Allows control over the match criteria by using a tolerance in the geometry comparison. It is suggested to use this in cases where trivial differences should be considered when matching elements.

Get: Tolerance(self: BoundingBoxIntersectsFilter) -> float

Set: Tolerance(self: BoundingBoxIntersectsFilter) = value
"""


