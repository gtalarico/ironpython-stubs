class Polyloop(object,IDisposable):
 """ A Polyloop represent a planar polygon with ordered points. """
 def ComputeArea(self):
  """
  ComputeArea(self: Polyloop) -> float

  

   Gets the area for this polygon.

   Returns: The area for this polygon.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Polyloop) """
  pass
 def GetPoints(self):
  """
  GetPoints(self: Polyloop) -> IList[XYZ]

  

   Gets the array of points in the polygon

   Returns: The array of points in the polygon
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Polyloop,disposing: bool) """
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
 Centroid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The polygon centroid.



Get: Centroid(self: Polyloop) -> XYZ



"""

 Direction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The direction for the outward normal for this polygon.



Get: Direction(self: Polyloop) -> XYZ



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: Polyloop) -> bool



"""


