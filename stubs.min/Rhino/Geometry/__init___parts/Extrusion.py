class Extrusion(Surface,IDisposable,ISerializable):
 """ Extrusion() """
 def AddInnerProfile(self,innerProfile):
  """ AddInnerProfile(self: Extrusion,innerProfile: Curve) -> bool """
  pass
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 @staticmethod
 def Create(planarCurve,height,cap):
  """ Create(planarCurve: Curve,height: float,cap: bool) -> Extrusion """
  pass
 @staticmethod
 def CreateCylinderExtrusion(cylinder,capBottom,capTop):
  """ CreateCylinderExtrusion(cylinder: Cylinder,capBottom: bool,capTop: bool) -> Extrusion """
  pass
 @staticmethod
 def CreatePipeExtrusion(cylinder,otherRadius,capTop,capBottom):
  """ CreatePipeExtrusion(cylinder: Cylinder,otherRadius: float,capTop: bool,capBottom: bool) -> Extrusion """
  pass
 def Dispose(self):
  """ Dispose(self: CommonObject,disposing: bool) """
  pass
 def GetMesh(self,meshType):
  """ GetMesh(self: Extrusion,meshType: MeshType) -> Mesh """
  pass
 def GetPathPlane(self,s):
  """ GetPathPlane(self: Extrusion,s: float) -> Plane """
  pass
 def GetProfilePlane(self,s):
  """ GetProfilePlane(self: Extrusion,s: float) -> Plane """
  pass
 def GetProfileTransformation(self,s):
  """ GetProfileTransformation(self: Extrusion,s: float) -> Transform """
  pass
 def NonConstOperation(self,*args):
  """ NonConstOperation(self: CommonObject) """
  pass
 def OnSwitchToNonConst(self,*args):
  """ OnSwitchToNonConst(self: GeometryBase) """
  pass
 def PathLineCurve(self):
  """ PathLineCurve(self: Extrusion) -> LineCurve """
  pass
 def Profile3d(self,*__args):
  """
  Profile3d(self: Extrusion,ci: ComponentIndex) -> Curve
  Profile3d(self: Extrusion,profileIndex: int,s: float) -> Curve
  """
  pass
 def ProfileIndex(self,profileParameter):
  """ ProfileIndex(self: Extrusion,profileParameter: float) -> int """
  pass
 def SetOuterProfile(self,outerProfile,cap):
  """ SetOuterProfile(self: Extrusion,outerProfile: Curve,cap: bool) -> bool """
  pass
 def SetPathAndUp(self,a,b,up):
  """ SetPathAndUp(self: Extrusion,a: Point3d,b: Point3d,up: Vector3d) -> bool """
  pass
 def ToBrep(self,splitKinkyFaces=None):
  """ ToBrep(self: Extrusion,splitKinkyFaces: bool) -> Brep """
  pass
 def WallEdge(self,ci):
  """ WallEdge(self: Extrusion,ci: ComponentIndex) -> Curve """
  pass
 def WallSurface(self,ci):
  """ WallSurface(self: Extrusion,ci: ComponentIndex) -> Surface """
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
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  __new__(cls: type)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 CapCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CapCount(self: Extrusion) -> int

"""

 IsCappedAtBottom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsCappedAtBottom(self: Extrusion) -> bool

"""

 IsCappedAtTop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsCappedAtTop(self: Extrusion) -> bool

"""

 IsMiteredAtEnd=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsMiteredAtEnd(self: Extrusion) -> bool

"""

 IsMiteredAtStart=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsMiteredAtStart(self: Extrusion) -> bool

"""

 IsSolid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsSolid(self: Extrusion) -> bool

"""

 MiterPlaneNormalAtEnd=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MiterPlaneNormalAtEnd(self: Extrusion) -> Vector3d

Set: MiterPlaneNormalAtEnd(self: Extrusion)=value
"""

 MiterPlaneNormalAtStart=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MiterPlaneNormalAtStart(self: Extrusion) -> Vector3d

Set: MiterPlaneNormalAtStart(self: Extrusion)=value
"""

 PathEnd=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PathEnd(self: Extrusion) -> Point3d

"""

 PathStart=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PathStart(self: Extrusion) -> Point3d

"""

 PathTangent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PathTangent(self: Extrusion) -> Vector3d

"""

 ProfileCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ProfileCount(self: Extrusion) -> int

"""


