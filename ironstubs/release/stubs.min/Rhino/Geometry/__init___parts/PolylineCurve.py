class PolylineCurve(Curve,IDisposable,ISerializable):
 """
 PolylineCurve()
 PolylineCurve(other: PolylineCurve)
 PolylineCurve(points: IEnumerable[Point3d])
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
 def Point(self,index):
  """ Point(self: PolylineCurve,index: int) -> Point3d """
  pass
 def SetPoint(self,index,point):
  """ SetPoint(self: PolylineCurve,index: int,point: Point3d) """
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
  __new__(cls: type,other: PolylineCurve)
  __new__(cls: type,points: IEnumerable[Point3d])
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 PointCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PointCount(self: PolylineCurve) -> int

"""


