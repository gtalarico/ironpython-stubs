class Sphere(object, IEpsilonComparable[Sphere]):
    """
    Sphere(center: Point3d, radius: float)
    Sphere(equatorialPlane: Plane, radius: float)
    """
    def ClosestParameter(self, testPoint, longitudeRadians, latitudeRadians):
        """ ClosestParameter(self: Sphere, testPoint: Point3d) -> (bool, float, float) """
        pass

    def ClosestPoint(self, testPoint):
        """ ClosestPoint(self: Sphere, testPoint: Point3d) -> Point3d """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Sphere, other: Sphere, epsilon: float) -> bool """
        pass

    def LatitudeDegrees(self, degrees):
        """ LatitudeDegrees(self: Sphere, degrees: float) -> Circle """
        pass

    def LatitudeRadians(self, radians):
        """ LatitudeRadians(self: Sphere, radians: float) -> Circle """
        pass

    def LongitudeDegrees(self, degrees):
        """ LongitudeDegrees(self: Sphere, degrees: float) -> Circle """
        pass

    def LongitudeRadians(self, radians):
        """ LongitudeRadians(self: Sphere, radians: float) -> Circle """
        pass

    def NormalAt(self, longitudeRadians, latitudeRadians):
        """ NormalAt(self: Sphere, longitudeRadians: float, latitudeRadians: float) -> Vector3d """
        pass

    def PointAt(self, longitudeRadians, latitudeRadians):
        """ PointAt(self: Sphere, longitudeRadians: float, latitudeRadians: float) -> Point3d """
        pass

    def Rotate(self, *__args):
        """
        Rotate(self: Sphere, sinAngle: float, cosAngle: float, axisOfRotation: Vector3d, centerOfRotation: Point3d) -> bool
        Rotate(self: Sphere, angleRadians: float, axisOfRotation: Vector3d, centerOfRotation: Point3d) -> bool
        Rotate(self: Sphere, sinAngle: float, cosAngle: float, axisOfRotation: Vector3d) -> bool
        Rotate(self: Sphere, angleRadians: float, axisOfRotation: Vector3d) -> bool
        """
        pass

    def ToBrep(self):
        """ ToBrep(self: Sphere) -> Brep """
        pass

    def ToNurbsSurface(self):
        """ ToNurbsSurface(self: Sphere) -> NurbsSurface """
        pass

    def ToRevSurface(self):
        """ ToRevSurface(self: Sphere) -> RevSurface """
        pass

    def Transform(self, xform):
        """ Transform(self: Sphere, xform: Transform) -> bool """
        pass

    def Translate(self, delta):
        """ Translate(self: Sphere, delta: Vector3d) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Sphere]() -> Sphere
        
        __new__(cls: type, center: Point3d, radius: float)
        __new__(cls: type, equatorialPlane: Plane, radius: float)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: Sphere) -> BoundingBox

"""

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Center(self: Sphere) -> Point3d

Set: Center(self: Sphere) = value
"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diameter(self: Sphere) -> float

Set: Diameter(self: Sphere) = value
"""

    EquitorialPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EquitorialPlane(self: Sphere) -> Plane

Set: EquitorialPlane(self: Sphere) = value
"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Sphere) -> bool

"""

    NorthPole = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NorthPole(self: Sphere) -> Point3d

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: Sphere) -> float

Set: Radius(self: Sphere) = value
"""

    SouthPole = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SouthPole(self: Sphere) -> Point3d

"""


    Unset = None

