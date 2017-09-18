class BooleanConverter(TypeConverter):
 """
 Provides a type converter to convert System.Boolean objects to and from various other representations.

 

 BooleanConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: BooleanConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Gets a value indicating whether this converter can convert an object in the given source type to 

    a Boolean object using the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   sourceType: A System.Type that represents the type you wish to convert from.

   Returns: true if this object can perform the conversion; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: BooleanConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the given value object to a Boolean object.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo that specifies the culture to which to convert.

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def GetStandardValues(self,context=None):
  """
  GetStandardValues(self: BooleanConverter,context: ITypeDescriptorContext) -> StandardValuesCollection

  

   Gets a collection of standard values for the Boolean data type.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: A System.ComponentModel.TypeConverter.StandardValuesCollection that holds a standard set of 

    valid values.
  """
  pass
 def GetStandardValuesExclusive(self,context=None):
  """
  GetStandardValuesExclusive(self: BooleanConverter,context: ITypeDescriptorContext) -> bool

  

   Gets a value indicating whether the list of standard values returned from the 

    System.ComponentModel.BooleanConverter.GetStandardValues(System.ComponentModel.ITypeDescriptorCon

    text) method is an exclusive list.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true because the System.ComponentModel.TypeConverter.StandardValuesCollection returned from 

    System.ComponentModel.BooleanConverter.GetStandardValues(System.ComponentModel.ITypeDescriptorCon

    text) is an exhaustive list of possible values. This method never returns false.
  """
  pass
 def GetStandardValuesSupported(self,context=None):
  """
  GetStandardValuesSupported(self: BooleanConverter,context: ITypeDescriptorContext) -> bool

  

   Gets a value indicating whether this object supports a standard set of values that can be picked 

    from a list.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true because 

    System.ComponentModel.BooleanConverter.GetStandardValues(System.ComponentModel.ITypeDescriptorCon

    text) can be called to find a common set of values the object supports. This method never 

    returns false.
  """
  pass
