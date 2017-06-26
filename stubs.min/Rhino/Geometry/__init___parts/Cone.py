class Cone(object, IEpsilonComparable[Cone]):
    """ Cone(plane: Plane, height: float, radius: float) """
    def AngleInDegrees(self):
        """ AngleInDegrees(self: Cone) -> float """
        pass

    def AngleInRadians(self):
        """ AngleInRadians(self: Cone) -> float """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Cone, other: Cone, epsilon: float) -> bool """
        pass

    def ToBrep(self, capBottom):
        """ ToBrep(self: Cone, capBottom: bool) -> Brep """
        pass

    def ToNurbsSurface(self):
        """ ToNurbsSurface(self: Cone) -> NurbsSurface """
        pass

    def ToRevSurface(self):
        """ ToRevSurface(self: Cone) -> RevSurface """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, plane, height, radius):
        """
        __new__[Cone]() -> Cone
        
        __new__(cls: type, plane: Plane, height: float, radius: float)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ApexPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApexPoint(self: Cone) -> Point3d

"""

    Axis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Axis(self: Cone) -> Vector3d

"""

    BasePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BasePoint(self: Cone) -> Point3d

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: Cone) -> float

Set: Height(self: Cone) = value
"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Cone) -> bool

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: Cone) -> Plane

Set: Plane(self: Cone) = value
"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: Cone) -> float

Set: Radius(self: Cone) = value
"""


    Unset = None

