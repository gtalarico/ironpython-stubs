class CursorConverter(TypeConverter):
 """
 Provides a type converter to convert System.Windows.Forms.Cursor objects to and from various other representations.

 

 CursorConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: CursorConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Determines if this converter can convert an object in the given source type to the native type 

    of the converter.

  

  

   context: A formatter context. This object can be used to extract additional information about the 

    environment this converter is being invoked from. This may be null,so you should always check. 

    Also,properties on the context object may also return null.

  

   sourceType: The type you wish to convert from.

   Returns: true if this object can perform the conversion.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: CursorConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Gets a value indicating whether this converter can convert an object to the given destination 

    type using the context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   destinationType: A System.Type that represents the type you wish to convert to.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: CursorConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: The System.Globalization.CultureInfo to use as the current culture.

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: CursorConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo. If null is passed,the current culture is assumed.

   value: The System.Object to convert.

   destinationType: The System.Type to convert the value parameter to.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def GetStandardValues(self,context=None):
  """
  GetStandardValues(self: CursorConverter,context: ITypeDescriptorContext) -> StandardValuesCollection

  

   Retrieves a collection containing a set of standard values for the data type this validator is 

    designed for. This will return null if the data type does not support a standard set of values.

  

  

   context: A formatter context. This object can be used to extract additional information about the 

    environment this converter is being invoked from. This may be null,so you should always check. 

    Also,properties on the context object may also return null.

  

   Returns: A collection containing a standard set of valid values,or null. The default implementation 

    always returns null.
  """
  pass
 def GetStandardValuesSupported(self,context=None):
  """
  GetStandardValuesSupported(self: CursorConverter,context: ITypeDescriptorContext) -> bool

  

   Determines if this object supports a standard set of values that can be picked from a list.

  

   context: A type descriptor through which additional context may be provided.

   Returns: Returns true if GetStandardValues should be called to find a common set of values the object 

    supports.
  """
  pass
