class Mesh(GeometryBase, IDisposable, ISerializable):
    """ Mesh() """
    def Append(self, other):
        """ Append(self: Mesh, other: Mesh) """
        pass

    def ClearTextureData(self):
        """ ClearTextureData(self: Mesh) """
        pass

    def Compact(self):
        """ Compact(self: Mesh) -> bool """
        pass

    def ConstructConstObject(self, *args): #cannot find CLR method
        """ ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int) """
        pass

    def CopyFrom(self, other):
        """ CopyFrom(self: Mesh, other: Mesh) """
        pass

    def CreatePartitions(self, maximumVertexCount, maximumTriangleCount):
        """ CreatePartitions(self: Mesh, maximumVertexCount: int, maximumTriangleCount: int) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def Duplicate(self):
        """ Duplicate(self: Mesh) -> GeometryBase """
        pass

    def DuplicateMesh(self):
        """ DuplicateMesh(self: Mesh) -> Mesh """
        pass

    def EvaluateMeshGeometry(self, surface):
        """ EvaluateMeshGeometry(self: Mesh, surface: Surface) -> bool """
        pass

    def Flip(self, vertexNormals, faceNormals, faceOrientation):
        """ Flip(self: Mesh, vertexNormals: bool, faceNormals: bool, faceOrientation: bool) """
        pass

    def GetCachedTextureCoordinates(self, textureMappingId):
        """ GetCachedTextureCoordinates(self: Mesh, textureMappingId: Guid) -> CachedTextureCoordinates """
        pass

    def GetNakedEdgePointStatus(self):
        """ GetNakedEdgePointStatus(self: Mesh) -> Array[bool] """
        pass

    def GetPartition(self, which):
        """ GetPartition(self: Mesh, which: int) -> MeshPart """
        pass

    def IsManifold(self, topologicalTest, isOriented, hasBoundary):
        """ IsManifold(self: Mesh, topologicalTest: bool) -> (bool, bool, bool) """
        pass

    def IsPointInside(self, point, tolerance, strictlyIn):
        """ IsPointInside(self: Mesh, point: Point3d, tolerance: float, strictlyIn: bool) -> bool """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """ NonConstOperation(self: CommonObject) """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """ OnSwitchToNonConst(self: Mesh) """
        pass

    def SetCachedTextureCoordinates(self, tm, xf):
        """ SetCachedTextureCoordinates(self: Mesh, tm: TextureMapping, xf: Transform) -> Transform """
        pass

    def SolidOrientation(self):
        """ SolidOrientation(self: Mesh) -> int """
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

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    DisjointMeshCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisjointMeshCount(self: Mesh) -> int

"""

    FaceNormals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FaceNormals(self: Mesh) -> MeshFaceNormalList

"""

    Faces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Faces(self: Mesh) -> MeshFaceList

"""

    HasCachedTextureCoordinates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasCachedTextureCoordinates(self: Mesh) -> bool

"""

    IsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsClosed(self: Mesh) -> bool

"""

    Normals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Normals(self: Mesh) -> MeshVertexNormalList

"""

    PartitionCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartitionCount(self: Mesh) -> int

"""

    TextureCoordinates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextureCoordinates(self: Mesh) -> MeshTextureCoordinateList

"""

    TopologyEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TopologyEdges(self: Mesh) -> MeshTopologyEdgeList

"""

    TopologyVertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TopologyVertices(self: Mesh) -> MeshTopologyVertexList

"""

    VertexColors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VertexColors(self: Mesh) -> MeshVertexColorList

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: Mesh) -> MeshVertexList

"""


