class RadialDimension(AnnotationBase,IDisposable,ISerializable):
 """
 RadialDimension(center: Point3d,arrowTip: Point3d,xAxis: Vector3d,normal: Vector3d,offsetDistance: float)
 RadialDimension(circle: Circle,arrowTip: Point3d,offsetDistance: float)
 """
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
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
 def __new__(self,*__args):
  """
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  __new__(cls: type,center: Point3d,arrowTip: Point3d,xAxis: Vector3d,normal: Vector3d,offsetDistance: float)
  __new__(cls: type,circle: Circle,arrowTip: Point3d,offsetDistance: float)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 IsDiameterDimension=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDiameterDimension(self: RadialDimension) -> bool

"""


