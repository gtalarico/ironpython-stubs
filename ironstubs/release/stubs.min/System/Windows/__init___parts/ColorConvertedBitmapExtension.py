class ColorConvertedBitmapExtension(MarkupExtension):
 """
 Implements a markup extension that enables System.Windows.Media.Imaging.ColorConvertedBitmap creation. A System.Windows.Media.Imaging.ColorConvertedBitmap does not have an embedded profile,the profile instead being based on source and destination values.
 
 ColorConvertedBitmapExtension()
 ColorConvertedBitmapExtension(image: object)
 """
 def ProvideValue(self,serviceProvider):
  """
  ProvideValue(self: ColorConvertedBitmapExtension,serviceProvider: IServiceProvider) -> object
  
   Returns an object that should be set on the property where this extension is 
    applied. For System.Windows.ColorConvertedBitmapExtension,this is the 
    completed System.Windows.Media.Imaging.ColorConvertedBitmap.
  
  
   serviceProvider: An object that can provide services for the markup extension. This service is 
    expected to provide results for System.Windows.Markup.IUriContext.
  
   Returns: A System.Windows.Media.Imaging.ColorConvertedBitmap based on the values passed 
    to the constructor.
  """
  pass
 @staticmethod
 def __new__(self,image=None):
  """
  __new__(cls: type)
  __new__(cls: type,image: object)
  """
  pass
