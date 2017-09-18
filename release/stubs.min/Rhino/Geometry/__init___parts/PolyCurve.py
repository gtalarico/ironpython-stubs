class PolyCurve(Curve,IDisposable,ISerializable):
 """ PolyCurve() """
 def Append(self,*__args):
  """
  Append(self: PolyCurve,curve: Curve) -> bool
  Append(self: PolyCurve,arc: Arc) -> bool
  Append(self: PolyCurve,line: Line) -> bool
  """
  pass
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 def Dispose(self):
  """ Dispose(self: Curve,disposing: bool) """
  pass
 def Duplicate(self):
  """ Duplicate(self: PolyCurve) -> GeometryBase """
  pass
 def DuplicatePolyCurve(self):
  """ DuplicatePolyCurve(self: PolyCurve) -> PolyCurve """
  pass
 def Explode(self):
  """ Explode(self: PolyCurve) -> Array[Curve] """
  pass
 def NonConstOperation(self,*args):
  """ NonConstOperation(self: Curve) """
  pass
 def OnSwitchToNonConst(self,*args):
  """ OnSwitchToNonConst(self: GeometryBase) """
  pass
 def PolyCurveParameter(self,segmentIndex,segmentCurveParameter):
  """ PolyCurveParameter(self: PolyCurve,segmentIndex: int,segmentCurveParameter: float) -> float """
  pass
 def RemoveNesting(self):
  """ RemoveNesting(self: PolyCurve) -> bool """
  pass
 def SegmentCurve(self,index):
  """ SegmentCurve(self: PolyCurve,index: int) -> Curve """
  pass
 def SegmentCurveParameter(self,polycurveParameter):
  """ SegmentCurveParameter(self: PolyCurve,polycurveParameter: float) -> float """
  pass
 def SegmentDomain(self,segmentIndex):
  """ SegmentDomain(self: PolyCurve,segmentIndex: int) -> Interval """
  pass
 def SegmentIndex(self,polycurveParameter):
  """ SegmentIndex(self: PolyCurve,polycurveParameter: float) -> int """
  pass
 def SegmentIndexes(self,subdomain,segmentIndex0,segmentIndex1):
  """ SegmentIndexes(self: PolyCurve,subdomain: Interval) -> (int,int,int) """
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
 HasGap=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasGap(self: PolyCurve) -> bool

"""

 IsNested=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsNested(self: PolyCurve) -> bool

"""

 SegmentCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SegmentCount(self: PolyCurve) -> int

"""


