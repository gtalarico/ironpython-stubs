class StructuralInstanceUsageFilter(ElementSlowFilter,IDisposable):
 """
 A filter used to find elements that are structural family instances (typically columns,beams or braces) of the given structural usage.

 

 StructuralInstanceUsageFilter(structuralUsage: StructuralInstanceUsage,inverted: bool)

 StructuralInstanceUsageFilter(structuralUsage: StructuralInstanceUsage)
 """
 def Dispose(self):
  """ Dispose(self: ElementFilter,A_0: bool) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ElementFilter,disposing: bool) """
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
 def __new__(self,structuralUsage,inverted=None):
  """
  __new__(cls: type,structuralUsage: StructuralInstanceUsage,inverted: bool)

  __new__(cls: type,structuralUsage: StructuralInstanceUsage)
  """
  pass
 StructuralUsage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The family instance structural usage.



Get: StructuralUsage(self: StructuralInstanceUsageFilter) -> StructuralInstanceUsage



"""


