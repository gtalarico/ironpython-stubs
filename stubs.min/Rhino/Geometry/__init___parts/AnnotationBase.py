class AnnotationBase(GeometryBase,IDisposable,ISerializable):
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
  """
  __new__(cls: type)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Index(self: AnnotationBase) -> int

Set: Index(self: AnnotationBase)=value
"""

 NumericValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NumericValue(self: AnnotationBase) -> float

"""

 Plane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Plane(self: AnnotationBase) -> Plane

Set: Plane(self: AnnotationBase)=value
"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Text(self: AnnotationBase) -> str

Set: Text(self: AnnotationBase)=value
"""

 TextFormula=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TextFormula(self: AnnotationBase) -> str

Set: TextFormula(self: AnnotationBase)=value
"""

 TextHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TextHeight(self: AnnotationBase) -> float

Set: TextHeight(self: AnnotationBase)=value
"""


