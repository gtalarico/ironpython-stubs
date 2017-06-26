class GridLengthConverter(TypeConverter):
 """
 Converts instances of other types to and from System.Windows.GridLength instances.
 
 GridLengthConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: GridLengthConverter,typeDescriptorContext: ITypeDescriptorContext,sourceType: Type) -> bool
  
   Determines whether a class can be converted from a given type to an instance of 
    System.Windows.GridLength.
  
  
   typeDescriptorContext: Describes the context information of a type.
   sourceType: The type of the source that is being evaluated for conversion.
   Returns: true if the converter can convert from the specified type to an instance of 
    System.Windows.GridLength; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: GridLengthConverter,typeDescriptorContext: ITypeDescriptorContext,destinationType: Type) -> bool
  
   Determines whether an instance of System.Windows.GridLength can be converted to 
    a different type.
  
  
   typeDescriptorContext: Describes the context information of a type.
   destinationType: The desired type that this instance of System.Windows.GridLength is being 
    evaluated for conversion.
  
   Returns: true if the converter can convert this instance of System.Windows.GridLength to 
    the specified type; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: GridLengthConverter,typeDescriptorContext: ITypeDescriptorContext,cultureInfo: CultureInfo,source: object) -> object
  
   Attempts to convert a specified object to an instance of 
    System.Windows.GridLength.
  
  
   typeDescriptorContext: Describes the context information of a type.
   cultureInfo: Cultural specific information that should be respected during conversion.
   source: The object being converted.
   Returns: The instance of System.Windows.GridLength that is created from the converted 
    source.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: GridLengthConverter,typeDescriptorContext: ITypeDescriptorContext,cultureInfo: CultureInfo,value: object,destinationType: Type) -> object
  
   Attempts to convert an instance of System.Windows.GridLength to a specified 
    type.
  
  
   typeDescriptorContext: Describes the context information of a type.
   cultureInfo: Cultural specific information that should be respected during conversion.
   value: The instance of System.Windows.GridLength to convert.
   destinationType: The type that this instance of System.Windows.GridLength is converted to.
   Returns: The object that is created from the converted instance of 
    System.Windows.GridLength.
  """
  pass
