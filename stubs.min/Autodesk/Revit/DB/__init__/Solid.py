class Solid(GeometryObject, IDisposable):
    """ A 3d solid. """
    def ComputeCentroid(self):
        """
        ComputeCentroid(self: Solid) -> XYZ
        
            Returns the Centroid of this solid.
            Returns: The XYZ point of the Centroid of this solid.
        """
        pass

    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def GetBoundingBox(self):
        """
        GetBoundingBox(self: Solid) -> BoundingBoxXYZ
        
            Retrieves a box that circumscribes the solid geometry.
        """
        pass

    def IntersectWithCurve(self, curve, options):
        """
        IntersectWithCurve(self: Solid, curve: Curve, options: SolidCurveIntersectionOptions) -> SolidCurveIntersection
        
            Calculates and returns the intersection between a curve and this solid.
        
            curve: The curve.
            options: The options.  If NULL, the default options will be used.
            Returns: The intersection results.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: GeometryObject) """
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

    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The edges that belong to the solid.

Get: Edges(self: Solid) -> EdgeArray

"""

    Faces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The faces that belong to the solid.

Get: Faces(self: Solid) -> FaceArray

"""

    SurfaceArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the total surface area of this solid.

Get: SurfaceArea(self: Solid) -> float

"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the signed volume of this solid.

Get: Volume(self: Solid) -> float

"""


