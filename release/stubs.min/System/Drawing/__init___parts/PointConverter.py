class PointConverter(TypeConverter):
 """
 Converts a System.Drawing.Point object from one data type to another.

 

 PointConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: PointConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Determines if this converter can convert an object in the given source type to the native type 

    of the converter.

  

  

   context: A formatter context. This object can be used to get additional information about the environment 

    this converter is being called from. This may be null,so you should always check. Also,

    properties on the context object may also return null.

  

   sourceType: The type you want to convert from.

   Returns: true if this object can perform the conversion; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: PointConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Gets a value indicating whether this converter can convert an object to the given destination 

    type using the context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext object that provides a format context.

   destinationType: A System.Type object that represents the type you want to convert to.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: PointConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the specified object to a System.Drawing.Point object.

  

   context: A formatter context. This object can be used to get additional information about the environment 

    this converter is being called from. This may be null,so you should always check. Also,

    properties on the context object may also return null.

  

   culture: An object that contains culture specific information,such as the language,calendar,and 

    cultural conventions associated with a specific culture. It is based on the RFC 1766 standard.

  

   value: The object to convert.

   Returns: The converted object.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: PointConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the specified object to the specified type.

  

   context: A formatter context. This object can be used to get additional information about the environment 

    this converter is being called from. This may be null,so you should always check. Also,

    properties on the context object may also return null.

  

   culture: An object that contains culture specific information,such as the language,calendar,and 

    cultural conventions associated with a specific culture. It is based on the RFC 1766 standard.

  

   value: The object to convert.

   destinationType: The type to convert the object to.

   Returns: The converted object.
  """
  pass
 def CreateInstance(self,*__args):
  """
  CreateInstance(self: PointConverter,context: ITypeDescriptorContext,propertyValues: IDictionary) -> object

  

   Creates an instance of this type given a set of property values for the object.

  

   context: A type descriptor through which additional context can be provided.

   propertyValues: A dictionary of new property values. The dictionary contains a series of name-value pairs,one 

    for each property returned from 

    System.Drawing.PointConverter.GetProperties(System.ComponentModel.ITypeDescriptorContext,System.O

    bject,System.Attribute[]).

  

   Returns: The newly created object,or null if the object could not be created. The default implementation 

    returns null.
  """
  pass
 def GetCreateInstanceSupported(self,context=None):
  """
  GetCreateInstanceSupported(self: PointConverter,context: ITypeDescriptorContext) -> bool

  

   Determines if changing a value on this object should require a call to 

    System.Drawing.PointConverter.CreateInstance(System.ComponentModel.ITypeDescriptorContext,System.

    Collections.IDictionary) to create a new value.

  

  

   context: A System.ComponentModel.TypeDescriptor through which additional context can be provided.

   Returns: true if the 

    System.Drawing.PointConverter.CreateInstance(System.ComponentModel.ITypeDescriptorContext,System.

    Collections.IDictionary) method should be called when a change is made to one or more properties 

    of this object; otherwise,false.
  """
  pass
 def GetProperties(self,*__args):
  """
  GetProperties(self: PointConverter,context: ITypeDescriptorContext,value: object,attributes: Array[Attribute]) -> PropertyDescriptorCollection

  

   Retrieves the set of properties for this type. By default,a type does not return any properties.

  

   context: A type descriptor through which additional context can be provided.

   value: The value of the object to get the properties for.

   attributes: An array of System.Attribute objects that describe the properties.

   Returns: The set of properties that are exposed for this data type. If no properties are exposed,this 

    method might return null. The default implementation always returns null.
  """
  pass
 def GetPropertiesSupported(self,context=None):
  """
  GetPropertiesSupported(self: PointConverter,context: ITypeDescriptorContext) -> bool

  

   Determines if this object supports properties. By default,this is false.

  

   context: A System.ComponentModel.TypeDescriptor through which additional context can be provided.

   Returns: true if 

    System.Drawing.PointConverter.GetProperties(System.ComponentModel.ITypeDescriptorContext,System.O

    bject,System.Attribute[]) should be called to find the properties of this object; otherwise,

    false.
  """
  pass
