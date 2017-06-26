class BoundarySegment(object,IDisposable):
 """ An object that represents a segment of an area boundary. """
 def Dispose(self):
  """ Dispose(self: BoundarySegment) """
  pass
 def GetCurve(self):
  """
  GetCurve(self: BoundarySegment) -> Curve
  
   Get a copy of the curve that is formed along this boundary.
   Returns: A copy of the curve.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: BoundarySegment,disposing: bool) """
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
 ElementId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieve the id of the element that produces this boundary segment.
   If the segment is created from an element in a link,this is the id of the RevitLinkInstance.

Get: ElementId(self: BoundarySegment) -> ElementId

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: BoundarySegment) -> bool

"""

 LinkElementId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieve the element id of the element in a link instance that forms this boundary.

Get: LinkElementId(self: BoundarySegment) -> ElementId

"""


