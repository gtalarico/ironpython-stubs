class OpacityConverter(TypeConverter):
 """
 Provides a type converter to convert opacity values to and from a string.

 

 OpacityConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: OpacityConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Returns a value indicating whether this converter can convert an object of the specified source 

    type to the native type of the converter that uses the specified context.

  

  

   context: A System.ComponentModel.ITypeDescriptorContext that provides information about the context of a 

    type converter.

  

   sourceType: The System.Type that represents the type you want to convert from.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: OpacityConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the specified object to the converter's native type.

  

   context: A System.ComponentModel.ITypeDescriptorContext that provides information about the context of a 

    type converter.

  

   culture: The locale information for the conversion.

   value: The object to convert.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: OpacityConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts from the converter's native type to a value of the destination type.

  

   context: A System.ComponentModel.ITypeDescriptorContext that provides information about the context of a 

    type converter.

  

   culture: The locale information for the conversion.

   value: The value to convert.

   destinationType: The type to convert the object to.

   Returns: An System.Object that represents the converted value.
  """
  pass
