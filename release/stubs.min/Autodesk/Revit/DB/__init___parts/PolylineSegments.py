class PolylineSegments(object,IDisposable):
 """ An output node that represents a tessellated polyline segments. """
 def Dispose(self):
  """ Dispose(self: PolylineSegments) """
  pass
 def GetVertices(self):
  """
  GetVertices(self: PolylineSegments) -> IList[XYZ]

  

   Returns an array of vertices of the polyline segments.

   Returns: Array of XYZ points.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: PolylineSegments,disposing: bool) """
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
 EndLocalParameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Local parameter associated with the end point.



Get: EndLocalParameter(self: PolylineSegments) -> float



"""

 EndParameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Parameter associated with the end point.



Get: EndParameter(self: PolylineSegments) -> float



"""

 IsFilled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the area enclosed by the polyline is to be filled or not.



Get: IsFilled(self: PolylineSegments) -> bool



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: PolylineSegments) -> bool



"""

 LineProperties=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Access to the line (pen) properties of the polyline



Get: LineProperties(self: PolylineSegments) -> LineProperties



"""

 StartLocalParameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Local parameter associated with the start point.



Get: StartLocalParameter(self: PolylineSegments) -> float



"""

 StartParameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Parameter associated with the start point.



Get: StartParameter(self: PolylineSegments) -> float



"""


