class TemplateBindingExtension(MarkupExtension):
 """
 Implements a markup extension that supports the binding between the value of a property in a template and the value of some other exposed property on the templated control.
 
 TemplateBindingExtension()
 TemplateBindingExtension(property: DependencyProperty)
 """
 def ProvideValue(self,serviceProvider):
  """
  ProvideValue(self: TemplateBindingExtension,serviceProvider: IServiceProvider) -> object
  
   Returns an object that should be set as the value on the target object's 
    property for this markup extension. For 
    System.Windows.TemplateBindingExtension,this is an expression 
    (System.Windows.TemplateBindingExpression) that supports the binding.
  
  
   serviceProvider: An object that can provide services for the markup extension. May be null in 
    this implementation.
  
   Returns: The expression that supports the binding.
  """
  pass
 @staticmethod
 def __new__(self,property=None):
  """
  __new__(cls: type)
  __new__(cls: type,property: DependencyProperty)
  """
  pass
 Converter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the converter that interprets between source and target of a binding.

Get: Converter(self: TemplateBindingExtension) -> IValueConverter

Set: Converter(self: TemplateBindingExtension)=value
"""

 ConverterParameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the parameter to pass to the converter.

Get: ConverterParameter(self: TemplateBindingExtension) -> object

Set: ConverterParameter(self: TemplateBindingExtension)=value
"""

 Property=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the property being bound to.

Get: Property(self: TemplateBindingExtension) -> DependencyProperty

Set: Property(self: TemplateBindingExtension)=value
"""


