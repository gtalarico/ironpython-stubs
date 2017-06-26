class Ellipse(object, IEpsilonComparable[Ellipse]):
    """
    Ellipse(plane: Plane, radius1: float, radius2: float)
    Ellipse(center: Point3d, second: Point3d, third: Point3d)
    """
    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Ellipse, other: Ellipse, epsilon: float) -> bool """
        pass

    def ToNurbsCurve(self):
        """ ToNurbsCurve(self: Ellipse) -> NurbsCurve """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Ellipse]() -> Ellipse
        
        __new__(cls: type, plane: Plane, radius1: float, radius2: float)
        __new__(cls: type, center: Point3d, second: Point3d, third: Point3d)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: Ellipse) -> Plane

Set: Plane(self: Ellipse) = value
"""

    Radius1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius1(self: Ellipse) -> float

Set: Radius1(self: Ellipse) = value
"""

    Radius2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius2(self: Ellipse) -> float

Set: Radius2(self: Ellipse) = value
"""


