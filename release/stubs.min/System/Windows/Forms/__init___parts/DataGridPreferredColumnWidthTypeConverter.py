class DataGridPreferredColumnWidthTypeConverter(TypeConverter):
 """
 Converts the value of an object to a different data type.

 

 DataGridPreferredColumnWidthTypeConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: DataGridPreferredColumnWidthTypeConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Gets a value that specifies whether the converter can convert an object in the given source type 

    to the native type of the converter.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   sourceType: A System.Type that represents the type you want to convert from.

   Returns: true,if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: DataGridPreferredColumnWidthTypeConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the given object to the native type of the converter.

  

   context: An System.ComponentModel.ITypeDescriptorContext that a provides format context.

   culture: A System.Globalization.CultureInfo to use for the current culture.

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: DataGridPreferredColumnWidthTypeConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the given value to the native type of the converter.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides format context.

   culture: A System.Globalization.CultureInfo to use for the current culture.

   value: The System.Object to convert.

   destinationType: The System.Type of the conversion.

   Returns: An System.Object that represents the converted value.
  """
  pass
