# encoding: utf-8
# module Tekla.Structures.Geometry3d calls itself Geometry3d
# from Tekla.Structures, Version=2017.0.0.0, Culture=neutral, PublicKeyToken=2f04dbe497b71114
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AABB(object):
    """
    AABB()
    AABB(MinPoint: Point, MaxPoint: Point)
    AABB(AABB: AABB)
    """
    def Collide(self, Other):
        """ Collide(self: AABB, Other: AABB) -> bool """
        pass

    def GetCenterPoint(self):
        """ GetCenterPoint(self: AABB) -> Point """
        pass

    def IsInside(self, *__args):
        """
        IsInside(self: AABB, LineSegment: LineSegment) -> bool
        IsInside(self: AABB, Point: Point) -> bool
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, MinPoint: Point, MaxPoint: Point)
        __new__(cls: type, AABB: AABB)
        """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(Point: Point, AABB: AABB) -> AABB
        __radd__(AABB1: AABB, AABB2: AABB) -> AABB
        """
        pass

    MaxPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxPoint(self: AABB) -> Point

Set: MaxPoint(self: AABB) = value
"""

    MinPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinPoint(self: AABB) -> Point

Set: MinPoint(self: AABB) = value
"""



class CoordinateSystem(object):
    """
    CoordinateSystem()
    CoordinateSystem(Origin: Point, AxisX: Vector, AxisY: Vector)
    """
    @staticmethod # known case of __new__
    def __new__(self, Origin=None, AxisX=None, AxisY=None):
        """
        __new__(cls: type)
        __new__(cls: type, Origin: Point, AxisX: Vector, AxisY: Vector)
        """
        pass

    AxisX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisX(self: CoordinateSystem) -> Vector

Set: AxisX(self: CoordinateSystem) = value
"""

    AxisY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisY(self: CoordinateSystem) -> Vector

Set: AxisY(self: CoordinateSystem) = value
"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Origin(self: CoordinateSystem) -> Point

Set: Origin(self: CoordinateSystem) = value
"""



class Distance(object):
    # no doc
    @staticmethod
    def PointToLine(Point, Line):
        """ PointToLine(Point: Point, Line: Line) -> float """
        pass

    @staticmethod
    def PointToLineSegment(Point, LineSegment):
        """ PointToLineSegment(Point: Point, LineSegment: LineSegment) -> float """
        pass

    @staticmethod
    def PointToPlane(Point, Plane):
        """ PointToPlane(Point: Point, Plane: GeometricPlane) -> float """
        pass

    @staticmethod
    def PointToPoint(Point1, Point2):
        """ PointToPoint(Point1: Point, Point2: Point) -> float """
        pass

    __all__ = [
        '__reduce_ex__',
        'PointToLine',
        'PointToLineSegment',
        'PointToPlane',
        'PointToPoint',
    ]


class FacetedBrep(object):
    """
    FacetedBrep(vertices: Array[Vector], outerWires: Array[Array[int]], innerWires: IDictionary[int, Array[Array[int]]])
    FacetedBrep(vertices: Array[Vector], outerWires: Array[Array[int]], innerWires: IDictionary[int, Array[Array[int]]], edges: IList[IndirectPolymeshEdge])
    """
    def CheckForTwoManifold(self):
        """ CheckForTwoManifold(self: FacetedBrep) -> bool """
        pass

    def GetInnerFace(self, faceIndex):
        """ GetInnerFace(self: FacetedBrep, faceIndex: int) -> Array[int] """
        pass

    def GetInnerFaceCount(self, faceIndex):
        """ GetInnerFaceCount(self: FacetedBrep, faceIndex: int) -> int """
        pass

    def GetOuterFace(self, faceIndex):
        """ GetOuterFace(self: FacetedBrep, faceIndex: int) -> Array[int] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, vertices, outerWires, innerWires, edges=None):
        """
        __new__(cls: type, vertices: Array[Vector], outerWires: Array[Array[int]], innerWires: IDictionary[int, Array[Array[int]]])
        __new__(cls: type, vertices: Array[Vector], outerWires: Array[Array[int]], innerWires: IDictionary[int, Array[Array[int]]], edges: IList[IndirectPolymeshEdge])
        """
        pass

    Faces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Faces(self: FacetedBrep) -> ICollection[FacetedBrepFace]

"""

    GetEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GetEdges(self: FacetedBrep) -> IList[IndirectPolymeshEdge]

"""

    InnerWires = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerWires(self: FacetedBrep) -> IDictionary[int, Array[Array[int]]]

"""

    OuterWires = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OuterWires(self: FacetedBrep) -> Array[Array[int]]

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: FacetedBrep) -> IList[Vector]

"""



class FacetedBrepFace(object):
    # no doc
    HasHoles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasHoles(self: FacetedBrepFace) -> bool

"""

    Holes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Holes(self: FacetedBrepFace) -> IList[FacetedBrepFaceHole]

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: FacetedBrepFace) -> bool

"""

    VerticeIndexes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticeIndexes(self: FacetedBrepFace) -> IList[int]

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: FacetedBrepFace) -> IList[Vector]

"""



class FacetedBrepFaceHole(object):
    # no doc
    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: FacetedBrepFaceHole) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: FacetedBrepFaceHole) -> bool

"""

    VerticeIndexes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticeIndexes(self: FacetedBrepFaceHole) -> IList[int]

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: FacetedBrepFaceHole) -> IList[Vector]

"""



class GeometricPlane(object):
    """
    GeometricPlane()
    GeometricPlane(Origin: Point, Normal: Vector)
    GeometricPlane(Origin: Point, Xaxis: Vector, Yaxis: Vector)
    GeometricPlane(CoordSys: CoordinateSystem)
    """
    def GetNormal(self):
        """ GetNormal(self: GeometricPlane) -> Vector """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, Origin: Point, Normal: Vector)
        __new__(cls: type, Origin: Point, Xaxis: Vector, Yaxis: Vector)
        __new__(cls: type, CoordSys: CoordinateSystem)
        """
        pass

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Normal(self: GeometricPlane) -> Vector

Set: Normal(self: GeometricPlane) = value
"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Origin(self: GeometricPlane) -> Point

Set: Origin(self: GeometricPlane) = value
"""



class GeometryConstants(object):
    """ GeometryConstants() """
    ANGULAR_EPSILON = 0.0017453292519943296
    DISTANCE_EPSILON = 0.00010000000000000001
    SCALAR_EPSILON = 1e-13


class IBoundingVolume:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IndirectPolymeshEdge(object):
    """ IndirectPolymeshEdge() """
    EdgeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeType(self: IndirectPolymeshEdge) -> PolymeshEdgeTypeEnum

Set: EdgeType(self: IndirectPolymeshEdge) = value
"""

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: IndirectPolymeshEdge) -> int

Set: EndPoint(self: IndirectPolymeshEdge) = value
"""

    ShellIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShellIndex(self: IndirectPolymeshEdge) -> int

Set: ShellIndex(self: IndirectPolymeshEdge) = value
"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: IndirectPolymeshEdge) -> int

Set: StartPoint(self: IndirectPolymeshEdge) = value
"""



class Intersection(object):
    # no doc
    @staticmethod
    def LineSegmentToObb(lineSegment, obb):
        """ LineSegmentToObb(lineSegment: LineSegment, obb: OBB) -> LineSegment """
        pass

    @staticmethod
    def LineSegmentToPlane(lineSegment, plane):
        """ LineSegmentToPlane(lineSegment: LineSegment, plane: GeometricPlane) -> Point """
        pass

    @staticmethod
    def LineToLine(line1, line2):
        """ LineToLine(line1: Line, line2: Line) -> LineSegment """
        pass

    @staticmethod
    def LineToObb(line, obb):
        """ LineToObb(line: Line, obb: OBB) -> LineSegment """
        pass

    @staticmethod
    def LineToPlane(line, plane):
        """ LineToPlane(line: Line, plane: GeometricPlane) -> Point """
        pass

    @staticmethod
    def PlaneToPlane(plane1, plane2):
        """ PlaneToPlane(plane1: GeometricPlane, plane2: GeometricPlane) -> Line """
        pass

    __all__ = [
        '__reduce_ex__',
        'LineSegmentToObb',
        'LineSegmentToPlane',
        'LineToLine',
        'LineToObb',
        'LineToPlane',
        'PlaneToPlane',
    ]


class Line(object):
    """
    Line()
    Line(p1: Point, p2: Point)
    Line(Point: Point, Direction: Vector)
    Line(LineSegment: LineSegment)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, p1: Point, p2: Point)
        __new__(cls: type, Point: Point, Direction: Vector)
        __new__(cls: type, LineSegment: LineSegment)
        """
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: Line) -> Vector

Set: Direction(self: Line) = value
"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Origin(self: Line) -> Point

Set: Origin(self: Line) = value
"""



class LineSegment(object):
    """
    LineSegment()
    LineSegment(Point1: Point, Point2: Point)
    """
    def Equals(self, o):
        """ Equals(self: LineSegment, o: object) -> bool """
        pass

    def GetDirectionVector(self):
        """ GetDirectionVector(self: LineSegment) -> Vector """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: LineSegment) -> int """
        pass

    def Length(self):
        """ Length(self: LineSegment) -> float """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, Point1=None, Point2=None):
        """
        __new__(cls: type)
        __new__(cls: type, Point1: Point, Point2: Point)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Point1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point1(self: LineSegment) -> Point

Set: Point1(self: LineSegment) = value
"""

    Point2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point2(self: LineSegment) -> Point

Set: Point2(self: LineSegment) = value
"""



class Matrix(object):
    """
    Matrix()
    Matrix(m: Matrix)
    """
    def GetTranspose(self):
        """ GetTranspose(self: Matrix) -> Matrix """
        pass

    def ToString(self):
        """ ToString(self: Matrix) -> str """
        pass

    def Transform(self, p):
        """ Transform(self: Matrix, p: Point) -> Point """
        pass

    def Transpose(self):
        """ Transpose(self: Matrix) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, m=None):
        """
        __new__(cls: type)
        __new__(cls: type, m: Matrix)
        """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(B: Matrix, A: Matrix) -> Matrix """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass


class MatrixFactory(object):
    # no doc
    @staticmethod
    def ByCoordinateSystems(CoordSys1, CoordSys2):
        """ ByCoordinateSystems(CoordSys1: CoordinateSystem, CoordSys2: CoordinateSystem) -> Matrix """
        pass

    @staticmethod
    def FromCoordinateSystem(CoordSys):
        """ FromCoordinateSystem(CoordSys: CoordinateSystem) -> Matrix """
        pass

    @staticmethod
    def Rotate(Angle, Axis):
        """ Rotate(Angle: float, Axis: Vector) -> Matrix """
        pass

    @staticmethod
    def ToCoordinateSystem(CoordSys):
        """ ToCoordinateSystem(CoordSys: CoordinateSystem) -> Matrix """
        pass

    __all__ = [
        '__reduce_ex__',
        'ByCoordinateSystems',
        'FromCoordinateSystem',
        'Rotate',
        'ToCoordinateSystem',
    ]


class OBB(object):
    """
    OBB()
    OBB(center: Point, axis0: Vector, axis1: Vector, axis2: Vector, extent0: float, extent1: float, extent2: float)
    OBB(center: Point, axis: Array[Vector], extent: Array[float])
    OBB(obb: OBB)
    """
    def ClosestPointTo(self, *__args):
        """
        ClosestPointTo(self: OBB, lineSegment: LineSegment) -> Point
        ClosestPointTo(self: OBB, line: Line) -> Point
        ClosestPointTo(self: OBB, point: Point) -> Point
        """
        pass

    def ComputeVertices(self):
        """ ComputeVertices(self: OBB) -> Array[Point] """
        pass

    def DistanceTo(self, *__args):
        """
        DistanceTo(self: OBB, lineSegment: LineSegment) -> float
        DistanceTo(self: OBB, line: Line) -> float
        DistanceTo(self: OBB, point: Point) -> float
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: OBB, other: OBB) -> bool
        Equals(self: OBB, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: OBB) -> int """
        pass

    def IntersectionPointsWith(self, *__args):
        """
        IntersectionPointsWith(self: OBB, lineSegment: LineSegment) -> Array[Point]
        IntersectionPointsWith(self: OBB, line: Line) -> Array[Point]
        """
        pass

    def IntersectionWith(self, *__args):
        """
        IntersectionWith(self: OBB, lineSegment: LineSegment) -> LineSegment
        IntersectionWith(self: OBB, line: Line) -> LineSegment
        """
        pass

    def Intersects(self, *__args):
        """
        Intersects(self: OBB, lineSegment: LineSegment) -> bool
        Intersects(self: OBB, geometricPlane: GeometricPlane) -> bool
        Intersects(self: OBB, obb: OBB) -> bool
        Intersects(self: OBB, line: Line) -> bool
        """
        pass

    def SetAxis(self, *__args):
        """ SetAxis(self: OBB, axis: Array[Vector])SetAxis(self: OBB, axis0: Vector, axis1: Vector, axis2: Vector) """
        pass

    def SetExtent(self, *__args):
        """ SetExtent(self: OBB, extent: Array[float])SetExtent(self: OBB, extent0: float, extent1: float, extent2: float) """
        pass

    def ShortestSegmentTo(self, *__args):
        """
        ShortestSegmentTo(self: OBB, point: Point) -> LineSegment
        ShortestSegmentTo(self: OBB, lineSegment: LineSegment) -> LineSegment
        ShortestSegmentTo(self: OBB, line: Line) -> LineSegment
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, center: Point, axis0: Vector, axis1: Vector, axis2: Vector, extent0: float, extent1: float, extent2: float)
        __new__(cls: type, center: Point, axis: Array[Vector], extent: Array[float])
        __new__(cls: type, obb: OBB)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Axis0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Axis0(self: OBB) -> Vector

"""

    Axis1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Axis1(self: OBB) -> Vector

"""

    Axis2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Axis2(self: OBB) -> Vector

"""

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Center(self: OBB) -> Point

Set: Center(self: OBB) = value
"""

    Extent0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Extent0(self: OBB) -> float

Set: Extent0(self: OBB) = value
"""

    Extent1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Extent1(self: OBB) -> float

Set: Extent1(self: OBB) = value
"""

    Extent2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Extent2(self: OBB) -> float

Set: Extent2(self: OBB) = value
"""



class Parallel(object):
    # no doc
    @staticmethod
    def LineSegmentToLineSegment(LineSegment1, LineSegment2, Tolerance=None):
        """
        LineSegmentToLineSegment(LineSegment1: LineSegment, LineSegment2: LineSegment, Tolerance: float) -> bool
        LineSegmentToLineSegment(LineSegment1: LineSegment, LineSegment2: LineSegment) -> bool
        """
        pass

    @staticmethod
    def LineSegmentToPlane(LineSegment, Plane, Tolerance=None):
        """
        LineSegmentToPlane(LineSegment: LineSegment, Plane: GeometricPlane, Tolerance: float) -> bool
        LineSegmentToPlane(LineSegment: LineSegment, Plane: GeometricPlane) -> bool
        """
        pass

    @staticmethod
    def LineToLine(Line1, Line2, Tolerance=None):
        """
        LineToLine(Line1: Line, Line2: Line, Tolerance: float) -> bool
        LineToLine(Line1: Line, Line2: Line) -> bool
        """
        pass

    @staticmethod
    def LineToPlane(Line, Plane, Tolerance=None):
        """
        LineToPlane(Line: Line, Plane: GeometricPlane, Tolerance: float) -> bool
        LineToPlane(Line: Line, Plane: GeometricPlane) -> bool
        """
        pass

    @staticmethod
    def PlaneToPlane(Plane1, Plane2, Tolerance=None):
        """
        PlaneToPlane(Plane1: GeometricPlane, Plane2: GeometricPlane, Tolerance: float) -> bool
        PlaneToPlane(Plane1: GeometricPlane, Plane2: GeometricPlane) -> bool
        """
        pass

    @staticmethod
    def VectorToPlane(Vector, Plane, Tolerance=None):
        """
        VectorToPlane(Vector: Vector, Plane: GeometricPlane, Tolerance: float) -> bool
        VectorToPlane(Vector: Vector, Plane: GeometricPlane) -> bool
        """
        pass

    @staticmethod
    def VectorToVector(Vector1, Vector2, Tolerance=None):
        """
        VectorToVector(Vector1: Vector, Vector2: Vector, Tolerance: float) -> bool
        VectorToVector(Vector1: Vector, Vector2: Vector) -> bool
        """
        pass

    __all__ = [
        '__reduce_ex__',
        'LineSegmentToLineSegment',
        'LineSegmentToPlane',
        'LineToLine',
        'LineToPlane',
        'PlaneToPlane',
        'VectorToPlane',
        'VectorToVector',
    ]


class Point(object):
    """
    Point()
    Point(X: float, Y: float, Z: float)
    Point(X: float, Y: float)
    Point(Point: Point)
    """
    @staticmethod
    def AreEqual(Point1, Point2):
        """ AreEqual(Point1: Point, Point2: Point) -> bool """
        pass

    def CompareTo(self, obj):
        """ CompareTo(self: Point, obj: object) -> int """
        pass

    def Equals(self, obj):
        """ Equals(self: Point, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Point) -> int """
        pass

    def ToString(self):
        """ ToString(self: Point) -> str """
        pass

    def Translate(self, X, Y, Z):
        """ Translate(self: Point, X: float, Y: float, Z: float) """
        pass

    def Zero(self):
        """ Zero(self: Point) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, X: float, Y: float, Z: float)
        __new__(cls: type, X: float, Y: float)
        __new__(cls: type, Point: Point)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(p1: Point, p2: Point) -> Point """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(p1: Point, p2: Point) -> Point """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    EPSILON_SQUARED = 0.00010000000000000001
    HASH_SEED = 69069
    X = None
    Y = None
    Z = None


class PolyLine(object):
    """ PolyLine(Points: IEnumerable) """
    def Equals(self, O):
        """ Equals(self: PolyLine, O: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: PolyLine) -> int """
        pass

    def Length(self):
        """ Length(self: PolyLine) -> float """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, Points):
        """ __new__(cls: type, Points: IEnumerable) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: PolyLine) -> ArrayList

Set: Points(self: PolyLine) = value
"""



class PolymeshEdgeTypeEnum(Enum):
    """ enum PolymeshEdgeTypeEnum, values: INVISIBLE_EDGE (2), VISIBLE_EDGE (1) """
    INVISIBLE_EDGE = None
    value__ = None
    VISIBLE_EDGE = None


class Projection(object):
    # no doc
    @staticmethod
    def LineSegmentToPlane(LineSegment, Plane):
        """ LineSegmentToPlane(LineSegment: LineSegment, Plane: GeometricPlane) -> LineSegment """
        pass

    @staticmethod
    def LineToPlane(Line, Plane):
        """ LineToPlane(Line: Line, Plane: GeometricPlane) -> Line """
        pass

    @staticmethod
    def PointToLine(Point, Line):
        """ PointToLine(Point: Point, Line: Line) -> Point """
        pass

    @staticmethod
    def PointToPlane(Point, Plane):
        """ PointToPlane(Point: Point, Plane: GeometricPlane) -> Point """
        pass

    __all__ = [
        '__reduce_ex__',
        'LineSegmentToPlane',
        'LineToPlane',
        'PointToLine',
        'PointToPlane',
    ]


class Vector(Point):
    """
    Vector()
    Vector(X: float, Y: float, Z: float)
    Vector(Point: Point)
    """
    def Cross(self, *__args):
        """
        Cross(Vector1: Vector, Vector2: Vector) -> Vector
        Cross(self: Vector, Vector: Vector) -> Vector
        """
        pass

    def Dot(self, *__args):
        """
        Dot(Vector1: Vector, Vector2: Vector) -> float
        Dot(self: Vector, Vector: Vector) -> float
        """
        pass

    def GetAngleBetween(self, Vector):
        """ GetAngleBetween(self: Vector, Vector: Vector) -> float """
        pass

    def GetLength(self):
        """ GetLength(self: Vector) -> float """
        pass

    def GetNormal(self):
        """ GetNormal(self: Vector) -> Vector """
        pass

    def Normalize(self, NewLength=None):
        """
        Normalize(self: Vector, NewLength: float) -> float
        Normalize(self: Vector) -> float
        """
        pass

    def ToString(self):
        """ ToString(self: Vector) -> str """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, X: float, Y: float, Z: float)
        __new__(cls: type, Point: Point)
        """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(Multiplier: float, Vector: Vector) -> Vector """
        pass


