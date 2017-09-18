class BoundingBoxXYZ(APIObject,IDisposable):
 """
 A three-dimensional rectangular box at an arbitrary location and orientation within the Revit model.
 
 BoundingBoxXYZ()
 """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: BoundingBoxXYZ) """
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
 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Defines whether the entire bounding box is enabled.

Get: Enabled(self: BoundingBoxXYZ) -> bool

Set: Enabled(self: BoundingBoxXYZ)=value
"""

 Max=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Maximum coordinates (upper-right-front corner of the box).

Get: Max(self: BoundingBoxXYZ) -> XYZ

Set: Max(self: BoundingBoxXYZ)=value
"""

 Min=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Minimum coordinates (lower-left-rear corner of the box).

Get: Min(self: BoundingBoxXYZ) -> XYZ

Set: Min(self: BoundingBoxXYZ)=value
"""

 Transform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The transform from the coordinate space of the box to the model coordinate space.

Get: Transform(self: BoundingBoxXYZ) -> Transform

Set: Transform(self: BoundingBoxXYZ)=value
"""


