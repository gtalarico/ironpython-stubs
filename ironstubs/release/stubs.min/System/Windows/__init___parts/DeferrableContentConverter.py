class DeferrableContentConverter(TypeConverter):
 """
 Converts a stream to a System.Windows.DeferrableContent instance.
 
 DeferrableContentConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: DeferrableContentConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool
  
   Returns whether this converter can convert the specified object to a 
    System.Windows.DeferrableContent object.
  
  
   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
   sourceType: A System.Type that represents the type you want to convert from.
   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: DeferrableContentConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object
  
   Converts the specified stream to a new System.Windows.DeferrableContent object.
  
   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
   culture: The System.Globalization.CultureInfo to use as the current culture.
   value: The source stream to convert.
   Returns: A new System.Windows.DeferrableContent object.
  """
  pass
