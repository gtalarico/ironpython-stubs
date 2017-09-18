class EnumConverter(TypeConverter):
 """
 Provides a type converter to convert System.Enum objects to and from various other representations.

 

 EnumConverter(type: Type)
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: EnumConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Gets a value indicating whether this converter can convert an object in the given source type to 

    an enumeration object using the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   sourceType: A System.Type that represents the type you wish to convert from.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: EnumConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Gets a value indicating whether this converter can convert an object to the given destination 

    type using the context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   destinationType: A System.Type that represents the type you wish to convert to.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: EnumConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the specified value object to an enumeration object.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: An optional System.Globalization.CultureInfo. If not supplied,the current culture is assumed.

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: EnumConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the given value object to the specified destination type.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: An optional System.Globalization.CultureInfo. If not supplied,the current culture is assumed.

   value: The System.Object to convert.

   destinationType: The System.Type to convert the value to.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def GetStandardValues(self,context=None):
  """
  GetStandardValues(self: EnumConverter,context: ITypeDescriptorContext) -> StandardValuesCollection

  

   Gets a collection of standard values for the data type this validator is designed for.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: A System.ComponentModel.TypeConverter.StandardValuesCollection that holds a standard set of 

    valid values,or null if the data type does not support a standard set of values.
  """
  pass
 def GetStandardValuesExclusive(self,context=None):
  """
  GetStandardValuesExclusive(self: EnumConverter,context: ITypeDescriptorContext) -> bool

  

   Gets a value indicating whether the list of standard values returned from 

    System.ComponentModel.TypeConverter.GetStandardValues is an exclusive list using the specified 

    context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true if the System.ComponentModel.TypeConverter.StandardValuesCollection returned from 

    System.ComponentModel.TypeConverter.GetStandardValues is an exhaustive list of possible values; 

    false if other values are possible.
  """
  pass
 def GetStandardValuesSupported(self,context=None):
  """
  GetStandardValuesSupported(self: EnumConverter,context: ITypeDescriptorContext) -> bool

  

   Gets a value indicating whether this object supports a standard set of values that can be picked 

    from a list using the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true because System.ComponentModel.TypeConverter.GetStandardValues should be called to find a 

    common set of values the object supports. This method never returns false.
  """
  pass
 def IsValid(self,*__args):
  """
  IsValid(self: EnumConverter,context: ITypeDescriptorContext,value: object) -> bool

  

   Gets a value indicating whether the given object value is valid for this type.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   value: The System.Object to test.

   Returns: true if the specified value is valid for this object; otherwise,false.
  """
  pass
 @staticmethod
 def __new__(self,type):
  """ __new__(cls: type,type: Type) """
  pass
 Comparer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an System.Collections.IComparer that can be used to sort the values of the enumeration.



"""

 EnumType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies the type of the enumerator this converter is associated with.



"""

 Values=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.ComponentModel.TypeConverter.StandardValuesCollection that specifies the possible values for the enumeration.



"""


