# encoding: utf-8
# module Autodesk.DesignScript.Geometry.TSpline calls itself TSpline
# from ProtoGeometry, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class TSplineEdge(Edge):
    # no doc
    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def Info(self):
        """ Info(self: TSplineEdge) -> Dictionary[str, object] """
        pass

    def ToString(self):
        """ ToString(self: TSplineEdge) -> str """
        pass

    AdjacentFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdjacentFaces(self: TSplineEdge) -> Array[TSplineFace]

"""

    EndVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndVertex(self: TSplineEdge) -> TSplineVertex

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: TSplineEdge) -> int

"""

    IsBorder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBorder(self: TSplineEdge) -> bool

"""

    IsManifold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsManifold(self: TSplineEdge) -> bool

"""

    StartVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartVertex(self: TSplineEdge) -> TSplineVertex

"""

    UVNFrame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UVNFrame(self: TSplineEdge) -> TSplineUVNFrame

"""


    mConstructor = None


class TSplineFace(Face):
    # no doc
    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def Info(self):
        """ Info(self: TSplineFace) -> Dictionary[str, object] """
        pass

    def ToString(self):
        """ ToString(self: TSplineFace) -> str """
        pass

    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edges(self: TSplineFace) -> Array[TSplineEdge]

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: TSplineFace) -> int

"""

    Sides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Sides(self: TSplineFace) -> int

"""

    UVNFrame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UVNFrame(self: TSplineFace) -> TSplineUVNFrame

"""

    Valence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Valence(self: TSplineFace) -> int

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: TSplineFace) -> Array[TSplineVertex]

"""


    mConstructor = None


class TSplineInitialSymmetry(DesignScriptEntity):
    # no doc
    @staticmethod
    def ByAxial(xAxis, yAxis, zAxis):
        """ ByAxial(xAxis: bool, yAxis: bool, zAxis: bool) -> TSplineInitialSymmetry """
        pass

    @staticmethod
    def ByRadial(symmetricFaces):
        """ ByRadial(symmetricFaces: int) -> TSplineInitialSymmetry """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: TSplineInitialSymmetry) -> str """
        pass

    IsRadial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRadial(self: TSplineInitialSymmetry) -> bool

"""

    RadialSymmetryFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RadialSymmetryFaces(self: TSplineInitialSymmetry) -> int

"""

    XAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XAxis(self: TSplineInitialSymmetry) -> bool

"""

    YAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YAxis(self: TSplineInitialSymmetry) -> bool

"""

    ZAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZAxis(self: TSplineInitialSymmetry) -> bool

"""


    mConstructor = None


class TSplineReflection(DesignScriptEntity):
    # no doc
    @staticmethod
    def ByAxial(plane):
        """ ByAxial(plane: Plane) -> TSplineReflection """
        pass

    @staticmethod
    def ByRadial(plane, segmentsCount, segmentAngle):
        """ ByRadial(plane: Plane, segmentsCount: int, segmentAngle: float) -> TSplineReflection """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: TSplineReflection) -> str """
        pass

    Axis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Axis(self: TSplineReflection) -> Vector

"""

    IsRadial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRadial(self: TSplineReflection) -> bool

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: TSplineReflection) -> Plane

"""

    SegmentAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentAngle(self: TSplineReflection) -> float

"""

    SegmentsCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentsCount(self: TSplineReflection) -> int

"""


    mConstructor = None


class TSplineTopology(Topology):
    # no doc
    def DecomposedEdges(self):
        """ DecomposedEdges(self: TSplineTopology) -> Dictionary[str, Array[TSplineEdge]] """
        pass

    def DecomposedFaces(self):
        """ DecomposedFaces(self: TSplineTopology) -> Dictionary[str, Array[TSplineFace]] """
        pass

    def DecomposedVertices(self):
        """ DecomposedVertices(self: TSplineTopology) -> Dictionary[str, Array[TSplineVertex]] """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def EdgeByIndex(self, index):
        """ EdgeByIndex(self: TSplineTopology, index: int) -> TSplineEdge """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def FaceByIndex(self, index):
        """ FaceByIndex(self: TSplineTopology, index: int) -> TSplineFace """
        pass

    def ToString(self):
        """ ToString(self: TSplineTopology) -> str """
        pass

    def VertexByIndex(self, index):
        """ VertexByIndex(self: TSplineTopology, index: int) -> TSplineVertex """
        pass

    BorderEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BorderEdges(self: TSplineTopology) -> Array[TSplineEdge]

"""

    BorderFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BorderFaces(self: TSplineTopology) -> Array[TSplineFace]

"""

    BorderVertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BorderVertices(self: TSplineTopology) -> Array[TSplineVertex]

"""

    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edges(self: TSplineTopology) -> Array[TSplineEdge]

"""

    EdgesCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgesCount(self: TSplineTopology) -> int

"""

    Faces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Faces(self: TSplineTopology) -> Array[TSplineFace]

"""

    FacesCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FacesCount(self: TSplineTopology) -> int

"""

    InnerEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerEdges(self: TSplineTopology) -> Array[TSplineEdge]

"""

    InnerFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerFaces(self: TSplineTopology) -> Array[TSplineFace]

"""

    InnerVertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerVertices(self: TSplineTopology) -> Array[TSplineVertex]

"""

    NGonFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NGonFaces(self: TSplineTopology) -> Array[TSplineFace]

"""

    NonManifoldEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NonManifoldEdges(self: TSplineTopology) -> Array[TSplineEdge]

"""

    NonManifoldVertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NonManifoldVertices(self: TSplineTopology) -> Array[TSplineVertex]

"""

    RegularFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RegularFaces(self: TSplineTopology) -> Array[TSplineFace]

"""

    RegularVertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RegularVertices(self: TSplineTopology) -> Array[TSplineVertex]

"""

    StarPointVertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StarPointVertices(self: TSplineTopology) -> Array[TSplineVertex]

"""

    TPointVertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TPointVertices(self: TSplineTopology) -> Array[TSplineVertex]

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: TSplineTopology) -> Array[TSplineVertex]

"""

    VerticesCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticesCount(self: TSplineTopology) -> int

"""


    mConstructor = None


class TSplineSurface(TSplineTopology):
    # no doc
    def AddReflections(self, reflections, weldSymmetricPortions, weldTolerance):
        """ AddReflections(self: TSplineSurface, reflections: IEnumerable[TSplineReflection], weldSymmetricPortions: bool, weldTolerance: float) -> TSplineSurface """
        pass

    def BevelEdges(self, edges, percentage, segments, keepOnFace, roundness):
        """ BevelEdges(self: TSplineSurface, edges: IEnumerable[TSplineEdge], percentage: float, segments: int, keepOnFace: bool, roundness: float) -> TSplineSurface """
        pass

    def BridgeEdgesToEdges(self, firstGroup, secondGroup, followCurves, frameRotations, spansCounts, cleanBorderBridges, keepSubdCreases, firstAlignVertices, secondAlignVertices, flipAlignmentFlags):
        """ BridgeEdgesToEdges(self: TSplineSurface, firstGroup: IEnumerable[TSplineEdge], secondGroup: IEnumerable[TSplineEdge], followCurves: IEnumerable[Curve], frameRotations: IEnumerable[int], spansCounts: IEnumerable[int], cleanBorderBridges: bool, keepSubdCreases: bool, firstAlignVertices: IEnumerable[TSplineVertex], secondAlignVertices: IEnumerable[TSplineVertex], flipAlignmentFlags: IEnumerable[bool]) -> TSplineSurface """
        pass

    def BridgeEdgesToFaces(self, firstGroup, secondGroup, followCurves, frameRotations, spansCounts, cleanBorderBridges, keepSubdCreases, firstAlignVertices, secondAlignVertices, flipAlignmentFlags):
        """ BridgeEdgesToFaces(self: TSplineSurface, firstGroup: IEnumerable[TSplineEdge], secondGroup: IEnumerable[TSplineFace], followCurves: IEnumerable[Curve], frameRotations: IEnumerable[int], spansCounts: IEnumerable[int], cleanBorderBridges: bool, keepSubdCreases: bool, firstAlignVertices: IEnumerable[TSplineVertex], secondAlignVertices: IEnumerable[TSplineVertex], flipAlignmentFlags: IEnumerable[bool]) -> TSplineSurface """
        pass

    def BridgeFacesToEdges(self, firstGroup, secondGroup, followCurves, frameRotations, spansCounts, cleanBorderBridges, keepSubdCreases, firstAlignVertices, secondAlignVertices, flipAlignmentFlags):
        """ BridgeFacesToEdges(self: TSplineSurface, firstGroup: IEnumerable[TSplineFace], secondGroup: IEnumerable[TSplineEdge], followCurves: IEnumerable[Curve], frameRotations: IEnumerable[int], spansCounts: IEnumerable[int], cleanBorderBridges: bool, keepSubdCreases: bool, firstAlignVertices: IEnumerable[TSplineVertex], secondAlignVertices: IEnumerable[TSplineVertex], flipAlignmentFlags: IEnumerable[bool]) -> TSplineSurface """
        pass

    def BridgeFacesToFaces(self, firstGroup, secondGroup, followCurves, frameRotations, spansCounts, cleanBorderBridges, keepSubdCreases, firstAlignVertices, secondAlignVertices, flipAlignmentFlags):
        """ BridgeFacesToFaces(self: TSplineSurface, firstGroup: IEnumerable[TSplineFace], secondGroup: IEnumerable[TSplineFace], followCurves: IEnumerable[Curve], frameRotations: IEnumerable[int], spansCounts: IEnumerable[int], cleanBorderBridges: bool, keepSubdCreases: bool, firstAlignVertices: IEnumerable[TSplineVertex], secondAlignVertices: IEnumerable[TSplineVertex], flipAlignmentFlags: IEnumerable[bool]) -> TSplineSurface """
        pass

    @staticmethod
    def BuildFromLines(lines, maxFaceValence, snappingTolerance, creaseOuterVertices, inSmoothMode):
        """ BuildFromLines(lines: IEnumerable[Curve], maxFaceValence: int, snappingTolerance: float, creaseOuterVertices: bool, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def BuildPipes(curves, defaultRadius, snappingTolerance, segmentsCount, endRotations, endRadii, endPercentage, inSmoothMode):
        """ BuildPipes(curves: IEnumerable[Curve], defaultRadius: float, snappingTolerance: float, segmentsCount: IEnumerable[int], endRotations: IEnumerable[float], endRadii: IEnumerable[float], endPercentage: IEnumerable[float], inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByBoxCorners(lowPoint, highPoint, xSpans, ySpans, zSpans, symmetry, inSmoothMode):
        """ ByBoxCorners(lowPoint: Point, highPoint: Point, xSpans: int, ySpans: int, zSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByBoxLengths(*__args):
        """
        ByBoxLengths(cs: CoordinateSystem, width: float, length: float, height: float, xSpans: int, ySpans: int, zSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        ByBoxLengths(origin: Point, width: float, length: float, height: float, xSpans: int, ySpans: int, zSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        ByBoxLengths(width: float, length: float, height: float, xSpans: int, ySpans: int, zSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        """
        pass

    @staticmethod
    def ByCombinedTSplineSurfaces(tSplineSurfaces):
        """ ByCombinedTSplineSurfaces(tSplineSurfaces: IEnumerable[TSplineSurface]) -> TSplineSurface """
        pass

    @staticmethod
    def ByConeCoordinateSystemHeightRadii(cs, height, startRadius, endRadius, radiusSpans, heightSpans, symmetry, inSmoothMode):
        """ ByConeCoordinateSystemHeightRadii(cs: CoordinateSystem, height: float, startRadius: float, endRadius: float, radiusSpans: int, heightSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByConeCoordinateSystemHeightRadius(cs, height, radius, radiusSpans, heightSpans, symmetry, inSmoothMode):
        """ ByConeCoordinateSystemHeightRadius(cs: CoordinateSystem, height: float, radius: float, radiusSpans: int, heightSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByConePointsRadii(startPoint, endPoint, startRadius, endRadius, radiusSpans, heightSpans, symmetry, inSmoothMode):
        """ ByConePointsRadii(startPoint: Point, endPoint: Point, startRadius: float, endRadius: float, radiusSpans: int, heightSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByConePointsRadius(startPoint, endPoint, radius, radiusSpans, heightSpans, symmetry, inSmoothMode):
        """ ByConePointsRadius(startPoint: Point, endPoint: Point, radius: float, radiusSpans: int, heightSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByCylinderPointsRadius(startPoint, endPoint, radius, radiusSpans, heightSpans, symmetry, inSmoothMode):
        """ ByCylinderPointsRadius(startPoint: Point, endPoint: Point, radius: float, radiusSpans: int, heightSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByCylinderRadiusHeight(cs, radius, height, radiusSpans, heightSpans, symmetry, inSmoothMode):
        """ ByCylinderRadiusHeight(cs: CoordinateSystem, radius: float, height: float, radiusSpans: int, heightSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByExtrude(curve, direction, frontDistance, backDistance, frontSpans, backSpans, profileSpans, uniform, inSmoothMode):
        """ ByExtrude(curve: Curve, direction: Vector, frontDistance: float, backDistance: float, frontSpans: int, backSpans: int, profileSpans: int, uniform: bool, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByNurbsSurfaceCurvature(nurbsSurface, inSmoothMode):
        """ ByNurbsSurfaceCurvature(nurbsSurface: NurbsSurface, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByNurbsSurfaceUniform(nurbsSurface, uSpans, vSpans, uUseArcLen, vUseArcLen, inSmoothMode):
        """ ByNurbsSurfaceUniform(nurbsSurface: NurbsSurface, uSpans: int, vSpans: int, uUseArcLen: bool, vUseArcLen: bool, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByPlaneBestFitThroughPoints(points, minCorner, maxCorner, xSpans, ySpans, symmetry, inSmoothMode):
        """ ByPlaneBestFitThroughPoints(points: IEnumerable[Point], minCorner: Point, maxCorner: Point, xSpans: int, ySpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByPlaneLineAndPoint(line, point, minCorner, maxCorner, xSpans, ySpans, symmetry, inSmoothMode):
        """ ByPlaneLineAndPoint(line: Line, point: Point, minCorner: Point, maxCorner: Point, xSpans: int, ySpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByPlaneOriginNormal(origin, normal, minCorner, maxCorner, xSpans, ySpans, symmetry, inSmoothMode):
        """ ByPlaneOriginNormal(origin: Point, normal: Vector, minCorner: Point, maxCorner: Point, xSpans: int, ySpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByPlaneOriginNormalXAxis(origin, normal, xAxis, minCorner, maxCorner, xSpans, ySpans, symmetry, inSmoothMode):
        """ ByPlaneOriginNormalXAxis(origin: Point, normal: Vector, xAxis: Vector, minCorner: Point, maxCorner: Point, xSpans: int, ySpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByPlaneOriginXAxisYAxis(origin, xAxis, yAxis, minCorner, maxCorner, xSpans, ySpans, symmetry, inSmoothMode):
        """ ByPlaneOriginXAxisYAxis(origin: Point, xAxis: Vector, yAxis: Vector, minCorner: Point, maxCorner: Point, xSpans: int, ySpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByPlaneThreePoints(p1, p2, p3, minCorner, maxCorner, xSpans, ySpans, symmetry, inSmoothMode):
        """ ByPlaneThreePoints(p1: Point, p2: Point, p3: Point, minCorner: Point, maxCorner: Point, xSpans: int, ySpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByQuadballCenterRadius(center, radius, spans, symmetry, inSmoothMode):
        """ ByQuadballCenterRadius(center: Point, radius: float, spans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByQuadballCoordinateSystemRadius(cs, radius, spans, symmetry, inSmoothMode):
        """ ByQuadballCoordinateSystemRadius(cs: CoordinateSystem, radius: float, spans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByRevolve(profile, axisOrigin, axisDirection, startAngle, sweepAngle, radialSpans, axialSpans, uniform, symmetry, inSmoothMode):
        """ ByRevolve(profile: Curve, axisOrigin: Point, axisDirection: Vector, startAngle: float, sweepAngle: float, radialSpans: int, axialSpans: int, uniform: bool, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def BySphereBestFit(points, radiusSpans, heightSpans, symmetry, inSmoothMode):
        """ BySphereBestFit(points: IEnumerable[Point], radiusSpans: int, heightSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def BySphereCenterPointRadius(centerPoint, radius, radiusSpans, heightSpans, symmetry, inSmoothMode):
        """ BySphereCenterPointRadius(centerPoint: Point, radius: float, radiusSpans: int, heightSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def BySphereFourPoints(points, radiusSpans, heightSpans, symmetry, inSmoothMode):
        """ BySphereFourPoints(points: IEnumerable[Point], radiusSpans: int, heightSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def BySweep(profile, path, parallel, pathSpans, profileSpans, pathUniform, profileUniform, inSmoothMode):
        """ BySweep(profile: Curve, path: Curve, parallel: bool, pathSpans: int, profileSpans: int, pathUniform: bool, profileUniform: bool, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByTorusCenterRadii(center, innerRadius, outerRadius, innerRadiusSpans, outerRadiusSpans, symmetry, inSmoothMode):
        """ ByTorusCenterRadii(center: Point, innerRadius: float, outerRadius: float, innerRadiusSpans: int, outerRadiusSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByTorusCoordinateSystemRadii(cs, innerRadius, outerRadius, innerRadiusSpans, outerRadiusSpans, symmetry, inSmoothMode):
        """ ByTorusCoordinateSystemRadii(cs: CoordinateSystem, innerRadius: float, outerRadius: float, innerRadiusSpans: int, outerRadiusSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    def CompressIndexes(self):
        """ CompressIndexes(self: TSplineSurface) -> TSplineSurface """
        pass

    def CreaseEdges(self, edges):
        """ CreaseEdges(self: TSplineSurface, edges: IEnumerable[TSplineEdge]) -> TSplineSurface """
        pass

    def CreaseVertices(self, vertices):
        """ CreaseVertices(self: TSplineSurface, vertices: IEnumerable[TSplineVertex]) -> TSplineSurface """
        pass

    def CreateMatch(self, tsEdges, *__args):
        """
        CreateMatch(self: TSplineSurface, tsEdges: IEnumerable[TSplineEdge], brepEdges: IEnumerable[Edge], continuity: int, useArclength: bool, useRefinement: bool, numRefinementSteps: int, refinementTolerance: float, usePropagation: bool, widthOfPropagation: float, tangentScale: float, curvParamWeight: float, flipSourceTargetAlignment: bool) -> TSplineSurface
        CreateMatch(self: TSplineSurface, tsEdges: IEnumerable[TSplineEdge], curves: IEnumerable[Curve], continuity: int, useArclength: bool, useRefinement: bool, numRefinementSteps: int, refinementTolerance: float, usePropagation: bool, widthOfPropagation: float, tangentScale: float, curvParamWeight: float, flipSourceTargetAlignment: bool) -> TSplineSurface
        """
        pass

    def DeleteEdges(self, edges):
        """ DeleteEdges(self: TSplineSurface, edges: IEnumerable[TSplineEdge]) -> TSplineSurface """
        pass

    def DeleteFaces(self, faces):
        """ DeleteFaces(self: TSplineSurface, faces: IEnumerable[TSplineFace]) -> TSplineSurface """
        pass

    def DeleteVertices(self, vertices):
        """ DeleteVertices(self: TSplineSurface, vertices: IEnumerable[TSplineVertex]) -> TSplineSurface """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DuplicateFaces(self, faces):
        """ DuplicateFaces(self: TSplineSurface, faces: IEnumerable[TSplineFace]) -> TSplineSurface """
        pass

    def EnableSmoothMode(self, enable):
        """ EnableSmoothMode(self: TSplineSurface, enable: bool) -> TSplineSurface """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    @staticmethod
    def ExportToTSM(tSplineSurface, filePath):
        """ ExportToTSM(tSplineSurface: TSplineSurface, filePath: str) -> str """
        pass

    @staticmethod
    def ExportToTSS(tSplineSurfaces, filePath):
        """ ExportToTSS(tSplineSurfaces: IEnumerable[TSplineSurface], filePath: str) -> str """
        pass

    def ExtrudeEdges(self, edges, direction, spans):
        """ ExtrudeEdges(self: TSplineSurface, edges: IEnumerable[TSplineEdge], direction: Vector, spans: int) -> TSplineSurface """
        pass

    def ExtrudeEdgesAlongCurve(self, edges, curve, spans):
        """ ExtrudeEdgesAlongCurve(self: TSplineSurface, edges: IEnumerable[TSplineEdge], curve: Curve, spans: int) -> TSplineSurface """
        pass

    def ExtrudeFaces(self, faces, direction, spans):
        """ ExtrudeFaces(self: TSplineSurface, faces: IEnumerable[TSplineFace], direction: Vector, spans: int) -> TSplineSurface """
        pass

    def ExtrudeFacesAlongCurve(self, faces, curve, spans):
        """ ExtrudeFacesAlongCurve(self: TSplineSurface, faces: IEnumerable[TSplineFace], curve: Curve, spans: int) -> TSplineSurface """
        pass

    def FillHole(self, edges, fillMethod, keepSubdCreases):
        """ FillHole(self: TSplineSurface, edges: IEnumerable[TSplineEdge], fillMethod: int, keepSubdCreases: bool) -> TSplineSurface """
        pass

    def FlattenVertices(self, vertices, parallelPlane=None):
        """
        FlattenVertices(self: TSplineSurface, vertices: IEnumerable[TSplineVertex], parallelPlane: Plane) -> TSplineSurface
        FlattenVertices(self: TSplineSurface, vertices: IEnumerable[TSplineVertex]) -> TSplineSurface
        """
        pass

    def FlipNormals(self):
        """ FlipNormals(self: TSplineSurface) -> TSplineSurface """
        pass

    @staticmethod
    def ImportFromTSM(*__args):
        """
        ImportFromTSM(file: FileInfo, inSmoothMode: bool) -> Array[TSplineSurface]
        ImportFromTSM(filePath: str, inSmoothMode: bool) -> Array[TSplineSurface]
        """
        pass

    @staticmethod
    def ImportFromTSS(*__args):
        """
        ImportFromTSS(file: FileInfo, inSmoothMode: bool) -> Array[TSplineSurface]
        ImportFromTSS(filePath: str, inSmoothMode: bool) -> Array[TSplineSurface]
        """
        pass

    def Interpolate(self, reverse):
        """ Interpolate(self: TSplineSurface, reverse: bool) -> TSplineSurface """
        pass

    def MakeUniform(self):
        """ MakeUniform(self: TSplineSurface) -> TSplineSurface """
        pass

    def MergeEdges(self, firstGroup, secondGroup, insertCreases):
        """ MergeEdges(self: TSplineSurface, firstGroup: IEnumerable[TSplineEdge], secondGroup: IEnumerable[TSplineEdge], insertCreases: bool) -> TSplineSurface """
        pass

    def MoveVertices(self, vertices, vector, onSurface):
        """ MoveVertices(self: TSplineSurface, vertices: IEnumerable[TSplineVertex], vector: Vector, onSurface: bool) -> TSplineSurface """
        pass

    def PullVertices(self, vertices, geometries, surfacePoints):
        """ PullVertices(self: TSplineSurface, vertices: IEnumerable[TSplineVertex], geometries: IEnumerable[Geometry], surfacePoints: bool) -> TSplineSurface """
        pass

    def RemoveReflections(self):
        """ RemoveReflections(self: TSplineSurface) -> TSplineSurface """
        pass

    def SlideEdges(self, edges, amount, roundness):
        """ SlideEdges(self: TSplineSurface, edges: IEnumerable[TSplineEdge], amount: float, roundness: float) -> TSplineSurface """
        pass

    def Standardize(self):
        """ Standardize(self: TSplineSurface) -> TSplineSurface """
        pass

    def SubdivideFaces(self, faces, exact):
        """ SubdivideFaces(self: TSplineSurface, faces: IEnumerable[TSplineFace], exact: bool) -> TSplineSurface """
        pass

    def Thicken(self, *__args):
        """
        Thicken(self: TSplineSurface, vector: Vector, softEdges: bool) -> TSplineSurface
        Thicken(self: TSplineSurface, distance: float, softEdges: bool) -> TSplineSurface
        """
        pass

    def ToBRep(self, matchTopology):
        """ ToBRep(self: TSplineSurface, matchTopology: bool) -> Array[Topology] """
        pass

    def ToMesh(self, minSegments, tolerance):
        """ ToMesh(self: TSplineSurface, minSegments: int, tolerance: float) -> Mesh """
        pass

    def ToString(self):
        """ ToString(self: TSplineSurface) -> str """
        pass

    def UncreaseEdges(self, edges):
        """ UncreaseEdges(self: TSplineSurface, edges: IEnumerable[TSplineEdge]) -> TSplineSurface """
        pass

    def UncreaseVertices(self, vertices):
        """ UncreaseVertices(self: TSplineSurface, vertices: IEnumerable[TSplineVertex]) -> TSplineSurface """
        pass

    def Unweld(self, *__args):
        """
        Unweld(self: TSplineSurface, vertices: IEnumerable[TSplineVertex]) -> TSplineSurface
        Unweld(self: TSplineSurface, edges: IEnumerable[TSplineEdge]) -> TSplineSurface
        """
        pass

    def WeldCoincidentVertices(self, tolerance):
        """ WeldCoincidentVertices(self: TSplineSurface, tolerance: float) -> TSplineSurface """
        pass

    def WeldVertices(self, *__args):
        """
        WeldVertices(self: TSplineSurface, firstGroup: IEnumerable[TSplineVertex], secondGroup: IEnumerable[TSplineVertex], keepSubdCreases: bool) -> TSplineSurface
        WeldVertices(self: TSplineSurface, vertices: IEnumerable[TSplineVertex], newPosition: Point, keepSubdCreases: bool) -> TSplineSurface
        """
        pass

    IsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsClosed(self: TSplineSurface) -> bool

"""

    IsExtractable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsExtractable(self: TSplineSurface) -> bool

"""

    IsInBoxMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInBoxMode(self: TSplineSurface) -> bool

"""

    IsStandard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsStandard(self: TSplineSurface) -> bool

"""

    IsWaterTight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsWaterTight(self: TSplineSurface) -> bool

"""

    Reflections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reflections(self: TSplineSurface) -> Array[TSplineReflection]

"""


    mConstructor = None


class TSplineUVNFrame(DesignScriptEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: TSplineUVNFrame) -> str """
        pass

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Normal(self: TSplineUVNFrame) -> Vector

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: TSplineUVNFrame) -> Point

"""

    U = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: U(self: TSplineUVNFrame) -> Vector

"""

    V = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: V(self: TSplineUVNFrame) -> Vector

"""


    mConstructor = None


class TSplineVertex(Vertex):
    # no doc
    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def Info(self):
        """ Info(self: TSplineVertex) -> Dictionary[str, object] """
        pass

    def ToString(self):
        """ ToString(self: TSplineVertex) -> str """
        pass

    AdjacentEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdjacentEdges(self: TSplineVertex) -> Array[TSplineEdge]

"""

    AdjacentFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdjacentFaces(self: TSplineVertex) -> Array[TSplineFace]

"""

    FunctionalValence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FunctionalValence(self: TSplineVertex) -> int

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: TSplineVertex) -> int

"""

    IsManifold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsManifold(self: TSplineVertex) -> bool

"""

    IsStarPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsStarPoint(self: TSplineVertex) -> bool

"""

    IsTPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTPoint(self: TSplineVertex) -> bool

"""

    UVNFrame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UVNFrame(self: TSplineVertex) -> TSplineUVNFrame

"""

    Valence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Valence(self: TSplineVertex) -> int

"""


    mConstructor = None


