# encoding: utf-8
# module Rhino.Geometry.Collections calls itself Collections
# from Rhino3dmIO, Version=5.1.30000.14, Culture=neutral, PublicKeyToken=null
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class BrepCurveList(object, IEnumerable[Curve], IEnumerable, IRhinoTable[Curve]):
    # no doc
    def Add(self, curve):
        """ Add(self: BrepCurveList, curve: Curve) -> int """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: BrepCurveList) -> IEnumerator[Curve] """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Curve](enumerable: IEnumerable[Curve], value: Curve) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: BrepCurveList) -> int

"""



class BrepEdgeList(object, IEnumerable[BrepEdge], IEnumerable, IRhinoTable[BrepEdge]):
    # no doc
    def Add(self, *__args):
        """
        Add(self: BrepEdgeList, startVertexIndex: int, endVertexIndex: int, curve3dIndex: int, subDomain: Interval, edgeTolerance: float) -> BrepEdge
        Add(self: BrepEdgeList, startVertexIndex: int, endVertexIndex: int, curve3dIndex: int, edgeTolerance: float) -> BrepEdge
        Add(self: BrepEdgeList, startVertex: BrepVertex, endVertex: BrepVertex, curve3dIndex: int, edgeTolerance: float) -> BrepEdge
        Add(self: BrepEdgeList, curve3dIndex: int) -> BrepEdge
        Add(self: BrepEdgeList, startVertex: BrepVertex, endVertex: BrepVertex, curve3dIndex: int, subDomain: Interval, edgeTolerance: float) -> BrepEdge
        """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: BrepEdgeList) -> IEnumerator[BrepEdge] """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BrepEdge](enumerable: IEnumerable[BrepEdge], value: BrepEdge) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: BrepEdgeList) -> int

"""



class BrepFaceList(object, IEnumerable[BrepFace], IEnumerable, IRhinoTable[BrepFace]):
    # no doc
    def Add(self, *__args):
        """
        Add(self: BrepFaceList, surface: Surface) -> BrepFace
        Add(self: BrepFaceList, surfaceIndex: int) -> BrepFace
        """
        pass

    def AddConeFace(self, vertex, edge, revEdge):
        """ AddConeFace(self: BrepFaceList, vertex: BrepVertex, edge: BrepEdge, revEdge: bool) -> BrepFace """
        pass

    def AddRuledFace(self, edgeA, revEdgeA, edgeB, revEdgeB):
        """ AddRuledFace(self: BrepFaceList, edgeA: BrepEdge, revEdgeA: bool, edgeB: BrepEdge, revEdgeB: bool) -> BrepFace """
        pass

    def ExtractFace(self, faceIndex):
        """ ExtractFace(self: BrepFaceList, faceIndex: int) -> Brep """
        pass

    def Flip(self, onlyReversedFaces):
        """ Flip(self: BrepFaceList, onlyReversedFaces: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: BrepFaceList) -> IEnumerator[BrepFace] """
        pass

    def RemoveAt(self, faceIndex):
        """ RemoveAt(self: BrepFaceList, faceIndex: int) """
        pass

    def RemoveSlits(self):
        """ RemoveSlits(self: BrepFaceList) -> bool """
        pass

    def ShrinkFaces(self):
        """ ShrinkFaces(self: BrepFaceList) -> bool """
        pass

    def StandardizeFaceSurface(self, faceIndex):
        """ StandardizeFaceSurface(self: BrepFaceList, faceIndex: int) -> bool """
        pass

    def StandardizeFaceSurfaces(self):
        """ StandardizeFaceSurfaces(self: BrepFaceList) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BrepFace](enumerable: IEnumerable[BrepFace], value: BrepFace) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: BrepFaceList) -> int

"""



class BrepLoopList(object, IEnumerable[BrepLoop], IEnumerable, IRhinoTable[BrepLoop]):
    # no doc
    def Add(self, loopType, face=None):
        """
        Add(self: BrepLoopList, loopType: BrepLoopType, face: BrepFace) -> BrepLoop
        Add(self: BrepLoopList, loopType: BrepLoopType) -> BrepLoop
        """
        pass

    def AddOuterLoop(self, faceIndex):
        """ AddOuterLoop(self: BrepLoopList, faceIndex: int) -> BrepLoop """
        pass

    def AddPlanarFaceLoop(self, faceIndex, loopType, boundaryCurves):
        """ AddPlanarFaceLoop(self: BrepLoopList, faceIndex: int, loopType: BrepLoopType, boundaryCurves: IEnumerable[Curve]) -> BrepLoop """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: BrepLoopList) -> IEnumerator[BrepLoop] """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BrepLoop](enumerable: IEnumerable[BrepLoop], value: BrepLoop) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: BrepLoopList) -> int

"""



class BrepSurfaceList(object, IEnumerable[Surface], IEnumerable, IRhinoTable[Surface]):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: BrepSurfaceList) -> IEnumerator[Surface] """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Surface](enumerable: IEnumerable[Surface], value: Surface) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: BrepSurfaceList) -> int

"""



class BrepTrimList(object, IEnumerable[BrepTrim], IEnumerable, IRhinoTable[BrepTrim]):
    # no doc
    def Add(self, *__args):
        """
        Add(self: BrepTrimList, rev3d: bool, edge: BrepEdge, curve2dIndex: int) -> BrepTrim
        Add(self: BrepTrimList, edge: BrepEdge, rev3d: bool, loop: BrepLoop, curve2dIndex: int) -> BrepTrim
        Add(self: BrepTrimList, curve2dIndex: int) -> BrepTrim
        Add(self: BrepTrimList, rev3d: bool, loop: BrepLoop, curve2dIndex: int) -> BrepTrim
        """
        pass

    def AddCurveOnFace(self, face, edge, rev3d, curve2dIndex):
        """ AddCurveOnFace(self: BrepTrimList, face: BrepFace, edge: BrepEdge, rev3d: bool, curve2dIndex: int) -> BrepTrim """
        pass

    def AddSingularTrim(self, vertex, loop, iso, curve2dIndex):
        """ AddSingularTrim(self: BrepTrimList, vertex: BrepVertex, loop: BrepLoop, iso: IsoStatus, curve2dIndex: int) -> BrepTrim """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: BrepTrimList) -> IEnumerator[BrepTrim] """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BrepTrim](enumerable: IEnumerable[BrepTrim], value: BrepTrim) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: BrepTrimList) -> int

"""



class BrepVertexList(object, IEnumerable[BrepVertex], IEnumerable, IRhinoTable[BrepVertex]):
    # no doc
    def Add(self, point=None, vertexTolerance=None):
        """
        Add(self: BrepVertexList, point: Point3d, vertexTolerance: float) -> BrepVertex
        Add(self: BrepVertexList) -> BrepVertex
        """
        pass

    def AddPointOnFace(self, face, s, t):
        """ AddPointOnFace(self: BrepVertexList, face: BrepFace, s: float, t: float) -> BrepVertex """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: BrepVertexList) -> IEnumerator[BrepVertex] """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BrepVertex](enumerable: IEnumerable[BrepVertex], value: BrepVertex) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: BrepVertexList) -> int

"""



class MeshFaceList(object, IEnumerable[MeshFace], IEnumerable, IRhinoTable[MeshFace]):
    # no doc
    def AddFace(self, *__args):
        """
        AddFace(self: MeshFaceList, vertex1: int, vertex2: int, vertex3: int, vertex4: int) -> int
        AddFace(self: MeshFaceList, vertex1: int, vertex2: int, vertex3: int) -> int
        AddFace(self: MeshFaceList, face: MeshFace) -> int
        """
        pass

    def AddFaces(self, faces):
        """ AddFaces(self: MeshFaceList, faces: IEnumerable[MeshFace]) -> Array[int] """
        pass

    def AdjacentFaces(self, faceIndex):
        """ AdjacentFaces(self: MeshFaceList, faceIndex: int) -> Array[int] """
        pass

    def Clear(self):
        """ Clear(self: MeshFaceList) """
        pass

    def ConvertQuadsToTriangles(self):
        """ ConvertQuadsToTriangles(self: MeshFaceList) -> bool """
        pass

    def ConvertTrianglesToQuads(self, angleToleranceRadians, minimumDiagonalLengthRatio):
        """ ConvertTrianglesToQuads(self: MeshFaceList, angleToleranceRadians: float, minimumDiagonalLengthRatio: float) -> bool """
        pass

    def CullDegenerateFaces(self):
        """ CullDegenerateFaces(self: MeshFaceList) -> int """
        pass

    def DeleteFaces(self, faceIndexes):
        """ DeleteFaces(self: MeshFaceList, faceIndexes: IEnumerable[int]) -> int """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MeshFaceList) -> IEnumerator[MeshFace] """
        pass

    def GetFace(self, index):
        """ GetFace(self: MeshFaceList, index: int) -> MeshFace """
        pass

    def GetFaceBoundingBox(self, faceIndex):
        """ GetFaceBoundingBox(self: MeshFaceList, faceIndex: int) -> BoundingBox """
        pass

    def GetFaceCenter(self, faceIndex):
        """ GetFaceCenter(self: MeshFaceList, faceIndex: int) -> Point3d """
        pass

    def GetFaceVertices(self, faceIndex, a, b, c, d):
        """ GetFaceVertices(self: MeshFaceList, faceIndex: int) -> (bool, Point3f, Point3f, Point3f, Point3f) """
        pass

    def GetTopologicalVertices(self, faceIndex):
        """ GetTopologicalVertices(self: MeshFaceList, faceIndex: int) -> Array[int] """
        pass

    def HasNakedEdges(self, faceIndex):
        """ HasNakedEdges(self: MeshFaceList, faceIndex: int) -> bool """
        pass

    def Insert(self, index, face):
        """ Insert(self: MeshFaceList, index: int, face: MeshFace) """
        pass

    def IsHidden(self, faceIndex):
        """ IsHidden(self: MeshFaceList, faceIndex: int) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MeshFaceList, index: int) """
        pass

    def SetFace(self, index, *__args):
        """
        SetFace(self: MeshFaceList, index: int, vertex1: int, vertex2: int, vertex3: int, vertex4: int) -> bool
        SetFace(self: MeshFaceList, index: int, vertex1: int, vertex2: int, vertex3: int) -> bool
        SetFace(self: MeshFaceList, index: int, face: MeshFace) -> bool
        """
        pass

    def ToIntArray(self, asTriangles):
        """ ToIntArray(self: MeshFaceList, asTriangles: bool) -> Array[int] """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MeshFace](enumerable: IEnumerable[MeshFace], value: MeshFace) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MeshFaceList) -> int

Set: Count(self: MeshFaceList) = value
"""

    QuadCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuadCount(self: MeshFaceList) -> int

"""

    TriangleCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TriangleCount(self: MeshFaceList) -> int

"""



class MeshFaceNormalList(object, IEnumerable[Vector3f], IEnumerable, IRhinoTable[Vector3f]):
    # no doc
    def AddFaceNormal(self, *__args):
        """
        AddFaceNormal(self: MeshFaceNormalList, normal: Vector3d) -> int
        AddFaceNormal(self: MeshFaceNormalList, normal: Vector3f) -> int
        AddFaceNormal(self: MeshFaceNormalList, x: Single, y: Single, z: Single) -> int
        AddFaceNormal(self: MeshFaceNormalList, x: float, y: float, z: float) -> int
        """
        pass

    def Clear(self):
        """ Clear(self: MeshFaceNormalList) """
        pass

    def ComputeFaceNormals(self):
        """ ComputeFaceNormals(self: MeshFaceNormalList) -> bool """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MeshFaceNormalList) -> IEnumerator[Vector3f] """
        pass

    def SetFaceNormal(self, index, *__args):
        """
        SetFaceNormal(self: MeshFaceNormalList, index: int, normal: Vector3d) -> bool
        SetFaceNormal(self: MeshFaceNormalList, index: int, normal: Vector3f) -> bool
        SetFaceNormal(self: MeshFaceNormalList, index: int, x: Single, y: Single, z: Single) -> bool
        SetFaceNormal(self: MeshFaceNormalList, index: int, x: float, y: float, z: float) -> bool
        """
        pass

    def UnitizeFaceNormals(self):
        """ UnitizeFaceNormals(self: MeshFaceNormalList) -> bool """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Vector3f](enumerable: IEnumerable[Vector3f], value: Vector3f) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MeshFaceNormalList) -> int

Set: Count(self: MeshFaceNormalList) = value
"""



class MeshTextureCoordinateList(object, IEnumerable[Point2f], IEnumerable, IRhinoTable[Point2f]):
    # no doc
    def Add(self, *__args):
        """
        Add(self: MeshTextureCoordinateList, tc: Point2f) -> int
        Add(self: MeshTextureCoordinateList, tc: Point3d) -> int
        Add(self: MeshTextureCoordinateList, s: Single, t: Single) -> int
        Add(self: MeshTextureCoordinateList, s: float, t: float) -> int
        """
        pass

    def AddRange(self, textureCoordinates):
        """ AddRange(self: MeshTextureCoordinateList, textureCoordinates: Array[Point2f]) -> bool """
        pass

    def Clear(self):
        """ Clear(self: MeshTextureCoordinateList) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MeshTextureCoordinateList) -> IEnumerator[Point2f] """
        pass

    def NormalizeTextureCoordinates(self):
        """ NormalizeTextureCoordinates(self: MeshTextureCoordinateList) -> bool """
        pass

    def ReverseTextureCoordinates(self, direction):
        """ ReverseTextureCoordinates(self: MeshTextureCoordinateList, direction: int) -> bool """
        pass

    def SetTextureCoordinate(self, index, *__args):
        """
        SetTextureCoordinate(self: MeshTextureCoordinateList, index: int, tc: Point2f) -> bool
        SetTextureCoordinate(self: MeshTextureCoordinateList, index: int, tc: Point3f) -> bool
        SetTextureCoordinate(self: MeshTextureCoordinateList, index: int, s: Single, t: Single) -> bool
        SetTextureCoordinate(self: MeshTextureCoordinateList, index: int, s: float, t: float) -> bool
        """
        pass

    def SetTextureCoordinates(self, *__args):
        """
        SetTextureCoordinates(self: MeshTextureCoordinateList, mapping: TextureMapping) -> bool
        SetTextureCoordinates(self: MeshTextureCoordinateList, textureCoordinates: Array[Point2f]) -> bool
        """
        pass

    def TransposeTextureCoordinates(self):
        """ TransposeTextureCoordinates(self: MeshTextureCoordinateList) -> bool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Point2f](enumerable: IEnumerable[Point2f], value: Point2f) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MeshTextureCoordinateList) -> int

Set: Count(self: MeshTextureCoordinateList) = value
"""



class MeshTopologyEdgeList(object):
    # no doc
    def CollapseEdge(self, topologyEdgeIndex):
        """ CollapseEdge(self: MeshTopologyEdgeList, topologyEdgeIndex: int) -> bool """
        pass

    def EdgeLine(self, topologyEdgeIndex):
        """ EdgeLine(self: MeshTopologyEdgeList, topologyEdgeIndex: int) -> Line """
        pass

    def GetConnectedFaces(self, topologyEdgeIndex, faceOrientationMatchesEdgeDirection=None):
        """
        GetConnectedFaces(self: MeshTopologyEdgeList, topologyEdgeIndex: int) -> (Array[int], Array[bool])
        GetConnectedFaces(self: MeshTopologyEdgeList, topologyEdgeIndex: int) -> Array[int]
        """
        pass

    def GetEdgeIndex(self, topologyVertex1, topologyVertex2):
        """ GetEdgeIndex(self: MeshTopologyEdgeList, topologyVertex1: int, topologyVertex2: int) -> int """
        pass

    def GetEdgesForFace(self, faceIndex, sameOrientation=None):
        """
        GetEdgesForFace(self: MeshTopologyEdgeList, faceIndex: int) -> (Array[int], Array[bool])
        GetEdgesForFace(self: MeshTopologyEdgeList, faceIndex: int) -> Array[int]
        """
        pass

    def GetTopologyVertices(self, topologyEdgeIndex):
        """ GetTopologyVertices(self: MeshTopologyEdgeList, topologyEdgeIndex: int) -> IndexPair """
        pass

    def IsHidden(self, topologyEdgeIndex):
        """ IsHidden(self: MeshTopologyEdgeList, topologyEdgeIndex: int) -> bool """
        pass

    def IsSwappableEdge(self, topologyEdgeIndex):
        """ IsSwappableEdge(self: MeshTopologyEdgeList, topologyEdgeIndex: int) -> bool """
        pass

    def SwapEdge(self, topologyEdgeIndex):
        """ SwapEdge(self: MeshTopologyEdgeList, topologyEdgeIndex: int) -> bool """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MeshTopologyEdgeList) -> int

"""



class MeshTopologyVertexList(object, IEnumerable[Point3f], IEnumerable, IRhinoTable[Point3f]):
    # no doc
    def ConnectedFaces(self, topologyVertexIndex):
        """ ConnectedFaces(self: MeshTopologyVertexList, topologyVertexIndex: int) -> Array[int] """
        pass

    def ConnectedTopologyVertices(self, topologyVertexIndex, sorted=None):
        """
        ConnectedTopologyVertices(self: MeshTopologyVertexList, topologyVertexIndex: int, sorted: bool) -> Array[int]
        ConnectedTopologyVertices(self: MeshTopologyVertexList, topologyVertexIndex: int) -> Array[int]
        """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MeshTopologyVertexList) -> IEnumerator[Point3f] """
        pass

    def IndicesFromFace(self, faceIndex):
        """ IndicesFromFace(self: MeshTopologyVertexList, faceIndex: int) -> Array[int] """
        pass

    def IsHidden(self, topologyVertexIndex):
        """ IsHidden(self: MeshTopologyVertexList, topologyVertexIndex: int) -> bool """
        pass

    def MeshVertexIndices(self, topologyVertexIndex):
        """ MeshVertexIndices(self: MeshTopologyVertexList, topologyVertexIndex: int) -> Array[int] """
        pass

    def SortEdges(self, topologyVertexIndex=None):
        """
        SortEdges(self: MeshTopologyVertexList, topologyVertexIndex: int) -> bool
        SortEdges(self: MeshTopologyVertexList) -> bool
        """
        pass

    def TopologyVertexIndex(self, vertexIndex):
        """ TopologyVertexIndex(self: MeshTopologyVertexList, vertexIndex: int) -> int """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Point3f](enumerable: IEnumerable[Point3f], value: Point3f) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MeshTopologyVertexList) -> int

"""



class MeshVertexColorList(object, IEnumerable[Color], IEnumerable, IRhinoTable[Color]):
    # no doc
    def Add(self, *__args):
        """
        Add(self: MeshVertexColorList, color: Color) -> int
        Add(self: MeshVertexColorList, red: int, green: int, blue: int) -> int
        """
        pass

    def AppendColors(self, colors):
        """ AppendColors(self: MeshVertexColorList, colors: Array[Color]) -> bool """
        pass

    def Clear(self):
        """ Clear(self: MeshVertexColorList) """
        pass

    def CreateMonotoneMesh(self, baseColor):
        """ CreateMonotoneMesh(self: MeshVertexColorList, baseColor: Color) -> bool """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MeshVertexColorList) -> IEnumerator[Color] """
        pass

    def SetColor(self, *__args):
        """
        SetColor(self: MeshVertexColorList, face: MeshFace, color: Color) -> bool
        SetColor(self: MeshVertexColorList, index: int, color: Color) -> bool
        SetColor(self: MeshVertexColorList, index: int, red: int, green: int, blue: int) -> bool
        """
        pass

    def SetColors(self, colors):
        """ SetColors(self: MeshVertexColorList, colors: Array[Color]) -> bool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Color](enumerable: IEnumerable[Color], value: Color) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MeshVertexColorList) -> int

Set: Count(self: MeshVertexColorList) = value
"""

    Tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tag(self: MeshVertexColorList) -> MappingTag

Set: Tag(self: MeshVertexColorList) = value
"""



class MeshVertexList(object, IEnumerable[Point3f], IEnumerable, IRhinoTable[Point3f]):
    # no doc
    def Add(self, *__args):
        """
        Add(self: MeshVertexList, vertex: Point3f) -> int
        Add(self: MeshVertexList, vertex: Point3d) -> int
        Add(self: MeshVertexList, x: Single, y: Single, z: Single) -> int
        Add(self: MeshVertexList, x: float, y: float, z: float) -> int
        """
        pass

    def AddVertices(self, vertices):
        """ AddVertices(self: MeshVertexList, vertices: IEnumerable[Point3f])AddVertices(self: MeshVertexList, vertices: IEnumerable[Point3d]) """
        pass

    def Clear(self):
        """ Clear(self: MeshVertexList) """
        pass

    def CombineIdentical(self, ignoreNormals, ignoreAdditional):
        """ CombineIdentical(self: MeshVertexList, ignoreNormals: bool, ignoreAdditional: bool) -> bool """
        pass

    def CullUnused(self):
        """ CullUnused(self: MeshVertexList) -> int """
        pass

    def GetConnectedVertices(self, vertexIndex):
        """ GetConnectedVertices(self: MeshVertexList, vertexIndex: int) -> Array[int] """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MeshVertexList) -> IEnumerator[Point3f] """
        pass

    def GetTopologicalIndenticalVertices(self, vertexIndex):
        """ GetTopologicalIndenticalVertices(self: MeshVertexList, vertexIndex: int) -> Array[int] """
        pass

    def GetVertexFaces(self, vertexIndex):
        """ GetVertexFaces(self: MeshVertexList, vertexIndex: int) -> Array[int] """
        pass

    def Hide(self, vertexIndex):
        """ Hide(self: MeshVertexList, vertexIndex: int) """
        pass

    def HideAll(self):
        """ HideAll(self: MeshVertexList) """
        pass

    def IsHidden(self, vertexIndex):
        """ IsHidden(self: MeshVertexList, vertexIndex: int) -> bool """
        pass

    def Remove(self, *__args):
        """
        Remove(self: MeshVertexList, indices: IEnumerable[int], shrinkFaces: bool) -> bool
        Remove(self: MeshVertexList, index: int, shrinkFaces: bool) -> bool
        """
        pass

    def SetVertex(self, index, *__args):
        """
        SetVertex(self: MeshVertexList, index: int, vertex: Point3f) -> bool
        SetVertex(self: MeshVertexList, index: int, vertex: Point3d) -> bool
        SetVertex(self: MeshVertexList, index: int, x: Single, y: Single, z: Single) -> bool
        SetVertex(self: MeshVertexList, index: int, x: float, y: float, z: float) -> bool
        """
        pass

    def Show(self, vertexIndex):
        """ Show(self: MeshVertexList, vertexIndex: int) """
        pass

    def ShowAll(self):
        """ ShowAll(self: MeshVertexList) """
        pass

    def ToFloatArray(self):
        """ ToFloatArray(self: MeshVertexList) -> Array[Single] """
        pass

    def ToPoint3dArray(self):
        """ ToPoint3dArray(self: MeshVertexList) -> Array[Point3d] """
        pass

    def ToPoint3fArray(self):
        """ ToPoint3fArray(self: MeshVertexList) -> Array[Point3f] """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Point3f](enumerable: IEnumerable[Point3f], value: Point3f) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MeshVertexList) -> int

Set: Count(self: MeshVertexList) = value
"""



class MeshVertexNormalList(object, IEnumerable[Vector3f], IEnumerable, IRhinoTable[Vector3f]):
    # no doc
    def Add(self, *__args):
        """
        Add(self: MeshVertexNormalList, normal: Vector3f) -> int
        Add(self: MeshVertexNormalList, normal: Vector3d) -> int
        Add(self: MeshVertexNormalList, x: Single, y: Single, z: Single) -> int
        Add(self: MeshVertexNormalList, x: float, y: float, z: float) -> int
        """
        pass

    def AddRange(self, normals):
        """ AddRange(self: MeshVertexNormalList, normals: Array[Vector3f]) -> bool """
        pass

    def Clear(self):
        """ Clear(self: MeshVertexNormalList) """
        pass

    def ComputeNormals(self):
        """ ComputeNormals(self: MeshVertexNormalList) -> bool """
        pass

    def Flip(self):
        """ Flip(self: MeshVertexNormalList) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MeshVertexNormalList) -> IEnumerator[Vector3f] """
        pass

    def SetNormal(self, index, *__args):
        """
        SetNormal(self: MeshVertexNormalList, index: int, normal: Vector3f) -> bool
        SetNormal(self: MeshVertexNormalList, index: int, normal: Vector3d) -> bool
        SetNormal(self: MeshVertexNormalList, index: int, x: Single, y: Single, z: Single) -> bool
        SetNormal(self: MeshVertexNormalList, index: int, x: float, y: float, z: float) -> bool
        """
        pass

    def SetNormals(self, normals):
        """ SetNormals(self: MeshVertexNormalList, normals: Array[Vector3f]) -> bool """
        pass

    def UnitizeNormals(self):
        """ UnitizeNormals(self: MeshVertexNormalList) -> bool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Vector3f](enumerable: IEnumerable[Vector3f], value: Vector3f) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MeshVertexNormalList) -> int

Set: Count(self: MeshVertexNormalList) = value
"""



class NurbsCurveKnotList(object, IEnumerable[float], IEnumerable, IRhinoTable[float], IEpsilonComparable[NurbsCurveKnotList]):
    # no doc
    def ClampEnd(self, end):
        """ ClampEnd(self: NurbsCurveKnotList, end: CurveEnd) -> bool """
        pass

    def CreatePeriodicKnots(self, knotSpacing):
        """ CreatePeriodicKnots(self: NurbsCurveKnotList, knotSpacing: float) -> bool """
        pass

    def CreateUniformKnots(self, knotSpacing):
        """ CreateUniformKnots(self: NurbsCurveKnotList, knotSpacing: float) -> bool """
        pass

    def EnsurePrivateCopy(self):
        """ EnsurePrivateCopy(self: NurbsCurveKnotList) """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: NurbsCurveKnotList, other: NurbsCurveKnotList, epsilon: float) -> bool """
        pass

    def InsertKnot(self, value, multiplicity=None):
        """
        InsertKnot(self: NurbsCurveKnotList, value: float, multiplicity: int) -> bool
        InsertKnot(self: NurbsCurveKnotList, value: float) -> bool
        """
        pass

    def KnotMultiplicity(self, index):
        """ KnotMultiplicity(self: NurbsCurveKnotList, index: int) -> int """
        pass

    def SuperfluousKnot(self, start):
        """ SuperfluousKnot(self: NurbsCurveKnotList, start: bool) -> float """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[float](enumerable: IEnumerable[float], value: float) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: NurbsCurveKnotList) -> int

"""

    IsClampedEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsClampedEnd(self: NurbsCurveKnotList) -> bool

"""

    IsClampedStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsClampedStart(self: NurbsCurveKnotList) -> bool

"""



class NurbsCurvePointList(object, IEnumerable[ControlPoint], IEnumerable, IRhinoTable[ControlPoint], IEpsilonComparable[NurbsCurvePointList]):
    # no doc
    def ChangeEndWeights(self, w0, w1):
        """ ChangeEndWeights(self: NurbsCurvePointList, w0: float, w1: float) -> bool """
        pass

    def ControlPolygon(self):
        """ ControlPolygon(self: NurbsCurvePointList) -> Polyline """
        pass

    def EnsurePrivateCopy(self):
        """ EnsurePrivateCopy(self: NurbsCurvePointList) """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: NurbsCurvePointList, other: NurbsCurvePointList, epsilon: float) -> bool """
        pass

    def MakeNonRational(self):
        """ MakeNonRational(self: NurbsCurvePointList) -> bool """
        pass

    def MakeRational(self):
        """ MakeRational(self: NurbsCurvePointList) -> bool """
        pass

    def SetPoint(self, index, *__args):
        """
        SetPoint(self: NurbsCurvePointList, index: int, point: Point4d) -> bool
        SetPoint(self: NurbsCurvePointList, index: int, point: Point3d) -> bool
        SetPoint(self: NurbsCurvePointList, index: int, x: float, y: float, z: float, weight: float) -> bool
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ControlPoint](enumerable: IEnumerable[ControlPoint], value: ControlPoint) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    ControlPolygonLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ControlPolygonLength(self: NurbsCurvePointList) -> float

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: NurbsCurvePointList) -> int

"""



class NurbsSurfaceKnotList(object, IEnumerable[float], IEnumerable, IRhinoTable[float], IEpsilonComparable[NurbsSurfaceKnotList]):
    # no doc
    def CreatePeriodicKnots(self, knotSpacing):
        """ CreatePeriodicKnots(self: NurbsSurfaceKnotList, knotSpacing: float) -> bool """
        pass

    def CreateUniformKnots(self, knotSpacing):
        """ CreateUniformKnots(self: NurbsSurfaceKnotList, knotSpacing: float) -> bool """
        pass

    def EnsurePrivateCopy(self):
        """ EnsurePrivateCopy(self: NurbsSurfaceKnotList) """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: NurbsSurfaceKnotList, other: NurbsSurfaceKnotList, epsilon: float) -> bool """
        pass

    def InsertKnot(self, value, multiplicity=None):
        """
        InsertKnot(self: NurbsSurfaceKnotList, value: float, multiplicity: int) -> bool
        InsertKnot(self: NurbsSurfaceKnotList, value: float) -> bool
        """
        pass

    def KnotMultiplicity(self, index):
        """ KnotMultiplicity(self: NurbsSurfaceKnotList, index: int) -> int """
        pass

    def SuperfluousKnot(self, start):
        """ SuperfluousKnot(self: NurbsSurfaceKnotList, start: bool) -> float """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[float](enumerable: IEnumerable[float], value: float) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    ClampedAtEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClampedAtEnd(self: NurbsSurfaceKnotList) -> bool

"""

    ClampedAtStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClampedAtStart(self: NurbsSurfaceKnotList) -> bool

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: NurbsSurfaceKnotList) -> int

"""



class NurbsSurfacePointList(object, IEnumerable[ControlPoint], IEnumerable, IEpsilonComparable[NurbsSurfacePointList]):
    # no doc
    def EnsurePrivateCopy(self):
        """ EnsurePrivateCopy(self: NurbsSurfacePointList) """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: NurbsSurfacePointList, other: NurbsSurfacePointList, epsilon: float) -> bool """
        pass

    def GetControlPoint(self, u, v):
        """ GetControlPoint(self: NurbsSurfacePointList, u: int, v: int) -> ControlPoint """
        pass

    def GetGrevillePoint(self, u, v):
        """ GetGrevillePoint(self: NurbsSurfacePointList, u: int, v: int) -> Point2d """
        pass

    def SetControlPoint(self, u, v, cp):
        """
        SetControlPoint(self: NurbsSurfacePointList, u: int, v: int, cp: ControlPoint) -> bool
        SetControlPoint(self: NurbsSurfacePointList, u: int, v: int, cp: Point3d) -> bool
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ControlPoint](enumerable: IEnumerable[ControlPoint], value: ControlPoint) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CountU = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CountU(self: NurbsSurfacePointList) -> int

"""

    CountV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CountV(self: NurbsSurfacePointList) -> int

"""



