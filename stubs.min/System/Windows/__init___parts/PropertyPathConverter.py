class PropertyPathConverter(TypeConverter):
 """
 Provides a type converter for System.Windows.PropertyPath objects.
 
 PropertyPathConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: PropertyPathConverter,typeDescriptorContext: ITypeDescriptorContext,sourceType: Type) -> bool
  
   Returns whether this converter can convert an object of one type to the 
    System.Windows.PropertyPath type.
  
  
   typeDescriptorContext: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
   sourceType: A System.Type that represents the type you want to convert from.
   Returns: true if sourceType is type System.String; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: PropertyPathConverter,typeDescriptorContext: ITypeDescriptorContext,destinationType: Type) -> bool
  
   Returns whether this converter can convert the object to the 
    System.Windows.PropertyPath type.
  
  
   typeDescriptorContext: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
   destinationType: A System.Type that represents the type you want to convert to.
   Returns: true if destinationType is type System.String; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: PropertyPathConverter,typeDescriptorContext: ITypeDescriptorContext,cultureInfo: CultureInfo,source: object) -> object
  
   Converts the specified value to the System.Windows.PropertyPath type.
  
   typeDescriptorContext: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
   cultureInfo: The System.Globalization.CultureInfo to use as the current culture.
   source: The object to convert to a System.Windows.PropertyPath. This is expected to be 
    a string.
  
   Returns: The converted System.Windows.PropertyPath.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: PropertyPathConverter,typeDescriptorContext: ITypeDescriptorContext,cultureInfo: CultureInfo,value: object,destinationType: Type) -> object
  
   Converts the specified value object to the System.Windows.PropertyPath type.
  
   typeDescriptorContext: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
   cultureInfo: The System.Globalization.CultureInfo to use as the current culture.
   value: The System.Windows.PropertyPath to convert.
   destinationType: The destination type. This is expected to be the System.String type.
   Returns: The converted destination System.String.
  """
  pass
