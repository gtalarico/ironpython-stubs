class ElementIntersectsSolidFilter(ElementIntersectsFilter,IDisposable):
 """
 A filter to find elements that intersect the given solid geometry.
 
 ElementIntersectsSolidFilter(solid: Solid,inverted: bool)
 ElementIntersectsSolidFilter(solid: Solid)
 """
 def Dispose(self):
  """ Dispose(self: ElementFilter,A_0: bool) """
  pass
 def GetSolid(self):
  """
  GetSolid(self: ElementIntersectsSolidFilter) -> Solid
  
   Gets the target solid geometry.
   Returns: The solid geometry.
  """
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
 def __new__(self,solid,inverted=None):
  """
  __new__(cls: type,solid: Solid,inverted: bool)
  __new__(cls: type,solid: Solid)
  """
  pass
