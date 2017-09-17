class RevSurface(Surface,IDisposable,ISerializable):
 # no doc
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 @staticmethod
 def Create(*__args):
  """
  Create(revoluteLine: Line,axisOfRevolution: Line) -> RevSurface
  Create(revolutePolyline: Polyline,axisOfRevolution: Line,startAngleRadians: float,endAngleRadians: float) -> RevSurface
  Create(revolutePolyline: Polyline,axisOfRevolution: Line) -> RevSurface
  Create(revoluteCurve: Curve,axisOfRevolution: Line,startAngleRadians: float,endAngleRadians: float) -> RevSurface
  Create(revoluteCurve: Curve,axisOfRevolution: Line) -> RevSurface
  Create(revoluteLine: Line,axisOfRevolution: Line,startAngleRadians: float,endAngleRadians: float) -> RevSurface
  """
  pass
 @staticmethod
 def CreateFromCone(cone):
  """ CreateFromCone(cone: Cone) -> RevSurface """
  pass
 @staticmethod
 def CreateFromCylinder(cylinder):
  """ CreateFromCylinder(cylinder: Cylinder) -> RevSurface """
  pass
 @staticmethod
 def CreateFromSphere(sphere):
  """ CreateFromSphere(sphere: Sphere) -> RevSurface """
  pass
 @staticmethod
 def CreateFromTorus(torus):
  """ CreateFromTorus(torus: Torus) -> RevSurface """
  pass
 def Dispose(self):
  """ Dispose(self: CommonObject,disposing: bool) """
  pass
 def NonConstOperation(self,*args):
  """ NonConstOperation(self: CommonObject) """
  pass
 def OnSwitchToNonConst(self,*args):
  """ OnSwitchToNonConst(self: GeometryBase) """
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
