class DataGridViewCellStyleConverter(TypeConverter):
 """
 Converts System.Windows.Forms.DataGridViewCellStyle objects to and from other data types.

 

 DataGridViewCellStyleConverter()
 """
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: DataGridViewCellStyleConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   destinationType: A System.Type that represents the type you want to convert to.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: DataGridViewCellStyleConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo. If null is passed,the current culture is assumed.

   value: The System.Object to convert.

   destinationType: The System.Type to convert the value parameter to.

   Returns: An System.Object that represents the converted value.
  """
  pass
