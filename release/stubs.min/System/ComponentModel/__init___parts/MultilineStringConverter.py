class MultilineStringConverter(TypeConverter):
 """
 Provides a type converter to convert multiline strings to a simple string.

 

 MultilineStringConverter()
 """
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: MultilineStringConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the given value object to the specified type,using the specified context and culture 

    information.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext  that provides a format context.

   culture: A System.Globalization.CultureInfo. If null is passed,the current culture is assumed.

   value: The System.Object to convert.

   destinationType: The System.Type to convert the value parameter to.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def GetProperties(self,*__args):
  """
  GetProperties(self: MultilineStringConverter,context: ITypeDescriptorContext,value: object,attributes: Array[Attribute]) -> PropertyDescriptorCollection

  

   Returns a collection of properties for the type of array specified by the value parameter,using 

    the specified context and attributes.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext  that provides a format context.

   value: An System.Object that specifies the type of array for which to get properties.

   attributes: An array of type System.Attribute that is used as a filter.

   Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that are exposed for 

    this data type,or null if there are no properties.
  """
  pass
 def GetPropertiesSupported(self,context=None):
  """
  GetPropertiesSupported(self: MultilineStringConverter,context: ITypeDescriptorContext) -> bool

  

   Returns whether this object supports properties,using the specified context.

  

   context: An System.ComponentModel.ITypeDescriptorContext  that provides a format context.

   Returns: true if erload:System.ComponentModel.MultilineStringConverter.GetProperties should be called to 

    find the properties of this object; otherwise,false.
  """
  pass
