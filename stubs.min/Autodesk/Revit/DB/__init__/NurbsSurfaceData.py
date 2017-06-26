class NurbsSurfaceData(object, IDisposable):
    """
    A class used to represent the definition of a NURBS surface.
    
    NurbsSurfaceData(other: NurbsSurfaceData)
    """
    @staticmethod
    def Create(degreeU, degreeV, knotsU, knotsV, controlPoints, weights, bReverseOrientation):
        """ Create(degreeU: int, degreeV: int, knotsU: IList[float], knotsV: IList[float], controlPoints: IList[XYZ], weights: IList[float], bReverseOrientation: bool) -> NurbsSurfaceData """
        pass

    def Dispose(self):
        """ Dispose(self: NurbsSurfaceData) """
        pass

    def GetControlPoints(self):
        """
        GetControlPoints(self: NurbsSurfaceData) -> IList[XYZ]
        
            Get the list of control points.
        """
        pass

    def GetKnotsU(self):
        """
        GetKnotsU(self: NurbsSurfaceData) -> IList[float]
        
            Get the list of knots in the u-direction.
        """
        pass

    def GetKnotsV(self):
        """
        GetKnotsV(self: NurbsSurfaceData) -> IList[float]
        
            Get the list of knots in the v-direction.
        """
        pass

    def GetWeights(self):
        """
        GetWeights(self: NurbsSurfaceData) -> IList[float]
        
            Get the list of weights.
        """
        pass

    def IsValid(self):
        """
        IsValid(self: NurbsSurfaceData) -> bool
        
            Check if the object contains a valid NurbsSurfaceData.
            Returns: True if it is a valid NurbsSurfaceData, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: NurbsSurfaceData, disposing: bool) """
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
    def __new__(self, other):
        """ __new__(cls: type, other: NurbsSurfaceData) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    DegreeU = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The degree of the spline in the u-direction.

Get: DegreeU(self: NurbsSurfaceData) -> int

"""

    DegreeV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The degree of the spline in the v-direction.

Get: DegreeV(self: NurbsSurfaceData) -> int

"""

    IsRational = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tells if the spline is rational or not.
   If it is true (rational), then the NURBS is a piecewise rational polynomial function.
   If it is false (non-rational), then the NURBS is a piecewise polynomial function.

Get: IsRational(self: NurbsSurfaceData) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: NurbsSurfaceData) -> bool

"""

    ReverseOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true, the surface's orientation is opposite to the canonical parametric orientation, otherwise it is the same.
   The canonical parametric orientation is a counter-clockwise sense of rotation in the uv-parameter plane.
   Extrinsically, the oriented normal vector for the canonical parametric orientation points in the direction of
   the cross product dS/du x dS/dv, which S(u, v) is the parameterized surface.

Get: ReverseOrientation(self: NurbsSurfaceData) -> bool

"""


