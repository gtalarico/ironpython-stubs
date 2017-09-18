class ListBindingConverter(TypeConverter):
 """
 Provides a type converter to convert System.Windows.Forms.Binding objects to and from various other representations.

 

 ListBindingConverter()
 """
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: ListBindingConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   destinationType: A System.Type that represents the type you want to convert to.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: ListBindingConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo. If null is passed,the current culture is assumed.

   value: The System.Object to convert.

   destinationType: The System.Type to convert the value parameter to.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def CreateInstance(self,*__args):
  """
  CreateInstance(self: ListBindingConverter,context: ITypeDescriptorContext,propertyValues: IDictionary) -> object

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   propertyValues: An System.Collections.IDictionary of new property values.

   Returns: An System.Object representing the given System.Collections.IDictionary,or null if the object 

    cannot be created. This method always returns null.
  """
  pass
 def GetCreateInstanceSupported(self,context=None):
  """
  GetCreateInstanceSupported(self: ListBindingConverter,context: ITypeDescriptorContext) -> bool

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true if changing a property on this object requires a call to 

    System.ComponentModel.TypeConverter.CreateInstance(System.Collections.IDictionary) to create a 

    new value; otherwise,false.
  """
  pass
