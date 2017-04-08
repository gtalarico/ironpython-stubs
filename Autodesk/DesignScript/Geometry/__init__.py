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
    def ClosestPointTo(self, other):
        """ ClosestPointTo(self: Geometry, other: Geometry) -> Point """
        pass

    @staticmethod
    def DeserializeFromSAB(buffer):
        """ DeserializeFromSAB(buffer: Array[Byte]) -> Array[Geometry] """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DistanceTo(self, other):
        """ DistanceTo(self: Geometry, other: Geometry) -> float """
        pass

    def DoesIntersect(self, other):
        """ DoesIntersect(self: Geometry, other: Geometry) -> bool """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def Explode(self):
        """ Explode(self: Geometry) -> Array[Geometry] """
        pass

    def ExportToSAT(self, *__args):
        """
        ExportToSAT(geometry: IEnumerable[Geometry], filePath: str) -> str
        ExportToSAT(geometry: IEnumerable[Geometry], filePath: str, unitsMM: float) -> str
        ExportToSAT(self: Geometry, filePath: str) -> str
        ExportToSAT(self: Geometry, filePath: str, unitsMM: float) -> str
        """
        pass

    @staticmethod
    def FromNativePointer(nativePointer):
        """ FromNativePointer(nativePointer: IntPtr) -> Array[Geometry] """
        pass

    @staticmethod
    def FromObject(ptr):
        """ FromObject(ptr: Int64) -> Geometry """
        pass

    @staticmethod
    def ImportFromSAT(*__args):
        """
        ImportFromSAT(filePath: str) -> Array[Geometry]
        ImportFromSAT(file: FileInfo) -> Array[Geometry]
        """
        pass

    def Intersect(self, other):
        """ Intersect(self: Geometry, other: Geometry) -> Array[Geometry] """
        pass

    def IntersectAll(self, others):
        """ IntersectAll(self: Geometry, others: IEnumerable[Geometry]) -> Array[Geometry] """
        pass

    def IsAlmostEqualTo(self, other):
        """ IsAlmostEqualTo(self: Geometry, other: Geometry) -> bool """
        pass

    def Mirror(self, mirrorPlane):
        """ Mirror(self: Geometry, mirrorPlane: Plane) -> Geometry """
        pass

    def Rotate(self, *__args):
        """
        Rotate(self: Geometry, basePlane: Plane, degrees: float) -> Geometry
        Rotate(self: Geometry, origin: Point, axis: Vector, degrees: float) -> Geometry
        """
        pass

    def Scale(self, *__args):
        """
        Scale(self: Geometry, plane: Plane, xamount: float, yamount: float, zamount: float) -> Geometry
        Scale(self: Geometry, basePoint: Point, from: Point, to: Point) -> Geometry
        Scale(self: Geometry, amount: float) -> Geometry
        Scale(self: Geometry, xamount: float, yamount: float, zamount: float) -> Geometry
        """
        pass

    def Scale1D(self, basePoint, from, to):
        """ Scale1D(self: Geometry, basePoint: Point, from: Point, to: Point) -> Geometry """
        pass

    def Scale2D(self, basePlane, from, to):
        """ Scale2D(self: Geometry, basePlane: Plane, from: Point, to: Point) -> Geometry """
        pass

    def SerializeAsSAB(self, geometry=None):
        """
        SerializeAsSAB(geometry: IEnumerable[Geometry]) -> Array[Byte]
        SerializeAsSAB(self: Geometry) -> Array[Byte]
        """
        pass

    def Split(self, other):
        """ Split(self: Geometry, other: Geometry) -> Array[Geometry] """
        pass

    @staticmethod
    def ToNativePointer(geometry):
        """ ToNativePointer(geometry: IEnumerable[Geometry]) -> Array[IntPtr] """
        pass

    def Transform(self, *__args):
        """
        Transform(self: Geometry, fromCoordinateSystem: CoordinateSystem, contextCoordinateSystem: CoordinateSystem) -> Geometry
        Transform(self: Geometry, cs: CoordinateSystem) -> Geometry
        """
        pass

    def Translate(self, *__args):
        """
        Translate(self: Geometry, direction: Vector, distance: float) -> Geometry
        Translate(self: Geometry, direction: Vector) -> Geometry
        Translate(self: Geometry, xTranslation: float, yTranslation: float, zTranslation: float) -> Geometry
        """
        pass

    def Trim(self, other, pick):
        """ Trim(self: Geometry, other: Geometry, pick: Point) -> Array[Geometry] """
        pass

    @staticmethod
    def UpdateDisplay():
        """ UpdateDisplay() """
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: Geometry) -> BoundingBox

"""

    ContextCoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContextCoordinateSystem(self: Geometry) -> CoordinateSystem

"""


    mConstructor = None


class Curve(Geometry):
    # no doc
    def ApproximateWithArcAndLineSegments(self):
        """ ApproximateWithArcAndLineSegments(self: Curve) -> Array[Curve] """
        pass

    @staticmethod
    def ByBlendBetweenCurves(curve1, curve2, endOrStart1, endOrStart2, isG2Continuous):
        """ ByBlendBetweenCurves(curve1: Curve, curve2: Curve, endOrStart1: bool, endOrStart2: bool, isG2Continuous: bool) -> Curve """
        pass

    @staticmethod
    def ByIsoCurveOnSurface(baseSurface, direction, parameter):
        """ ByIsoCurveOnSurface(baseSurface: Surface, direction: int, parameter: float) -> Curve """
        pass

    @staticmethod
    def ByParameterLineOnSurface(baseSurface, startParams, endParams):
        """ ByParameterLineOnSurface(baseSurface: Surface, startParams: UV, endParams: UV) -> Curve """
        pass

    def CoordinateSystemAtDistance(self, segmentLength):
        """ CoordinateSystemAtDistance(self: Curve, segmentLength: float) -> CoordinateSystem """
        pass

    def CoordinateSystemAtParameter(self, param):
        """ CoordinateSystemAtParameter(self: Curve, param: float) -> CoordinateSystem """
        pass

    def CoordinateSystemAtSegmentLength(self, segmentLength):
        """ CoordinateSystemAtSegmentLength(self: Curve, segmentLength: float) -> CoordinateSystem """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DistanceAtParameter(self, param):
        """ DistanceAtParameter(self: Curve, param: float) -> float """
        pass

    def DivideByDistance(self, divisions):
        """ DivideByDistance(self: Curve, divisions: int) -> Array[Curve] """
        pass

    def DivideByDistanceFromParameter(self, distance, parameter):
        """ DivideByDistanceFromParameter(self: Curve, distance: float, parameter: float) -> Array[Curve] """
        pass

    def DivideByLengthFromParameter(self, length, parameter):
        """ DivideByLengthFromParameter(self: Curve, length: float, parameter: float) -> Array[Curve] """
        pass

    def DivideEqually(self, divisions):
        """ DivideEqually(self: Curve, divisions: int) -> Array[Curve] """
        pass

    def EndParameter(self):
        """ EndParameter(self: Curve) -> float """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def Extend(self, distance, pickSide):
        """ Extend(self: Curve, distance: float, pickSide: Point) -> Curve """
        pass

    def ExtendEnd(self, distance):
        """ ExtendEnd(self: Curve, distance: float) -> Curve """
        pass

    def ExtendStart(self, distance):
        """ ExtendStart(self: Curve, distance: float) -> Curve """
        pass

    def Extrude(self, *__args):
        """
        Extrude(self: Curve, direction: Vector, distance: float) -> Surface
        Extrude(self: Curve, direction: Vector) -> Surface
        Extrude(self: Curve, distance: float) -> Surface
        """
        pass

    def ExtrudeAsSolid(self, *__args):
        """
        ExtrudeAsSolid(self: Curve, direction: Vector, distance: float) -> Solid
        ExtrudeAsSolid(self: Curve, direction: Vector) -> Solid
        ExtrudeAsSolid(self: Curve, distance: float) -> Solid
        """
        pass

    def HorizontalFrameAtParameter(self, param):
        """ HorizontalFrameAtParameter(self: Curve, param: float) -> CoordinateSystem """
        pass

    def Join(self, *__args):
        """
        Join(self: Curve, curves: IEnumerable[Curve]) -> PolyCurve
        Join(self: Curve, curve: Curve) -> PolyCurve
        """
        pass

    def LengthBetweenParameters(self, startParam, endParam):
        """ LengthBetweenParameters(self: Curve, startParam: float, endParam: float) -> float """
        pass

    def NormalAtParameter(self, param):
        """ NormalAtParameter(self: Curve, param: float) -> Vector """
        pass

    def Offset(self, distance):
        """ Offset(self: Curve, distance: float) -> Curve """
        pass

    def ParameterAtChordLength(self, chordLength, parameter, forward):
        """ ParameterAtChordLength(self: Curve, chordLength: float, parameter: float, forward: bool) -> float """
        pass

    def ParameterAtDistance(self, segmentLength):
        """ ParameterAtDistance(self: Curve, segmentLength: float) -> float """
        pass

    def ParameterAtPoint(self, point):
        """ ParameterAtPoint(self: Curve, point: Point) -> float """
        pass

    def ParameterAtSegmentLength(self, segmentLength):
        """ ParameterAtSegmentLength(self: Curve, segmentLength: float) -> float """
        pass

    def ParameterSplit(self, *__args):
        """
        ParameterSplit(self: Curve, parameters: Array[float]) -> Array[Curve]
        ParameterSplit(self: Curve, parameter: float) -> Array[Curve]
        """
        pass

    def ParameterTrim(self, startParameter, endParameter):
        """ ParameterTrim(self: Curve, startParameter: float, endParameter: float) -> Curve """
        pass

    def ParameterTrimEnd(self, endParameter):
        """ ParameterTrimEnd(self: Curve, endParameter: float) -> Curve """
        pass

    def ParameterTrimInterior(self, startParameter, endParameter):
        """ ParameterTrimInterior(self: Curve, startParameter: float, endParameter: float) -> Array[Curve] """
        pass

    def ParameterTrimSegments(self, parameters):
        """ ParameterTrimSegments(self: Curve, parameters: Array[float]) -> Array[Curve] """
        pass

    def ParameterTrimStart(self, startParameter):
        """ ParameterTrimStart(self: Curve, startParameter: float) -> Curve """
        pass

    def Patch(self):
        """ Patch(self: Curve) -> Surface """
        pass

    def PlaneAtDistance(self, segmentLength):
        """ PlaneAtDistance(self: Curve, segmentLength: float) -> Plane """
        pass

    def PlaneAtParameter(self, param):
        """ PlaneAtParameter(self: Curve, param: float) -> Plane """
        pass

    def PlaneAtSegmentLength(self, segmentLength):
        """ PlaneAtSegmentLength(self: Curve, segmentLength: float) -> Plane """
        pass

    def PointAtChordLength(self, chordLength, parameterLocation, forward):
        """ PointAtChordLength(self: Curve, chordLength: float, parameterLocation: float, forward: bool) -> Point """
        pass

    def PointAtDistance(self, segmentLength):
        """ PointAtDistance(self: Curve, segmentLength: float) -> Point """
        pass

    def PointAtParameter(self, param):
        """ PointAtParameter(self: Curve, param: float) -> Point """
        pass

    def PointAtSegmentLength(self, segmentLength):
        """ PointAtSegmentLength(self: Curve, segmentLength: float) -> Point """
        pass

    def PointsAtChordLengthFromPoint(self, point, chordLength):
        """ PointsAtChordLengthFromPoint(self: Curve, point: Point, chordLength: float) -> Array[Point] """
        pass

    def PointsAtEqualChordLength(self, divisions):
        """ PointsAtEqualChordLength(self: Curve, divisions: int) -> Array[Point] """
        pass

    def PointsAtEqualSegmentLength(self, divisions):
        """ PointsAtEqualSegmentLength(self: Curve, divisions: int) -> Array[Point] """
        pass

    def PointsAtSegmentLengthFromPoint(self, point, segmentLength):
        """ PointsAtSegmentLengthFromPoint(self: Curve, point: Point, segmentLength: float) -> Array[Point] """
        pass

    def Project(self, baseGeometry, projectionDirection):
        """ Project(self: Curve, baseGeometry: Geometry, projectionDirection: Vector) -> Array[Geometry] """
        pass

    def PullOntoPlane(self, plane):
        """ PullOntoPlane(self: Curve, plane: Plane) -> Curve """
        pass

    def PullOntoSurface(self, surface):
        """ PullOntoSurface(self: Curve, surface: Surface) -> Curve """
        pass

    def Reverse(self):
        """ Reverse(self: Curve) -> Curve """
        pass

    def SegmentLengthAtParameter(self, param):
        """ SegmentLengthAtParameter(self: Curve, param: float) -> float """
        pass

    def SegmentLengthBetweenParameters(self, startParam, endParam):
        """ SegmentLengthBetweenParameters(self: Curve, startParam: float, endParam: float) -> float """
        pass

    def Simplify(self, tolerance):
        """ Simplify(self: Curve, tolerance: float) -> Curve """
        pass

    def SplitByParameter(self, *__args):
        """
        SplitByParameter(self: Curve, parameters: Array[float]) -> Array[Curve]
        SplitByParameter(self: Curve, parameter: float) -> Array[Curve]
        """
        pass

    def SplitByPoints(self, points):
        """ SplitByPoints(self: Curve, points: IEnumerable[Point]) -> Array[Curve] """
        pass

    def StartParameter(self):
        """ StartParameter(self: Curve) -> float """
        pass

    def SweepAsSolid(self, path):
        """ SweepAsSolid(self: Curve, path: Curve) -> Solid """
        pass

    def SweepAsSurface(self, path):
        """ SweepAsSurface(self: Curve, path: Curve) -> Surface """
        pass

    def TangentAtParameter(self, param):
        """ TangentAtParameter(self: Curve, param: float) -> Vector """
        pass

    def ToNurbsCurve(self):
        """ ToNurbsCurve(self: Curve) -> NurbsCurve """
        pass

    def ToString(self):
        """ ToString(self: Curve) -> str """
        pass

    def TrimByEndParameter(self, endParameter):
        """ TrimByEndParameter(self: Curve, endParameter: float) -> Curve """
        pass

    def TrimByParameter(self, startParameter, endParameter):
        """ TrimByParameter(self: Curve, startParameter: float, endParameter: float) -> Curve """
        pass

    def TrimByStartParameter(self, startParameter):
        """ TrimByStartParameter(self: Curve, startParameter: float) -> Curve """
        pass

    def TrimInteriorByParameter(self, startParameter, endParameter):
        """ TrimInteriorByParameter(self: Curve, startParameter: float, endParameter: float) -> Array[Curve] """
        pass

    def TrimSegmentsByParameter(self, parameters, discardEvenSegments=None):
        """
        TrimSegmentsByParameter(self: Curve, parameters: Array[float], discardEvenSegments: bool) -> Array[Curve]
        TrimSegmentsByParameter(self: Curve, parameters: Array[float]) -> Array[Curve]
        """
        pass

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: Curve) -> Point

"""

    IsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsClosed(self: Curve) -> bool

"""

    IsPlanar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPlanar(self: Curve) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Curve) -> float

"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Normal(self: Curve) -> Vector

"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: Curve) -> Point

"""


    mConstructor = None


class Arc(Curve):
    # no doc
    @staticmethod
    def ByBestFitThroughPoints(points):
        """ ByBestFitThroughPoints(points: IEnumerable[Point]) -> Arc """
        pass

    @staticmethod
    def ByCenterPointRadiusAngle(center, radius, startAngle, endAngle, normal):
        """ ByCenterPointRadiusAngle(center: Point, radius: float, startAngle: float, endAngle: float, normal: Vector) -> Arc """
        pass

    @staticmethod
    def ByCenterPointStartPointEndPoint(centerPoint, startPoint, endPoint):
        """ ByCenterPointStartPointEndPoint(centerPoint: Point, startPoint: Point, endPoint: Point) -> Arc """
        pass

    @staticmethod
    def ByCenterPointStartPointSweepAngle(centerPoint, startPoint, sweepAngle, normal):
        """ ByCenterPointStartPointSweepAngle(centerPoint: Point, startPoint: Point, sweepAngle: float, normal: Vector) -> Arc """
        pass

    @staticmethod
    def ByFillet(curve1, curve2, radius):
        """ ByFillet(curve1: Curve, curve2: Curve, radius: float) -> Arc """
        pass

    @staticmethod
    def ByFilletTangentToCurve(curve1, curveTangentTo, curve2):
        """ ByFilletTangentToCurve(curve1: Curve, curveTangentTo: Curve, curve2: Curve) -> Arc """
        pass

    @staticmethod
    def ByStartEndAndTangencies(point1, vector1, point2, vector2):
        """ ByStartEndAndTangencies(point1: Point, vector1: Vector, point2: Point, vector2: Vector) -> Array[Arc] """
        pass

    @staticmethod
    def ByStartPointEndPointStartTangent(startPoint, endPoint, startTangent):
        """ ByStartPointEndPointStartTangent(startPoint: Point, endPoint: Point, startTangent: Vector) -> Arc """
        pass

    @staticmethod
    def ByThreePoints(firstPoint, secondPoint, thirdPoint):
        """ ByThreePoints(firstPoint: Point, secondPoint: Point, thirdPoint: Point) -> Arc """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Arc) -> str """
        pass

    CenterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterPoint(self: Arc) -> Point

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: Arc) -> float

"""

    StartAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartAngle(self: Arc) -> float

"""

    SweepAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SweepAngle(self: Arc) -> float

"""


    mConstructor = None


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
    @staticmethod
    def ByBestFitThroughPoints(points):
        """ ByBestFitThroughPoints(points: IEnumerable[Point]) -> Circle """
        pass

    @staticmethod
    def ByCenterPointRadius(centerPoint, radius):
        """ ByCenterPointRadius(centerPoint: Point, radius: float) -> Circle """
        pass

    @staticmethod
    def ByCenterPointRadiusNormal(centerPoint, radius, normal):
        """ ByCenterPointRadiusNormal(centerPoint: Point, radius: float, normal: Vector) -> Circle """
        pass

    @staticmethod
    def ByPlaneRadius(plane, radius):
        """ ByPlaneRadius(plane: Plane, radius: float) -> Circle """
        pass

    @staticmethod
    def ByThreePoints(p1, p2, p3):
        """ ByThreePoints(p1: Point, p2: Point, p3: Point) -> Circle """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Circle) -> str """
        pass

    CenterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterPoint(self: Circle) -> Point

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: Circle) -> float

"""


    mConstructor = None


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
    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Topology) -> str """
        pass

    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edges(self: Topology) -> Array[Edge]

"""

    Faces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Faces(self: Topology) -> Array[Face]

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: Topology) -> Array[Vertex]

"""


    mConstructor = None


class Solid(Topology):
    # no doc
    @staticmethod
    def ByJoinedSurfaces(facesOfSolid):
        """ ByJoinedSurfaces(facesOfSolid: IEnumerable[Surface]) -> Solid """
        pass

    @staticmethod
    def ByLoft(crossSections, *__args):
        """
        ByLoft(crossSections: IEnumerable[Curve], guideCurves: IEnumerable[Curve]) -> Solid
        ByLoft(crossSections: IEnumerable[Curve], guideCurve: Curve) -> Solid
        ByLoft(crossSections: IEnumerable[Curve]) -> Solid
        """
        pass

    @staticmethod
    def ByRevolve(profile, axisOrigin, axisDirection, startAngle, sweepAngle):
        """ ByRevolve(profile: Curve, axisOrigin: Point, axisDirection: Vector, startAngle: float, sweepAngle: float) -> Solid """
        pass

    @staticmethod
    def BySweep(profile, path):
        """ BySweep(profile: Curve, path: Curve) -> Solid """
        pass

    @staticmethod
    def BySweep2Rails(path, guideRail, profile):
        """ BySweep2Rails(path: Curve, guideRail: Curve, profile: Curve) -> Solid """
        pass

    @staticmethod
    def ByUnion(solids):
        """ ByUnion(solids: IEnumerable[Solid]) -> Solid """
        pass

    def Centroid(self):
        """ Centroid(self: Solid) -> Point """
        pass

    def Chamfer(self, edges, offset):
        """ Chamfer(self: Solid, edges: IEnumerable[Edge], offset: float) -> Solid """
        pass

    def Difference(self, other):
        """ Difference(self: Solid, other: Solid) -> Solid """
        pass

    def DifferenceAll(self, others):
        """ DifferenceAll(self: Solid, others: IEnumerable[Solid]) -> Solid """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def Fillet(self, edges, radius):
        """ Fillet(self: Solid, edges: IEnumerable[Edge], radius: float) -> Solid """
        pass

    def ProjectInputOnto(self, geometryToProject, projectDirection):
        """ ProjectInputOnto(self: Solid, geometryToProject: Geometry, projectDirection: Vector) -> Array[Geometry] """
        pass

    def ThinShell(self, internalFaceThickness, externalFaceThickness):
        """ ThinShell(self: Solid, internalFaceThickness: float, externalFaceThickness: float) -> Solid """
        pass

    def ToString(self):
        """ ToString(self: Solid) -> str """
        pass

    def Union(self, solid):
        """ Union(self: Solid, solid: Solid) -> Solid """
        pass

    def UnionAll(self, solids):
        """ UnionAll(self: Solid, solids: IEnumerable[Solid]) -> Solid """
        pass

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Area(self: Solid) -> float

"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Volume(self: Solid) -> float

"""


    mConstructor = None


class Cone(Solid):
    # no doc
    @staticmethod
    def ByCoordinateSystemHeightRadii(cs, height, startRadius, endRadius):
        """ ByCoordinateSystemHeightRadii(cs: CoordinateSystem, height: float, startRadius: float, endRadius: float) -> Cone """
        pass

    @staticmethod
    def ByCoordinateSystemHeightRadius(cs, height, startRadius):
        """ ByCoordinateSystemHeightRadius(cs: CoordinateSystem, height: float, startRadius: float) -> Cone """
        pass

    @staticmethod
    def ByPointsRadii(startPoint, endPoint, startRadius, endRadius):
        """ ByPointsRadii(startPoint: Point, endPoint: Point, startRadius: float, endRadius: float) -> Cone """
        pass

    @staticmethod
    def ByPointsRadius(startPoint, endPoint, startRadius):
        """ ByPointsRadius(startPoint: Point, endPoint: Point, startRadius: float) -> Cone """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Cone) -> str """
        pass

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: Cone) -> Point

"""

    EndRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndRadius(self: Cone) -> float

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: Cone) -> float

"""

    RadiusRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RadiusRatio(self: Cone) -> float

"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: Cone) -> Point

"""

    StartRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartRadius(self: Cone) -> float

"""


    mConstructor = None


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
    @staticmethod
    def ByCorners(lowPoint, highPoint):
        """ ByCorners(lowPoint: Point, highPoint: Point) -> Cuboid """
        pass

    @staticmethod
    def ByLengths(*__args):
        """
        ByLengths(cs: CoordinateSystem, width: float, length: float, height: float) -> Cuboid
        ByLengths(origin: Point, width: float, length: float, height: float) -> Cuboid
        ByLengths(width: float, length: float, height: float) -> Cuboid
        """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Cuboid) -> str """
        pass

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: Cuboid) -> float

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Cuboid) -> float

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: Cuboid) -> float

"""


    mConstructor = None


class Cylinder(Cone):
    # no doc
    @staticmethod
    def ByPointsRadius(startPoint, endPoint, radius):
        """ ByPointsRadius(startPoint: Point, endPoint: Point, radius: float) -> Cylinder """
        pass

    @staticmethod
    def ByRadiusHeight(cs, radius, height):
        """ ByRadiusHeight(cs: CoordinateSystem, radius: float, height: float) -> Cylinder """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Cylinder) -> str """
        pass

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: Cylinder) -> float

"""


    mConstructor = None


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
    @staticmethod
    def ByCoordinateSystemRadii(origin, xAxisRadius, yAxisRadius):
        """ ByCoordinateSystemRadii(origin: CoordinateSystem, xAxisRadius: float, yAxisRadius: float) -> Ellipse """
        pass

    @staticmethod
    def ByOriginRadii(origin, xAxisRadius, yAxisRadius):
        """ ByOriginRadii(origin: Point, xAxisRadius: float, yAxisRadius: float) -> Ellipse """
        pass

    @staticmethod
    def ByOriginVectors(origin, xAxisRadius, yAxisRadius):
        """ ByOriginVectors(origin: Point, xAxisRadius: Vector, yAxisRadius: Vector) -> Ellipse """
        pass

    @staticmethod
    def ByPlaneRadii(plane, xAxisRadius, yAxisRadius):
        """ ByPlaneRadii(plane: Plane, xAxisRadius: float, yAxisRadius: float) -> Ellipse """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Ellipse) -> str """
        pass

    CenterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterPoint(self: Ellipse) -> Point

"""

    MajorAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorAxis(self: Ellipse) -> Vector

"""

    MinorAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorAxis(self: Ellipse) -> Vector

"""


    mConstructor = None


class EllipseArc(Curve):
    # no doc
    @staticmethod
    def ByPlaneRadiiAngles(plane, xRadius, yRadius, startAngle, sweepAngle):
        """ ByPlaneRadiiAngles(plane: Plane, xRadius: float, yRadius: float, startAngle: float, sweepAngle: float) -> EllipseArc """
        pass

    @staticmethod
    def ByPlaneRadiiStartAngleSweepAngle(plane, xRadius, yRadius, startAngle, sweepAngle):
        """ ByPlaneRadiiStartAngleSweepAngle(plane: Plane, xRadius: float, yRadius: float, startAngle: float, sweepAngle: float) -> EllipseArc """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: EllipseArc) -> str """
        pass

    CenterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterPoint(self: EllipseArc) -> Point

"""

    MajorAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorAxis(self: EllipseArc) -> Vector

"""

    MinorAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorAxis(self: EllipseArc) -> Vector

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: EllipseArc) -> Plane

"""

    StartAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartAngle(self: EllipseArc) -> float

"""

    SweepAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SweepAngle(self: EllipseArc) -> float

"""


    mConstructor = None


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


class GeometryExtension(object):
    # no doc
    @staticmethod
    def AreCoincident(pts):
        """ AreCoincident(pts: Array[IPointEntity]) -> bool """
        pass

    @staticmethod
    def ConvertAll(array, converter):
        """ ConvertAll[(TInput, TOutput)](array: Array[TInput], converter: Converter[TInput, TOutput]) -> Array[TOutput] """
        pass

    @staticmethod
    def DegreesToRadians(deg):
        """ DegreesToRadians(deg: float) -> float """
        pass

    @staticmethod
    def Equals(*__args):
        """ Equals(x: float, y: float, tolerance: float) -> bool """
        pass

    @staticmethod
    def EqualsTo(thisValue, value):
        """ EqualsTo(thisValue: float, value: float) -> bool """
        pass

    @staticmethod
    def ForEach(array, action):
        """ ForEach[T](array: Array[Array[T]], action: Action[T])ForEach[T](array: Array[T], action: Action[T]) """
        pass

    @staticmethod
    def GetCurveEntity(curve, checkClosed):
        """ GetCurveEntity(curve: Curve, checkClosed: bool) -> ICurveEntity """
        pass

    @staticmethod
    def LessThanOrEquals(x, y, tolerance):
        """ LessThanOrEquals(x: float, y: float, tolerance: float) -> bool """
        pass

    @staticmethod
    def LessThanOrEqualTo(thisValue, value):
        """ LessThanOrEqualTo(thisValue: float, value: float) -> bool """
        pass

    @staticmethod
    def LocateFile(fileName):
        """ LocateFile(fileName: str) -> str """
        pass

    @staticmethod
    def RadiansToDegrees(rad):
        """ RadiansToDegrees(rad: float) -> float """
        pass

    @staticmethod
    def ToEntity(data):
        """ ToEntity(data: DesignScriptEntity) -> IDesignScriptEntity """
        pass

    @staticmethod
    def ToPointArray(points, checkRectangular):
        """ ToPointArray(points: Array[Array[IPointEntity]], checkRectangular: bool) -> Array[Array[Point]] """
        pass

    @staticmethod
    def ToPointEntityArray(points, checkRectangular):
        """ ToPointEntityArray(points: Array[Array[Point]], checkRectangular: bool) -> Array[Array[IPointEntity]] """
        pass

    PI = 3.141592653589793
    __all__ = [
        'AreCoincident',
        'ConvertAll',
        'DegreesToRadians',
        'Equals',
        'EqualsTo',
        'ForEach',
        'GetCurveEntity',
        'LessThanOrEquals',
        'LessThanOrEqualTo',
        'LocateFile',
        'PI',
        'RadiansToDegrees',
        'ToEntity',
        'ToPointArray',
        'ToPointEntityArray',
    ]


class Helix(Curve):
    # no doc
    @staticmethod
    def ByAxis(axisPoint, axisDirection, startPoint, pitch, angleTurns):
        """ ByAxis(axisPoint: Point, axisDirection: Vector, startPoint: Point, pitch: float, angleTurns: float) -> Helix """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Helix) -> str """
        pass

    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Angle(self: Helix) -> float

"""

    AxisDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisDirection(self: Helix) -> Vector

"""

    AxisPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisPoint(self: Helix) -> Point

"""

    Pitch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pitch(self: Helix) -> float

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: Helix) -> float

"""


    mConstructor = None


class HostFactory(object):
    # no doc
    def PreloadAsmLibraries(self, baseDirectory):
        """ PreloadAsmLibraries(self: HostFactory, baseDirectory: str) """
        pass

    def ShutDown(self):
        """ ShutDown(self: HostFactory) """
        pass

    def StartUp(self):
        """ StartUp(self: HostFactory) """
        pass

    Factory = None
    Instance = None
    PersistenceManager = None


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
    @staticmethod
    def ByBestFitThroughPoints(bestFitPoints):
        """ ByBestFitThroughPoints(bestFitPoints: IEnumerable[Point]) -> Line """
        pass

    @staticmethod
    def ByStartPointDirectionLength(startPoint, direction, length):
        """ ByStartPointDirectionLength(startPoint: Point, direction: Vector, length: float) -> Line """
        pass

    @staticmethod
    def ByStartPointEndPoint(startPoint, endPoint):
        """ ByStartPointEndPoint(startPoint: Point, endPoint: Point) -> Line """
        pass

    @staticmethod
    def ByTangency(curve, parameter):
        """ ByTangency(curve: Curve, parameter: float) -> Line """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Line) -> str """
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: Line) -> Vector

"""


    mConstructor = None


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


    mConstructor = None


class Mesh(DesignScriptEntity):
    # no doc
    @staticmethod
    def ByPointsFaceIndices(vertexPositions, indices):
        """ ByPointsFaceIndices(vertexPositions: IEnumerable[Point], indices: IEnumerable[IndexGroup]) -> Mesh """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Mesh) -> str """
        pass

    FaceIndices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FaceIndices(self: Mesh) -> Array[IndexGroup]

"""

    VertexNormals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VertexNormals(self: Mesh) -> Array[Vector]

"""

    VertexPositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VertexPositions(self: Mesh) -> Array[Point]

"""


    mConstructor = None


class NurbsCurve(Curve):
    # no doc
    @staticmethod
    def ByControlPoints(points, degree=None, closeCurve=None):
        """
        ByControlPoints(points: IEnumerable[Point], degree: int, closeCurve: bool) -> NurbsCurve
        ByControlPoints(points: IEnumerable[Point], degree: int) -> NurbsCurve
        ByControlPoints(points: IEnumerable[Point]) -> NurbsCurve
        """
        pass

    @staticmethod
    def ByControlPointsWeightsKnots(points, weights, knots, degree):
        """ ByControlPointsWeightsKnots(points: IEnumerable[Point], weights: Array[float], knots: Array[float], degree: int) -> NurbsCurve """
        pass

    @staticmethod
    def ByPoints(points, *__args):
        """
        ByPoints(points: IEnumerable[Point], degree: int) -> NurbsCurve
        ByPoints(points: IEnumerable[Point], closeCurve: bool) -> NurbsCurve
        ByPoints(points: IEnumerable[Point]) -> NurbsCurve
        """
        pass

    @staticmethod
    def ByPointsTangents(points, startTangent, endTangent):
        """ ByPointsTangents(points: IEnumerable[Point], startTangent: Vector, endTangent: Vector) -> NurbsCurve """
        pass

    def ControlPoints(self):
        """ ControlPoints(self: NurbsCurve) -> Array[Point] """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def Knots(self):
        """ Knots(self: NurbsCurve) -> Array[float] """
        pass

    def ToString(self):
        """ ToString(self: NurbsCurve) -> str """
        pass

    def Weights(self):
        """ Weights(self: NurbsCurve) -> Array[float] """
        pass

    Degree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Degree(self: NurbsCurve) -> int

"""

    IsPeriodic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPeriodic(self: NurbsCurve) -> bool

"""

    IsRational = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRational(self: NurbsCurve) -> bool

"""


    mConstructor = None


class Surface(Topology):
    # no doc
    def ApproximateWithTolerance(self, tolerance):
        """ ApproximateWithTolerance(self: Surface, tolerance: float) -> NurbsSurface """
        pass

    @staticmethod
    def ByLoft(crossSections, *__args):
        """
        ByLoft(crossSections: IEnumerable[Curve], guideCurves: IEnumerable[Curve]) -> Surface
        ByLoft(crossSections: IEnumerable[Curve], guideCurve: Curve) -> Surface
        ByLoft(crossSections: IEnumerable[Curve]) -> Surface
        """
        pass

    @staticmethod
    def ByPatch(closedCurve):
        """ ByPatch(closedCurve: Curve) -> Surface """
        pass

    @staticmethod
    def ByPerimeterPoints(points):
        """ ByPerimeterPoints(points: IEnumerable[Point]) -> Surface """
        pass

    @staticmethod
    def ByRevolve(profile, axisOrigin, axisDirection, startAngle, sweepAngle):
        """ ByRevolve(profile: Curve, axisOrigin: Point, axisDirection: Vector, startAngle: float, sweepAngle: float) -> Surface """
        pass

    @staticmethod
    def ByRuledLoft(crossSections):
        """ ByRuledLoft(crossSections: IEnumerable[Line]) -> Surface """
        pass

    @staticmethod
    def BySweep(profile, path):
        """ BySweep(profile: Curve, path: Curve) -> Surface """
        pass

    @staticmethod
    def BySweep2Rails(path, guideRail, profile):
        """ BySweep2Rails(path: Curve, guideRail: Curve, profile: Curve) -> Surface """
        pass

    def CoordinateSystemAtParameter(self, u, v):
        """ CoordinateSystemAtParameter(self: Surface, u: float, v: float) -> CoordinateSystem """
        pass

    def CurvatureAtParameter(self, u, v):
        """ CurvatureAtParameter(self: Surface, u: float, v: float) -> CoordinateSystem """
        pass

    def DerivativesAtParameter(self, u, v):
        """ DerivativesAtParameter(self: Surface, u: float, v: float) -> Array[Vector] """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def FlipNormalDirection(self):
        """ FlipNormalDirection(self: Surface) -> Surface """
        pass

    def GaussianCurvatureAtParameter(self, u, v):
        """ GaussianCurvatureAtParameter(self: Surface, u: float, v: float) -> float """
        pass

    def GetIsoline(self, isoDirection, parameter):
        """ GetIsoline(self: Surface, isoDirection: int, parameter: float) -> Curve """
        pass

    def Join(self, *__args):
        """
        Join(self: Surface, otherSurfaces: IEnumerable[Surface]) -> PolySurface
        Join(self: Surface, otherSurface: Surface) -> PolySurface
        """
        pass

    def NormalAtParameter(self, u, v):
        """ NormalAtParameter(self: Surface, u: float, v: float) -> Vector """
        pass

    def NormalAtPoint(self, point):
        """ NormalAtPoint(self: Surface, point: Point) -> Vector """
        pass

    def Offset(self, distance):
        """ Offset(self: Surface, distance: float) -> Surface """
        pass

    def PerimeterCurves(self):
        """ PerimeterCurves(self: Surface) -> Array[Curve] """
        pass

    def PointAtParameter(self, u, v):
        """ PointAtParameter(self: Surface, u: float, v: float) -> Point """
        pass

    def PrincipalCurvaturesAtParameter(self, u, v):
        """ PrincipalCurvaturesAtParameter(self: Surface, u: float, v: float) -> Array[float] """
        pass

    def PrincipalDirectionsAtParameter(self, u, v):
        """ PrincipalDirectionsAtParameter(self: Surface, u: float, v: float) -> Array[Vector] """
        pass

    def ProjectInputOnto(self, geometryToProject, projectionDirection):
        """ ProjectInputOnto(self: Surface, geometryToProject: Geometry, projectionDirection: Vector) -> Array[Geometry] """
        pass

    def SubtractFrom(self, trimmingEntity):
        """ SubtractFrom(self: Surface, trimmingEntity: Solid) -> Array[Geometry] """
        pass

    def TangentAtUParameter(self, u, v):
        """ TangentAtUParameter(self: Surface, u: float, v: float) -> Vector """
        pass

    def TangentAtVParameter(self, u, v):
        """ TangentAtVParameter(self: Surface, u: float, v: float) -> Vector """
        pass

    def Thicken(self, thickness, both_sides=None):
        """
        Thicken(self: Surface, thickness: float, both_sides: bool) -> Solid
        Thicken(self: Surface, thickness: float) -> Solid
        """
        pass

    def ToNurbsSurface(self):
        """ ToNurbsSurface(self: Surface) -> NurbsSurface """
        pass

    def ToString(self):
        """ ToString(self: Surface) -> str """
        pass

    def TrimWithEdgeLoops(self, loops):
        """ TrimWithEdgeLoops(self: Surface, loops: IEnumerable[PolyCurve]) -> Surface """
        pass

    def UVParameterAtPoint(self, point):
        """ UVParameterAtPoint(self: Surface, point: Point) -> UV """
        pass

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Area(self: Surface) -> float

"""

    Closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Closed(self: Surface) -> bool

"""

    ClosedInU = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClosedInU(self: Surface) -> bool

"""

    ClosedInV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClosedInV(self: Surface) -> bool

"""

    Perimeter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Perimeter(self: Surface) -> float

"""


    mConstructor = None


class NurbsSurface(Surface):
    # no doc
    @staticmethod
    def ByControlPoints(controlVertices, uDegree, vDegree):
        """ ByControlPoints(controlVertices: Array[Array[Point]], uDegree: int, vDegree: int) -> NurbsSurface """
        pass

    @staticmethod
    def ByControlPointsWeightsKnots(controlVertices, weights, knotsU, knotsV, uDegree, vDegree):
        """ ByControlPointsWeightsKnots(controlVertices: Array[Array[Point]], weights: Array[Array[float]], knotsU: Array[float], knotsV: Array[float], uDegree: int, vDegree: int) -> NurbsSurface """
        pass

    @staticmethod
    def ByPoints(points, uDegree, vDegree):
        """ ByPoints(points: Array[Array[Point]], uDegree: int, vDegree: int) -> NurbsSurface """
        pass

    @staticmethod
    def ByPointsTangents(points, startUTangents, endUTangents, startVTangents, endVTangents):
        """ ByPointsTangents(points: Array[Array[Point]], startUTangents: IEnumerable[Vector], endUTangents: IEnumerable[Vector], startVTangents: IEnumerable[Vector], endVTangents: IEnumerable[Vector]) -> NurbsSurface """
        pass

    @staticmethod
    def ByPointsTangentsKnotsDerivatives(points, startUTangents, endUTangents, startVTangents, endVTangents, uKnots, vKnots, cornerTwistDerivatives):
        """ ByPointsTangentsKnotsDerivatives(points: Array[Array[Point]], startUTangents: IEnumerable[Vector], endUTangents: IEnumerable[Vector], startVTangents: IEnumerable[Vector], endVTangents: IEnumerable[Vector], uKnots: Array[float], vKnots: Array[float], cornerTwistDerivatives: IEnumerable[Vector]) -> NurbsSurface """
        pass

    def ControlPoints(self):
        """ ControlPoints(self: NurbsSurface) -> Array[Array[Point]] """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: NurbsSurface) -> str """
        pass

    def UKnots(self):
        """ UKnots(self: NurbsSurface) -> Array[float] """
        pass

    def VKnots(self):
        """ VKnots(self: NurbsSurface) -> Array[float] """
        pass

    def Weights(self):
        """ Weights(self: NurbsSurface) -> Array[Array[float]] """
        pass

    DegreeU = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DegreeU(self: NurbsSurface) -> int

"""

    DegreeV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DegreeV(self: NurbsSurface) -> int

"""

    IsPeriodicInU = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPeriodicInU(self: NurbsSurface) -> bool

"""

    IsPeriodicInV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPeriodicInV(self: NurbsSurface) -> bool

"""

    IsRational = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRational(self: NurbsSurface) -> bool

"""

    NumControlPointsU = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumControlPointsU(self: NurbsSurface) -> int

"""

    NumControlPointsV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumControlPointsV(self: NurbsSurface) -> int

"""


    mConstructor = None


class Plane(Geometry):
    # no doc
    @staticmethod
    def ByBestFitThroughPoints(points):
        """ ByBestFitThroughPoints(points: IEnumerable[Point]) -> Plane """
        pass

    @staticmethod
    def ByLineAndPoint(line, point):
        """ ByLineAndPoint(line: Line, point: Point) -> Plane """
        pass

    @staticmethod
    def ByOriginNormal(origin, normal):
        """ ByOriginNormal(origin: Point, normal: Vector) -> Plane """
        pass

    @staticmethod
    def ByOriginNormalXAxis(origin, normal, xAxis):
        """ ByOriginNormalXAxis(origin: Point, normal: Vector, xAxis: Vector) -> Plane """
        pass

    @staticmethod
    def ByOriginXAxisYAxis(origin, xAxis, yAxis):
        """ ByOriginXAxisYAxis(origin: Point, xAxis: Vector, yAxis: Vector) -> Plane """
        pass

    @staticmethod
    def ByThreePoints(origin, planePoint, xAxisPoint):
        """ ByThreePoints(origin: Point, planePoint: Point, xAxisPoint: Point) -> Plane """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def Offset(self, dist):
        """ Offset(self: Plane, dist: float) -> Plane """
        pass

    def ToCoordinateSystem(self):
        """ ToCoordinateSystem(self: Plane) -> CoordinateSystem """
        pass

    def ToString(self):
        """ ToString(self: Plane) -> str """
        pass

    @staticmethod
    def XY():
        """ XY() -> Plane """
        pass

    @staticmethod
    def XZ():
        """ XZ() -> Plane """
        pass

    @staticmethod
    def YZ():
        """ YZ() -> Plane """
        pass

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Normal(self: Plane) -> Vector

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Origin(self: Plane) -> Point

"""

    XAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XAxis(self: Plane) -> Vector

"""

    YAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YAxis(self: Plane) -> Vector

"""


    mConstructor = None


class Point(Geometry):
    # no doc
    def Add(self, vectorToAdd):
        """ Add(self: Point, vectorToAdd: Vector) -> Point """
        pass

    def AsVector(self):
        """ AsVector(self: Point) -> Vector """
        pass

    @staticmethod
    def ByCartesianCoordinates(cs, x, y, z):
        """ ByCartesianCoordinates(cs: CoordinateSystem, x: float, y: float, z: float) -> Point """
        pass

    @staticmethod
    def ByCoordinates(x, y, z=None):
        """
        ByCoordinates(x: float, y: float, z: float) -> Point
        ByCoordinates(x: float, y: float) -> Point
        """
        pass

    @staticmethod
    def ByCylindricalCoordinates(cs, angle, elevation, radius):
        """ ByCylindricalCoordinates(cs: CoordinateSystem, angle: float, elevation: float, radius: float) -> Point """
        pass

    @staticmethod
    def BySphericalCoordinates(cs, phi, theta, radius):
        """ BySphericalCoordinates(cs: CoordinateSystem, phi: float, theta: float, radius: float) -> Point """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: Point, other: DesignScriptEntity) -> bool """
        pass

    @staticmethod
    def Origin():
        """ Origin() -> Point """
        pass

    def Project(self, baseGeometry, projectionDirection):
        """ Project(self: Point, baseGeometry: Geometry, projectionDirection: Vector) -> Array[Geometry] """
        pass

    @staticmethod
    def PruneDuplicates(points, tolerance):
        """ PruneDuplicates(points: IEnumerable[Point], tolerance: float) -> Array[Point] """
        pass

    def Subtract(self, vectorToSubtract):
        """ Subtract(self: Point, vectorToSubtract: Vector) -> Point """
        pass

    def ToString(self):
        """ ToString(self: Point) -> str """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: Point) -> float

"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: Point) -> float

"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: Point) -> float

"""


    mConstructor = None


class PolyCurve(Curve):
    # no doc
    def BasePlane(self):
        """ BasePlane(self: PolyCurve) -> Plane """
        pass

    @staticmethod
    def ByJoinedCurves(curves):
        """ ByJoinedCurves(curves: IEnumerable[Curve]) -> PolyCurve """
        pass

    @staticmethod
    def ByPoints(points, connectLastToFirst):
        """ ByPoints(points: IEnumerable[Point], connectLastToFirst: bool) -> PolyCurve """
        pass

    @staticmethod
    def ByThickeningCurve(curve, thickness, nor):
        """ ByThickeningCurve(curve: Curve, thickness: float, nor: Vector) -> PolyCurve """
        pass

    def CloseWithLine(self):
        """ CloseWithLine(self: PolyCurve) -> PolyCurve """
        pass

    def CloseWithLineAndTangentArcs(self, radiusAtStart, radiusAtEnd):
        """ CloseWithLineAndTangentArcs(self: PolyCurve, radiusAtStart: float, radiusAtEnd: float) -> PolyCurve """
        pass

    def CurveAtIndex(self, index, endOrStart):
        """ CurveAtIndex(self: PolyCurve, index: int, endOrStart: bool) -> Curve """
        pass

    def Curves(self):
        """ Curves(self: PolyCurve) -> Array[Curve] """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ExtendWithArc(self, length, radius, endOrStart):
        """ ExtendWithArc(self: PolyCurve, length: float, radius: float, endOrStart: bool) -> PolyCurve """
        pass

    def ExtendWithEllipse(self, length, radius1, radius2, endEllipseParameter, endOrStart):
        """ ExtendWithEllipse(self: PolyCurve, length: float, radius1: float, radius2: float, endEllipseParameter: float, endOrStart: bool) -> PolyCurve """
        pass

    def Fillet(self, radius, rightSide):
        """ Fillet(self: PolyCurve, radius: float, rightSide: bool) -> PolyCurve """
        pass

    def Offset(self, distance, extendCircular=None):
        """ Offset(self: PolyCurve, distance: float, extendCircular: bool) -> Curve """
        pass

    def ToString(self):
        """ ToString(self: PolyCurve) -> str """
        pass

    NumberOfCurves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfCurves(self: PolyCurve) -> int

"""


    mConstructor = None


class Polygon(PolyCurve):
    # no doc
    @staticmethod
    def ByPoints(points):
        """ ByPoints(points: IEnumerable[Point]) -> Polygon """
        pass

    def Center(self):
        """ Center(self: Polygon) -> Point """
        pass

    def ContainmentTest(self, point):
        """ ContainmentTest(self: Polygon, point: Point) -> bool """
        pass

    def Corners(self):
        """ Corners(self: Polygon) -> Array[Point] """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    @staticmethod
    def RegularPolygon(circle, numberSides):
        """ RegularPolygon(circle: Circle, numberSides: int) -> Polygon """
        pass

    def SelfIntersections(self):
        """ SelfIntersections(self: Polygon) -> Array[Point] """
        pass

    def ToString(self):
        """ ToString(self: Polygon) -> str """
        pass

    PlaneDeviation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlaneDeviation(self: Polygon) -> float

"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: Polygon) -> Array[Point]

"""


    mConstructor = None


class PolySurface(Surface):
    # no doc
    @staticmethod
    def ByJoinedSurfaces(surfaces):
        """ ByJoinedSurfaces(surfaces: IEnumerable[Surface]) -> PolySurface """
        pass

    @staticmethod
    def ByLoft(crossSections, guideCurve=None):
        """
        ByLoft(crossSections: IEnumerable[Curve], guideCurve: Curve) -> PolySurface
        ByLoft(crossSections: IEnumerable[Curve]) -> PolySurface
        """
        pass

    @staticmethod
    def ByLoftGuides(crossSections, guideCurves):
        """ ByLoftGuides(crossSections: IEnumerable[Curve], guideCurves: IEnumerable[Curve]) -> PolySurface """
        pass

    @staticmethod
    def BySolid(solid):
        """ BySolid(solid: Solid) -> PolySurface """
        pass

    @staticmethod
    def BySweep(rail, *__args):
        """
        BySweep(rail: Curve, profile: Curve) -> PolySurface
        BySweep(rail: Curve, crossSection: IEnumerable[Curve]) -> PolySurface
        """
        pass

    def Chamfer(self, edges, offset):
        """ Chamfer(self: PolySurface, edges: IEnumerable[Edge], offset: float) -> PolySurface """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def EdgeCount(self):
        """ EdgeCount(self: PolySurface) -> int """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ExtractSolids(self):
        """ ExtractSolids(self: PolySurface) -> Array[Solid] """
        pass

    def Fillet(self, edges, radius):
        """ Fillet(self: PolySurface, edges: IEnumerable[Edge], radius: float) -> PolySurface """
        pass

    def LocateSurfacesByLine(self, line):
        """ LocateSurfacesByLine(self: PolySurface, line: Line) -> Array[Surface] """
        pass

    def LocateSurfacesByPoint(self, point, direction):
        """ LocateSurfacesByPoint(self: PolySurface, point: Point, direction: Vector) -> Array[Surface] """
        pass

    def SurfaceCount(self):
        """ SurfaceCount(self: PolySurface) -> int """
        pass

    def Surfaces(self):
        """ Surfaces(self: PolySurface) -> Array[Surface] """
        pass

    def ToString(self):
        """ ToString(self: PolySurface) -> str """
        pass

    def UnconnectedBoundaries(self):
        """ UnconnectedBoundaries(self: PolySurface) -> Array[PolyCurve] """
        pass

    def VertexCount(self):
        """ VertexCount(self: PolySurface) -> int """
        pass

    mConstructor = None


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
    @staticmethod
    def ByCornerPoints(*__args):
        """
        ByCornerPoints(p1: Point, p2: Point, p3: Point, p4: Point) -> Rectangle
        ByCornerPoints(points: IEnumerable[Point]) -> Rectangle
        """
        pass

    @staticmethod
    def ByWidthLength(*__args):
        """
        ByWidthLength(cs: CoordinateSystem, width: float, length: float) -> Rectangle
        ByWidthLength(plane: Plane, width: float, length: float) -> Rectangle
        ByWidthLength(width: float, length: float) -> Rectangle
        """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Rectangle) -> str """
        pass

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: Rectangle) -> float

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: Rectangle) -> float

"""


    mConstructor = None


class Sphere(Solid):
    # no doc
    @staticmethod
    def ByBestFit(points):
        """ ByBestFit(points: IEnumerable[Point]) -> Sphere """
        pass

    @staticmethod
    def ByCenterPointRadius(centerPoint, radius):
        """ ByCenterPointRadius(centerPoint: Point, radius: float) -> Sphere """
        pass

    @staticmethod
    def ByFourPoints(points):
        """ ByFourPoints(points: IEnumerable[Point]) -> Sphere """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Sphere) -> str """
        pass

    CenterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterPoint(self: Sphere) -> Point

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: Sphere) -> float

"""


    mConstructor = None


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
    def Add(self, vectorToAdd):
        """ Add(self: Vector, vectorToAdd: Vector) -> Vector """
        pass

    def AngleAboutAxis(self, otherVector, rotationAxis):
        """ AngleAboutAxis(self: Vector, otherVector: Vector, rotationAxis: Vector) -> float """
        pass

    def AngleBetween(self, otherVector, rotationAxis=None):
        """
        AngleBetween(self: Vector, otherVector: Vector, rotationAxis: Vector) -> float
        AngleBetween(self: Vector, otherVector: Vector) -> float
        """
        pass

    def AngleWithVector(self, otherVector):
        """ AngleWithVector(self: Vector, otherVector: Vector) -> float """
        pass

    def AsPoint(self):
        """ AsPoint(self: Vector) -> Point """
        pass

    @staticmethod
    def ByCoordinates(x, y, z, normalized=None):
        """
        ByCoordinates(x: float, y: float, z: float, normalized: bool) -> Vector
        ByCoordinates(x: float, y: float, z: float) -> Vector
        """
        pass

    @staticmethod
    def ByTwoPoints(start, end):
        """ ByTwoPoints(start: Point, end: Point) -> Vector """
        pass

    def Cross(self, cross):
        """ Cross(self: Vector, cross: Vector) -> Vector """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def Dot(self, vec):
        """ Dot(self: Vector, vec: Vector) -> float """
        pass

    def Equals(self, obj):
        """ Equals(self: Vector, other: DesignScriptEntity) -> bool """
        pass

    def IsAlmostEqualTo(self, other):
        """ IsAlmostEqualTo(self: Vector, other: Vector) -> bool """
        pass

    def IsParallel(self, other):
        """ IsParallel(self: Vector, other: Vector) -> bool """
        pass

    def Normalized(self):
        """ Normalized(self: Vector) -> Vector """
        pass

    def Reverse(self):
        """ Reverse(self: Vector) -> Vector """
        pass

    def Rotate(self, *__args):
        """
        Rotate(self: Vector, plane: Plane, degrees: float) -> Vector
        Rotate(self: Vector, axis: Vector, degrees: float) -> Vector
        """
        pass

    def Scale(self, *__args):
        """
        Scale(self: Vector, xScaleFactor: float, yScaleFactor: float, zScaleFactor: float) -> Vector
        Scale(self: Vector, scale_factor: float) -> Vector
        """
        pass

    def Subtract(self, vectorToSubtract):
        """ Subtract(self: Vector, vectorToSubtract: Vector) -> Vector """
        pass

    def ToString(self):
        """ ToString(self: Vector) -> str """
        pass

    def Transform(self, cs):
        """ Transform(self: Vector, cs: CoordinateSystem) -> Vector """
        pass

    @staticmethod
    def XAxis():
        """ XAxis() -> Vector """
        pass

    @staticmethod
    def YAxis():
        """ YAxis() -> Vector """
        pass

    @staticmethod
    def ZAxis():
        """ ZAxis() -> Vector """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Vector) -> float

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: Vector) -> float

"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: Vector) -> float

"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: Vector) -> float

"""


    mConstructor = None


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

