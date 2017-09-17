class RenderingSettings(object,IDisposable):
 """ Represents the rendering settings for a 3d view. """
 def Dispose(self):
  """ Dispose(self: RenderingSettings) """
  pass
 def GetBackgroundSettings(self):
  """
  GetBackgroundSettings(self: RenderingSettings) -> BackgroundSettings
  
   Returns an object that represents the rendering background settings.
   Returns: The rendering background settings.
  """
  pass
 def GetRenderingImageExposureSettings(self):
  """
  GetRenderingImageExposureSettings(self: RenderingSettings) -> RenderingImageExposureSettings
  
   Returns an  object that represents the rendering image exposure settings.
   Returns: The rendering image exposure settings.
  """
  pass
 def GetRenderingQualitySettings(self):
  """
  GetRenderingQualitySettings(self: RenderingSettings) -> RenderingQualitySettings
  
   Returns an object that represents the rendering quality settings.
   Returns: The rendering quality settings.
  """
  pass
 def GetRenderingRegionOutline(self):
  """
  GetRenderingRegionOutline(self: RenderingSettings) -> Outline
  
   Returns the outline of the rendering region.
   Returns: The outline of the rendering region.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RenderingSettings,disposing: bool) """
  pass
 def SetBackgroundSettings(self,background):
  """
  SetBackgroundSettings(self: RenderingSettings,background: BackgroundSettings)
   Changes the rendering background settings details for the current background 
    style.
  
  
   background: An instance of the new rendering background settings.
  """
  pass
 def SetRenderingImageExposureSettings(self,exposure):
  """
  SetRenderingImageExposureSettings(self: RenderingSettings,exposure: RenderingImageExposureSettings)
   Changes the rendering image exposure settings.
  
   exposure: An instance of the new rendering image exposure settings.
  """
  pass
 def SetRenderingQualitySettings(self,settings):
  """
  SetRenderingQualitySettings(self: RenderingSettings,settings: RenderingQualitySettings)
   Change rendering quality settings.
  
   settings: An instance of the new rendering quality settings.
  """
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
 BackgroundStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The enum value that controls the background style for rendering.

Get: BackgroundStyle(self: RenderingSettings) -> BackgroundStyle

Set: BackgroundStyle(self: RenderingSettings)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RenderingSettings) -> bool

"""

 LightingSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The lighting scheme type.

Get: LightingSource(self: RenderingSettings) -> LightingSource

Set: LightingSource(self: RenderingSettings)=value
"""

 PrinterResolution=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The resolution level when using printer.

Get: PrinterResolution(self: RenderingSettings) -> PrinterResolution

Set: PrinterResolution(self: RenderingSettings)=value
"""

 ResolutionTarget=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The resolution target.

Get: ResolutionTarget(self: RenderingSettings) -> ResolutionTarget

Set: ResolutionTarget(self: RenderingSettings)=value
"""

 ResolutionValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The rendering resolution in dots per inch (DPI).

Get: ResolutionValue(self: RenderingSettings) -> int

"""

 UsesRegionRendering=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The bool value that indicates whether to use region rendering.

Get: UsesRegionRendering(self: RenderingSettings) -> bool

Set: UsesRegionRendering(self: RenderingSettings)=value
"""


