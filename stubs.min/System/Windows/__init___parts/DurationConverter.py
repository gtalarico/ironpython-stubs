class DurationConverter(TypeConverter):
 """
 Converts instances of System.Windows.Duration to and from other type representations.
 
 DurationConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: DurationConverter,td: ITypeDescriptorContext,t: Type) -> bool
  
   Determines if conversion from a given type to an instance of 
    System.Windows.Duration is possible.
  
  
   td: Context information used for conversion.
   t: Type being evaluated for conversion.
   Returns: true if t is of type System.String; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: DurationConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool
  
   Determines if conversion to a specified type is possible.
  
   context: Context information used for conversion.
   destinationType: Type being evaluated for conversion.
   Returns: true if destinationType is of type System.String; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: DurationConverter,td: ITypeDescriptorContext,cultureInfo: CultureInfo,value: object) -> object
  
   Converts a given string value to an instance of System.Windows.Duration.
  
   td: Context information used for conversion.
   cultureInfo: Cultural information that is respected during conversion.
   value: String value to convert to an instance of System.Windows.Duration.
   Returns: A new instance of System.Windows.Duration.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: DurationConverter,context: ITypeDescriptorContext,cultureInfo: CultureInfo,value: object,destinationType: Type) -> object
  
   Converts an instance of System.Windows.Duration to another type.
  
   context: Context information used for conversion.
   cultureInfo: Cultural information that is respected during conversion.
   value: Duration value to convert from.
   destinationType: Type being evaluated for conversion.
   Returns: A new instance of the destinationType.
  """
  pass
