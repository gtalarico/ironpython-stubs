class IntegerRange(object,IDisposable):
 """ A class to define a range of a sequence of consecutive integer numbers """
 def Dispose(self):
  """ Dispose(self: IntegerRange) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: IntegerRange,disposing: bool) """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 High=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The upper limit of the range



Get: High(self: IntegerRange) -> int



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: IntegerRange) -> bool



"""

 Low=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The lower limit of the range



Get: Low(self: IntegerRange) -> int



"""


