class LineSegment(object,IDisposable):
 """ An output node that represents a tessellated line segment. """
 def Dispose(self):
  """ Dispose(self: LineSegment) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: LineSegment,disposing: bool) """
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
 EndParameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Parameter associated with the end point.

Get: EndParameter(self: LineSegment) -> float

"""

 EndPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """End point of the line segment.

Get: EndPoint(self: LineSegment) -> XYZ

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: LineSegment) -> bool

"""

 LineProperties=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Access to the line (pen) properties of the line

Get: LineProperties(self: LineSegment) -> LineProperties

"""

 StartParameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Parameter associated with the start point.

Get: StartParameter(self: LineSegment) -> float

"""

 StartPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Start point of the line segment.

Get: StartPoint(self: LineSegment) -> XYZ

"""


