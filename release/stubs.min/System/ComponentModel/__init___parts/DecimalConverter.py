class DecimalConverter(BaseNumberConverter):
 """
 Provides a type converter to convert System.Decimal objects to and from various other representations.

 

 DecimalConverter()
 """
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: DecimalConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Gets a value indicating whether this converter can convert an object to the given destination 

    type using the context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   destinationType: A System.Type that represents the type you wish to convert to.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: DecimalConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the given value object to a System.Decimal using the arguments.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: An optional System.Globalization.CultureInfo. If not supplied,the current culture is assumed.

   value: The System.Object to convert.

   destinationType: The System.Type to convert the value to.

   Returns: An System.Object that represents the converted value.
  """
  pass
