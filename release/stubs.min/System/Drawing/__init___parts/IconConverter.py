class IconConverter(ExpandableObjectConverter):
 """
 Converts an System.Drawing.Icon object from one data type to another. Access this class through the System.ComponentModel.TypeDescriptor object.

 

 IconConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: IconConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Determines whether this System.Drawing.IconConverter can convert an instance of a specified type 

    to an System.Drawing.Icon,using the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   sourceType: A System.Type that specifies the type you want to convert from.

   Returns: This method returns true if this System.Drawing.IconConverter can perform the conversion; 

    otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: IconConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Determines whether this System.Drawing.IconConverter can convert an System.Drawing.Icon to an 

    instance of a specified type,using the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   destinationType: A System.Type that specifies the type you want to convert to.

   Returns: This method returns true if this System.Drawing.IconConverter can perform the conversion; 

    otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: IconConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts a specified object to an System.Drawing.Icon.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo that holds information about a specific culture.

   value: The System.Object to be converted.

   Returns: If this method succeeds,it returns the System.Drawing.Icon that it created by converting the 

    specified object. Otherwise,it throws an exception.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: IconConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts an System.Drawing.Icon (or an object that can be cast to an System.Drawing.Icon) to a 

    specified type.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo object that specifies formatting conventions used by a 

    particular culture.

  

   value: The object to convert. This object should be of type icon or some type that can be cast to 

    System.Drawing.Icon.

  

   destinationType: The type to convert the icon to.

   Returns: This method returns the converted object.
  """
  pass
