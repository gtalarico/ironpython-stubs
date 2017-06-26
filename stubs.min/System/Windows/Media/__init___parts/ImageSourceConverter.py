class ImageSourceConverter(TypeConverter):
 """
 Converts a System.Windows.Media.ImageSource to and from other data types.
 
 ImageSourceConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: ImageSourceConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool
  
   Determines whether the converter can convert an object of the given type to an 
    instance of System.Windows.Media.ImageSource.
  
  
   context: Type context information used to evaluate conversion.
   sourceType: The type of the source that is being evaluated for conversion.
   Returns: true if the converter can convert the provided type to an instance of 
    System.Windows.Media.ImageSource; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: ImageSourceConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool
  
   Determines whether an instance of System.Windows.Media.ImageSource can be 
    converted to a different type.
  
  
   context: Type context information used to evaluate conversion.
   destinationType: The desired type to evaluate the conversion to.
   Returns: true if the converter can convert this instance of 
    System.Windows.Media.ImageSource; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: ImageSourceConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object
  
   Attempts to convert a specified object to an instance of 
    System.Windows.Media.ImageSource.
  
  
   context: Type context information used for conversion.
   culture: Cultural information that is respected during conversion.
   value: The object being converted.
   Returns: A new instance of System.Windows.Media.ImageSource.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: ImageSourceConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object
  
   Attempts to convert an instance of System.Windows.Media.ImageSource to a 
    specified type.
  
  
   context: Context information used for conversion.
   culture: Cultural information that is respected during conversion.
   value: System.Windows.Media.ImageSource to convert.
   destinationType: Type being evaluated for conversion.
   Returns: A new instance of the destinationType.
  """
  pass
