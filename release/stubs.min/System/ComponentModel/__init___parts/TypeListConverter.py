class TypeListConverter(TypeConverter):
 """ Provides a type converter that can be used to populate a list box with available types. """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: TypeListConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Gets a value indicating whether this converter can convert the specified System.Type of the 

    source object using the given context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   sourceType: The System.Type of the source object.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: TypeListConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Gets a value indicating whether this converter can convert an object to the given destination 

    type using the context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   destinationType: A System.Type that represents the type you wish to convert to.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: TypeListConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the specified object to the native type of the converter.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo that specifies the culture used to represent the font.

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: TypeListConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

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
  GetStandardValues(self: TypeListConverter,context: ITypeDescriptorContext) -> StandardValuesCollection

  

   Gets a collection of standard values for the data type this validator is designed for.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: A System.ComponentModel.TypeConverter.StandardValuesCollection that holds a standard set of 

    valid values,or null if the data type does not support a standard set of values.
  """
  pass
 def GetStandardValuesExclusive(self,context=None):
  """
  GetStandardValuesExclusive(self: TypeListConverter,context: ITypeDescriptorContext) -> bool

  

   Gets a value indicating whether the list of standard values returned from the 

    System.ComponentModel.TypeListConverter.GetStandardValues(System.ComponentModel.ITypeDescriptorCo

    ntext) method is an exclusive list.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true because the System.ComponentModel.TypeConverter.StandardValuesCollection returned from 

    System.ComponentModel.TypeListConverter.GetStandardValues(System.ComponentModel.ITypeDescriptorCo

    ntext) is an exhaustive list of possible values. This method never returns false.
  """
  pass
 def GetStandardValuesSupported(self,context=None):
  """
  GetStandardValuesSupported(self: TypeListConverter,context: ITypeDescriptorContext) -> bool

  

   Gets a value indicating whether this object supports a standard set of values that can be picked 

    from a list using the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true because 

    System.ComponentModel.TypeListConverter.GetStandardValues(System.ComponentModel.ITypeDescriptorCo

    ntext) should be called to find a common set of values the object supports. This method never 

    returns false.
  """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,types: Array[Type]) """
  pass
