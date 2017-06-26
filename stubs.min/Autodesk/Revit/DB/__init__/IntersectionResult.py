class IntersectionResult(APIObject, IDisposable):
    """
    This class captures results of intersecting geometric entities. "Intersecting" is meant 
    in generalized sense, so the same class will be used for projection, containment, etc.
    Refer to the documentation of the method providing the result for the precise meaning of properties.
    
    IntersectionResult()
    """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
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

    Distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance from the original object to located point.

Get: Distance(self: IntersectionResult) -> float

"""

    EdgeObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Edge of the face close to the point of intersection.

Get: EdgeObject(self: IntersectionResult) -> Edge

"""

    EdgeParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Parameter of a point on the edge closest to the point of intersection.

Get: EdgeParameter(self: IntersectionResult) -> float

"""

    Parameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """1d parameter of the point of intersection.

Get: Parameter(self: IntersectionResult) -> float

"""

    UVPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """2d (or two 1d) parameters of the point of intersection.

Get: UVPoint(self: IntersectionResult) -> UV

"""

    XYZPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Point of intersection in local 3d coordinates.

Get: XYZPoint(self: IntersectionResult) -> XYZ

"""


