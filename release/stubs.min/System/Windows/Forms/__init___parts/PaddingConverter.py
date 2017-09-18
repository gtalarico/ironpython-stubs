class PaddingConverter(TypeConverter):
 """
 Provides a type converter to convert System.Windows.Forms.Padding values to and from various other representations.

 

 PaddingConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: PaddingConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Returns whether this converter can convert an object of one type to the type of this converter.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   sourceType: A System.Type that represents the type you wish to convert from.

   Returns: true if this object can perform the conversion; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: PaddingConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Returns whether this converter can convert the object to the specified type,using the specified 

    context.

  

  

   destinationType: A T:System.Type that represents the type you want to convert to.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: PaddingConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: The System.Globalization.CultureInfo to use as the current culture.

   value: The System.Object to convert.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: PaddingConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo. If null is passed,the current culture is assumed.

   value: The System.Object to convert.

   destinationType: The System.Type to convert the value parameter to.
  """
  pass
 def CreateInstance(self,*__args):
  """
  CreateInstance(self: PaddingConverter,context: ITypeDescriptorContext,propertyValues: IDictionary) -> object

  

   Creates an instance of the type that this System.ComponentModel.TypeConverter is associated 

    with,using the specified context,given a set of property values for the object.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   propertyValues: An System.Collections.IDictionary of new property values.

   Returns: An System.Object representing the given System.Collections.IDictionary,or null if the object 

    cannot be created. This method always returns null.
  """
  pass
 def GetCreateInstanceSupported(self,context=None):
  """
  GetCreateInstanceSupported(self: PaddingConverter,context: ITypeDescriptorContext) -> bool

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
  """
  pass
 def GetProperties(self,*__args):
  """
  GetProperties(self: PaddingConverter,context: ITypeDescriptorContext,value: object,attributes: Array[Attribute]) -> PropertyDescriptorCollection

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   value: An System.Object that specifies the type of array for which to get properties.

   attributes: An array of type System.Attribute that is used as a filter.
  """
  pass
 def GetPropertiesSupported(self,context=None):
  """
  GetPropertiesSupported(self: PaddingConverter,context: ITypeDescriptorContext) -> bool

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
  """
  pass
