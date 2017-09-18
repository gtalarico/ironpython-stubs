class BoundingBoxUV(object,IDisposable):
 """
 A two-dimensional rectangle,parallel to the coordinate axes.

 

 BoundingBoxUV(min_u: float,min_v: float,max_u: float,max_v: float)

 BoundingBoxUV()
 """
 def Dispose(self):
  """ Dispose(self: BoundingBoxUV) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: BoundingBoxUV,disposing: bool) """
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
 def __new__(self,min_u=None,min_v=None,max_u=None,max_v=None):
  """
  __new__(cls: type,min_u: float,min_v: float,max_u: float,max_v: float)

  __new__(cls: type)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Max=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Maximum coordinates (upper-right corner of the box).



Get: Max(self: BoundingBoxUV) -> UV



Set: Max(self: BoundingBoxUV)=value

"""

 Min=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Minimum coordinates (lower-left corner of the box).



Get: Min(self: BoundingBoxUV) -> UV



Set: Min(self: BoundingBoxUV)=value

"""


