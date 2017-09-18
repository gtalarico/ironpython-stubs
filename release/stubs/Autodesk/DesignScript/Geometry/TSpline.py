# encoding: utf-8
# module Autodesk.DesignScript.Geometry.TSpline calls itself TSpline
# from ProtoGeometry, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class TSplineEdge(Edge, IDisposable, IGraphicItem):
    # no doc
    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: DesignScriptEntity) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: DesignScriptEntity) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def Info(self):
        """
        Info(self: TSplineEdge) -> Dictionary[str, object]
        
            A bunch of TSEdge properties: uvnFrame and index, whether TSEdge is on Border, is Manifold or not
        """
        pass

    def ToString(self):
        """ ToString(self: TSplineEdge) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AdjacentFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdjacentFaces(self: TSplineEdge) -> Array[TSplineFace]

"""

    EndVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndVertex(self: TSplineEdge) -> TSplineVertex

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index of the TSEdge

Get: Index(self: TSplineEdge) -> int

"""

    IsBorder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the TSEdge is on border

Get: IsBorder(self: TSplineEdge) -> bool

"""

    IsManifold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the TSEdge is manifold

Get: IsManifold(self: TSplineEdge) -> bool

"""

    StartVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartVertex(self: TSplineEdge) -> TSplineVertex

"""

    UVNFrame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return UVN Frame of the TSEdge (point on the hull, U vector, V vector and normal)

Get: UVNFrame(self: TSplineEdge) -> TSplineUVNFrame

"""


    mConstructor = None


class TSplineFace(Face, IDisposable, IGraphicItem):
    # no doc
    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: DesignScriptEntity) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: DesignScriptEntity) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def Info(self):
        """
        Info(self: TSplineFace) -> Dictionary[str, object]
        
            A bunch of TSplineFace properties: uvnFrame, index, valence and number of sides
        """
        pass

    def ToString(self):
        """ ToString(self: TSplineFace) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edges(self: TSplineFace) -> Array[TSplineEdge]

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index of the TSFace

Get: Index(self: TSplineFace) -> int

"""

    Sides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of parametric sides on the TSFace

Get: Sides(self: TSplineFace) -> int

"""

    UVNFrame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return UVN Frame of the TSplineFace (point on the hull, U vector, V vector and normal)

Get: UVNFrame(self: TSplineFace) -> TSplineUVNFrame

"""

    Valence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of edges or vertices on the TSFace

Get: Valence(self: TSplineFace) -> int

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: TSplineFace) -> Array[TSplineVertex]

"""


    mConstructor = None


class TSplineInitialSymmetry(DesignScriptEntity, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByAxial(xAxis, yAxis, zAxis):
        """
        ByAxial(xAxis: bool, yAxis: bool, zAxis: bool) -> TSplineInitialSymmetry
        
            Create an axial TSplineInitialSymmetry with given symmetry axes.
        """
        pass

    @staticmethod
    def ByRadial(symmetricFaces):
        """
        ByRadial(symmetricFaces: int) -> TSplineInitialSymmetry
        
            Create a radial TSplineInitialSymmetry with given amount of spans per symmetric segment.
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: DesignScriptEntity) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: DesignScriptEntity) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: TSplineInitialSymmetry) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsRadial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether newly created t-spline has radial symmetry.

Get: IsRadial(self: TSplineInitialSymmetry) -> bool

"""

    RadialSymmetryFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of faces in symmetry segment. Only available if t-spline has radial symmetry.

Get: RadialSymmetryFaces(self: TSplineInitialSymmetry) -> int

"""

    XAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether newly created t-spline has symmetry on x axis.

Get: XAxis(self: TSplineInitialSymmetry) -> bool

"""

    YAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether newly created t-spline has symmetry on y axis.

Get: YAxis(self: TSplineInitialSymmetry) -> bool

"""

    ZAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether newly created t-spline has symmetry on z axis.

Get: ZAxis(self: TSplineInitialSymmetry) -> bool

"""


    mConstructor = None


class TSplineReflection(DesignScriptEntity, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByAxial(plane):
        """
        ByAxial(plane: Plane) -> TSplineReflection
        
            Create axial reflection for t-spline symmetry by given plane.
        
            plane: Plane for t-spline axial reflection. Given in World coordinates
            Returns: T-Spline axial reflection
        """
        pass

    @staticmethod
    def ByRadial(plane, segmentsCount, segmentAngle):
        """
        ByRadial(plane: Plane, segmentsCount: int, segmentAngle: float) -> TSplineReflection
        
            Create radial reflection for t-spline symmetry by given plane with given segments count and 
             given angle (in degrees) between each pair of segments.
        
        
            plane: Plane which normal is axis for t-spline radial reflection. Given in World coordinates
            segmentsCount: Number of segments of radial reflection
            segmentAngle: Angle between each pair of segments of radial symmetry (in degrees). If is set to 0 it is 
             defined by (360 / segmentsCount)
        
            Returns: T-Spline radial reflection
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: DesignScriptEntity) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: DesignScriptEntity) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: TSplineReflection) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Axis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Axis of the reflection

Get: Axis(self: TSplineReflection) -> Vector

"""

    IsRadial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the reflection is radial

Get: IsRadial(self: TSplineReflection) -> bool

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Plane of the reflection

Get: Plane(self: TSplineReflection) -> Plane

"""

    SegmentAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Angle between each pair of symmetric segments of radial reflection

Get: SegmentAngle(self: TSplineReflection) -> float

"""

    SegmentsCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of segments of radial reflection

Get: SegmentsCount(self: TSplineReflection) -> int

"""


    mConstructor = None


class TSplineTopology(Topology, IDisposable, IGraphicItem):
    # no doc
    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def DecomposedEdges(self):
        """
        DecomposedEdges(self: TSplineTopology) -> Dictionary[str, Array[TSplineEdge]]
        
            Decomposed Edges differed by type
            Returns: Set of edges
        """
        pass

    def DecomposedFaces(self):
        """
        DecomposedFaces(self: TSplineTopology) -> Dictionary[str, Array[TSplineFace]]
        
            Decomposed Faces differed by type
            Returns: Set of faces
        """
        pass

    def DecomposedVertices(self):
        """
        DecomposedVertices(self: TSplineTopology) -> Dictionary[str, Array[TSplineVertex]]
        
            Decomposed Vertices differed by type
            Returns: Set of vertices
        """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def EdgeByIndex(self, index):
        """
        EdgeByIndex(self: TSplineTopology, index: int) -> TSplineEdge
        
            Return edge at given index
        
            index: Index to get edge at
            Returns: T-Spline Edge
        """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def FaceByIndex(self, index):
        """
        FaceByIndex(self: TSplineTopology, index: int) -> TSplineFace
        
            Return face at given index
        
            index: Index to get face at
            Returns: T-Spline Face
        """
        pass

    def ToString(self):
        """ ToString(self: TSplineTopology) -> str """
        pass

    def VertexByIndex(self, index):
        """
        VertexByIndex(self: TSplineTopology, index: int) -> TSplineVertex
        
            Return vertex at given index
        
            index: Index to get vertex at
            Returns: T-Spline Vertex
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BorderEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Border Edges contained in the T-Spline Surface

Get: BorderEdges(self: TSplineTopology) -> Array[TSplineEdge]

"""

    BorderFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Border Faces contained in the T-Spline Surface

Get: BorderFaces(self: TSplineTopology) -> Array[TSplineFace]

"""

    BorderVertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Border Vertices contained in the T-Spline Surface

Get: BorderVertices(self: TSplineTopology) -> Array[TSplineVertex]

"""

    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edges(self: TSplineTopology) -> Array[TSplineEdge]

"""

    EdgesCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return number of edges in the T-Spline Surface

Get: EdgesCount(self: TSplineTopology) -> int

"""

    Faces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Faces(self: TSplineTopology) -> Array[TSplineFace]

"""

    FacesCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return number of faces in the T-Spline Surface

Get: FacesCount(self: TSplineTopology) -> int

"""

    InnerEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Inner Edges contained in the T-Spline Surface

Get: InnerEdges(self: TSplineTopology) -> Array[TSplineEdge]

"""

    InnerFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Inner Faces contained in the T-Spline Surface

Get: InnerFaces(self: TSplineTopology) -> Array[TSplineFace]

"""

    InnerVertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Inner Vertices contained in the T-Spline Surface

Get: InnerVertices(self: TSplineTopology) -> Array[TSplineVertex]

"""

    NGonFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """N-Gon Faces contained in the T-Spline Surface

Get: NGonFaces(self: TSplineTopology) -> Array[TSplineFace]

"""

    NonManifoldEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Non-Manifold Edges contained in the T-Spline Surface

Get: NonManifoldEdges(self: TSplineTopology) -> Array[TSplineEdge]

"""

    NonManifoldVertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Non-Manifold Vertices contained in the T-Spline Surface

Get: NonManifoldVertices(self: TSplineTopology) -> Array[TSplineVertex]

"""

    RegularFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Regular Faces contained in the T-Spline Surface

Get: RegularFaces(self: TSplineTopology) -> Array[TSplineFace]

"""

    RegularVertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Regular Vertices contained in the T-Spline Surface

Get: RegularVertices(self: TSplineTopology) -> Array[TSplineVertex]

"""

    StarPointVertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Star-Point Vertices contained in the T-Spline Surface

Get: StarPointVertices(self: TSplineTopology) -> Array[TSplineVertex]

"""

    TPointVertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """T-Point Vertices contained in the T-Spline Surface

Get: TPointVertices(self: TSplineTopology) -> Array[TSplineVertex]

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: TSplineTopology) -> Array[TSplineVertex]

"""

    VerticesCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return number of vertices in the T-Spline Surface

Get: VerticesCount(self: TSplineTopology) -> int

"""


    mConstructor = None


class TSplineSurface(TSplineTopology, IDisposable, IGraphicItem):
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
        """
        ByBoxCorners(lowPoint: Point, highPoint: Point, xSpans: int, ySpans: int, zSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        
            Create an T-Spline Box spanning from low Point to high Point.
        
            lowPoint: First corner point
            highPoint: Second corner point
            xSpans: Number spans in width
            ySpans: Number spans in length
            zSpans: Number spans in height
            symmetry: Symmetry options of a T-Spline Surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: T-Spline Cuboid
        """
        pass

    @staticmethod
    def ByBoxLengths(*__args):
        """
        ByBoxLengths(cs: CoordinateSystem, width: float, length: float, height: float, xSpans: int, ySpans: int, zSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        
            Create a T-Spline Box centered and oriented to input CoordinateSystem, with  specified width, 
             length, and height.
        
        
            cs: Box's X-Y plane will be aligned with correspondi X
            width: Width of a box
            length: Length of a box
            height: Height of a box
            xSpans: Number spans in width
            ySpans: Number spans in length
            zSpans: Number spans in height
            symmetry: Symmetry options of a T-Spline Surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: T-Spline Cuboid
        ByBoxLengths(origin: Point, width: float, length: float, height: float, xSpans: int, ySpans: int, zSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        
            Create a T-Spline Box centered at input Point, with specified width, length,  and height.
        
            origin: Center of a box
            width: Width of a box
            length: Length of a box
            height: Height of a box
            xSpans: Number spans in width
            ySpans: Number spans in length
            zSpans: Number spans in height
            symmetry: Symmetry options of a T-Spline Surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: T-Spline Cuboid
        ByBoxLengths(width: float, length: float, height: float, xSpans: int, ySpans: int, zSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        
            Create a T-Spline Box centered at WCS origin, with width, length, and height.
        
            width: Width of a box
            length: Length of a box
            height: Height of a box
            xSpans: Number spans in width
            ySpans: Number spans in length
            zSpans: Number spans in height
            symmetry: Symmetry options of a T-Spline Surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: T-Spline Cuboid
        """
        pass

    @staticmethod
    def ByCombinedTSplineSurfaces(tSplineSurfaces):
        """ ByCombinedTSplineSurfaces(tSplineSurfaces: IEnumerable[TSplineSurface]) -> TSplineSurface """
        pass

    @staticmethod
    def ByConeCoordinateSystemHeightRadii(cs, height, startRadius, endRadius, radiusSpans, heightSpans, symmetry, inSmoothMode):
        """
        ByConeCoordinateSystemHeightRadii(cs: CoordinateSystem, height: float, startRadius: float, endRadius: float, radiusSpans: int, heightSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        
            Create a T-Splines Cone with base Point at CoordinateSystem origin, extending in the direction 
             of CoordinateSystem Z-axis,
                    with its circular base in the CoordinateSystem XY 
             Plane.
        
        
            cs: Cone's center and base will be fit at X-Y plane of this coordinate system
            height: Height of a cone
            startRadius: Start radius of a cone
            endRadius: End radius of a cone
            radiusSpans: Number of spans in circumference
            heightSpans: Number of spans in height
            symmetry: Symmetry options of a T-Spline Surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: Conical T-Spline Surface
        """
        pass

    @staticmethod
    def ByConeCoordinateSystemHeightRadius(cs, height, radius, radiusSpans, heightSpans, symmetry, inSmoothMode):
        """
        ByConeCoordinateSystemHeightRadius(cs: CoordinateSystem, height: float, radius: float, radiusSpans: int, heightSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        
            Create a T-Splines Cone with base Point at CoordinateSystem origin, extending in the direction 
             of CoordinateSystem's Z-axis,
                     with a  circular base in the CoordinateSystem XY 
             Plane.
        
        
            cs: Cone's center and base will be fit at X-Y plane of this coordinate system
            height: Height of a cone
            radius: Radius of a cone
            radiusSpans: Number of spans in circumference
            heightSpans: Number of spans in height
            symmetry: Symmetry options of a T-Spline Surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: Conical T-Spline Surface
        """
        pass

    @staticmethod
    def ByConePointsRadii(startPoint, endPoint, startRadius, endRadius, radiusSpans, heightSpans, symmetry, inSmoothMode):
        """
        ByConePointsRadii(startPoint: Point, endPoint: Point, startRadius: float, endRadius: float, radiusSpans: int, heightSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        
            Create a T-Splines Cone with axis from start Point to end Point, with given radii at start and 
             end. 
                    This object does not have an apex, and is in the shape of a frustum.
        
        
            startPoint: Start point of a cone
            endPoint: End point of a cone
            startRadius: Start radius of a cone
            endRadius: End radius of a cone
            radiusSpans: Number of spans in circumference
            heightSpans: Number of spans in height
            symmetry: Symmetry options of a T-Spline Surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: Conical T-Spline Surface
        """
        pass

    @staticmethod
    def ByConePointsRadius(startPoint, endPoint, radius, radiusSpans, heightSpans, symmetry, inSmoothMode):
        """
        ByConePointsRadius(startPoint: Point, endPoint: Point, radius: float, radiusSpans: int, heightSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        
            Create a T-Splines Cone with given base radius at start Point,
                    extending to an apex 
             at end Point.
        
        
            startPoint: Start point of a cone
            endPoint: End point of a cone
            radius: Radius of a cone's base
            radiusSpans: Number of spans in circumference
            heightSpans: Number of spans in height
            symmetry: Symmetry options of a T-Spline Surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: Conical T-Spline Surface
        """
        pass

    @staticmethod
    def ByCylinderPointsRadius(startPoint, endPoint, radius, radiusSpans, heightSpans, symmetry, inSmoothMode):
        """
        ByCylinderPointsRadius(startPoint: Point, endPoint: Point, radius: float, radiusSpans: int, heightSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        
            Construct a T-Splines Cylinder given the bottom and top center point of the Cylinder.
        
            startPoint: Start point of a cylinder
            endPoint: End point of a cylinder
            radius: Radius of a cylinder
            radiusSpans: Number of spans in circumference
            heightSpans: Number of spans in height
            symmetry: Symmetry options of a T-Spline Surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: Cylindric T-Spline Surface
        """
        pass

    @staticmethod
    def ByCylinderRadiusHeight(cs, radius, height, radiusSpans, heightSpans, symmetry, inSmoothMode):
        """
        ByCylinderRadiusHeight(cs: CoordinateSystem, radius: float, height: float, radiusSpans: int, heightSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        
            Construct a T-Spline Cylinder defined by a parent CoordinateSystem, the radius, and the height 
             of the cylinder
        
        
            cs: Cylinder's center and base will be fit at X-Y plane of this coordinate system
            radius: Radius of a cylinder
            height: Height of a cylinder
            radiusSpans: Number of spans in circumference
            heightSpans: Number of spans in height
            symmetry: Symmetry options of a T-Spline Surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: Cylindric T-Spline Surface
        """
        pass

    @staticmethod
    def ByExtrude(curve, direction, frontDistance, backDistance, frontSpans, backSpans, profileSpans, uniform, inSmoothMode):
        """ ByExtrude(curve: Curve, direction: Vector, frontDistance: float, backDistance: float, frontSpans: int, backSpans: int, profileSpans: int, uniform: bool, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByNurbsSurfaceCurvature(nurbsSurface, inSmoothMode):
        """
        ByNurbsSurfaceCurvature(nurbsSurface: NurbsSurface, inSmoothMode: bool) -> TSplineSurface
        
            Construct T-Spline surface from NURBS Surface using curvature subdivision strategy.
                    
             Input NURBS surface is rebuilt to degree 3. Output T-Spline has span counts and 
                    
             positions in each direction detected automatically depending on curvature.
        
        
            nurbsSurface: Input NURBS surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
        """
        pass

    @staticmethod
    def ByNurbsSurfaceUniform(nurbsSurface, uSpans, vSpans, uUseArcLen, vUseArcLen, inSmoothMode):
        """
        ByNurbsSurfaceUniform(nurbsSurface: NurbsSurface, uSpans: int, vSpans: int, uUseArcLen: bool, vUseArcLen: bool, inSmoothMode: bool) -> TSplineSurface
        
            Construct T-Spline surface from NURBS Surface using uniform strategy. 
                    Input NURBS 
             surface is rebuilt with uniform knots placed at equal parametric or 
                    arc length 
             intervals depending on corresponding useArcLen flag, and approximated by 
                    degree 3 
             NURBS surface. Output T-Spline is divided by given span counts 
                    in u and v 
             directions.
        
        
            nurbsSurface: Input NURBS surface
            uSpans: Required spans number in u direction
            vSpans: Required spans number in v direction
            uUseArcLen: Whether to use arc length or parametric subdivision in u parametric direction
            vUseArcLen: Whether to use arc length or parametric subdivision in v parametric direction
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
        """
        pass

    @staticmethod
    def ByPlaneBestFitThroughPoints(points, minCorner, maxCorner, xSpans, ySpans, symmetry, inSmoothMode):
        """ ByPlaneBestFitThroughPoints(points: IEnumerable[Point], minCorner: Point, maxCorner: Point, xSpans: int, ySpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def ByPlaneLineAndPoint(line, point, minCorner, maxCorner, xSpans, ySpans, symmetry, inSmoothMode):
        """
        ByPlaneLineAndPoint(line: Line, point: Point, minCorner: Point, maxCorner: Point, xSpans: int, ySpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        
            Create the T-Spline Plane containing the input Line and external Point. Point cannot lie on the 
             Line or anywhere on the axis of the Line.
        
        
            line: Line to build a plane
            point: Point to build a plane
            minCorner: 2D point of minimum corner in plane's coordinates
            maxCorner: 2D point of maximum corner in plane's coordinates
            xSpans: Number of spans in width
            ySpans: Number of spans in length
            symmetry: Symmetry options of a T-Spline Surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: Plane T-Spline Surface
        """
        pass

    @staticmethod
    def ByPlaneOriginNormal(origin, normal, minCorner, maxCorner, xSpans, ySpans, symmetry, inSmoothMode):
        """
        ByPlaneOriginNormal(origin: Point, normal: Vector, minCorner: Point, maxCorner: Point, xSpans: int, ySpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        
            Create a T-Spline Plane centered at root Point, with input normal Vector.
        
            origin: Plane's root point
            normal: Plane's normal
            minCorner: 2D point of minimum corner in plane's coordinates
            maxCorner: 2D point of maximum corner in plane's coordinates
            xSpans: Number of spans in width
            ySpans: Number of spans in length
            symmetry: Symmetry options of a T-Spline Surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: Plane T-Spline Surface
        """
        pass

    @staticmethod
    def ByPlaneOriginNormalXAxis(origin, normal, xAxis, minCorner, maxCorner, xSpans, ySpans, symmetry, inSmoothMode):
        """
        ByPlaneOriginNormalXAxis(origin: Point, normal: Vector, xAxis: Vector, minCorner: Point, maxCorner: Point, xSpans: int, ySpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        
            Create an "oriented" T-Spline Plane, positioned at Point origin with Vector normal, but with a 
             specific X-axis orientation. 
                    This has no impact to splitting, intersect, project, 
             etc. operations, it only specifies the orientation of the input CoordinateSystem.
        
        
            origin: Plane's root point
            normal: Plane's normal
            xAxis: Plane's x-axis
            minCorner: 2D point of minimum corner in plane's coordinates
            maxCorner: 2D point of maximum corner in plane's coordinates
            xSpans: Number of spans in width
            ySpans: Number of spans in length
            symmetry: Symmetry options of a T-Spline Surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: Plane T-Spline Surface
        """
        pass

    @staticmethod
    def ByPlaneOriginXAxisYAxis(origin, xAxis, yAxis, minCorner, maxCorner, xSpans, ySpans, symmetry, inSmoothMode):
        """
        ByPlaneOriginXAxisYAxis(origin: Point, xAxis: Vector, yAxis: Vector, minCorner: Point, maxCorner: Point, xSpans: int, ySpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        
            Create a Plane by origin and X, Y axis.
                    The Z axis is the cross product of the two 
             Vectors.
        
        
            origin: Plane's root point
            xAxis: Plane's x-axis
            yAxis: Plane's y-axis
            minCorner: 2D point of minimum corner in plane's coordinates
            maxCorner: 2D point of maximum corner in plane's coordinates
            xSpans: Number of spans in width
            ySpans: Number of spans in length
            symmetry: Symmetry options of a T-Spline Surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: Plane T-Spline Surface
        """
        pass

    @staticmethod
    def ByPlaneThreePoints(p1, p2, p3, minCorner, maxCorner, xSpans, ySpans, symmetry, inSmoothMode):
        """
        ByPlaneThreePoints(p1: Point, p2: Point, p3: Point, minCorner: Point, maxCorner: Point, xSpans: int, ySpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        
            Create a T-Spline Plane containing the three input Points. The Points cannot lie on a straight 
             line
        
        
            p1: First point to build a plane
            p2: Second point to build a plane
            p3: Third point to build a plane
            minCorner: 2D point of minimum corner in plane's coordinates
            maxCorner: 2D point of maximum corner in plane's coordinates
            xSpans: Number of spans in width
            ySpans: Number of spans in length
            symmetry: Symmetry options of a T-Spline Surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: Plane T-Spline Surface
        """
        pass

    @staticmethod
    def ByQuadballCenterRadius(center, radius, spans, symmetry, inSmoothMode):
        """
        ByQuadballCenterRadius(center: Point, radius: float, spans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        
            Create a T-Splines Quadball with given center and radius, aligned with  default World XY plane
        
            center: Quadball center point
            radius: Quadball radius
            spans: Spans number in two dimensions of quadball's sides
            symmetry: Symmetry options of a T-Spline Surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: T-Spline Quadball
        """
        pass

    @staticmethod
    def ByQuadballCoordinateSystemRadius(cs, radius, spans, symmetry, inSmoothMode):
        """
        ByQuadballCoordinateSystemRadius(cs: CoordinateSystem, radius: float, spans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        
            Create a T-Splines Quadball with center at CoordinateSystem origin  and given radius
        
            cs: Local coordinate system
            radius: Quadball radius
            spans: Spans number in two dimensions of quadball's sides
            symmetry: Symmetry options of a T-Spline Surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: T-Spline Quadball
        """
        pass

    @staticmethod
    def ByRevolve(profile, axisOrigin, axisDirection, startAngle, sweepAngle, radialSpans, axialSpans, uniform, symmetry, inSmoothMode):
        """
        ByRevolve(profile: Curve, axisOrigin: Point, axisDirection: Vector, startAngle: float, sweepAngle: float, radialSpans: int, axialSpans: int, uniform: bool, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        
            Create a T-Spline Surface by sweeping the profile Curve around the axis formed
                    by 
             the axis origin and axis direction, starting at start_angle in degrees, 
                    and 
             sweeping by sweep_angle in degrees.
        
        
            profile: Profile curve
            axisOrigin: Rotation center
            axisDirection: Rotation axis
            startAngle: Angle to start rotation from
            sweepAngle: Angle to finish rotation at
            radialSpans: Spans number in radius
            axialSpans: Spans number in height. Automatically defined if 0 or less
            uniform: Use uniform or curvature strategy for spans distribution
            symmetry: Symmetry options of a T-Spline Surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
        """
        pass

    @staticmethod
    def BySphereBestFit(points, radiusSpans, heightSpans, symmetry, inSmoothMode):
        """ BySphereBestFit(points: IEnumerable[Point], radiusSpans: int, heightSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def BySphereCenterPointRadius(centerPoint, radius, radiusSpans, heightSpans, symmetry, inSmoothMode):
        """
        BySphereCenterPointRadius(centerPoint: Point, radius: float, radiusSpans: int, heightSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        
            Create a T-Spline Sphere cetered at the input Point, with given radius.
        
            centerPoint: Center of a sphere
            radius: Radius of a sphere
            radiusSpans: Number of radial spans
            heightSpans: Number of spans in height
            symmetry: Symmetry options of a T-Spline Surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: Spherical T-Spline Surface
        """
        pass

    @staticmethod
    def BySphereFourPoints(points, radiusSpans, heightSpans, symmetry, inSmoothMode):
        """ BySphereFourPoints(points: IEnumerable[Point], radiusSpans: int, heightSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface """
        pass

    @staticmethod
    def BySweep(profile, path, parallel, pathSpans, profileSpans, pathUniform, profileUniform, inSmoothMode):
        """
        BySweep(profile: Curve, path: Curve, parallel: bool, pathSpans: int, profileSpans: int, pathUniform: bool, profileUniform: bool, inSmoothMode: bool) -> TSplineSurface
        
            Construct a T-Spline by sweeping a cross section Curve along a path.
        
            profile: Profile curve
            path: Path curve
            parallel: Is spans should be parallel in path directio
            pathSpans: Spans number in path
            profileSpans: Spans number in profile. Automatically defined if 0 or less
            pathUniform: Use uniform or curvature strategy for spans distribution along path
            profileUniform: Use uniform or curvature strategy for spans distribution along profile
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
        """
        pass

    @staticmethod
    def ByTorusCenterRadii(center, innerRadius, outerRadius, innerRadiusSpans, outerRadiusSpans, symmetry, inSmoothMode):
        """
        ByTorusCenterRadii(center: Point, innerRadius: float, outerRadius: float, innerRadiusSpans: int, outerRadiusSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        
            Create a T-Splines Torus with given center and radii, aligned with  default World XY plane
        
            center: Center of a torus
            innerRadius: Inner radius of a torus
            outerRadius: Outer radius of a torus
            innerRadiusSpans: Number of inner radial spans
            outerRadiusSpans: Number of outer radial spans
            symmetry: Symmetry options of a T-Spline Surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: Toroidal T-Spline Surface
        """
        pass

    @staticmethod
    def ByTorusCoordinateSystemRadii(cs, innerRadius, outerRadius, innerRadiusSpans, outerRadiusSpans, symmetry, inSmoothMode):
        """
        ByTorusCoordinateSystemRadii(cs: CoordinateSystem, innerRadius: float, outerRadius: float, innerRadiusSpans: int, outerRadiusSpans: int, symmetry: TSplineInitialSymmetry, inSmoothMode: bool) -> TSplineSurface
        
            Create a T-Splines Torus with center at CoordinateSystem origin and given radii
        
            cs: Torus will be aligned in the X-Y plane of given coordinate system with center in its origin
            innerRadius: Inner radius of a torus
            outerRadius: Outer radius of a torus
            innerRadiusSpans: Number of inner radial spans
            outerRadiusSpans: Number of outer radial spans
            symmetry: Symmetry options of a T-Spline Surface
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: Toroidal T-Spline Surface
        """
        pass

    def CompressIndexes(self):
        """
        CompressIndexes(self: TSplineSurface) -> TSplineSurface
        
            Compress all topology on the surface and make the indices contiguous. This function maintains 
             the relative order of the indices.
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
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

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def DuplicateFaces(self, faces):
        """ DuplicateFaces(self: TSplineSurface, faces: IEnumerable[TSplineFace]) -> TSplineSurface """
        pass

    def EnableSmoothMode(self, enable):
        """
        EnableSmoothMode(self: TSplineSurface, enable: bool) -> TSplineSurface
        
            Change visualization style of t-spline.
                    Smooth visualization if true passed, box 
             otherwise.
        
        
            enable: Enable or disable smooth visualization
            Returns: t-spline with chosen visualization style
        """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    @staticmethod
    def ExportToTSM(tSplineSurface, filePath):
        """
        ExportToTSM(tSplineSurface: TSplineSurface, filePath: str) -> str
        
            Export given T-Spline surface to T-Spline Mesh file
        
            tSplineSurface: T-Spline surface to export
            filePath: Path to file to save to
            Returns: File path where T-Spline Surface is being saved
        """
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
        """
        FlipNormals(self: TSplineSurface) -> TSplineSurface
        
            Inverts the normals of all faces in the mesh.
            Returns: T-Spline Surface with inverted normals
        """
        pass

    @staticmethod
    def ImportFromTSM(*__args):
        """
        ImportFromTSM(file: FileInfo, inSmoothMode: bool) -> Array[TSplineSurface]
        
            Load a T-Spline Surface from given T-Spline Mesh file
        
            file: File to load from
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: Newly loaded T-Spline surface in list
        ImportFromTSM(filePath: str, inSmoothMode: bool) -> Array[TSplineSurface]
        
            Load a T-Spline Surface from given T-Spline Mesh file
        
            filePath: Path to file to load from
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: Newly loaded T-Spline surface in list
        """
        pass

    @staticmethod
    def ImportFromTSS(*__args):
        """
        ImportFromTSS(file: FileInfo, inSmoothMode: bool) -> Array[TSplineSurface]
        
            Load set of a T-Spline surfaces from given T-Spline Scene file
        
            file: File to load from
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: A set of newly loaded T-Spline Surfaces
        ImportFromTSS(filePath: str, inSmoothMode: bool) -> Array[TSplineSurface]
        
            Load set of a T-Spline surfaces from given T-Spline Scene file
        
            filePath: Path to file to load from
            inSmoothMode: Show T-Spline Surface in box or smooth visualization
            Returns: A set of newly loaded T-Spline Surfaces
        """
        pass

    def Interpolate(self, reverse):
        """
        Interpolate(self: TSplineSurface, reverse: bool) -> TSplineSurface
        
            Forward interpolation moves control points to their parametric locations on the surface. Reverse 
             interpolation generates a point on the surface for each original control point and moves this 
             control point to its corresponding surface point.
        
        
            reverse: Interpolation direction: forward if false, reverse otherwise
            Returns: Interpolated T-Spline in given direction
        """
        pass

    def MakeUniform(self):
        """
        MakeUniform(self: TSplineSurface) -> TSplineSurface
        
            Set all knot intervals uniform.
            Returns: T-Spline Surface with uniform internals
        """
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
        """
        RemoveReflections(self: TSplineSurface) -> TSplineSurface
        
            Remove all reflections from the t-spline
            Returns: T-Spline surface with given reflections removed
        """
        pass

    def SlideEdges(self, edges, amount, roundness):
        """ SlideEdges(self: TSplineSurface, edges: IEnumerable[TSplineEdge], amount: float, roundness: float) -> TSplineSurface """
        pass

    def Standardize(self):
        """
        Standardize(self: TSplineSurface) -> TSplineSurface
        
            Standardize the t-spline to the point where exact insertion
                    can be performed. If it 
             cannot be standardized, exception is thrown
                    with the reason
        
            Returns: Standardized T-Spline Surface
        """
        pass

    def SubdivideFaces(self, faces, exact):
        """ SubdivideFaces(self: TSplineSurface, faces: IEnumerable[TSplineFace], exact: bool) -> TSplineSurface """
        pass

    def Thicken(self, *__args):
        """
        Thicken(self: TSplineSurface, vector: Vector, softEdges: bool) -> TSplineSurface
        
            Thicken TSpline surface by given vector.
        
            vector: Direction to thicken
            softEdges: Determines if resulting edges should be creased
            Returns: Thickened TSpline surface
        Thicken(self: TSplineSurface, distance: float, softEdges: bool) -> TSplineSurface
        
            Thicken TSpline surface by given distance in the direction of its face normals
        
            distance: Distance to thicken
            softEdges: Determines if resulting edges should be creased
            Returns: Thickened TSpline surface
        """
        pass

    def ToBRep(self, matchTopology):
        """
        ToBRep(self: TSplineSurface, matchTopology: bool) -> Array[Topology]
        
            Convert TSpline surface to Solid or Surface depending on shape
        
            matchTopology: Determines should resulted body has the same topology as TSpline has
            Returns: Topology entity (Solid or Surface)
        """
        pass

    def ToMesh(self, minSegments, tolerance):
        """
        ToMesh(self: TSplineSurface, minSegments: int, tolerance: float) -> Mesh
        
            Convert t-spline surface to mesh. Mesh can have both triangles and quads.
        
            minSegments: The minimum number of segments in each direction. At least one segment will always be produced.
            tolerance: Maximum allowed distance from the mesh to the surface. Setting to a zero or a negative value 
             will disable its use
        
            Returns: Mesh entity
        """
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
        """
        WeldCoincidentVertices(self: TSplineSurface, tolerance: float) -> TSplineSurface
        
            Find all coincident vertices and weld them together.
        
            tolerance: Tolerance to seek coincidence within
            Returns: TSpline surface without coincident vertices
        """
        pass

    def WeldVertices(self, *__args):
        """
        WeldVertices(self: TSplineSurface, firstGroup: IEnumerable[TSplineVertex], secondGroup: IEnumerable[TSplineVertex], keepSubdCreases: bool) -> TSplineSurface
        WeldVertices(self: TSplineSurface, vertices: IEnumerable[TSplineVertex], newPosition: Point, keepSubdCreases: bool) -> TSplineSurface
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether t-spline is is open.

Get: IsClosed(self: TSplineSurface) -> bool

"""

    IsExtractable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether t-spline is extractable (Could be displayed in smooth mode)

Get: IsExtractable(self: TSplineSurface) -> bool

"""

    IsInBoxMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether t-spline in box or smooth mode

Get: IsInBoxMode(self: TSplineSurface) -> bool

"""

    IsStandard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Check all guarantees required for standardization to determine
            if the t-spline is standard

Get: IsStandard(self: TSplineSurface) -> bool

"""

    IsWaterTight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """All closed surfaces are watertight, but some watertight surfaces are open.

Get: IsWaterTight(self: TSplineSurface) -> bool

"""

    Reflections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of reflections applied to the t-spline

Get: Reflections(self: TSplineSurface) -> Array[TSplineReflection]

"""


    mConstructor = None


class TSplineUVNFrame(DesignScriptEntity, IDisposable, IGraphicItem):
    # no doc
    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: DesignScriptEntity) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: DesignScriptEntity) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: TSplineUVNFrame) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Normal of the TopologyItem

Get: Normal(self: TSplineUVNFrame) -> Vector

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Point of the TopologyItem on the hull

Get: Position(self: TSplineUVNFrame) -> Point

"""

    U = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """U vector of the TopologyItem

Get: U(self: TSplineUVNFrame) -> Vector

"""

    V = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """V vector of the TopologyItem

Get: V(self: TSplineUVNFrame) -> Vector

"""


    mConstructor = None


class TSplineVertex(Vertex, IDisposable, IGraphicItem):
    # no doc
    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: DesignScriptEntity) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: DesignScriptEntity) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def Info(self):
        """
        Info(self: TSplineVertex) -> Dictionary[str, object]
        
            A bunch of TSVertex properties: uvnFrame, index, valence and functionalValence, whether TSVertex 
             is a StarPoint, TPoint, Manifold or not
        """
        pass

    def ToString(self):
        """ ToString(self: TSplineVertex) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AdjacentEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdjacentEdges(self: TSplineVertex) -> Array[TSplineEdge]

"""

    AdjacentFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdjacentFaces(self: TSplineVertex) -> Array[TSplineFace]

"""

    FunctionalValence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Functional valence of the TSVertex, taking T-points into account

Get: FunctionalValence(self: TSplineVertex) -> int

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index of the TSVertex

Get: Index(self: TSplineVertex) -> int

"""

    IsManifold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the TSVertex is manifold

Get: IsManifold(self: TSplineVertex) -> bool

"""

    IsStarPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the TSVertex is a star point

Get: IsStarPoint(self: TSplineVertex) -> bool

"""

    IsTPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the TSVertex is a T-point

Get: IsTPoint(self: TSplineVertex) -> bool

"""

    UVNFrame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return UVN Frame of the TSVertex (point on the hull, U vector, V vector and normal)

Get: UVNFrame(self: TSplineVertex) -> TSplineUVNFrame

"""

    Valence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of edges or faces on the TSVertex

Get: Valence(self: TSplineVertex) -> int

"""


    mConstructor = None


