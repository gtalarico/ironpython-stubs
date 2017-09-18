class ImageKeyConverter(StringConverter):
 """
 Provides a type converter to convert data for an image key to and from another data type.

 

 ImageKeyConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: ImageKeyConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Returns whether this converter can convert an object of the given type to a string using the 

    specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   sourceType: A System.Type that specifies the type you want to convert from.

   Returns: true to indicate the specified conversion can be performed; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: ImageKeyConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts from the specified object to a string.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo to provide locale information.

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: ImageKeyConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the given object to the specified type.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context,which can be 

    used to extract additional information about the environment this type converter is being 

    invoked from. This parameter or properties of this parameter can be null.

  

   culture: A System.Globalization.CultureInfo that provides locale information.

   value: The object to convert,typically an image key.

   destinationType: The type to convert the object to.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def GetStandardValues(self,context=None):
  """
  GetStandardValues(self: ImageKeyConverter,context: ITypeDescriptorContext) -> StandardValuesCollection

  

   Returns a collection of standard image keys for the image list associated with the specified 

    context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context,which can be 

    used to extract additional information about the environment this type converter is being 

    invoked from. This parameter or properties of this parameter can be null.

  

   Returns: A System.ComponentModel.TypeConverter.StandardValuesCollection that contains the standard set of 

    image key values.
  """
  pass
 def GetStandardValuesExclusive(self,context=None):
  """
  GetStandardValuesExclusive(self: ImageKeyConverter,context: ITypeDescriptorContext) -> bool

  

   Determines whether the list of standard values for the System.Windows.Forms.ImageKeyConverter is 

    exclusive (that is,whether it allows values other than those returned by 

    erload:System.Windows.Forms.ImageKeyConverter.GetStandardValues).

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context,which can be 

    used to extract additional information about the environment this type converter is being 

    invoked from. This parameter or properties of this parameter can be null.

  

   Returns: true to indicate the list does not allow additional values; otherwise,false. Always returns 

    true.
  """
  pass
 def GetStandardValuesSupported(self,context=None):
  """
  GetStandardValuesSupported(self: ImageKeyConverter,context: ITypeDescriptorContext) -> bool

  

   Determines whether this type converter supports a standard set of values that can be picked from 

    a list.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context,which can be 

    used to extract additional information about the environment this type converter is being 

    invoked from. This parameter or properties of this parameter can be null.

  

   Returns: true to indicate a list of standard values is supported; otherwise,false. Always returns true.
  """
  pass
 IncludeNoneAsStandardValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether null is valid in the System.ComponentModel.TypeConverter.StandardValuesCollection collection.



"""


