class ExpandableObjectConverter(TypeConverter):
 """
 Provides a type converter to convert expandable objects to and from various other representations.

 

 ExpandableObjectConverter()
 """
 def GetProperties(self,*__args):
  """
  GetProperties(self: ExpandableObjectConverter,context: ITypeDescriptorContext,value: object,attributes: Array[Attribute]) -> PropertyDescriptorCollection

  

   Gets a collection of properties for the type of object specified by the value parameter.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   value: An System.Object that specifies the type of object to get the properties for.

   attributes: An array of type System.Attribute that will be used as a filter.

   Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that are exposed for 

    the component,or null if there are no properties.
  """
  pass
 def GetPropertiesSupported(self,context=None):
  """
  GetPropertiesSupported(self: ExpandableObjectConverter,context: ITypeDescriptorContext) -> bool

  

   Gets a value indicating whether this object supports properties using the specified context.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true because System.ComponentModel.TypeConverter.GetProperties(System.Object) should be called 

    to find the properties of this object. This method never returns false.
  """
  pass
