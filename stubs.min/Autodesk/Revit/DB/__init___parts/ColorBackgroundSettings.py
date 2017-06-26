class ColorBackgroundSettings(BackgroundSettings,IDisposable):
 """ Represents the rendering color background settings. """
 def Dispose(self):
  """ Dispose(self: BackgroundSettings,A_0: bool) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: BackgroundSettings,disposing: bool) """
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
 Color=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The color of the rendering background.

Get: Color(self: ColorBackgroundSettings) -> Color

Set: Color(self: ColorBackgroundSettings)=value
"""


