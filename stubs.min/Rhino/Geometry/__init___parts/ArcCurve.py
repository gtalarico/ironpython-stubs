class ArcCurve(Curve,IDisposable,ISerializable):
 """
 ArcCurve()
 ArcCurve(other: ArcCurve)
 ArcCurve(arc: Arc)
 ArcCurve(arc: Arc,t0: float,t1: float)
 ArcCurve(circle: Circle)
 ArcCurve(circle: Circle,t0: float,t1: float)
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
  __new__(cls: type,other: ArcCurve)
  __new__(cls: type,arc: Arc)
  __new__(cls: type,arc: Arc,t0: float,t1: float)
  __new__(cls: type,circle: Circle)
  __new__(cls: type,circle: Circle,t0: float,t1: float)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 AngleDegrees=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AngleDegrees(self: ArcCurve) -> float

"""

 AngleRadians=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AngleRadians(self: ArcCurve) -> float

"""

 Arc=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Arc(self: ArcCurve) -> Arc

"""

 IsCompleteCircle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsCompleteCircle(self: ArcCurve) -> bool

"""

 Radius=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Radius(self: ArcCurve) -> float

"""


