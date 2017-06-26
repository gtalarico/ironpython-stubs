class Plane(object, IEquatable[Plane], IEpsilonComparable[Plane]):
    """
    Plane(other: Plane)
    Plane(origin: Point3d, normal: Vector3d)
    Plane(origin: Point3d, xDirection: Vector3d, yDirection: Vector3d)
    Plane(origin: Point3d, xPoint: Point3d, yPoint: Point3d)
    Plane(a: float, b: float, c: float, d: float)
    """
    def ClosestParameter(self, testPoint, s, t):
        """ ClosestParameter(self: Plane, testPoint: Point3d) -> (bool, float, float) """
        pass

    def ClosestPoint(self, testPoint):
        """ ClosestPoint(self: Plane, testPoint: Point3d) -> Point3d """
        pass

    def DistanceTo(self, testPoint):
        """ DistanceTo(self: Plane, testPoint: Point3d) -> float """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Plane, other: Plane, epsilon: float) -> bool """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Plane, plane: Plane) -> bool
        Equals(self: Plane, obj: object) -> bool
        """
        pass

    def ExtendThroughBox(self, box, s, t):
        """
        ExtendThroughBox(self: Plane, box: Box) -> (bool, Interval, Interval)
        ExtendThroughBox(self: Plane, box: BoundingBox) -> (bool, Interval, Interval)
        """
        pass

    def Flip(self):
        """ Flip(self: Plane) """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Plane) -> int """
        pass

    def GetPlaneEquation(self):
        """ GetPlaneEquation(self: Plane) -> Array[float] """
        pass

    def PointAt(self, u, v, w=None):
        """
        PointAt(self: Plane, u: float, v: float, w: float) -> Point3d
        PointAt(self: Plane, u: float, v: float) -> Point3d
        """
        pass

    def RemapToPlaneSpace(self, ptSample, ptPlane):
        """ RemapToPlaneSpace(self: Plane, ptSample: Point3d) -> (bool, Point3d) """
        pass

    def Rotate(self, *__args):
        """
        Rotate(self: Plane, angle: float, axis: Vector3d, centerOfRotation: Point3d) -> bool
        Rotate(self: Plane, sinAngle: float, cosAngle: float, axis: Vector3d, centerOfRotation: Point3d) -> bool
        Rotate(self: Plane, sinAngle: float, cosAngle: float, axis: Vector3d) -> bool
        Rotate(self: Plane, angle: float, axis: Vector3d) -> bool
        """
        pass

    def ToString(self):
        """ ToString(self: Plane) -> str """
        pass

    def Transform(self, xform):
        """ Transform(self: Plane, xform: Transform) -> bool """
        pass

    def Translate(self, delta):
        """ Translate(self: Plane, delta: Vector3d) -> bool """
        pass

    def ValueAt(self, p):
        """ ValueAt(self: Plane, p: Point3d) -> float """
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
        __new__[Plane]() -> Plane
        
        __new__(cls: type, other: Plane)
        __new__(cls: type, origin: Point3d, normal: Vector3d)
        __new__(cls: type, origin: Point3d, xDirection: Vector3d, yDirection: Vector3d)
        __new__(cls: type, origin: Point3d, xPoint: Point3d, yPoint: Point3d)
        __new__(cls: type, a: float, b: float, c: float, d: float)
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

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Plane) -> bool

"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Normal(self: Plane) -> Vector3d

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Origin(self: Plane) -> Point3d

Set: Origin(self: Plane) = value
"""

    OriginX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginX(self: Plane) -> float

Set: OriginX(self: Plane) = value
"""

    OriginY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginY(self: Plane) -> float

Set: OriginY(self: Plane) = value
"""

    OriginZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginZ(self: Plane) -> float

Set: OriginZ(self: Plane) = value
"""

    XAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XAxis(self: Plane) -> Vector3d

Set: XAxis(self: Plane) = value
"""

    YAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YAxis(self: Plane) -> Vector3d

Set: YAxis(self: Plane) = value
"""

    ZAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZAxis(self: Plane) -> Vector3d

Set: ZAxis(self: Plane) = value
"""


    Unset = None
    WorldXY = None
    WorldYZ = None
    WorldZX = None

