class ColumnHeaderConverter(ExpandableObjectConverter):
 """
 Provides a type converter to convert System.Windows.Forms.ColumnHeader objects from one type to another.

 

 ColumnHeaderConverter()
 """
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: ColumnHeaderConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Returns a value indicating whether the System.Windows.Forms.ColumnHeaderConverter can convert a 

    System.Windows.Forms.ColumnHeader to the specified type,using the specified context.

  

  

   context: A System.ComponentModel.ITypeDescriptorContext that provides a format context.

   destinationType: A type representing the type to convert to.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: ColumnHeaderConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the specified object to the specified type,using the specified context and culture 

    information.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo that represents information about a culture,such as language 

    and calendar system. Can be null.

  

   value: The System.Object to convert.

   destinationType: The System.Type to convert to.

   Returns: The System.Object that is the result of the conversion.
  """
  pass
