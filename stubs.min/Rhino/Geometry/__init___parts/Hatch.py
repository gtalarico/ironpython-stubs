class Hatch(GeometryBase,IDisposable,ISerializable):
 # no doc
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 def Dispose(self):
  """ Dispose(self: CommonObject,disposing: bool) """
  pass
 def Get3dCurves(self,outer):
  """ Get3dCurves(self: Hatch,outer: bool) -> Array[Curve] """
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
 PatternIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PatternIndex(self: Hatch) -> int

Set: PatternIndex(self: Hatch)=value
"""

 PatternRotation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PatternRotation(self: Hatch) -> float

Set: PatternRotation(self: Hatch)=value
"""

 PatternScale=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PatternScale(self: Hatch) -> float

Set: PatternScale(self: Hatch)=value
"""


