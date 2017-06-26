class LineProperties(object,IDisposable):
 """
 A structure that has access to the pen properties of lines/curves
    that are currently being drawn/exported via an export context
    during a custom export process.
 """
 def Dispose(self):
  """ Dispose(self: LineProperties) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: LineProperties,disposing: bool) """
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
 Color=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The current color used when drawing lines/curves.

Get: Color(self: LineProperties) -> Color

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: LineProperties) -> bool

"""

 LineWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The current width (thickness) of the pen stroke when drawing lines/curves.

Get: LineWidth(self: LineProperties) -> float

"""

 PatternId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Id of the current Line pattern element used when drawing lines/curves.

Get: PatternId(self: LineProperties) -> ElementId

"""

 Transparency=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The current transparency level to be applied to the current color.

Get: Transparency(self: LineProperties) -> int

"""


