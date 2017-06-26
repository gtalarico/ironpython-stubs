class CurveExtents(object,IDisposable):
 """ Represents the start and end parameters for a curve segment. """
 def Dispose(self):
  """ Dispose(self: CurveExtents) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: CurveExtents,disposing: bool) """
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
 """The end parameter of the curve extents.

Get: EndParameter(self: CurveExtents) -> float

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: CurveExtents) -> bool

"""

 StartParameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The start parameter of the curve extents.

Get: StartParameter(self: CurveExtents) -> float

"""


