class ColorConverter(TypeConverter):
 """
 Converts colors from one data type to another. Access this class through the System.ComponentModel.TypeDescriptor.

 

 ColorConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: ColorConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Determines if this converter can convert an object in the given source type to the native type 

    of the converter.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context. You can use this 

    object to get additional information about the environment from which this converter is being 

    invoked.

  

   sourceType: The type from which you want to convert.

   Returns: true if this object can perform the conversion; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: ColorConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Returns a value indicating whether this converter can convert an object to the given destination 

    type using the context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   destinationType: A System.Type that represents the type to which you want to convert.

   Returns: true if this converter can perform the operation; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: ColorConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the given object to the converter's native type.

  

   context: A System.ComponentModel.TypeDescriptor that provides a format context. You can use this object 

    to get additional information about the environment from which this converter is being invoked.

  

   culture: A System.Globalization.CultureInfo that specifies the culture to represent the color.

   value: The object to convert.

   Returns: An System.Object representing the converted value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: ColorConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the specified object to another type.

  

   context: A formatter context. Use this object to extract additional information about the environment 

    from which this converter is being invoked. Always check whether this value is null. Also,

    properties on the context object may return null.

  

   culture: A System.Globalization.CultureInfo that specifies the culture to represent the color.

   value: The object to convert.

   destinationType: The type to convert the object to.

   Returns: An System.Object representing the converted value.
  """
  pass
 def GetStandardValues(self,context=None):
  """
  GetStandardValues(self: ColorConverter,context: ITypeDescriptorContext) -> StandardValuesCollection

  

   Retrieves a collection containing a set of standard values for the data type for which this 

    validator is designed. This will return null if the data type does not support a standard set of 

    values.

  

  

   context: A formatter context. Use this object to extract additional information about the environment 

    from which this converter is being invoked. Always check whether this value is null. Also,

    properties on the context object may return null.

  

   Returns: A collection containing null or a standard set of valid values. The default implementation 

    always returns null.
  """
  pass
 def GetStandardValuesSupported(self,context=None):
  """
  GetStandardValuesSupported(self: ColorConverter,context: ITypeDescriptorContext) -> bool

  

   Determines if this object supports a standard set of values that can be chosen from a list.

  

   context: A System.ComponentModel.TypeDescriptor through which additional context can be provided.

   Returns: true if erload:System.Drawing.ColorConverter.GetStandardValues must be called to find a common 

    set of values the object supports; otherwise,false.
  """
  pass
