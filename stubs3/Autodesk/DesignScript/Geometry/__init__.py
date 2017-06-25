# encoding: utf-8
# module Autodesk.DesignScript.Geometry calls itself Geometry
# from ProtoGeometry, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Application(object):
    # no doc
    def PreloadAsmLibraries(self, baseDirectory):
        """ PreloadAsmLibraries(self: Application, baseDirectory: str) """
        pass

    def ShutDown(self):
        """ ShutDown(self: Application) """
        pass

    def StartUp(self):
        """ StartUp(self: Application) """
        pass

    IsExecuting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsExecuting(self: Application) -> bool

"""


    Instance = None


class DesignScriptEntity(object):
    # no doc
    def CheckArgsForAsmExtents(self, *args): #cannot find CLR method
        """ CheckArgsForAsmExtents(args: List[float]) """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: DesignScriptEntity) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: DesignScriptEntity) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: DesignScriptEntity) -> int """
        pass

    def Tessellate(self, package, parameters):
        """ Tessellate(self: DesignScriptEntity, package: IRenderPackage, parameters: TessellationParameters) """
        pass

    def ToString(self):
        """ ToString(self: DesignScriptEntity) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    mConstructor = None
    Tags = None


class Geometry(DesignScriptEntity):
    # no doc

class Curve(Geometry):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class Arc(Curve):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class BoundingBox(DesignScriptEntity):
    # no doc
    @staticmethod
    def ByCorners(min, max):
        """ ByCorners(min: Point, max: Point) -> BoundingBox """
        pass

    @staticmethod
    def ByCornersCoordinateSystem(min, max, cs):
        """ ByCornersCoordinateSystem(min: Point, max: Point, cs: CoordinateSystem) -> BoundingBox """
        pass

    @staticmethod
    def ByGeometry(geom):
        """
        ByGeometry(geom: IEnumerable[Geometry]) -> BoundingBox
        ByGeometry(geom: Geometry) -> BoundingBox
        """
        pass

    @staticmethod
    def ByGeometryCoordinateSystem(geom, cs):
        """
        ByGeometryCoordinateSystem(geom: IEnumerable[Geometry], cs: CoordinateSystem) -> BoundingBox
        ByGeometryCoordinateSystem(geom: Geometry, cs: CoordinateSystem) -> BoundingBox
        """
        pass

    def Contains(self, point):
        """ Contains(self: BoundingBox, point: Point) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: BoundingBox, other: DesignScriptEntity) -> bool """
        pass

    def Intersection(self, other):
        """ Intersection(self: BoundingBox, other: BoundingBox) -> BoundingBox """
        pass

    def Intersects(self, other):
        """ Intersects(self: BoundingBox, other: BoundingBox) -> bool """
        pass

    def IsEmpty(self):
        """ IsEmpty(self: BoundingBox) -> bool """
        pass

    def ToCuboid(self):
        """ ToCuboid(self: BoundingBox) -> Cuboid """
        pass

    def ToPolySurface(self):
        """ ToPolySurface(self: BoundingBox) -> PolySurface """
        pass

    def ToString(self):
        """ ToString(self: BoundingBox) -> str """
        pass

    ContextCoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContextCoordinateSystem(self: BoundingBox) -> CoordinateSystem

"""

    MaxPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxPoint(self: BoundingBox) -> Point

"""

    MinPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinPoint(self: BoundingBox) -> Point

"""


    mConstructor = None


class Circle(Curve):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class CoEdge(DesignScriptEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: CoEdge) -> str """
        pass

    Edge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edge(self: CoEdge) -> Edge

"""

    EndVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndVertex(self: CoEdge) -> Vertex

"""

    Loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loop(self: CoEdge) -> Loop

"""

    Next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Next(self: CoEdge) -> CoEdge

"""

    ParameterCurve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParameterCurve(self: CoEdge) -> Curve

"""

    Partner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Partner(self: CoEdge) -> CoEdge

"""

    Previous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Previous(self: CoEdge) -> CoEdge

"""

    Reversed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reversed(self: CoEdge) -> bool

"""

    StartVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartVertex(self: CoEdge) -> Vertex

"""


    mConstructor = None


class Topology(Geometry):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class Solid(Topology):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class Cone(Solid):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class CoordinateSystem(DesignScriptEntity):
    # no doc
    @staticmethod
    def ByCylindricalCoordinates(cs, radius, theta, height):
        """ ByCylindricalCoordinates(cs: CoordinateSystem, radius: float, theta: float, height: float) -> CoordinateSystem """
        pass

    @staticmethod
    def ByMatrix(matrix):
        """ ByMatrix(matrix: Array[float]) -> CoordinateSystem """
        pass

    @staticmethod
    def ByOrigin(*__args):
        """
        ByOrigin(origin: Point) -> CoordinateSystem
        ByOrigin(x: float, y: float, z: float) -> CoordinateSystem
        ByOrigin(x: float, y: float) -> CoordinateSystem
        """
        pass

    @staticmethod
    def ByOriginVectors(origin, xAxis, yAxis, zAxis=None):
        """
        ByOriginVectors(origin: Point, xAxis: Vector, yAxis: Vector, zAxis: Vector) -> CoordinateSystem
        ByOriginVectors(origin: Point, xAxis: Vector, yAxis: Vector) -> CoordinateSystem
        """
        pass

    @staticmethod
    def ByPlane(plane):
        """ ByPlane(plane: Plane) -> CoordinateSystem """
        pass

    @staticmethod
    def BySphericalCoordinates(cs, radius, theta, phi):
        """ BySphericalCoordinates(cs: CoordinateSystem, radius: float, theta: float, phi: float) -> CoordinateSystem """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    @staticmethod
    def Identity():
        """ Identity() -> CoordinateSystem """
        pass

    def Inverse(self):
        """ Inverse(self: CoordinateSystem) -> CoordinateSystem """
        pass

    def IsEqualTo(self, other):
        """ IsEqualTo(self: CoordinateSystem, other: CoordinateSystem) -> bool """
        pass

    def Mirror(self, mirrorPlane):
        """ Mirror(self: CoordinateSystem, mirrorPlane: Plane) -> CoordinateSystem """
        pass

    def PostMultiplyBy(self, other):
        """ PostMultiplyBy(self: CoordinateSystem, other: CoordinateSystem) -> CoordinateSystem """
        pass

    def PreMultiplyBy(self, other):
        """ PreMultiplyBy(self: CoordinateSystem, other: CoordinateSystem) -> CoordinateSystem """
        pass

    def Rotate(self, *__args):
        """
        Rotate(self: CoordinateSystem, plane: Plane, degrees: float) -> CoordinateSystem
        Rotate(self: CoordinateSystem, origin: Point, axis: Vector, degrees: float) -> CoordinateSystem
        """
        pass

    def Scale(self, *__args):
        """
        Scale(self: CoordinateSystem, plane: Plane, xamount: float, yamount: float, zamount: float) -> CoordinateSystem
        Scale(self: CoordinateSystem, basePoint: Point, from: Point, to: Point) -> CoordinateSystem
        Scale(self: CoordinateSystem, amount: float) -> CoordinateSystem
        Scale(self: CoordinateSystem, xamount: float, yamount: float, zamount: float) -> CoordinateSystem
        """
        pass

    def Scale1D(self, basePoint, from, to):
        """ Scale1D(self: CoordinateSystem, basePoint: Point, from: Point, to: Point) -> CoordinateSystem """
        pass

    def Scale2D(self, basePlane, from, to):
        """ Scale2D(self: CoordinateSystem, basePlane: Plane, from: Point, to: Point) -> CoordinateSystem """
        pass

    def ScaleFactor(self):
        """ ScaleFactor(self: CoordinateSystem) -> Vector """
        pass

    def ToString(self):
        """ ToString(self: CoordinateSystem) -> str """
        pass

    def Transform(self, *__args):
        """
        Transform(self: CoordinateSystem, fromCoordinateSystem: CoordinateSystem, contextCoordinateSystem: CoordinateSystem) -> CoordinateSystem
        Transform(self: CoordinateSystem, cs: CoordinateSystem) -> CoordinateSystem
        """
        pass

    def Translate(self, *__args):
        """
        Translate(self: CoordinateSystem, direction: Vector, distance: float) -> CoordinateSystem
        Translate(self: CoordinateSystem, direction: Vector) -> CoordinateSystem
        Translate(self: CoordinateSystem, xTranslation: float, yTranslation: float, zTranslation: float) -> CoordinateSystem
        """
        pass

    Determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Determinant(self: CoordinateSystem) -> float

"""

    IsScaledOrtho = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsScaledOrtho(self: CoordinateSystem) -> bool

"""

    IsSingular = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSingular(self: CoordinateSystem) -> bool

"""

    IsUniscaledOrtho = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUniscaledOrtho(self: CoordinateSystem) -> bool

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Origin(self: CoordinateSystem) -> Point

"""

    XAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XAxis(self: CoordinateSystem) -> Vector

"""

    XScaleFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XScaleFactor(self: CoordinateSystem) -> float

"""

    XYPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XYPlane(self: CoordinateSystem) -> Plane

"""

    YAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YAxis(self: CoordinateSystem) -> Vector

"""

    YScaleFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YScaleFactor(self: CoordinateSystem) -> float

"""

    YZPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YZPlane(self: CoordinateSystem) -> Plane

"""

    ZAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZAxis(self: CoordinateSystem) -> Vector

"""

    ZScaleFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZScaleFactor(self: CoordinateSystem) -> float

"""

    ZXPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZXPlane(self: CoordinateSystem) -> Plane

"""


    mConstructor = None


class Cuboid(Solid):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class Cylinder(Cone):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class Edge(DesignScriptEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Edge) -> str """
        pass

    AdjacentFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdjacentFaces(self: Edge) -> Array[Face]

"""

    CoEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoEdges(self: Edge) -> Array[CoEdge]

"""

    CurveGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveGeometry(self: Edge) -> Curve

"""

    EndVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndVertex(self: Edge) -> Vertex

"""

    StartVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartVertex(self: Edge) -> Vertex

"""


    mConstructor = None


class Ellipse(Curve):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class EllipseArc(Curve):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class Face(DesignScriptEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def SurfaceGeometry(self):
        """ SurfaceGeometry(self: Face) -> Surface """
        pass

    def ToString(self):
        """ ToString(self: Face) -> str """
        pass

    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edges(self: Face) -> Array[Edge]

"""

    Loops = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loops(self: Face) -> Array[Loop]

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: Face) -> Array[Vertex]

"""


    mConstructor = None


class Helix(Curve):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class HostFactory(object):
    # no doc

class IndexGroup(object):
    # no doc
    @staticmethod
    def ByIndices(a, b, c, d=None):
        """
        ByIndices(a: UInt32, b: UInt32, c: UInt32) -> IndexGroup
        ByIndices(a: UInt32, b: UInt32, c: UInt32, d: UInt32) -> IndexGroup
        """
        pass

    def Equals(self, other):
        """ Equals(self: IndexGroup, other: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: IndexGroup) -> int """
        pass

    def ToString(self):
        """ ToString(self: IndexGroup) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    A = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: A(self: IndexGroup) -> UInt32

"""

    B = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: B(self: IndexGroup) -> UInt32

"""

    C = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: C(self: IndexGroup) -> UInt32

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: IndexGroup) -> UInt32

"""

    D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: D(self: IndexGroup) -> UInt32

"""



class IProtoGeometryConfiguration:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    GeometryFactoryFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryFactoryFileName(self: IProtoGeometryConfiguration) -> str

Set: GeometryFactoryFileName(self: IProtoGeometryConfiguration) = value
"""

    PersistentManagerFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PersistentManagerFileName(self: IProtoGeometryConfiguration) -> str

Set: PersistentManagerFileName(self: IProtoGeometryConfiguration) = value
"""



class Line(Curve):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class Loop(DesignScriptEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Loop) -> str """
        pass

    CoEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoEdges(self: Loop) -> Array[CoEdge]

"""

    Face = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Face(self: Loop) -> Face

"""

    IsExternal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsExternal(self: Loop) -> bool

"""


    mConstructor = None


class Mesh(DesignScriptEntity):
    # no doc

class NurbsCurve(Curve):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class Surface(Topology):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class NurbsSurface(Surface):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class Plane(Geometry):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class Point(Geometry):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class PolyCurve(Curve):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class Polygon(PolyCurve):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class PolySurface(Surface):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class ProtoGeometryConfiguration(object):
    # no doc
    GeometryFactoryFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryFactoryFileName(self: ProtoGeometryConfiguration) -> str

Set: GeometryFactoryFileName(self: ProtoGeometryConfiguration) = value
"""

    PersistentManagerFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PersistentManagerFileName(self: ProtoGeometryConfiguration) -> str

Set: PersistentManagerFileName(self: ProtoGeometryConfiguration) = value
"""



class Rectangle(Polygon):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class Sphere(Solid):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class UV(object):
    # no doc
    @staticmethod
    def ByCoordinates(u, v):
        """ ByCoordinates(u: float, v: float) -> UV """
        pass

    def Equals(self, other):
        """ Equals(self: UV, other: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: UV) -> int """
        pass

    def ToString(self):
        """ ToString(self: UV) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    U = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: U(self: UV) -> float

"""

    V = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: V(self: UV) -> float

"""



class Vector(DesignScriptEntity):
    # no doc

class Vertex(DesignScriptEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Vertex) -> str """
        pass

    AdjacentEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdjacentEdges(self: Vertex) -> Array[Edge]

"""

    AdjacentFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdjacentFaces(self: Vertex) -> Array[Face]

"""

    PointGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointGeometry(self: Vertex) -> Point

"""


    mConstructor = None


# variables with complex values

