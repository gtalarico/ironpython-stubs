class ViewDisplaySketchyLines(object,IDisposable):
 """ Represents the settings for sketchy lines. """
 def Dispose(self):
  """ Dispose(self: ViewDisplaySketchyLines) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ViewDisplaySketchyLines,disposing: bool) """
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
 EnableSketchyLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True to enable sketchy lines visibility. False to disable it.



Get: EnableSketchyLines(self: ViewDisplaySketchyLines) -> bool



Set: EnableSketchyLines(self: ViewDisplaySketchyLines)=value

"""

 Extension=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The extension scale value. Controls the magnitude of line's extension.

   Values between 0 and 10.



Get: Extension(self: ViewDisplaySketchyLines) -> int



Set: Extension(self: ViewDisplaySketchyLines)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: ViewDisplaySketchyLines) -> bool



"""

 Jitter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The jitter defines jitteriness of the line.

   Values between 0 and 10.



Get: Jitter(self: ViewDisplaySketchyLines) -> int



Set: Jitter(self: ViewDisplaySketchyLines)=value

"""


