class TypeConverter(object):
 """
 Provides a unified way of converting types of values to other types,as well as for accessing standard values and subproperties.

 

 TypeConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: TypeConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Returns whether this converter can convert an object of the given type to the type of this 

    converter,using the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   sourceType: A System.Type that represents the type you want to convert from.

   Returns: true if this converter can perform the conversion; otherwise,false.

  CanConvertFrom(self: TypeConverter,sourceType: Type) -> bool

  

   Returns whether this converter can convert an object of the given type to the type of this 

    converter.

  

  

   sourceType: A System.Type that represents the type you want to convert from.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: TypeConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Returns whether this converter can convert the object to the specified type,using the specified 

    context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   destinationType: A System.Type that represents the type you want to convert to.

   Returns: true if this converter can perform the conversion; otherwise,false.

  CanConvertTo(self: TypeConverter,destinationType: Type) -> bool

  

   Returns whether this converter can convert the object to the specified type.

  

   destinationType: A System.Type that represents the type you want to convert to.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: TypeConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the given object to the type of this converter,using the specified context and culture 

    information.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: The System.Globalization.CultureInfo to use as the current culture.

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.

  ConvertFrom(self: TypeConverter,value: object) -> object

  

   Converts the given value to the type of this converter.

  

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def ConvertFromInvariantString(self,*__args):
  """
  ConvertFromInvariantString(self: TypeConverter,context: ITypeDescriptorContext,text: str) -> object

  

   Converts the given string to the type of this converter,using the invariant culture and the 

    specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   text: The System.String to convert.

   Returns: An System.Object that represents the converted text.

  ConvertFromInvariantString(self: TypeConverter,text: str) -> object

  

   Converts the given string to the type of this converter,using the invariant culture.

  

   text: The System.String to convert.

   Returns: An System.Object that represents the converted text.
  """
  pass
 def ConvertFromString(self,*__args):
  """
  ConvertFromString(self: TypeConverter,context: ITypeDescriptorContext,culture: CultureInfo,text: str) -> object

  

   Converts the given text to an object,using the specified context and culture information.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo. If null is passed,the current culture is assumed.

   text: The System.String to convert.

   Returns: An System.Object that represents the converted text.

  ConvertFromString(self: TypeConverter,context: ITypeDescriptorContext,text: str) -> object

  

   Converts the given text to an object,using the specified context.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   text: The System.String to convert.

   Returns: An System.Object that represents the converted text.

  ConvertFromString(self: TypeConverter,text: str) -> object

  

   Converts the specified text to an object.

  

   text: The text representation of the object to convert.

   Returns: An System.Object that represents the converted text.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: TypeConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the given value object to the specified type,using the specified context and culture 

    information.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo. If null is passed,the current culture is assumed.

   value: The System.Object to convert.

   destinationType: The System.Type to convert the value parameter to.

   Returns: An System.Object that represents the converted value.

  ConvertTo(self: TypeConverter,value: object,destinationType: Type) -> object

  

   Converts the given value object to the specified type,using the arguments.

  

   value: The System.Object to convert.

   destinationType: The System.Type to convert the value parameter to.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def ConvertToInvariantString(self,*__args):
  """
  ConvertToInvariantString(self: TypeConverter,context: ITypeDescriptorContext,value: object) -> str

  

   Converts the specified value to a culture-invariant string representation,using the specified 

    context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   value: The System.Object to convert.

   Returns: A System.String that represents the converted value.

  ConvertToInvariantString(self: TypeConverter,value: object) -> str

  

   Converts the specified value to a culture-invariant string representation.

  

   value: The System.Object to convert.

   Returns: A System.String that represents the converted value.
  """
  pass
 def ConvertToString(self,*__args):
  """
  ConvertToString(self: TypeConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> str

  

   Converts the given value to a string representation,using the specified context and culture 

    information.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo. If null is passed,the current culture is assumed.

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.

  ConvertToString(self: TypeConverter,context: ITypeDescriptorContext,value: object) -> str

  

   Converts the given value to a string representation,using the given context.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.

  ConvertToString(self: TypeConverter,value: object) -> str

  

   Converts the specified value to a string representation.

  

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def CreateInstance(self,*__args):
  """
  CreateInstance(self: TypeConverter,context: ITypeDescriptorContext,propertyValues: IDictionary) -> object

  

   Creates an instance of the type that this System.ComponentModel.TypeConverter is associated 

    with,using the specified context,given a set of property values for the object.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   propertyValues: An System.Collections.IDictionary of new property values.

   Returns: An System.Object representing the given System.Collections.IDictionary,or null if the object 

    cannot be created. This method always returns null.

  

  CreateInstance(self: TypeConverter,propertyValues: IDictionary) -> object

  

   Re-creates an System.Object given a set of property values for the object.

  

   propertyValues: An System.Collections.IDictionary that represents a dictionary of new property values.

   Returns: An System.Object representing the given System.Collections.IDictionary,or null if the object 

    cannot be created. This method always returns null.
  """
  pass
 def GetConvertFromException(self,*args):
  """
  GetConvertFromException(self: TypeConverter,value: object) -> Exception

  

   Returns an exception to throw when a conversion cannot be performed.

  

   value: The System.Object to convert,or null if the object is not available.

   Returns: An System.Exception that represents the exception to throw when a conversion cannot be performed.
  """
  pass
 def GetConvertToException(self,*args):
  """
  GetConvertToException(self: TypeConverter,value: object,destinationType: Type) -> Exception

  

   Returns an exception to throw when a conversion cannot be performed.

  

   value: The System.Object to convert,or null if the object is not available.

   destinationType: A System.Type that represents the type the conversion was trying to convert to.

   Returns: An System.Exception that represents the exception to throw when a conversion cannot be performed.
  """
  pass
 def GetCreateInstanceSupported(self,context=None):
  """
  GetCreateInstanceSupported(self: TypeConverter,context: ITypeDescriptorContext) -> bool

  

   Returns whether changing a value on this object requires a call to 

    System.ComponentModel.TypeConverter.CreateInstance(System.Collections.IDictionary) to create a 

    new value,using the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true if changing a property on this object requires a call to 

    System.ComponentModel.TypeConverter.CreateInstance(System.Collections.IDictionary) to create a 

    new value; otherwise,false.

  

  GetCreateInstanceSupported(self: TypeConverter) -> bool

  

   Returns whether changing a value on this object requires a call to the 

    System.ComponentModel.TypeConverter.CreateInstance(System.Collections.IDictionary) method to 

    create a new value.

  

   Returns: true if changing a property on this object requires a call to 

    System.ComponentModel.TypeConverter.CreateInstance(System.Collections.IDictionary) to create a 

    new value; otherwise,false.
  """
  pass
 def GetProperties(self,*__args):
  """
  GetProperties(self: TypeConverter,context: ITypeDescriptorContext,value: object,attributes: Array[Attribute]) -> PropertyDescriptorCollection

  

   Returns a collection of properties for the type of array specified by the value parameter,using 

    the specified context and attributes.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   value: An System.Object that specifies the type of array for which to get properties.

   attributes: An array of type System.Attribute that is used as a filter.

   Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that are exposed for 

    this data type,or null if there are no properties.

  

  GetProperties(self: TypeConverter,context: ITypeDescriptorContext,value: object) -> PropertyDescriptorCollection

  

   Returns a collection of properties for the type of array specified by the value parameter,using 

    the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   value: An System.Object that specifies the type of array for which to get properties.

   Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that are exposed for 

    this data type,or null if there are no properties.

  

  GetProperties(self: TypeConverter,value: object) -> PropertyDescriptorCollection

  

   Returns a collection of properties for the type of array specified by the value parameter.

  

   value: An System.Object that specifies the type of array for which to get properties.

   Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that are exposed for 

    this data type,or null if there are no properties.
  """
  pass
 def GetPropertiesSupported(self,context=None):
  """
  GetPropertiesSupported(self: TypeConverter,context: ITypeDescriptorContext) -> bool

  

   Returns whether this object supports properties,using the specified context.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true if System.ComponentModel.TypeConverter.GetProperties(System.Object) should be called to 

    find the properties of this object; otherwise,false.

  

  GetPropertiesSupported(self: TypeConverter) -> bool

  

   Returns whether this object supports properties.

   Returns: true if System.ComponentModel.TypeConverter.GetProperties(System.Object) should be called to 

    find the properties of this object; otherwise,false.
  """
  pass
 def GetStandardValues(self,context=None):
  """
  GetStandardValues(self: TypeConverter,context: ITypeDescriptorContext) -> StandardValuesCollection

  

   Returns a collection of standard values for the data type this type converter is designed for 

    when provided with a format context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context that can be used 

    to extract additional information about the environment from which this converter is invoked. 

    This parameter or properties of this parameter can be null.

  

   Returns: A System.ComponentModel.TypeConverter.StandardValuesCollection that holds a standard set of 

    valid values,or null if the data type does not support a standard set of values.

  

  GetStandardValues(self: TypeConverter) -> ICollection

  

   Returns a collection of standard values from the default context for the data type this type 

    converter is designed for.

  

   Returns: A System.ComponentModel.TypeConverter.StandardValuesCollection containing a standard set of 

    valid values,or null if the data type does not support a standard set of values.
  """
  pass
 def GetStandardValuesExclusive(self,context=None):
  """
  GetStandardValuesExclusive(self: TypeConverter,context: ITypeDescriptorContext) -> bool

  

   Returns whether the collection of standard values returned from 

    System.ComponentModel.TypeConverter.GetStandardValues is an exclusive list of possible values,

    using the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true if the System.ComponentModel.TypeConverter.StandardValuesCollection returned from 

    System.ComponentModel.TypeConverter.GetStandardValues is an exhaustive list of possible values; 

    false if other values are possible.

  

  GetStandardValuesExclusive(self: TypeConverter) -> bool

  

   Returns whether the collection of standard values returned from 

    System.ComponentModel.TypeConverter.GetStandardValues is an exclusive list.

  

   Returns: true if the System.ComponentModel.TypeConverter.StandardValuesCollection returned from 

    System.ComponentModel.TypeConverter.GetStandardValues is an exhaustive list of possible values; 

    false if other values are possible.
  """
  pass
 def GetStandardValuesSupported(self,context=None):
  """
  GetStandardValuesSupported(self: TypeConverter,context: ITypeDescriptorContext) -> bool

  

   Returns whether this object supports a standard set of values that can be picked from a list,

    using the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true if System.ComponentModel.TypeConverter.GetStandardValues should be called to find a common 

    set of values the object supports; otherwise,false.

  

  GetStandardValuesSupported(self: TypeConverter) -> bool

  

   Returns whether this object supports a standard set of values that can be picked from a list.

   Returns: true if System.ComponentModel.TypeConverter.GetStandardValues should be called to find a common 

    set of values the object supports; otherwise,false.
  """
  pass
 def IsValid(self,*__args):
  """
  IsValid(self: TypeConverter,context: ITypeDescriptorContext,value: object) -> bool

  

   Returns whether the given value object is valid for this type and for the specified context.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   value: The System.Object to test for validity.

   Returns: true if the specified value is valid for this object; otherwise,false.

  IsValid(self: TypeConverter,value: object) -> bool

  

   Returns whether the given value object is valid for this type.

  

   value: The object to test for validity.

   Returns: true if the specified value is valid for this object; otherwise,false.
  """
  pass
 def SortProperties(self,*args):
  """
  SortProperties(self: TypeConverter,props: PropertyDescriptorCollection,names: Array[str]) -> PropertyDescriptorCollection

  

   Sorts a collection of properties.

  

   props: A System.ComponentModel.PropertyDescriptorCollection that has the properties to sort.

   names: An array of names in the order you want the properties to appear in the collection.

   Returns: A System.ComponentModel.PropertyDescriptorCollection that contains the sorted properties.
  """
  pass
 SimplePropertyDescriptor=None
 StandardValuesCollection=None

