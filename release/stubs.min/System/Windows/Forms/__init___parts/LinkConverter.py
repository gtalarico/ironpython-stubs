class LinkConverter(TypeConverter):
 """
 Provides a type converter for System.Windows.Forms.LinkLabel.Link objects.

 

 LinkConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: LinkConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Retrieves a value that determines if this System.Windows.Forms.LinkConverter can convert an 

    object having the specified context and source type to the native type of the 

    System.Windows.Forms.LinkConverter.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext providing contextual information about the 

    object to be converted.

  

   sourceType: The type of the object to be converted.

   Returns: true if this System.Windows.Forms.LinkConverter can convert the specified object; otherwise,

    false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: LinkConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Retrieves a value that determines if this System.Windows.Forms.LinkConverter can convert an 

    object having the specified context to the specified type.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext providing contextual information about the 

    object to be converted.

  

   destinationType: The type to convert the object to.

   Returns: true if this System.Windows.Forms.LinkConverter can convert the specified object; otherwise,

    false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: LinkConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the specified object to the native type of the System.Windows.Forms.LinkConverter.

  

   context: An System.ComponentModel.ITypeDescriptorContext providing contextual information about the 

    object to be converted.

  

   culture: Cultural attributes of the object to be converted. If this parameter is null,the 

    System.Globalization.CultureInfo.CurrentCulture property value is used.

  

   value: The object to be converted.

   Returns: The converted object.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: LinkConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the specified object to another type.

  

   context: An System.ComponentModel.ITypeDescriptorContext providing contextual information about the 

    object to be converted.

  

   culture: Cultural attributes of the object to be converted. If this parameter is null,the 

    System.Globalization.CultureInfo.CurrentCulture property value is used.

  

   value: The object to be converted.

   destinationType: The type to convert the object to.

   Returns: The converted object.
  """
  pass
