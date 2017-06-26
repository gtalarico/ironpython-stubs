class LineCurve(Curve,IDisposable,ISerializable):
 """
 LineCurve()
 LineCurve(other: LineCurve)
 LineCurve(from: Point2d,to: Point2d)
 LineCurve(from: Point3d,to: Point3d)
 LineCurve(line: Line)
 LineCurve(line: Line,t0: float,t1: float)
 """
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 def Dispose(self):
  """ Dispose(self: Curve,disposing: bool) """
  pass
 def NonConstOperation(self,*args):
  """ NonConstOperation(self: Curve) """
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
  __new__(cls: type)
  __new__(cls: type,other: LineCurve)
  __new__(cls: type,from: Point2d,to: Point2d)
  __new__(cls: type,from: Point3d,to: Point3d)
  __new__(cls: type,line: Line)
  __new__(cls: type,line: Line,t0: float,t1: float)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 Line=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Line(self: LineCurve) -> Line

Set: Line(self: LineCurve)=value
"""


