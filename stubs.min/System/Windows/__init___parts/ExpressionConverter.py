class ExpressionConverter(TypeConverter):
 """
 Converts instances of System.Windows.Expression  to and from other types.
 
 ExpressionConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: ExpressionConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool
  
   Returns whether this converter can convert from a source object to an 
    System.Windows.Expression object.
  
  
   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
   sourceType: A System.Type that represents the type you wish to convert from.
   Returns: Always false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: ExpressionConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool
  
   Returns whether this converter can convert an System.Windows.Expression object 
    to a specific destination type.
  
  
   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
   destinationType: A System.Type that represents the type you wish to convert to.
   Returns: Always false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: ExpressionConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object
  
   Converts the provided value to the System.Windows.Expression type.
  
   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
   culture: The System.Globalization.CultureInfo to use as the current culture.
   value: The object to convert.
   Returns: Always throws an exception and returns null.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: ExpressionConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object
  
   Converts the provided System.Windows.Expression object to the specified type.
  
   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
   culture: The System.Globalization.CultureInfo to use as the current culture.
   value: The object to convert.
   destinationType: A System.Type that represents the type you wish to convert to.
   Returns: Always throws an exception and returns null.
  """
  pass
