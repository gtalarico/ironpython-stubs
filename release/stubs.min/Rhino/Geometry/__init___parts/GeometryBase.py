class GeometryBase(CommonObject,IDisposable,ISerializable):
 # no doc
 def ComponentIndex(self):
  """ ComponentIndex(self: GeometryBase) -> ComponentIndex """
  pass
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 def Dispose(self):
  """ Dispose(self: CommonObject,disposing: bool) """
  pass
 def Duplicate(self):
  """ Duplicate(self: GeometryBase) -> GeometryBase """
  pass
 def DuplicateShallow(self):
  """ DuplicateShallow(self: GeometryBase) -> GeometryBase """
  pass
 def GetBoundingBox(self,*__args):
  """
  GetBoundingBox(self: GeometryBase,plane: Plane) -> BoundingBox
  GetBoundingBox(self: GeometryBase,plane: Plane) -> (BoundingBox,Box)
  GetBoundingBox(self: GeometryBase,accurate: bool) -> BoundingBox
  GetBoundingBox(self: GeometryBase,xform: Transform) -> BoundingBox
  """
  pass
 def GetUserString(self,key):
  """ GetUserString(self: GeometryBase,key: str) -> str """
  pass
 def GetUserStrings(self):
  """ GetUserStrings(self: GeometryBase) -> NameValueCollection """
  pass
 def MakeDeformable(self):
  """ MakeDeformable(self: GeometryBase) -> bool """
  pass
 def MemoryEstimate(self):
  """ MemoryEstimate(self: GeometryBase) -> UInt32 """
  pass
 def NonConstOperation(self,*args):
  """ NonConstOperation(self: CommonObject) """
  pass
 def OnSwitchToNonConst(self,*args):
  """ OnSwitchToNonConst(self: GeometryBase) """
  pass
 def Rotate(self,angleRadians,rotationAxis,rotationCenter):
  """ Rotate(self: GeometryBase,angleRadians: float,rotationAxis: Vector3d,rotationCenter: Point3d) -> bool """
  pass
 def Scale(self,scaleFactor):
  """ Scale(self: GeometryBase,scaleFactor: float) -> bool """
  pass
 def SetUserString(self,key,value):
  """ SetUserString(self: GeometryBase,key: str,value: str) -> bool """
  pass
 def Transform(self,xform):
  """ Transform(self: GeometryBase,xform: Transform) -> bool """
  pass
 def Translate(self,*__args):
  """
  Translate(self: GeometryBase,x: float,y: float,z: float) -> bool
  Translate(self: GeometryBase,translationVector: Vector3d) -> bool
  """
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
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,info: SerializationInfo,context: StreamingContext) """
  pass
 def __reduce_ex__(self,*args):
  pass
 HasBrepForm=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasBrepForm(self: GeometryBase) -> bool

"""

 IsDeformable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDeformable(self: GeometryBase) -> bool

"""

 IsDocumentControlled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDocumentControlled(self: GeometryBase) -> bool

"""

 ObjectType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ObjectType(self: GeometryBase) -> ObjectType

"""

 UserStringCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UserStringCount(self: GeometryBase) -> int

"""


