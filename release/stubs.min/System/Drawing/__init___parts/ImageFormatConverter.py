class ImageFormatConverter(TypeConverter):
 """
 System.Drawing.ImageFormatConverter is a class that can be used to convert System.Drawing.Imaging.ImageFormat objects from one data type to another. Access this class through the System.ComponentModel.TypeDescriptor object.

 

 ImageFormatConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: ImageFormatConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Indicates whether this converter can convert an object in the specified source type to the 

    native type of the converter.

  

  

   context: A formatter context. This object can be used to get more information about the environment this 

    converter is being called from. This may be null,so you should always check. Also,properties 

    on the context object may also return null.

  

   sourceType: The type you want to convert from.

   Returns: This method returns true if this object can perform the conversion.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: ImageFormatConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Gets a value indicating whether this converter can convert an object to the specified 

    destination type using the context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that specifies the context for this type 

    conversion.

  

   destinationType: The System.Type that represents the type to which you want to convert this 

    System.Drawing.Imaging.ImageFormat object.

  

   Returns: This method returns true if this object can perform the conversion.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: ImageFormatConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the specified object to an System.Drawing.Imaging.ImageFormat object.

  

   context: A formatter context. This object can be used to get more information about the environment this 

    converter is being called from. This may be null,so you should always check. Also,properties 

    on the context object may also return null.

  

   culture: A System.Globalization.CultureInfo object that specifies formatting conventions for a particular 

    culture.

  

   value: The object to convert.

   Returns: The converted object.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: ImageFormatConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the specified object to the specified type.

  

   context: A formatter context. This object can be used to get more information about the environment this 

    converter is being called from. This may be null,so you should always check. Also,properties 

    on the context object may also return null.

  

   culture: A System.Globalization.CultureInfo object that specifies formatting conventions for a particular 

    culture.

  

   value: The object to convert.

   destinationType: The type to convert the object to.

   Returns: The converted object.
  """
  pass
 def GetStandardValues(self,context=None):
  """
  GetStandardValues(self: ImageFormatConverter,context: ITypeDescriptorContext) -> StandardValuesCollection

  

   Gets a collection that contains a set of standard values for the data type this validator is 

    designed for. Returns null if the data type does not support a standard set of values.

  

  

   context: A formatter context. This object can be used to get more information about the environment this 

    converter is being called from. This may be null,so you should always check. Also,properties 

    on the context object may also return null.

  

   Returns: A collection that contains a standard set of valid values,or null. The default implementation 

    always returns null.
  """
  pass
 def GetStandardValuesSupported(self,context=None):
  """
  GetStandardValuesSupported(self: ImageFormatConverter,context: ITypeDescriptorContext) -> bool

  

   Indicates whether this object supports a standard set of values that can be picked from a list.

  

   context: A type descriptor through which additional context can be provided.

   Returns: This method returns true if the erload:System.Drawing.ImageFormatConverter.GetStandardValues 

    method should be called to find a common set of values the object supports.
  """
  pass
