# encoding: utf-8
# module Grasshopper.Kernel.Geometry.Voronoi calls itself Voronoi
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Cell2(object):
    """
    Cell2()
    Cell2(pt: Node2, Radius: float)
    Cell2(pt: Node2, Contour: IEnumerable[Node2])
    """
    def Edges(self):
        """ Edges(self: Cell2) -> List[Line2] """
        pass

    def Radius(self):
        """ Radius(self: Cell2) -> float """
        pass

    def Slice(self, *__args):
        """
        Slice(self: Cell2, line: Line2) -> bool
        Slice(self: Cell2, other: Node2) -> bool
        """
        pass

    @staticmethod
    def SliceConvexNGon(V, line, side, changed):
        """ SliceConvexNGon(V: List[Node2], line: Line2, side: Side2, changed: bool) -> (List[Node2], bool) """
        pass

    def ToGraphicsPath(self):
        """ ToGraphicsPath(self: Cell2) -> GraphicsPath """
        pass

    def ToPolyCurve(self, radius):
        """ ToPolyCurve(self: Cell2, radius: float) -> PolyCurve """
        pass

    def ToPolyline(self):
        """ ToPolyline(self: Cell2) -> Polyline """
        pass

    @staticmethod # known case of __new__
    def __new__(self, pt=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, pt: Node2, Radius: float)
        __new__(cls: type, pt: Node2, Contour: IEnumerable[Node2])
        """
        pass

    C = None
    M = None


class Cell3(object):
    """
    Cell3(center: Point3d, box: Box)
    Cell3(other: Cell3)
    """
    @staticmethod
    def MidPlane(A, B):
        """ MidPlane(A: Point3d, B: Point3d) -> Plane """
        pass

    def Slice(self, *__args):
        """ Slice(self: Cell3, pt: Array[Point3d])Slice(self: Cell3, section: Plane)Slice(self: Cell3, pt: Point3d)Slice(self: Cell3, pt: IEnumerable[Point3d]) """
        pass

    def ToBrep(self):
        """ ToBrep(self: Cell3) -> Brep """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, center: Point3d, box: Box)
        __new__(cls: type, other: Cell3)
        """
        pass

    AngleTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleTolerance(self: Cell3) -> float

"""

    BoundaryCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundaryCount(self: Cell3) -> int

"""

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Center(self: Cell3) -> Point3d

"""

    Facets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Facets(self: Cell3) -> List[Cell3Facet]

"""

    Tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tolerance(self: Cell3) -> float

Set: Tolerance(self: Cell3) = value
"""



class Cell3Facet(Polyline, IList[Point3d], ICollection[Point3d], IEnumerable[Point3d], IEnumerable, IList, ICollection):
    """
    Cell3Facet()
    Cell3Facet(pts: IEnumerable[Point3d])
    Cell3Facet(other: Cell3Facet)
    """
    def CleanUp(self, tolerance, minDistance):
        """ CleanUp(self: Cell3Facet, tolerance: float, minDistance: float) -> float """
        pass

    def DestroyCaches(self):
        """ DestroyCaches(self: Cell3Facet) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, pts: IEnumerable[Point3d])
        __new__(cls: type, other: Cell3Facet)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    MidPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MidPoint(self: Cell3Facet) -> Point3d

"""

    Original = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Original(self: Cell3Facet) -> bool

Set: Original(self: Cell3Facet) = value
"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: Cell3Facet) -> float

"""



class Solver(object):
    # no doc
    @staticmethod
    def Solve_BruteForce(nodes, outline):
        """ Solve_BruteForce(nodes: Node2List, outline: IEnumerable[Node2]) -> List[Cell2] """
        pass

    @staticmethod
    def Solve_Connectivity(nodes, diagram, outline):
        """ Solve_Connectivity(nodes: Node2List, diagram: Connectivity, outline: IEnumerable[Node2]) -> List[Cell2] """
        pass


