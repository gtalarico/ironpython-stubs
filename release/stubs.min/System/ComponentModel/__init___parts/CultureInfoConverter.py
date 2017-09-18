class CultureInfoConverter(TypeConverter):
 """
 Provides a type converter to convert System.Globalization.CultureInfo objects to and from various other representations.

 

 CultureInfoConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: CultureInfoConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Gets a value indicating whether this converter can convert an object in the given source type to 

    a System.Globalization.CultureInfo using the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   sourceType: A System.Type that represents the type you wish to convert from.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: CultureInfoConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Gets a value indicating whether this converter can convert an object to the given destination 

    type using the context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   destinationType: A System.Type that represents the type you wish to convert to.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: CultureInfoConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the specified value object to a System.Globalization.CultureInfo.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo that specifies the culture to which to convert.

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: CultureInfoConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the given value object to the specified destination type.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo that specifies the culture to which to convert.

   value: The System.Object to convert.

   destinationType: The System.Type to convert the value to.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def GetCultureName(self,*args):
  """
  GetCultureName(self: CultureInfoConverter,culture: CultureInfo) -> str

  

   Retrieves the name of the specified culture.

  

   culture: A System.Globalization.CultureInfo that specifies the culture to get the name for.

   Returns: The name of the specified culture.
  """
  pass
 def GetStandardValues(self,context=None):
  """
  GetStandardValues(self: CultureInfoConverter,context: ITypeDescriptorContext) -> StandardValuesCollection

  

   Gets a collection of standard values for a System.Globalization.CultureInfo object using the 

    specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: A System.ComponentModel.TypeConverter.StandardValuesCollection containing a standard set of 

    valid values,or null if the data type does not support a standard set of values.
  """
  pass
 def GetStandardValuesExclusive(self,context=None):
  """
  GetStandardValuesExclusive(self: CultureInfoConverter,context: ITypeDescriptorContext) -> bool

  

   Gets a value indicating whether the list of standard values returned from 

    System.ComponentModel.CultureInfoConverter.GetStandardValues(System.ComponentModel.ITypeDescripto

    rContext) is an exhaustive list.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: false because the System.ComponentModel.TypeConverter.StandardValuesCollection returned from 

    System.ComponentModel.CultureInfoConverter.GetStandardValues(System.ComponentModel.ITypeDescripto

    rContext) is not an exhaustive list of possible values (that is,other values are possible). 

    This method never returns true.
  """
  pass
 def GetStandardValuesSupported(self,context=None):
  """
  GetStandardValuesSupported(self: CultureInfoConverter,context: ITypeDescriptorContext) -> bool

  

   Gets a value indicating whether this object supports a standard set of values that can be picked 

    from a list using the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true because 

    System.ComponentModel.CultureInfoConverter.GetStandardValues(System.ComponentModel.ITypeDescripto

    rContext) should be called to find a common set of values the object supports. This method never 

    returns false.
  """
  pass
