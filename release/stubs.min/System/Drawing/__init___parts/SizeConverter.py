class SizeConverter(TypeConverter):
 """
 The System.Drawing.SizeConverter class is used to convert from one data type to another. Access this class through the System.ComponentModel.TypeDescriptor object.

 

 SizeConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: SizeConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Determines whether this converter can convert an object in the specified source type to the 

    native type of the converter.

  

  

   context: A System.ComponentModel.ITypeDescriptorContext that can be used to get additional information 

    about the environment this converter is being called from. This may be null,so you should 

    always check. Also,properties on the context object may also return null.

  

   sourceType: The type you want to convert from.

   Returns: This method returns true if this object can perform the conversion.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: SizeConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Gets a value indicating whether this converter can convert an object to the given destination 

    type using the context.

  

  

   context: A System.ComponentModel.ITypeDescriptorContext that can be used to get additional information 

    about the environment this converter is being called from. This can be null,so always check. 

    Also,properties on the context object can return null.

  

   destinationType: A System.Type that represents the type you want to convert to.

   Returns: This method returns true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: SizeConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the specified object to the converter's native type.

  

   context: A System.ComponentModel.ITypeDescriptorContext that can be used to get additional information 

    about the environment this converter is being called from. This may be null,so you should 

    always check. Also,properties on the context object may also return null.

  

   culture: An System.Globalization.CultureInfo object that contains culture specific information,such as 

    the language,calendar,and cultural conventions associated with a specific culture. It is based 

    on the RFC 1766 standard.

  

   value: The object to convert.

   Returns: The converted object.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: SizeConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the specified object to the specified type.

  

   context: A System.ComponentModel.ITypeDescriptorContext that can be used to get additional information 

    about the environment this converter is being called from. This may be null,so you should 

    always check. Also,properties on the context object may also return null.

  

   culture: An System.Globalization.CultureInfo object that contains culture specific information,such as 

    the language,calendar,and cultural conventions associated with a specific culture. It is based 

    on the RFC 1766 standard.

  

   value: The object to convert.

   destinationType: The type to convert the object to.

   Returns: The converted object.
  """
  pass
 def CreateInstance(self,*__args):
  """
  CreateInstance(self: SizeConverter,context: ITypeDescriptorContext,propertyValues: IDictionary) -> object

  

   Creates an object of this type by using a specified set of property values for the object. This 

    is useful for creating non-changeable objects that have changeable properties.

  

  

   context: A System.ComponentModel.TypeDescriptor through which additional context can be provided.

   propertyValues: A dictionary of new property values. The dictionary contains a series of name-value pairs,one 

    for each property returned from the 

    System.Drawing.SizeConverter.GetProperties(System.ComponentModel.ITypeDescriptorContext,System.Ob

    ject,System.Attribute[]) method.

  

   Returns: The newly created object,or null if the object could not be created. The default implementation 

    returns null.
  """
  pass
 def GetCreateInstanceSupported(self,context=None):
  """
  GetCreateInstanceSupported(self: SizeConverter,context: ITypeDescriptorContext) -> bool

  

   Determines whether changing a value on this object should require a call to the 

    System.Drawing.SizeConverter.CreateInstance(System.ComponentModel.ITypeDescriptorContext,System.C

    ollections.IDictionary) method to create a new value.

  

  

   context: A System.ComponentModel.TypeDescriptor through which additional context can be provided.

   Returns: true if the 

    System.Drawing.SizeConverter.CreateInstance(System.ComponentModel.ITypeDescriptorContext,System.C

    ollections.IDictionary) object should be called when a change is made to one or more properties 

    of this object.
  """
  pass
 def GetProperties(self,*__args):
  """
  GetProperties(self: SizeConverter,context: ITypeDescriptorContext,value: object,attributes: Array[Attribute]) -> PropertyDescriptorCollection

  

   Retrieves the set of properties for this type. By default,a type does not have any properties 

    to return.

  

  

   context: A System.ComponentModel.TypeDescriptor through which additional context can be provided.

   value: The value of the object to get the properties for.

   attributes: An array of System.Attribute objects that describe the properties.

   Returns: The set of properties that should be exposed for this data type. If no properties should be 

    exposed,this may return null. The default implementation always returns null.
  """
  pass
 def GetPropertiesSupported(self,context=None):
  """
  GetPropertiesSupported(self: SizeConverter,context: ITypeDescriptorContext) -> bool

  

   Determines whether this object supports properties. By default,this is false.

  

   context: A System.ComponentModel.TypeDescriptor through which additional context can be provided.

   Returns: true if the 

    System.Drawing.SizeConverter.GetProperties(System.ComponentModel.ITypeDescriptorContext,System.Ob

    ject,System.Attribute[]) method should be called to find the properties of this object.
  """
  pass
