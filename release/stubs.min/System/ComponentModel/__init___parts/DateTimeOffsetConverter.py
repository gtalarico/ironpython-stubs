class DateTimeOffsetConverter(TypeConverter):
 """
 Provides a type converter to convert System.DateTimeOffset structures to and from various other representations.

 

 DateTimeOffsetConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: DateTimeOffsetConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Returns a value that indicates whether an object of the specified source type can be converted 

    to a System.DateTimeOffset.

  

  

   context: The date format context.

   sourceType: The source type to check.

   Returns: true if the specified type can be converted to a System.DateTimeOffset; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: DateTimeOffsetConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Returns a value that indicates whether a System.DateTimeOffset can be converted to an object of 

    the specified type.

  

  

   context: The date format context.

   destinationType: The destination type to check.

   Returns: true if a System.DateTimeOffset can be converted to the specified type; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: DateTimeOffsetConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the specified object to a System.DateTimeOffset.

  

   context: The date format context.

   culture: The date culture.

   value: The object to be converted.

   Returns: A System.DateTimeOffset that represents the specified object.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: DateTimeOffsetConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts a System.DateTimeOffset to an object of the specified type.

  

   context: The date format context.

   culture: The date culture.

   value: The System.DateTimeOffset to be converted.

   destinationType: The type to convert to.

   Returns: An object of the specified type that represents the System.DateTimeOffset.
  """
  pass
