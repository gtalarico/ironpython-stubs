class PixelFormatConverter(TypeConverter):
 """
 Converts a System.Windows.Media.PixelFormat to and from other data types.
 
 PixelFormatConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: PixelFormatConverter,td: ITypeDescriptorContext,t: Type) -> bool
  
   Determines whether the converter can convert an object of the given type to an 
    instance of System.Windows.Media.PixelFormat.
  
  
   td: Type context information used to evaluate conversion.
   t: The type of the source that is being evaluated for conversion.
   Returns: true if the converter can convert the provided type to an instance of 
    System.Windows.Media.PixelFormat; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: PixelFormatConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool
  
   Determines whether an instance of System.Windows.Media.PixelFormat can be 
    converted to a different type.
  
  
   context: Type context information used to evaluate conversion.
   destinationType: The desired type to evaluate the conversion to.
   Returns: true if the converter can convert this instance of 
    System.Windows.Media.PixelFormat; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: PixelFormatConverter,td: ITypeDescriptorContext,ci: CultureInfo,o: object) -> object
  
   Attempts to convert a specified object to an instance of 
    System.Windows.Media.PixelFormat.
  
  
   td: Type context information used for conversion.
   ci: Cultural information that is respected during conversion.
   o: The object being converted.
   Returns: An System.Object that represents the converted value.
  """
  pass
 def ConvertFromString(self,*__args):
  """
  ConvertFromString(self: PixelFormatConverter,value: str) -> object
  
   Attempts to convert a string to a System.Windows.Media.PixelFormat.
  
   value: The string to convert to a System.Windows.Media.PixelFormat.
   Returns: A new instance of System.Windows.Media.PixelFormat.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: PixelFormatConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object
  
   Attempts to convert an instance of System.Windows.Media.PixelFormat to a 
    specified type.
  
  
   context: Context information used for conversion.
   culture: Cultural information that is respected during conversion.
   value: System.Windows.Media.PixelFormat to convert.
   destinationType: Type being evaluated for conversion.
   Returns: A new instance of the destinationType.
  """
  pass
