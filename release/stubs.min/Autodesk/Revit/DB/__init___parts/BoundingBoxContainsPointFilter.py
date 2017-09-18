class BoundingBoxContainsPointFilter(ElementQuickFilter,IDisposable):
 """
 A filter used to match elements with a bounding box that contains the given point.

 

 BoundingBoxContainsPointFilter(point: XYZ,tolerance: float,inverted: bool)

 BoundingBoxContainsPointFilter(point: XYZ,tolerance: float)

 BoundingBoxContainsPointFilter(point: XYZ,inverted: bool)

 BoundingBoxContainsPointFilter(point: XYZ)
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
 def __new__(self,point,*__args):
  """
  __new__(cls: type,point: XYZ,tolerance: float,inverted: bool)

  __new__(cls: type,point: XYZ,tolerance: float)

  __new__(cls: type,point: XYZ,inverted: bool)

  __new__(cls: type,point: XYZ)
  """
  pass
 Point=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The XYZ point to use when matching element bounding boxes.



Get: Point(self: BoundingBoxContainsPointFilter) -> XYZ



Set: Point(self: BoundingBoxContainsPointFilter)=value

"""

 Tolerance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Allows control over the match criteria by using a tolerance in the geometry comparison. It is suggested to use this in cases where trivial differences should be considered when matching elements.



Get: Tolerance(self: BoundingBoxContainsPointFilter) -> float



Set: Tolerance(self: BoundingBoxContainsPointFilter)=value

"""


