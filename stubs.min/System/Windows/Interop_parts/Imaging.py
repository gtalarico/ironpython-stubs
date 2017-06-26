class Imaging(object):
 """ Provides managed to unmanaged interoperation support for creating image objects. """
 @staticmethod
 def CreateBitmapSourceFromHBitmap(bitmap,palette,sourceRect,sizeOptions):
  """
  CreateBitmapSourceFromHBitmap(bitmap: IntPtr,palette: IntPtr,sourceRect: Int32Rect,sizeOptions: BitmapSizeOptions) -> BitmapSource
  
   Returns a managed System.Windows.Media.Imaging.BitmapSource,based on the 
    provided pointer to an unmanaged bitmap and palette information.
  
  
   bitmap: A pointer to the unmanaged bitmap.
   palette: A pointer to the bitmap's palette map.
   sourceRect: The size of the source image.
   sizeOptions: A value of the enumeration that specifies how to handle conversions.
   Returns: The created System.Windows.Media.Imaging.BitmapSource.
  """
  pass
 @staticmethod
 def CreateBitmapSourceFromHIcon(icon,sourceRect,sizeOptions):
  """
  CreateBitmapSourceFromHIcon(icon: IntPtr,sourceRect: Int32Rect,sizeOptions: BitmapSizeOptions) -> BitmapSource
  
   Returns a managed System.Windows.Media.Imaging.BitmapSource,based on the 
    provided pointer to an unmanaged icon image.
  
  
   icon: A pointer to the unmanaged icon source.
   sourceRect: The size of the source image.
   sizeOptions: A value of the enumeration that specifies how to handle conversions.
   Returns: The created System.Windows.Media.Imaging.BitmapSource.
  """
  pass
 @staticmethod
 def CreateBitmapSourceFromMemorySection(section,pixelWidth,pixelHeight,format,stride,offset):
  """
  CreateBitmapSourceFromMemorySection(section: IntPtr,pixelWidth: int,pixelHeight: int,format: PixelFormat,stride: int,offset: int) -> BitmapSource
  
   Returns a managed System.Windows.Media.Imaging.BitmapSource,based on the 
    provided unmanaged memory location.
  
  
   section: A pointer to a memory section.
   pixelWidth: An integer that specifies the width,in pixels,of the bitmap.
   pixelHeight: An integer that specifies the height,in pixels,of the bitmap.
   format: A value of the enumeration.
   stride: The stride of the bitmap.
   offset: The byte offset into the memory stream where the image starts.
   Returns: The created System.Windows.Media.Imaging.BitmapSource.
  """
  pass
 __all__=[
  'CreateBitmapSourceFromHBitmap',
  'CreateBitmapSourceFromHIcon',
  'CreateBitmapSourceFromMemorySection',
 ]

