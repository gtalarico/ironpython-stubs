class CurveProxy(Curve,IDisposable,ISerializable):
 # no doc
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
 ProxyCurveIsReversed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ProxyCurveIsReversed(self: CurveProxy) -> bool

"""


