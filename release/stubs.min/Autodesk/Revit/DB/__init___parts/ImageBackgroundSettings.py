class ImageBackgroundSettings(BackgroundSettings,IDisposable):
 """ Represents the rendering image background settings. """
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
 BackgroundImageFit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The background image fit type.



Get: BackgroundImageFit(self: ImageBackgroundSettings) -> BackgroundImageFit



Set: BackgroundImageFit(self: ImageBackgroundSettings)=value

"""

 FilePath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """File path of the image for the rendering background.



Get: FilePath(self: ImageBackgroundSettings) -> str



Set: FilePath(self: ImageBackgroundSettings)=value

"""

 OffsetHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The vertical offset of the rendering image to the rendering region.



Get: OffsetHeight(self: ImageBackgroundSettings) -> float



Set: OffsetHeight(self: ImageBackgroundSettings)=value

"""

 OffsetWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The horizontal offset of the rendering image to the rendering region.



Get: OffsetWidth(self: ImageBackgroundSettings) -> float



Set: OffsetWidth(self: ImageBackgroundSettings)=value

"""


