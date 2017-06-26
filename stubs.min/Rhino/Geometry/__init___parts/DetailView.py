class DetailView(GeometryBase,IDisposable,ISerializable):
 # no doc
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
 def SetScale(self,modelLength,modelUnits,pageLength,pageUnits):
  """ SetScale(self: DetailView,modelLength: float,modelUnits: UnitSystem,pageLength: float,pageUnits: UnitSystem) -> bool """
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
 IsParallelProjection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsParallelProjection(self: DetailView) -> bool

Set: IsParallelProjection(self: DetailView)=value
"""

 IsPerspectiveProjection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsPerspectiveProjection(self: DetailView) -> bool

Set: IsPerspectiveProjection(self: DetailView)=value
"""

 IsProjectionLocked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsProjectionLocked(self: DetailView) -> bool

Set: IsProjectionLocked(self: DetailView)=value
"""

 PageToModelRatio=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PageToModelRatio(self: DetailView) -> float

"""


