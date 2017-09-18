class ReferenceConverter(TypeConverter):
 """
 Provides a type converter to convert object references to and from other representations.

 

 ReferenceConverter(type: Type)
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: ReferenceConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Gets a value indicating whether this converter can convert an object in the given source type to 

    a reference object using the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   sourceType: A System.Type that represents the type you wish to convert from.

   Returns: true if this object can perform the conversion; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: ReferenceConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the given object to the reference type.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo that specifies the culture used to represent the font.

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: ReferenceConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the given value object to the reference type using the specified context and arguments.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo that specifies the culture used to represent the font.

   value: The System.Object to convert.

   destinationType: The type to convert the object to.

   Returns: The converted object.
  """
  pass
 def GetStandardValues(self,context=None):
  """
  GetStandardValues(self: ReferenceConverter,context: ITypeDescriptorContext) -> StandardValuesCollection

  

   Gets a collection of standard values for the reference data type.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: A System.ComponentModel.TypeConverter.StandardValuesCollection that holds a standard set of 

    valid values,or null if the data type does not support a standard set of values.
  """
  pass
 def GetStandardValuesExclusive(self,context=None):
  """
  GetStandardValuesExclusive(self: ReferenceConverter,context: ITypeDescriptorContext) -> bool

  

   Gets a value indicating whether the list of standard values returned from 

    System.ComponentModel.ReferenceConverter.GetStandardValues(System.ComponentModel.ITypeDescriptorC

    ontext) is an exclusive list.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true because the System.ComponentModel.TypeConverter.StandardValuesCollection returned from 

    System.ComponentModel.ReferenceConverter.GetStandardValues(System.ComponentModel.ITypeDescriptorC

    ontext) is an exhaustive list of possible values. This method never returns false.
  """
  pass
 def GetStandardValuesSupported(self,context=None):
  """
  GetStandardValuesSupported(self: ReferenceConverter,context: ITypeDescriptorContext) -> bool

  

   Gets a value indicating whether this object supports a standard set of values that can be picked 

    from a list.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true because 

    System.ComponentModel.ReferenceConverter.GetStandardValues(System.ComponentModel.ITypeDescriptorC

    ontext) can be called to find a common set of values the object supports. This method never 

    returns false.
  """
  pass
 def IsValueAllowed(self,*args):
  """
  IsValueAllowed(self: ReferenceConverter,context: ITypeDescriptorContext,value: object) -> bool

  

   Returns a value indicating whether a particular value can be added to the standard values 

    collection.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides an additional context.

   value: The value to check.

   Returns: true if the value is allowed and can be added to the standard values collection; false if the 

    value cannot be added to the standard values collection.
  """
  pass
 @staticmethod
 def __new__(self,type):
  """ __new__(cls: type,type: Type) """
  pass
