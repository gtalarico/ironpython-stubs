class ImageConverter(TypeConverter):
 """
 System.Drawing.ImageConverter  is a class that can be used to convert System.Drawing.Image objects from one data type to another. Access this class through the System.ComponentModel.TypeDescriptor object.

 

 ImageConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: ImageConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Determines whether this System.Drawing.ImageConverter can convert an instance of a specified 

    type to an System.Drawing.Image,using the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   sourceType: A System.Type that specifies the type you want to convert from.

   Returns: This method returns true if this System.Drawing.ImageConverter can perform the conversion; 

    otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: ImageConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Determines whether this System.Drawing.ImageConverter can convert an System.Drawing.Image to an 

    instance of a specified type,using the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   destinationType: A System.Type that specifies the type you want to convert to.

   Returns: This method returns true if this System.Drawing.ImageConverter can perform the conversion; 

    otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: ImageConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts a specified object to an System.Drawing.Image.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo that holds information about a specific culture.

   value: The System.Object to be converted.

   Returns: If this method succeeds,it returns the System.Drawing.Image that it created by converting the 

    specified object. Otherwise,it throws an exception.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: ImageConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts an System.Drawing.Image (or an object that can be cast to an System.Drawing.Image) to 

    the specified type.

  

  

   context: A formatter context. This object can be used to get more information about the environment this 

    converter is being called from. This may be null,so you should always check. Also,properties 

    on the context object may also return null.

  

   culture: A System.Globalization.CultureInfo object that specifies formatting conventions used by a 

    particular culture.

  

   value: The System.Drawing.Image to convert.

   destinationType: The System.Type to convert the System.Drawing.Image to.

   Returns: This method returns the converted object.
  """
  pass
 def GetProperties(self,*__args):
  """
  GetProperties(self: ImageConverter,context: ITypeDescriptorContext,value: object,attributes: Array[Attribute]) -> PropertyDescriptorCollection

  

   Gets the set of properties for this type.

  

   context: A type descriptor through which additional context can be provided.

   value: The value of the object to get the properties for.

   attributes: An array of System.Attribute objects that describe the properties.

   Returns: The set of properties that should be exposed for this data type. If no properties should be 

    exposed,this can return null. The default implementation always returns null.
  """
  pass
 def GetPropertiesSupported(self,context=None):
  """
  GetPropertiesSupported(self: ImageConverter,context: ITypeDescriptorContext) -> bool

  

   Indicates whether this object supports properties. By default,this is false.

  

   context: A type descriptor through which additional context can be provided.

   Returns: This method returns true if the erload:System.Drawing.ImageConverter.GetProperties method should 

    be called to find the properties of this object.
  """
  pass
