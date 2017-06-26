class Arc(object, IEquatable[Arc], IEpsilonComparable[Arc]):
    """
    Arc(circle: Circle, angleRadians: float)
    Arc(circle: Circle, angleIntervalRadians: Interval)
    Arc(plane: Plane, radius: float, angleRadians: float)
    Arc(center: Point3d, radius: float, angleRadians: float)
    Arc(plane: Plane, center: Point3d, radius: float, angleRadians: float)
    Arc(startPoint: Point3d, pointOnInterior: Point3d, endPoint: Point3d)
    Arc(pointA: Point3d, tangentA: Vector3d, pointB: Point3d)
    """
    def BoundingBox(self):
        """ BoundingBox(self: Arc) -> BoundingBox """
        pass

    def ClosestParameter(self, testPoint):
        """ ClosestParameter(self: Arc, testPoint: Point3d) -> float """
        pass

    def ClosestPoint(self, testPoint):
        """ ClosestPoint(self: Arc, testPoint: Point3d) -> Point3d """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Arc, other: Arc, epsilon: float) -> bool """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Arc, other: Arc) -> bool
        Equals(self: Arc, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Arc) -> int """
        pass

    def PointAt(self, t):
        """ PointAt(self: Arc, t: float) -> Point3d """
        pass

    def Reverse(self):
        """ Reverse(self: Arc) """
        pass

    def TangentAt(self, t):
        """ TangentAt(self: Arc, t: float) -> Vector3d """
        pass

    def ToNurbsCurve(self):
        """ ToNurbsCurve(self: Arc) -> NurbsCurve """
        pass

    def Transform(self, xform):
        """ Transform(self: Arc, xform: Transform) -> bool """
        pass

    def Trim(self, domain):
        """ Trim(self: Arc, domain: Interval) -> bool """
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
        __new__[Arc]() -> Arc
        
        __new__(cls: type, circle: Circle, angleRadians: float)
        __new__(cls: type, circle: Circle, angleIntervalRadians: Interval)
        __new__(cls: type, plane: Plane, radius: float, angleRadians: float)
        __new__(cls: type, center: Point3d, radius: float, angleRadians: float)
        __new__(cls: type, plane: Plane, center: Point3d, radius: float, angleRadians: float)
        __new__(cls: type, startPoint: Point3d, pointOnInterior: Point3d, endPoint: Point3d)
        __new__(cls: type, pointA: Point3d, tangentA: Vector3d, pointB: Point3d)
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

    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Angle(self: Arc) -> float

Set: Angle(self: Arc) = value
"""

    AngleDegrees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleDegrees(self: Arc) -> float

Set: AngleDegrees(self: Arc) = value
"""

    AngleDomain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleDomain(self: Arc) -> Interval

Set: AngleDomain(self: Arc) = value
"""

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Center(self: Arc) -> Point3d

Set: Center(self: Arc) = value
"""

    Circumference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Circumference(self: Arc) -> float

"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diameter(self: Arc) -> float

Set: Diameter(self: Arc) = value
"""

    EndAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndAngle(self: Arc) -> float

Set: EndAngle(self: Arc) = value
"""

    EndAngleDegrees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndAngleDegrees(self: Arc) -> float

Set: EndAngleDegrees(self: Arc) = value
"""

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: Arc) -> Point3d

"""

    IsCircle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCircle(self: Arc) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Arc) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Arc) -> float

"""

    MidPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MidPoint(self: Arc) -> Point3d

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: Arc) -> Plane

Set: Plane(self: Arc) = value
"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: Arc) -> float

Set: Radius(self: Arc) = value
"""

    StartAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartAngle(self: Arc) -> float

Set: StartAngle(self: Arc) = value
"""

    StartAngleDegrees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartAngleDegrees(self: Arc) -> float

Set: StartAngleDegrees(self: Arc) = value
"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: Arc) -> Point3d

"""


