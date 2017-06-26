class BoundingBoxUV(object, IDisposable):
    """
    A two-dimensional rectangle, parallel to the coordinate axes.
    
    BoundingBoxUV(min_u: float, min_v: float, max_u: float, max_v: float)
    BoundingBoxUV()
    """
    def Dispose(self):
        """ Dispose(self: BoundingBoxUV) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: BoundingBoxUV, disposing: bool) """
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
    def __new__(self, min_u=None, min_v=None, max_u=None, max_v=None):
        """
        __new__(cls: type, min_u: float, min_v: float, max_u: float, max_v: float)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum coordinates (upper-right corner of the box).

Get: Max(self: BoundingBoxUV) -> UV

Set: Max(self: BoundingBoxUV) = value
"""

    Min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Minimum coordinates (lower-left corner of the box).

Get: Min(self: BoundingBoxUV) -> UV

Set: Min(self: BoundingBoxUV) = value
"""


