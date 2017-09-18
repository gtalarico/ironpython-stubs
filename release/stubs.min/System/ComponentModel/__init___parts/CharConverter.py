class CharConverter(TypeConverter):
 """
 Provides a type converter to convert Unicode character objects to and from various other representations.

 

 CharConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: CharConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Gets a value indicating whether this converter can convert an object in the given source type to 

    a Unicode character object using the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   sourceType: A System.Type that represents the type you want to convert from.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: CharConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the given object to a Unicode character object.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: The culture into which value will be converted.

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: CharConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the given value object to a Unicode character object using the arguments.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: The culture into which value will be converted.

   value: The System.Object to convert.

   destinationType: The System.Type to convert the value to.

   Returns: An System.Object that represents the converted value.
  """
  pass
