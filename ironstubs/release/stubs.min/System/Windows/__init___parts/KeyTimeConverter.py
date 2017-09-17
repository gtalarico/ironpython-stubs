class KeyTimeConverter(TypeConverter):
 """
 Converts instances of System.Windows.Media.Animation.KeyTime to and from other types.
 
 KeyTimeConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: KeyTimeConverter,typeDescriptorContext: ITypeDescriptorContext,type: Type) -> bool
  
   Determines whether an object can be converted from a given type to an instance 
    of a System.Windows.Media.Animation.KeyTime.
  
  
   typeDescriptorContext: Contextual information required for conversion.
   type: Type being evaluated for conversion.
   Returns: true if this type can be converted; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: KeyTimeConverter,typeDescriptorContext: ITypeDescriptorContext,type: Type) -> bool
  
   Determines if a given type can be converted to an instance of 
    System.Windows.Media.Animation.KeyTime.
  
  
   typeDescriptorContext: Contextual information required for conversion.
   type: Type being evaluated for conversion.
   Returns: true if this type can be converted; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: KeyTimeConverter,typeDescriptorContext: ITypeDescriptorContext,cultureInfo: CultureInfo,value: object) -> object
  
   Attempts to convert a given object to an instance of 
    System.Windows.Media.Animation.KeyTime.
  
  
   typeDescriptorContext: Context information required for conversion.
   cultureInfo: Cultural information that is respected during conversion.
   value: The object being converted to an instance of 
    System.Windows.Media.Animation.KeyTime.
  
   Returns: A new instance of System.Windows.Media.Animation.KeyTime,based on the supplied 
    value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: KeyTimeConverter,typeDescriptorContext: ITypeDescriptorContext,cultureInfo: CultureInfo,value: object,destinationType: Type) -> object
  
   Attempts to convert an instance of System.Windows.Media.Animation.KeyTime to 
    another type.
  
  
   typeDescriptorContext: Context information required for conversion.
   cultureInfo: Cultural information that is respected during conversion.
   value: System.Windows.Media.Animation.KeyTime value to convert from.
   destinationType: Type being evaluated for conversion.
   Returns: A new object,based on value.
  """
  pass
