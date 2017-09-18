class SelectionRangeConverter(TypeConverter):
 """
 Provides a type converter to convert System.Windows.Forms.SelectionRange objects to and from various other types.

 

 SelectionRangeConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: SelectionRangeConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Determines if this converter can convert an object of the specified source type to the native 

    type of the converter by querying the supplied type descriptor context.

  

  

   context: A System.ComponentModel.ITypeDescriptorContext that provides a format context.

   sourceType: The source System.Type to be converted.

   Returns: true if the converter can perform the specified conversion; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: SelectionRangeConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Gets a value indicating whether this converter can convert an object to the specified 

    destination type by using the specified context.

  

  

   context: A System.ComponentModel.ITypeDescriptorContext that provides a format context.

   destinationType: The destination System.Type to convert into.

   Returns: true if this converter can perform the specified conversion; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: SelectionRangeConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the specified value to the converter's native type by using the specified locale.

  

   context: A System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: The locale information for the conversion.

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: SelectionRangeConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the specified System.Windows.Forms.SelectionRangeConverter object to another type by 

    using the specified culture.

  

  

   context: A System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: The locale information for the conversion.

   value: The System.Object to convert.

   destinationType: The destination System.Type to convert into.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def CreateInstance(self,*__args):
  """
  CreateInstance(self: SelectionRangeConverter,context: ITypeDescriptorContext,propertyValues: IDictionary) -> object

  

   Creates a System.Windows.Forms.SelectionRange object by using the specified type descriptor and 

    set of property values for that object.

  

  

   context: A System.ComponentModel.ITypeDescriptorContext that provides a format context.

   propertyValues: An System.Collections.IDictionary that contains the new property values.

   Returns: If successful,the newly created System.Windows.Forms.SelectionRange; otherwise,this method 

    throws an exception.
  """
  pass
 def GetCreateInstanceSupported(self,context=None):
  """
  GetCreateInstanceSupported(self: SelectionRangeConverter,context: ITypeDescriptorContext) -> bool

  

   Determines if changing a value on an instance should require a call to 

    erload:System.Windows.Forms.SelectionRangeConverter.CreateInstance to create a new value.

  

  

   context: A System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true if erload:System.Windows.Forms.SelectionRangeConverter.CreateInstance must be called to 

    make a change to one or more properties; otherwise false.
  """
  pass
 def GetProperties(self,*__args):
  """
  GetProperties(self: SelectionRangeConverter,context: ITypeDescriptorContext,value: object,attributes: Array[Attribute]) -> PropertyDescriptorCollection

  

   Returns the set of filtered properties for the System.Windows.Forms.SelectionRange type

  

   context: A System.ComponentModel.ITypeDescriptorContext that provides a format context.

   value: An System.Object that specifies the type of array for which to get properties.

   attributes: An array of type System.Attribute that is used as a filter.

   Returns: If successful,the set of properties that should be exposed for the 

    System.Windows.Forms.SelectionRange type; otherwise,null.
  """
  pass
 def GetPropertiesSupported(self,context=None):
  """
  GetPropertiesSupported(self: SelectionRangeConverter,context: ITypeDescriptorContext) -> bool

  

   Determines whether the current object supports properties that use the specified type descriptor 

    context.

  

  

   context: A System.ComponentModel.ITypeDescriptorContext that provides a format context.

   Returns: true if erload:System.Windows.Forms.SelectionRangeConverter.GetProperties can be called to find 

    the properties of a System.Windows.Forms.SelectionRange object; otherwise,false.
  """
  pass
