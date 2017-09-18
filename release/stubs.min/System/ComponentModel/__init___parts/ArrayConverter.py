class ArrayConverter(CollectionConverter):
 """
 Provides a type converter to convert System.Array objects to and from various other representations.

 

 ArrayConverter()
 """
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: ArrayConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the given value object to the specified destination type.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: The culture into which value will be converted.

   value: The System.Object to convert.

   destinationType: The System.Type to convert the value to.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def GetProperties(self,*__args):
  """
  GetProperties(self: ArrayConverter,context: ITypeDescriptorContext,value: object,attributes: Array[Attribute]) -> PropertyDescriptorCollection

  

   Gets a collection of properties for the type of array specified by the value parameter.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   value: An System.Object that specifies the type of array to get the properties for.

   attributes: An array of type System.Attribute that will be used as a filter.

   Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that are exposed for an 

    array,or null if there are no properties.
  """
  pass
 def GetPropertiesSupported(self,context=None):
  """
  GetPropertiesSupported(self: ArrayConverter,context: ITypeDescriptorContext) -> bool

  

   Gets a value indicating whether this object supports properties.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true because 

    System.ComponentModel.ArrayConverter.GetProperties(System.ComponentModel.ITypeDescriptorContext,S

    ystem.Object,System.Attribute[]) should be called to find the properties of this object. This 

    method never returns false.
  """
  pass
