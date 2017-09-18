class FontConverter(TypeConverter):
 """
 Converts System.Drawing.Font objects from one data type to another.

 

 FontConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: FontConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Determines whether this converter can convert an object in the specified source type to the 

    native type of the converter.

  

  

   context: A formatter context. This object can be used to get additional information about the environment 

    this converter is being called from. This may be null,so you should always check. Also,

    properties on the context object may also return null.

  

   sourceType: The type you want to convert from.

   Returns: This method returns true if this object can perform the conversion.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: FontConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Gets a value indicating whether this converter can convert an object to the given destination 

    type using the context.

  

  

   context: An ITypeDescriptorContext object that provides a format context.

   destinationType: A System.Type object that represents the type you want to convert to.

   Returns: This method returns true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: FontConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the specified object to the native type of the converter.

  

   context: A formatter context. This object can be used to get additional information about the environment 

    this converter is being called from. This may be null,so you should always check. Also,

    properties on the context object may also return null.

  

   culture: A CultureInfo object that specifies the culture used to represent the font.

   value: The object to convert.

   Returns: The converted object.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: FontConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the specified object to another type.

  

   context: A formatter context. This object can be used to get additional information about the environment 

    this converter is being called from. This may be null,so you should always check. Also,

    properties on the context object may also return null.

  

   culture: A System.Globalization.CultureInfo object that specifies the culture used to represent the 

    object.

  

   value: The object to convert.

   destinationType: The data type to convert the object to.

   Returns: The converted object.
  """
  pass
 def CreateInstance(self,*__args):
  """
  CreateInstance(self: FontConverter,context: ITypeDescriptorContext,propertyValues: IDictionary) -> object

  

   Creates an object of this type by using a specified set of property values for the object.

  

   context: A type descriptor through which additional context can be provided.

   propertyValues: A dictionary of new property values. The dictionary contains a series of name-value pairs,one 

    for each property returned from the erload:System.Drawing.FontConverter.GetProperties method.

  

   Returns: The newly created object,or null if the object could not be created. The default implementation 

    returns 

    null.System.Drawing.FontConverter.CreateInstance(System.ComponentModel.ITypeDescriptorContext,Sys

    tem.Collections.IDictionary) useful for creating non-changeable objects that have changeable 

    properties.
  """
  pass
 def GetCreateInstanceSupported(self,context=None):
  """
  GetCreateInstanceSupported(self: FontConverter,context: ITypeDescriptorContext) -> bool

  

   Determines whether changing a value on this object should require a call to the 

    erload:System.Drawing.FontConverter.CreateInstance method to create a new value.

  

  

   context: A type descriptor through which additional context can be provided.

   Returns: This method returns true if the CreateInstance object should be called when a change is made to 

    one or more properties of this object; otherwise,false.
  """
  pass
 def GetProperties(self,*__args):
  """
  GetProperties(self: FontConverter,context: ITypeDescriptorContext,value: object,attributes: Array[Attribute]) -> PropertyDescriptorCollection

  

   Retrieves the set of properties for this type. By default,a type does not have any properties 

    to return.

  

  

   context: A type descriptor through which additional context can be provided.

   value: The value of the object to get the properties for.

   attributes: An array of System.Attribute objects that describe the properties.

   Returns: The set of properties that should be exposed for this data type. If no properties should be 

    exposed,this may return null. The default implementation always returns null.An easy 

    implementation of this method can call the 

    erload:System.ComponentModel.TypeConverter.GetProperties method for the correct data type.
  """
  pass
 def GetPropertiesSupported(self,context=None):
  """
  GetPropertiesSupported(self: FontConverter,context: ITypeDescriptorContext) -> bool

  

   Determines whether this object supports properties. The default is false.

  

   context: A type descriptor through which additional context can be provided.

   Returns: This method returns true if the 

    System.Drawing.FontConverter.GetPropertiesSupported(System.ComponentModel.ITypeDescriptorContext)

     method should be called to find the properties of this object; otherwise,false.
  """
  pass
 FontNameConverter=None
 FontUnitConverter=None

