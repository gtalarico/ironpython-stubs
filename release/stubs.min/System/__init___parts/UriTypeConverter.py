class UriTypeConverter(TypeConverter):
 """
 Converts a System.String type to a System.Uri type,and vice versa.

 

 UriTypeConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: UriTypeConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Returns whether this converter can convert an object of the given type to the type of this 

    converter.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext  that provides a format context.

   sourceType: A System.Type that represents the type that you want to convert from.

   Returns: true if sourceType is a System.String type or a System.Uri type can be assigned from sourceType; 

    otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: UriTypeConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Returns whether this converter can convert the object to the specified type,using the specified 

    context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext  that provides a format context.

   destinationType: A System.Type that represents the type that you want to convert to.

   Returns: true if destinationType is of type 

    System.ComponentModel.Design.Serialization.InstanceDescriptor,System.String,or System.Uri; 

    otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: UriTypeConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the given object to the type of this converter,using the specified context and culture 

    information.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext  that provides a format context.

   culture: The System.Globalization.CultureInfo to use as the current culture.

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: UriTypeConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts a given value object to the specified type,using the specified context and culture 

    information.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext  that provides a format context.

   culture: A System.Globalization.CultureInfo. If null is passed,the current culture is assumed.

   value: The System.Object to convert.

   destinationType: The System.Type to convert the value parameter to.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def IsValid(self,*__args):
  """
  IsValid(self: UriTypeConverter,context: ITypeDescriptorContext,value: object) -> bool

  

   Returns whether the given value object is a System.Uri or a System.Uri can be created from it.

  

   context: An System.ComponentModel.ITypeDescriptorContext  that provides a format context.

   value: The System.Object to test for validity.

   Returns: true if value is a System.Uri or a System.String from which a System.Uri can be created; 

    otherwise,false.
  """
  pass
