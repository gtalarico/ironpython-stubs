class LocationPoint(Location,IDisposable):
 """ Provides location functionality for all elements that have a single insertion point. """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
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
 Point=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The physical location of the element.



Get: Point(self: LocationPoint) -> XYZ



Set: Point(self: LocationPoint)=value

"""

 Rotation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The angle of rotation around the insertion point,in radians.



Get: Rotation(self: LocationPoint) -> float



"""


