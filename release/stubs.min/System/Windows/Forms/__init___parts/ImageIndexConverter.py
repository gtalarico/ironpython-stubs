class ImageIndexConverter(Int32Converter):
 """
 Provides a type converter to convert data for an image index to and from a string.

 

 ImageIndexConverter()
 """
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: ImageIndexConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the specified value object to a 32-bit signed integer object.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo to provide locale information.

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: ImageIndexConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the specified object to the specified destination type.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context,which can be 

    used to extract additional information about the environment this type converter is being 

    invoked from. This parameter or properties of this parameter can be null.

  

   culture: A System.Globalization.CultureInfo that provides locale information.

   value: The object to convert,typically an index represented as an System.Int32.

   destinationType: The type to convert the object to,often a System.String.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def GetStandardValues(self,context=None):
  """
  GetStandardValues(self: ImageIndexConverter,context: ITypeDescriptorContext) -> StandardValuesCollection

  

   Returns a collection of standard index values for the image list associated with the specified 

    format context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context,which can be 

    used to extract additional information about the environment this type converter is being 

    invoked from. This parameter or properties of this parameter can be null.

  

   Returns: A System.ComponentModel.TypeConverter.StandardValuesCollection that holds a standard set of 

    valid index values. If no image list is found,this collection will contain a single object with 

    a value of -1.
  """
  pass
 def GetStandardValuesExclusive(self,context=None):
  """
  GetStandardValuesExclusive(self: ImageIndexConverter,context: ITypeDescriptorContext) -> bool

  

   Determines if the list of standard values returned from the 

    erload:System.Windows.Forms.ImageIndexConverter.GetStandardValues method is an exclusive list.

  

  

   context: A formatter context.

   Returns: true if the erload:System.Windows.Forms.ImageIndexConverter.GetStandardValues method returns an 

    exclusive list of valid values; otherwise,false. This implementation always returns false.
  """
  pass
 def GetStandardValuesSupported(self,context=None):
  """
  GetStandardValuesSupported(self: ImageIndexConverter,context: ITypeDescriptorContext) -> bool

  

   Determines if the type converter supports a standard set of values that can be picked from a 

    list.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context,which can be 

    used to extract additional information about the environment this type converter is being 

    invoked from. This parameter or properties of this parameter can be null.

  

   Returns: true if the erload:System.Windows.Forms.ImageIndexConverter.GetStandardValues method returns a 

    standard set of values; otherwise,false. Always returns true.
  """
  pass
 IncludeNoneAsStandardValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether a none or null value is valid in the System.ComponentModel.TypeConverter.StandardValuesCollection collection.



"""


