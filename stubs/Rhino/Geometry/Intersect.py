# encoding: utf-8
# module Rhino.Geometry.Intersect calls itself Intersect
# from Rhino3dmIO, Version=5.1.30000.14, Culture=neutral, PublicKeyToken=null
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Intersection(object):
    # no doc
    @staticmethod
    def LineBox(line, box, tolerance, lineParameters):
        """
        LineBox(line: Line, box: Box, tolerance: float) -> (bool, Interval)
        LineBox(line: Line, box: BoundingBox, tolerance: float) -> (bool, Interval)
        """
        pass

    @staticmethod
    def LineCircle(line, circle, t1, point1, t2, point2):
        """ LineCircle(line: Line, circle: Circle) -> (LineCircleIntersection, float, Point3d, float, Point3d) """
        pass

    @staticmethod
    def LineCylinder(line, cylinder, intersectionPoint1, intersectionPoint2):
        """ LineCylinder(line: Line, cylinder: Cylinder) -> (LineCylinderIntersection, Point3d, Point3d) """
        pass

    @staticmethod
    def LineLine(lineA, lineB, a, b, tolerance=None, finiteSegments=None):
        """
        LineLine(lineA: Line, lineB: Line) -> (bool, float, float)
        LineLine(lineA: Line, lineB: Line, tolerance: float, finiteSegments: bool) -> (bool, float, float)
        """
        pass

    @staticmethod
    def LinePlane(line, plane, lineParameter):
        """ LinePlane(line: Line, plane: Plane) -> (bool, float) """
        pass

    @staticmethod
    def LineSphere(line, sphere, intersectionPoint1, intersectionPoint2):
        """ LineSphere(line: Line, sphere: Sphere) -> (LineSphereIntersection, Point3d, Point3d) """
        pass

    @staticmethod
    def PlaneCircle(plane, circle, firstCircleParameter, secondCircleParameter):
        """ PlaneCircle(plane: Plane, circle: Circle) -> (PlaneCircleIntersection, float, float) """
        pass

    @staticmethod
    def PlanePlane(planeA, planeB, intersectionLine):
        """ PlanePlane(planeA: Plane, planeB: Plane) -> (bool, Line) """
        pass

    @staticmethod
    def PlanePlanePlane(planeA, planeB, planeC, intersectionPoint):
        """ PlanePlanePlane(planeA: Plane, planeB: Plane, planeC: Plane) -> (bool, Point3d) """
        pass

    @staticmethod
    def PlaneSphere(plane, sphere, intersectionCircle):
        """ PlaneSphere(plane: Plane, sphere: Sphere) -> (PlaneSphereIntersection, Circle) """
        pass

    @staticmethod
    def SphereSphere(sphereA, sphereB, intersectionCircle):
        """ SphereSphere(sphereA: Sphere, sphereB: Sphere) -> (SphereSphereIntersection, Circle) """
        pass

    __all__ = [
        'LineBox',
        'LineCircle',
        'LineCylinder',
        'LineLine',
        'LinePlane',
        'LineSphere',
        'PlaneCircle',
        'PlanePlane',
        'PlanePlanePlane',
        'PlaneSphere',
        'SphereSphere',
    ]


class LineCircleIntersection(Enum, IComparable, IFormattable, IConvertible):
    """ enum LineCircleIntersection, values: Multiple (2), None (0), Single (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Multiple = None
    None = None
    Single = None
    value__ = None


class LineCylinderIntersection(Enum, IComparable, IFormattable, IConvertible):
    """ enum LineCylinderIntersection, values: Multiple (2), None (0), Overlap (3), Single (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Multiple = None
    None = None
    Overlap = None
    Single = None
    value__ = None


class LineSphereIntersection(Enum, IComparable, IFormattable, IConvertible):
    """ enum LineSphereIntersection, values: Multiple (2), None (0), Single (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Multiple = None
    None = None
    Single = None
    value__ = None


class PlaneCircleIntersection(Enum, IComparable, IFormattable, IConvertible):
    """ enum PlaneCircleIntersection, values: Coincident (4), None (0), Parallel (3), Secant (2), Tangent (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Coincident = None
    None = None
    Parallel = None
    Secant = None
    Tangent = None
    value__ = None


class PlaneSphereIntersection(Enum, IComparable, IFormattable, IConvertible):
    """ enum PlaneSphereIntersection, values: Circle (2), None (0), Point (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Circle = None
    None = None
    Point = None
    value__ = None


class SphereSphereIntersection(Enum, IComparable, IFormattable, IConvertible):
    """ enum SphereSphereIntersection, values: Circle (2), None (0), Overlap (3), Point (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Circle = None
    None = None
    Overlap = None
    Point = None
    value__ = None


