class TextEntity(AnnotationBase,IDisposable,ISerializable):
 """ TextEntity() """
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
 def __new__(self):
  """
  __new__(cls: type)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 AnnotativeScalingEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AnnotativeScalingEnabled(self: TextEntity) -> bool

Set: AnnotativeScalingEnabled(self: TextEntity)=value
"""

 FontIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FontIndex(self: TextEntity) -> int

Set: FontIndex(self: TextEntity)=value
"""

 Justification=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Justification(self: TextEntity) -> TextJustification

Set: Justification(self: TextEntity)=value
"""

 MaskColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MaskColor(self: TextEntity) -> Color

Set: MaskColor(self: TextEntity)=value
"""

 MaskEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MaskEnabled(self: TextEntity) -> bool

Set: MaskEnabled(self: TextEntity)=value
"""

 MaskOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MaskOffset(self: TextEntity) -> float

Set: MaskOffset(self: TextEntity)=value
"""

 MaskUsesViewportColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MaskUsesViewportColor(self: TextEntity) -> bool

Set: MaskUsesViewportColor(self: TextEntity)=value
"""


