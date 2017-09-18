class RepeatBehaviorConverter(TypeConverter):
 """
 Converts instances of System.Windows.Media.Animation.RepeatBehavior to and from other data types.

 

 RepeatBehaviorConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: RepeatBehaviorConverter,td: ITypeDescriptorContext,t: Type) -> bool

  

   Determines whether or not conversion from a specified data type is possible.

  

   td: Context information required for conversion.

   t: Type to evaluate for conversion.

   Returns: true if conversion is supported; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: RepeatBehaviorConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Determines if conversion to a specified type is possible.

  

   context: Context information required for conversion.

   destinationType: Destination type being evaluated for conversion.

   Returns: true if conversion is possible; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: RepeatBehaviorConverter,td: ITypeDescriptorContext,cultureInfo: CultureInfo,value: object) -> object

  

   Converts a given string value to an instance of 

    System.Windows.Media.Animation.RepeatBehaviorConverter.

  

  

   td: Context information required for conversion.

   cultureInfo: Cultural information to respect during conversion.

   value: Object being evaluated for conversion.

   Returns: A new System.Windows.Media.Animation.RepeatBehavior object based on value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: RepeatBehaviorConverter,context: ITypeDescriptorContext,cultureInfo: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts an instance of System.Windows.Media.Animation.RepeatBehavior to a supported destination 

    type.

  

  

   context: Context information required for conversion.

   cultureInfo: Cultural information to respect during conversion.

   value: Object being evaluated for conversion.

   destinationType: Destination type being evaluated for conversion.

   Returns: The only supported destination types are System.String and 

    System.ComponentModel.Design.Serialization.InstanceDescriptor.
  """
  pass
