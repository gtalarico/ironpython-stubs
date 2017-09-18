class HistoryRecord(object,IDisposable):
 """ HistoryRecord(command: Command,version: int) """
 def Dispose(self):
  """
  Dispose(self: HistoryRecord)

   Actively reclaims unmanaged resources that this instance uses.
  """
  pass
 def SetBool(self,id,value):
  """ SetBool(self: HistoryRecord,id: int,value: bool) -> bool """
  pass
 def SetBools(self,id,values):
  """ SetBools(self: HistoryRecord,id: int,values: IEnumerable[bool]) -> bool """
  pass
 def SetBrep(self,id,value):
  """ SetBrep(self: HistoryRecord,id: int,value: Brep) -> bool """
  pass
 def SetColor(self,id,value):
  """ SetColor(self: HistoryRecord,id: int,value: Color) -> bool """
  pass
 def SetColors(self,id,values):
  """ SetColors(self: HistoryRecord,id: int,values: IEnumerable[Color]) -> bool """
  pass
 def SetCurve(self,id,value):
  """ SetCurve(self: HistoryRecord,id: int,value: Curve) -> bool """
  pass
 def SetDouble(self,id,value):
  """ SetDouble(self: HistoryRecord,id: int,value: float) -> bool """
  pass
 def SetDoubles(self,id,values):
  """ SetDoubles(self: HistoryRecord,id: int,values: IEnumerable[float]) -> bool """
  pass
 def SetGuid(self,id,value):
  """ SetGuid(self: HistoryRecord,id: int,value: Guid) -> bool """
  pass
 def SetGuids(self,id,values):
  """ SetGuids(self: HistoryRecord,id: int,values: IEnumerable[Guid]) -> bool """
  pass
 def SetInt(self,id,value):
  """ SetInt(self: HistoryRecord,id: int,value: int) -> bool """
  pass
 def SetInts(self,id,values):
  """ SetInts(self: HistoryRecord,id: int,values: IEnumerable[int]) -> bool """
  pass
 def SetMesh(self,id,value):
  """ SetMesh(self: HistoryRecord,id: int,value: Mesh) -> bool """
  pass
 def SetObjRef(self,id,value):
  """ SetObjRef(self: HistoryRecord,id: int,value: ObjRef) -> bool """
  pass
 def SetPoint3d(self,id,value):
  """ SetPoint3d(self: HistoryRecord,id: int,value: Point3d) -> bool """
  pass
 def SetPoint3dOnObject(self,id,objref,value):
  """ SetPoint3dOnObject(self: HistoryRecord,id: int,objref: ObjRef,value: Point3d) -> bool """
  pass
 def SetPoint3ds(self,id,values):
  """ SetPoint3ds(self: HistoryRecord,id: int,values: IEnumerable[Point3d]) -> bool """
  pass
 def SetString(self,id,value):
  """ SetString(self: HistoryRecord,id: int,value: str) -> bool """
  pass
 def SetStrings(self,id,values):
  """ SetStrings(self: HistoryRecord,id: int,values: IEnumerable[str]) -> bool """
  pass
 def SetSurface(self,id,value):
  """ SetSurface(self: HistoryRecord,id: int,value: Surface) -> bool """
  pass
 def SetTransorm(self,id,value):
  """ SetTransorm(self: HistoryRecord,id: int,value: Transform) -> bool """
  pass
 def SetVector3d(self,id,value):
  """ SetVector3d(self: HistoryRecord,id: int,value: Vector3d) -> bool """
  pass
 def SetVector3ds(self,id,values):
  """ SetVector3ds(self: HistoryRecord,id: int,values: IEnumerable[Vector3d]) -> bool """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,command,version):
  """ __new__(cls: type,command: Command,version: int) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Handle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Wrapped native C++ pointer to CRhinoHistory instance



Get: Handle(self: HistoryRecord) -> IntPtr



"""


