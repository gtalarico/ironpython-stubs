class ViewDisplayBackground(object,IDisposable):
 """
 Set of values that control how background is drawn in a view.

    Background can only be set for a 3d view or for a section or elevation view.
 """
 @staticmethod
 def CreateGradient(skyColor,horizonColor,groundColor):
  """
  CreateGradient(skyColor: Color,horizonColor: Color,groundColor: Color) -> ViewDisplayBackground

  

   Creates an object that can be passed to DBView::setBackground function

     to 

    set the background of the Gradient type.

  

  

   skyColor: The top of the sky gradient if the sky is visible.

   horizonColor: The bottom or the sky gradient if the sky is visible,

     or the top of the 

    ground gradient otherwise.

  

   groundColor: The ground color if the sky is visible (ground shown in uniform color),

     or 

    the bottom of the ground gradient if the sky is not visible.

  

   Returns: New background object to pass to DBView::setBackground.
  """
  pass
 @staticmethod
 def CreateImage(imagePath,flags,imageOffsets,imageScales):
  """
  CreateImage(imagePath: str,flags: ViewDisplayBackgroundImageFlags,imageOffsets: UV,imageScales: UV) -> ViewDisplayBackground

  

   Creates an object that can be passed to DBView::setBackground function

     to 

    set the background of the Image type.

  

  

   imagePath: File path with the image to be used.

   flags: Combination of flags (binary) that control how image is displayed in relation

   

      to the view/crop boundary.

  

   imageOffsets: Horizontal (u) and vertical (v) offsets of the image.

   imageScales: Horizontal (u) and vertical (v) scales of the image (1 == no change).

   Returns: New background object to pass to DBView::setBackground.
  """
  pass
 @staticmethod
 def CreateSky():
  """
  CreateSky() -> ViewDisplayBackground

  

   Creates an object that can be passed to DBView::setBackground function

     to 

    set the background of the SunAndClouds type.

  

   Returns: New background object to pass to DBView::setBackground.
  """
  pass
 def Dispose(self):
  """ Dispose(self: ViewDisplayBackground) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ViewDisplayBackground,disposing: bool) """
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
 BackgroundColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The color of the horizon when the type is 'Gradient'.



Get: BackgroundColor(self: ViewDisplayBackground) -> Color



"""

 GroundColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The color of the ground when the type is 'Gradient' or 'SunAndClouds'.



Get: GroundColor(self: ViewDisplayBackground) -> Color



"""

 HorizontalImageOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The distance between the left viewport boundary and the left edge of the background image.



Get: HorizontalImageOffset(self: ViewDisplayBackground) -> float



"""

 HorizontalImageScale=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The horizontal scale of the background image; the scale of 1.0 puts the image pixel-to-pixel.



Get: HorizontalImageScale(self: ViewDisplayBackground) -> float



"""

 ImageFlags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The image alignment indicators when the type is 'Image'.



Get: ImageFlags(self: ViewDisplayBackground) -> ViewDisplayBackgroundImageFlags



"""

 ImagePath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The path to the image file when the type is 'Image'.



Get: ImagePath(self: ViewDisplayBackground) -> str



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: ViewDisplayBackground) -> bool



"""

 SkyColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The color of the sky when the type is 'Gradient'.



Get: SkyColor(self: ViewDisplayBackground) -> Color



"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type of the background.



Get: Type(self: ViewDisplayBackground) -> ViewDisplayBackgroundType



"""

 VerticalImageOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The distance between the bottom viewport boundary and the bottom edge of the background image.



Get: VerticalImageOffset(self: ViewDisplayBackground) -> float



"""

 VerticalImageScale=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The vertical scale of the background image; the scale of 1.0 puts the image pixel-to-pixel.



Get: VerticalImageScale(self: ViewDisplayBackground) -> float



"""


