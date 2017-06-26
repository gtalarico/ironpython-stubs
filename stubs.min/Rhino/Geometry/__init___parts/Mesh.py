class Mesh(GeometryBase,IDisposable,ISerializable):
 """ Mesh() """
 def Append(self,other):
  """ Append(self: Mesh,other: Mesh) """
  pass
 def ClearTextureData(self):
  """ ClearTextureData(self: Mesh) """
  pass
 def Compact(self):
  """ Compact(self: Mesh) -> bool """
  pass
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 def CopyFrom(self,other):
  """ CopyFrom(self: Mesh,other: Mesh) """
  pass
 def CreatePartitions(self,maximumVertexCount,maximumTriangleCount):
  """ CreatePartitions(self: Mesh,maximumVertexCount: int,maximumTriangleCount: int) -> bool """
  pass
 def Dispose(self):
  """ Dispose(self: CommonObject,disposing: bool) """
  pass
 def Duplicate(self):
  """ Duplicate(self: Mesh) -> GeometryBase """
  pass
 def DuplicateMesh(self):
  """ DuplicateMesh(self: Mesh) -> Mesh """
  pass
 def EvaluateMeshGeometry(self,surface):
  """ EvaluateMeshGeometry(self: Mesh,surface: Surface) -> bool """
  pass
 def Flip(self,vertexNormals,faceNormals,faceOrientation):
  """ Flip(self: Mesh,vertexNormals: bool,faceNormals: bool,faceOrientation: bool) """
  pass
 def GetCachedTextureCoordinates(self,textureMappingId):
  """ GetCachedTextureCoordinates(self: Mesh,textureMappingId: Guid) -> CachedTextureCoordinates """
  pass
 def GetNakedEdgePointStatus(self):
  """ GetNakedEdgePointStatus(self: Mesh) -> Array[bool] """
  pass
 def GetPartition(self,which):
  """ GetPartition(self: Mesh,which: int) -> MeshPart """
  pass
 def IsManifold(self,topologicalTest,isOriented,hasBoundary):
  """ IsManifold(self: Mesh,topologicalTest: bool) -> (bool,bool,bool) """
  pass
 def IsPointInside(self,point,tolerance,strictlyIn):
  """ IsPointInside(self: Mesh,point: Point3d,tolerance: float,strictlyIn: bool) -> bool """
  pass
 def NonConstOperation(self,*args):
  """ NonConstOperation(self: CommonObject) """
  pass
 def OnSwitchToNonConst(self,*args):
  """ OnSwitchToNonConst(self: Mesh) """
  pass
 def SetCachedTextureCoordinates(self,tm,xf):
  """ SetCachedTextureCoordinates(self: Mesh,tm: TextureMapping,xf: Transform) -> Transform """
  pass
 def SolidOrientation(self):
  """ SolidOrientation(self: Mesh) -> int """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self):
  """
  __new__(cls: type)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 DisjointMeshCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DisjointMeshCount(self: Mesh) -> int

"""

 FaceNormals=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FaceNormals(self: Mesh) -> MeshFaceNormalList

"""

 Faces=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Faces(self: Mesh) -> MeshFaceList

"""

 HasCachedTextureCoordinates=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasCachedTextureCoordinates(self: Mesh) -> bool

"""

 IsClosed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsClosed(self: Mesh) -> bool

"""

 Normals=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Normals(self: Mesh) -> MeshVertexNormalList

"""

 PartitionCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PartitionCount(self: Mesh) -> int

"""

 TextureCoordinates=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TextureCoordinates(self: Mesh) -> MeshTextureCoordinateList

"""

 TopologyEdges=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TopologyEdges(self: Mesh) -> MeshTopologyEdgeList

"""

 TopologyVertices=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TopologyVertices(self: Mesh) -> MeshTopologyVertexList

"""

 VertexColors=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: VertexColors(self: Mesh) -> MeshVertexColorList

"""

 Vertices=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Vertices(self: Mesh) -> MeshVertexList

"""


