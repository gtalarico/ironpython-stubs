class Point(GeometryObject,IDisposable):
 """ A 3D point. """
 @staticmethod
 def Create(coord,id=None):
  """
  Create(coord: XYZ) -> Point
  
   Creates a point at the given coordinates.
  
   coord: The coordinates where the point will be created.
   Returns: A Point object.
  Create(coord: XYZ,id: ElementId) -> Point
  
   Creates a point at the given coordinates and assigns it the specified color.
  
   coord: The coordinates where the point will be created.
   id: The id of the GraphicsStyle element from which to apply the point properties.
   Returns: A Point object.
  """
  pass
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
 Coord=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the coordinates of the point.

Get: Coord(self: Point) -> XYZ

"""

 Reference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns a stable reference to the point.

Get: Reference(self: Point) -> Reference

"""


