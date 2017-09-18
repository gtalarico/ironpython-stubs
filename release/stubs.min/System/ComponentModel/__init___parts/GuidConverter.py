class GuidConverter(TypeConverter):
 """
 Provides a type converter to convert System.Guid objects to and from various other representations.

 

 GuidConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: GuidConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Gets a value indicating whether this converter can convert an object in the given source type to 

    a GUID object using the context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   sourceType: A System.Type that represents the type you wish to convert from.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: GuidConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Gets a value indicating whether this converter can convert an object to the given destination 

    type using the context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   destinationType: A System.Type that represents the type you wish to convert to.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: GuidConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the given object to a GUID object.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: An optional System.Globalization.CultureInfo. If not supplied,the current culture is assumed.

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: GuidConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the given object to another type.

  

   context: A formatter context.

   culture: The culture into which value will be converted.

   value: The object to convert.

   destinationType: The type to convert the object to.

   Returns: The converted object.
  """
  pass
