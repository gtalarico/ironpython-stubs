class NullableConverter(TypeConverter):
 """
 Provides automatic conversion between a nullable type and its underlying primitive type.

 

 NullableConverter(type: Type)
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: NullableConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Returns whether this converter can convert an object of the given type to the type of this 

    converter,using the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext  that provides a format context.

   sourceType: A System.Type that represents the type you want to convert from.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: NullableConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Returns whether this converter can convert the object to the specified type,using the specified 

    context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   destinationType: A System.Type that represents the type you want to convert to.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: NullableConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the given object to the type of this converter,using the specified context and culture 

    information.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: The System.Globalization.CultureInfo to use as the current culture.

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: NullableConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the given value object to the specified type,using the specified context and culture 

    information.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: The System.Globalization.CultureInfo to use as the current culture.

   value: The System.Object to convert.

   destinationType: The System.Type to convert the value parameter to.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def CreateInstance(self,*__args):
  """
  CreateInstance(self: NullableConverter,context: ITypeDescriptorContext,propertyValues: IDictionary) -> object

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   propertyValues: An System.Collections.IDictionary of new property values.

   Returns: An System.Object representing the given System.Collections.IDictionary,or null if the object 

    cannot be created. This method always returns null.
  """
  pass
 def GetCreateInstanceSupported(self,context=None):
  """
  GetCreateInstanceSupported(self: NullableConverter,context: ITypeDescriptorContext) -> bool

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true if changing a property on this object requires a call to 

    System.ComponentModel.TypeConverter.CreateInstance(System.Collections.IDictionary) to create a 

    new value; otherwise,false.
  """
  pass
 def GetProperties(self,*__args):
  """
  GetProperties(self: NullableConverter,context: ITypeDescriptorContext,value: object,attributes: Array[Attribute]) -> PropertyDescriptorCollection

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   value: An System.Object that specifies the type of array for which to get properties.

   attributes: An array of type System.Attribute that is used as a filter.

   Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that are exposed for 

    this data type,or null if there are no properties.
  """
  pass
 def GetPropertiesSupported(self,context=None):
  """
  GetPropertiesSupported(self: NullableConverter,context: ITypeDescriptorContext) -> bool

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true if System.ComponentModel.TypeConverter.GetProperties(System.Object) should be called to 

    find the properties of this object; otherwise,false.
  """
  pass
 def GetStandardValues(self,context=None):
  """
  GetStandardValues(self: NullableConverter,context: ITypeDescriptorContext) -> StandardValuesCollection

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context that can be used 

    to extract additional information about the environment from which this converter is invoked. 

    This parameter or properties of this parameter can be null.

  

   Returns: A System.ComponentModel.TypeConverter.StandardValuesCollection that holds a standard set of 

    valid values,or null if the data type does not support a standard set of values.
  """
  pass
 def GetStandardValuesExclusive(self,context=None):
  """
  GetStandardValuesExclusive(self: NullableConverter,context: ITypeDescriptorContext) -> bool

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true if the System.ComponentModel.TypeConverter.StandardValuesCollection returned from 

    System.ComponentModel.TypeConverter.GetStandardValues is an exhaustive list of possible values; 

    false if other values are possible.
  """
  pass
 def GetStandardValuesSupported(self,context=None):
  """
  GetStandardValuesSupported(self: NullableConverter,context: ITypeDescriptorContext) -> bool

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true if System.ComponentModel.TypeConverter.GetStandardValues should be called to find a common 

    set of values the object supports; otherwise,false.
  """
  pass
 def IsValid(self,*__args):
  """
  IsValid(self: NullableConverter,context: ITypeDescriptorContext,value: object) -> bool

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   value: The System.Object to test for validity.
  """
  pass
 @staticmethod
 def __new__(self,type):
  """ __new__(cls: type,type: Type) """
  pass
 NullableType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the nullable type.



Get: NullableType(self: NullableConverter) -> Type



"""

 UnderlyingType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the underlying type.



Get: UnderlyingType(self: NullableConverter) -> Type



"""

 UnderlyingTypeConverter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the underlying type converter.



Get: UnderlyingTypeConverter(self: NullableConverter) -> TypeConverter



"""


