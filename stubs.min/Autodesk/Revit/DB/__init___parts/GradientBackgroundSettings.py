class GradientBackgroundSettings(BackgroundSettings,IDisposable):
 """ Represents the view gradient background settings. """
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
 GroundColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The color of the ground.

Get: GroundColor(self: GradientBackgroundSettings) -> Color

Set: GroundColor(self: GradientBackgroundSettings)=value
"""

 HorizonColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The color of the horizon.

Get: HorizonColor(self: GradientBackgroundSettings) -> Color

Set: HorizonColor(self: GradientBackgroundSettings)=value
"""

 SkyColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The color of the top of the sky.

Get: SkyColor(self: GradientBackgroundSettings) -> Color

Set: SkyColor(self: GradientBackgroundSettings)=value
"""


