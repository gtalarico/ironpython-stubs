class StringConverter(TypeConverter):
 """
 Provides a type converter to convert string objects to and from other representations.

 

 StringConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: StringConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Gets a value indicating whether this converter can convert an object in the given source type to 

    a string using the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   sourceType: A System.Type that represents the type you wish to convert from.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: StringConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the specified value object to a System.String object.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: The System.Globalization.CultureInfo to use.

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.
  """
  pass
