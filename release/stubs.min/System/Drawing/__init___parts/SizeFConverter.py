class SizeFConverter(TypeConverter):
 """
 Converts System.Drawing.SizeF objects from one type to another.

 

 SizeFConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: SizeFConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Returns a value indicating whether the converter can convert from the type specified to the 

    System.Drawing.SizeF type,using the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext through which additional context can be supplied.

   sourceType: A System.Type the represents the type you wish to convert from.

   Returns: true to indicate the conversion can be performed; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: SizeFConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Returns a value indicating whether the System.Drawing.SizeFConverter can convert a 

    System.Drawing.SizeF to the specified type.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext through which additional context can be supplied.

   destinationType: A System.Type that represents the type you want to convert from.

   Returns: true if this converter can perform the conversion otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: SizeFConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: The System.Globalization.CultureInfo to use as the current culture.

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: SizeFConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo. If null is passed,the current culture is assumed.

   value: The System.Object to convert.

   destinationType: The System.Type to convert the value parameter to.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def CreateInstance(self,*__args):
  """
  CreateInstance(self: SizeFConverter,context: ITypeDescriptorContext,propertyValues: IDictionary) -> object

  

   Creates an instance of a System.Drawing.SizeF with the specified property values using the 

    specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext through which additional context can be supplied.

   propertyValues: An System.Collections.IDictionary containing property names and values.

   Returns: An System.Object representing the new System.Drawing.SizeF,or null if the object cannot be 

    created.
  """
  pass
 def GetCreateInstanceSupported(self,context=None):
  """
  GetCreateInstanceSupported(self: SizeFConverter,context: ITypeDescriptorContext) -> bool

  

   Returns a value indicating whether changing a value on this object requires a call to the 

    erload:System.Drawing.SizeFConverter.CreateInstance method to create a new value.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context. This may be null.

   Returns: Always returns true.
  """
  pass
 def GetProperties(self,*__args):
  """
  GetProperties(self: SizeFConverter,context: ITypeDescriptorContext,value: object,attributes: Array[Attribute]) -> PropertyDescriptorCollection

  

   Retrieves a set of properties for the System.Drawing.SizeF type using the specified context and 

    attributes.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext through which additional context can be supplied.

   value: The System.Object to return properties for.

   attributes: An array of System.Attribute objects that describe the properties.

   Returns: A System.ComponentModel.PropertyDescriptorCollection containing the properties.
  """
  pass
 def GetPropertiesSupported(self,context=None):
  """
  GetPropertiesSupported(self: SizeFConverter,context: ITypeDescriptorContext) -> bool

  

   Returns whether the System.Drawing.SizeF type supports properties.

  

   context: An System.ComponentModel.ITypeDescriptorContext through which additional context can be supplied.

   Returns: Always returns true.
  """
  pass
