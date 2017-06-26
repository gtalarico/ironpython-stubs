class TextDot(GeometryBase,IDisposable,ISerializable):
 """ TextDot(text: str,location: Point3d) """
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
 def __new__(self,text,location):
  """
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  __new__(cls: type,text: str,location: Point3d)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 FontFace=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FontFace(self: TextDot) -> str

Set: FontFace(self: TextDot)=value
"""

 FontHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FontHeight(self: TextDot) -> int

Set: FontHeight(self: TextDot)=value
"""

 Point=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Point(self: TextDot) -> Point3d

Set: Point(self: TextDot)=value
"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Text(self: TextDot) -> str

Set: Text(self: TextDot)=value
"""


