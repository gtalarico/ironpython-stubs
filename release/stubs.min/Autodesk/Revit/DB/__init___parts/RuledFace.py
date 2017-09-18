class RuledFace(Face,IDisposable):
 """ A ruled face of a 3d solid or open shell. """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: GeometryObject) """
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
 IsExtruded=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines if this is an extruded ruled surface.

Get: IsExtruded(self: RuledFace) -> bool

"""

 RulingsAreParallel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines if the rulings of this ruled surface are parallel.

Get: RulingsAreParallel(self: RuledFace) -> bool

"""


