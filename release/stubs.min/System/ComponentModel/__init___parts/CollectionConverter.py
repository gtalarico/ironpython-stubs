class CollectionConverter(TypeConverter):
 """
 Provides a type converter to convert collection objects to and from various other representations.

 

 CollectionConverter()
 """
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: CollectionConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the given value object to the specified destination type.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: The culture to which value will be converted.

   value: The System.Object to convert. This parameter must inherit from System.Collections.ICollection.

   destinationType: The System.Type to convert the value to.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def GetProperties(self,*__args):
  """
  GetProperties(self: CollectionConverter,context: ITypeDescriptorContext,value: object,attributes: Array[Attribute]) -> PropertyDescriptorCollection

  

   Gets a collection of properties for the type of array specified by the value parameter using the 

    specified context and attributes.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   value: An System.Object that specifies the type of array to get the properties for.

   attributes: An array of type System.Attribute that will be used as a filter.

   Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that are exposed for 

    this data type,or null if there are no properties. This method always returns null.
  """
  pass
 def GetPropertiesSupported(self,context=None):
  """
  GetPropertiesSupported(self: CollectionConverter,context: ITypeDescriptorContext) -> bool

  

   Gets a value indicating whether this object supports properties.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: false because 

    System.ComponentModel.CollectionConverter.GetProperties(System.ComponentModel.ITypeDescriptorCont

    ext,System.Object,System.Attribute[]) should not be called to find the properties of this 

    object. This method never returns true.
  """
  pass
