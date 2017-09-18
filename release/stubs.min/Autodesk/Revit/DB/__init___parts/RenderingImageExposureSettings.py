class RenderingImageExposureSettings(object,IDisposable):
 """ Represents the exposure settings of rendering. """
 def Dispose(self):
  """ Dispose(self: RenderingImageExposureSettings) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RenderingImageExposureSettings,disposing: bool) """
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
 ExposureValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The value of rendering image exposure.



Get: ExposureValue(self: RenderingImageExposureSettings) -> float



Set: ExposureValue(self: RenderingImageExposureSettings)=value

"""

 Highlights=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The highlights value.



Get: Highlights(self: RenderingImageExposureSettings) -> float



Set: Highlights(self: RenderingImageExposureSettings)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: RenderingImageExposureSettings) -> bool



"""

 Saturation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The value of rendering image saturation.



Get: Saturation(self: RenderingImageExposureSettings) -> float



Set: Saturation(self: RenderingImageExposureSettings)=value

"""

 Shadows=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The shadows value.



Get: Shadows(self: RenderingImageExposureSettings) -> float



Set: Shadows(self: RenderingImageExposureSettings)=value

"""

 WhitePoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The white point value.



Get: WhitePoint(self: RenderingImageExposureSettings) -> float



Set: WhitePoint(self: RenderingImageExposureSettings)=value

"""


