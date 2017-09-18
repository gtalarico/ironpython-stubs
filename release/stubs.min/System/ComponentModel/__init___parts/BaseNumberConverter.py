class BaseNumberConverter(TypeConverter):
 """ Provides a base type converter for nonfloating-point numerical types. """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: BaseNumberConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Determines if this converter can convert an object in the given source type to the native type 

    of the converter.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   sourceType: A System.Type that represents the type from which you want to convert.

   Returns: true if this converter can perform the operation; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: BaseNumberConverter,context: ITypeDescriptorContext,t: Type) -> bool

  

   Returns a value indicating whether this converter can convert an object to the given destination 

    type using the context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   t: A System.Type that represents the type to which you want to convert.

   Returns: true if this converter can perform the operation; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: BaseNumberConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the given object to the converter's native type.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo that specifies the culture to represent the number.

   value: The object to convert.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: BaseNumberConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the specified object to another type.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo that specifies the culture to represent the number.

   value: The object to convert.

   destinationType: The type to convert the object to.

   Returns: An System.Object that represents the converted value.
  """
  pass
