class Line(object, IEquatable[Line], IEpsilonComparable[Line]):
    """
    Line(from: Point3d, to: Point3d)
    Line(start: Point3d, span: Vector3d)
    Line(start: Point3d, direction: Vector3d, length: float)
    Line(x0: float, y0: float, z0: float, x1: float, y1: float, z1: float)
    """
    def ClosestParameter(self, testPoint):
        """ ClosestParameter(self: Line, testPoint: Point3d) -> float """
        pass

    def ClosestPoint(self, testPoint, limitToFiniteSegment):
        """ ClosestPoint(self: Line, testPoint: Point3d, limitToFiniteSegment: bool) -> Point3d """
        pass

    def DistanceTo(self, testPoint, limitToFiniteSegment):
        """ DistanceTo(self: Line, testPoint: Point3d, limitToFiniteSegment: bool) -> float """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Line, other: Line, epsilon: float) -> bool """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Line, other: Line) -> bool
        Equals(self: Line, obj: object) -> bool
        """
        pass

    def Extend(self, startLength, endLength):
        """ Extend(self: Line, startLength: float, endLength: float) -> bool """
        pass

    def ExtendThroughBox(self, box, additionalLength=None):
        """
        ExtendThroughBox(self: Line, box: Box) -> bool
        ExtendThroughBox(self: Line, box: Box, additionalLength: float) -> bool
        ExtendThroughBox(self: Line, box: BoundingBox) -> bool
        ExtendThroughBox(self: Line, box: BoundingBox, additionalLength: float) -> bool
        """
        pass

    def Flip(self):
        """ Flip(self: Line) """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Line) -> int """
        pass

    def MaximumDistanceTo(self, *__args):
        """
        MaximumDistanceTo(self: Line, testLine: Line) -> float
        MaximumDistanceTo(self: Line, testPoint: Point3d) -> float
        """
        pass

    def MinimumDistanceTo(self, *__args):
        """
        MinimumDistanceTo(self: Line, testLine: Line) -> float
        MinimumDistanceTo(self: Line, testPoint: Point3d) -> float
        """
        pass

    def PointAt(self, t):
        """ PointAt(self: Line, t: float) -> Point3d """
        pass

    def ToNurbsCurve(self):
        """ ToNurbsCurve(self: Line) -> NurbsCurve """
        pass

    def ToString(self):
        """ ToString(self: Line) -> str """
        pass

    def Transform(self, xform):
        """ Transform(self: Line, xform: Transform) -> bool """
        pass

    def TryGetPlane(self, plane):
        """ TryGetPlane(self: Line) -> (bool, Plane) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Line]() -> Line
        
        __new__(cls: type, from: Point3d, to: Point3d)
        __new__(cls: type, start: Point3d, span: Vector3d)
        __new__(cls: type, start: Point3d, direction: Vector3d, length: float)
        __new__(cls: type, x0: float, y0: float, z0: float, x1: float, y1: float, z1: float)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: Line) -> BoundingBox

"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: Line) -> Vector3d

"""

    From = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: From(self: Line) -> Point3d

Set: From(self: Line) = value
"""

    FromX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromX(self: Line) -> float

Set: FromX(self: Line) = value
"""

    FromY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromY(self: Line) -> float

Set: FromY(self: Line) = value
"""

    FromZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromZ(self: Line) -> float

Set: FromZ(self: Line) = value
"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Line) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Line) -> float

Set: Length(self: Line) = value
"""

    To = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: To(self: Line) -> Point3d

Set: To(self: Line) = value
"""

    ToX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToX(self: Line) -> float

Set: ToX(self: Line) = value
"""

    ToY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToY(self: Line) -> float

Set: ToY(self: Line) = value
"""

    ToZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToZ(self: Line) -> float

Set: ToZ(self: Line) = value
"""

    UnitTangent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitTangent(self: Line) -> Vector3d

"""


    Unset = None

