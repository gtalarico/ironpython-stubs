class BrepTrim(CurveProxy,IDisposable,ISerializable):
 # no doc
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 def Dispose(self):
  """ Dispose(self: Curve,disposing: bool) """
  pass
 def GetTolerances(self,toleranceU,toleranceV):
  """ GetTolerances(self: BrepTrim) -> (float,float) """
  pass
 def NonConstOperation(self,*args):
  """ NonConstOperation(self: Curve) """
  pass
 def OnSwitchToNonConst(self,*args):
  """ OnSwitchToNonConst(self: GeometryBase) """
  pass
 def SetTolerances(self,toleranceU,toleranceV):
  """ SetTolerances(self: BrepTrim,toleranceU: float,toleranceV: float) """
  pass
 def SetTrimCurve(self,curve2dIndex,subDomain=None):
  """
  SetTrimCurve(self: BrepTrim,curve2dIndex: int,subDomain: Interval) -> bool
  SetTrimCurve(self: BrepTrim,curve2dIndex: int) -> bool
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
 Brep=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Brep(self: BrepTrim) -> Brep

"""

 Edge=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Edge(self: BrepTrim) -> BrepEdge

"""

 Face=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Face(self: BrepTrim) -> BrepFace

"""

 IsoStatus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsoStatus(self: BrepTrim) -> IsoStatus

Set: IsoStatus(self: BrepTrim)=value
"""

 Loop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Loop(self: BrepTrim) -> BrepLoop

"""

 TrimIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TrimIndex(self: BrepTrim) -> int

"""

 TrimType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TrimType(self: BrepTrim) -> BrepTrimType

Set: TrimType(self: BrepTrim)=value
"""


