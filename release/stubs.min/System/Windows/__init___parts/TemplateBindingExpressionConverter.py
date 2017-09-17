class TemplateBindingExpressionConverter(TypeConverter):
 """
 A type converter that is used to construct a markup extension from a System.Windows.TemplateBindingExpression instance during serialization.
 
 TemplateBindingExpressionConverter()
 """
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: TemplateBindingExpressionConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool
  
   Returns whether this converter can convert the object to the specified type,
    using the specified context.
  
  
   context: An System.ComponentModel.ITypeDescriptorContext implementation that provides a 
    format context.
  
   destinationType: The desired type of the conversion's output.
   Returns: true if this converter can perform the requested conversion; otherwise,false. 
    Only a destinationType of System.Windows.Markup.MarkupExtension returns true.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: TemplateBindingExpressionConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object
  
   Converts the given value object to a System.Windows.Markup.MarkupExtension type.
  
   context: An System.ComponentModel.ITypeDescriptorContext implementation that provides a 
    format context.
  
   culture: A System.Globalization.CultureInfo object. If a null reference is passed,the 
    current culture is assumed.
  
   value: The value to convert.
   destinationType: The desired type to convert to.
   Returns: The converted value.
  """
  pass
