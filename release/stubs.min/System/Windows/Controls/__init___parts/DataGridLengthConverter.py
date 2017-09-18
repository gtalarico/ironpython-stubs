class DataGridLengthConverter(TypeConverter):
 """
 Converts instances of various types to and from instances of the System.Windows.Controls.DataGridLength class.

 

 DataGridLengthConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: DataGridLengthConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Determines whether an instance of the specified type can be converted to an instance of the 

    System.Windows.Controls.DataGridLength class.

  

  

   context: An object that provides a format context.

   sourceType: The type to convert from.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: DataGridLengthConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Determines whether an instance of the System.Windows.Controls.DataGridLength class can be 

    converted to an instance of the specified type.

  

  

   context: An object that provides a format context.

   destinationType: The type to convert to.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: DataGridLengthConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the specified object to an instance of the System.Windows.Controls.DataGridLength class.

  

   context: An object that provides a format context.

   culture: The object to use as the current culture.

   value: The value to convert.

   Returns: The converted value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: DataGridLengthConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts an instance of the System.Windows.Controls.DataGridLength class to an instance of the 

    specified type.

  

  

   context: An object that provides a format context.

   culture: The object to use as the current culture.

   value: The System.Windows.Controls.DataGridLength to convert.

   destinationType: The type to convert the value to.

   Returns: The converted value.
  """
  pass
