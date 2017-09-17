class MorphControl(GeometryBase,IDisposable,ISerializable):
 """ MorphControl(originCurve: NurbsCurve,targetCurve: NurbsCurve) """
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
 def __new__(self,originCurve,targetCurve):
  """
  __new__(cls: type,originCurve: NurbsCurve,targetCurve: NurbsCurve)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 PreserveStructure=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreserveStructure(self: MorphControl) -> bool

Set: PreserveStructure(self: MorphControl)=value
"""

 QuickPreview=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: QuickPreview(self: MorphControl) -> bool

Set: QuickPreview(self: MorphControl)=value
"""

 SpaceMorphTolerance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SpaceMorphTolerance(self: MorphControl) -> float

Set: SpaceMorphTolerance(self: MorphControl)=value
"""


