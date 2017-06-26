class Brep(GeometryBase,IDisposable,ISerializable):
 """ Brep() """
 def AddEdgeCurve(self,curve):
  """ AddEdgeCurve(self: Brep,curve: Curve) -> int """
  pass
 def AddSurface(self,surface):
  """ AddSurface(self: Brep,surface: Surface) -> int """
  pass
 def AddTrimCurve(self,curve):
  """ AddTrimCurve(self: Brep,curve: Curve) -> int """
  pass
 def Append(self,other):
  """ Append(self: Brep,other: Brep) """
  pass
 def Compact(self):
  """ Compact(self: Brep) """
  pass
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 @staticmethod
 def CreateFromBox(*__args):
  """
  CreateFromBox(corners: IEnumerable[Point3d]) -> Brep
  CreateFromBox(box: Box) -> Brep
  CreateFromBox(box: BoundingBox) -> Brep
  """
  pass
 @staticmethod
 def CreateFromCone(cone,capBottom):
  """ CreateFromCone(cone: Cone,capBottom: bool) -> Brep """
  pass
 @staticmethod
 def CreateFromCylinder(cylinder,capBottom,capTop):
  """ CreateFromCylinder(cylinder: Cylinder,capBottom: bool,capTop: bool) -> Brep """
  pass
 @staticmethod
 def CreateFromMesh(mesh,trimmedTriangles):
  """ CreateFromMesh(mesh: Mesh,trimmedTriangles: bool) -> Brep """
  pass
 @staticmethod
 def CreateFromRevSurface(surface,capStart,capEnd):
  """ CreateFromRevSurface(surface: RevSurface,capStart: bool,capEnd: bool) -> Brep """
  pass
 @staticmethod
 def CreateFromSphere(sphere):
  """ CreateFromSphere(sphere: Sphere) -> Brep """
  pass
 @staticmethod
 def CreateFromSurface(surface):
  """ CreateFromSurface(surface: Surface) -> Brep """
  pass
 @staticmethod
 def CreatePlanarBreps(*__args):
  """
  CreatePlanarBreps(inputLoop: Curve) -> Array[Brep]
  CreatePlanarBreps(inputLoops: IEnumerable[Curve]) -> Array[Brep]
  """
  pass
 def CullUnused2dCurves(self):
  """ CullUnused2dCurves(self: Brep) -> bool """
  pass
 def CullUnused3dCurves(self):
  """ CullUnused3dCurves(self: Brep) -> bool """
  pass
 def CullUnusedEdges(self):
  """ CullUnusedEdges(self: Brep) -> bool """
  pass
 def CullUnusedFaces(self):
  """ CullUnusedFaces(self: Brep) -> bool """
  pass
 def CullUnusedLoops(self):
  """ CullUnusedLoops(self: Brep) -> bool """
  pass
 def CullUnusedSurfaces(self):
  """ CullUnusedSurfaces(self: Brep) -> bool """
  pass
 def CullUnusedTrims(self):
  """ CullUnusedTrims(self: Brep) -> bool """
  pass
 def CullUnusedVertices(self):
  """ CullUnusedVertices(self: Brep) -> bool """
  pass
 def Dispose(self):
  """ Dispose(self: CommonObject,disposing: bool) """
  pass
 def Duplicate(self):
  """ Duplicate(self: Brep) -> GeometryBase """
  pass
 def DuplicateBrep(self):
  """ DuplicateBrep(self: Brep) -> Brep """
  pass
 def DuplicateEdgeCurves(self,nakedOnly=None):
  """
  DuplicateEdgeCurves(self: Brep,nakedOnly: bool) -> Array[Curve]
  DuplicateEdgeCurves(self: Brep) -> Array[Curve]
  """
  pass
 def DuplicateNakedEdgeCurves(self,outer,inner):
  """ DuplicateNakedEdgeCurves(self: Brep,outer: bool,inner: bool) -> Array[Curve] """
  pass
 def DuplicateSubBrep(self,faceIndices):
  """ DuplicateSubBrep(self: Brep,faceIndices: IEnumerable[int]) -> Brep """
  pass
 def DuplicateVertices(self):
  """ DuplicateVertices(self: Brep) -> Array[Point3d] """
  pass
 def Flip(self):
  """ Flip(self: Brep) """
  pass
 def IsDuplicate(self,other,tolerance):
  """ IsDuplicate(self: Brep,other: Brep,tolerance: float) -> bool """
  pass
 def IsValidGeometry(self,log):
  """ IsValidGeometry(self: Brep) -> (bool,str) """
  pass
 def IsValidTolerancesAndFlags(self,log):
  """ IsValidTolerancesAndFlags(self: Brep) -> (bool,str) """
  pass
 def IsValidTopology(self,log):
  """ IsValidTopology(self: Brep) -> (bool,str) """
  pass
 def NonConstOperation(self,*args):
  """ NonConstOperation(self: CommonObject) """
  pass
 def OnSwitchToNonConst(self,*args):
  """ OnSwitchToNonConst(self: GeometryBase) """
  pass
 def SetTrimIsoFlags(self):
  """ SetTrimIsoFlags(self: Brep) """
  pass
 def SetVertices(self):
  """ SetVertices(self: Brep) """
  pass
 def Standardize(self):
  """ Standardize(self: Brep) """
  pass
 @staticmethod
 def TryConvertBrep(geometry):
  """ TryConvertBrep(geometry: GeometryBase) -> Brep """
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
 Curves2D=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Curves2D(self: Brep) -> BrepCurveList

"""

 Curves3D=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Curves3D(self: Brep) -> BrepCurveList

"""

 Edges=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Edges(self: Brep) -> BrepEdgeList

"""

 Faces=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Faces(self: Brep) -> BrepFaceList

"""

 IsManifold=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsManifold(self: Brep) -> bool

"""

 IsSolid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsSolid(self: Brep) -> bool

"""

 IsSurface=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsSurface(self: Brep) -> bool

"""

 Loops=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Loops(self: Brep) -> BrepLoopList

"""

 SolidOrientation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SolidOrientation(self: Brep) -> BrepSolidOrientation

"""

 Surfaces=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Surfaces(self: Brep) -> BrepSurfaceList

"""

 Trims=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Trims(self: Brep) -> BrepTrimList

"""

 Vertices=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Vertices(self: Brep) -> BrepVertexList

"""


