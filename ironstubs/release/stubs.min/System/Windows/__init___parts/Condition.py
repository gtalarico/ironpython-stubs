class Condition(object,ISupportInitialize):
 """
 Represents a condition for the System.Windows.MultiTrigger and the System.Windows.MultiDataTrigger,which apply changes to property values based on a set of conditions.
 
 Condition()
 Condition(conditionProperty: DependencyProperty,conditionValue: object)
 Condition(conditionProperty: DependencyProperty,conditionValue: object,sourceName: str)
 Condition(binding: BindingBase,conditionValue: object)
 """
 @staticmethod
 def ReceiveMarkupExtension(targetObject,eventArgs):
  """
  ReceiveMarkupExtension(targetObject: object,eventArgs: XamlSetMarkupExtensionEventArgs)
   Handles cases where a markup extension provides a value for a property of a 
    System.Windows.Condition object
  
  
   targetObject: The object where the markup extension sets the value.
   eventArgs: Data that is relevant for markup extension processing.
  """
  pass
 @staticmethod
 def ReceiveTypeConverter(targetObject,eventArgs):
  """
  ReceiveTypeConverter(targetObject: object,eventArgs: XamlSetTypeConverterEventArgs)
   Handles cases where a type converter provides a value for a property of on 
    aSystem.Windows.Condition object.
  
  
   targetObject: The object where the type converter sets the value.
   eventArgs: Data that is relevant for type converter processing.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,conditionProperty: DependencyProperty,conditionValue: object)
  __new__(cls: type,conditionProperty: DependencyProperty,conditionValue: object,sourceName: str)
  __new__(cls: type,binding: BindingBase,conditionValue: object)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Binding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the binding that specifies the property of the condition. This is only applicable to System.Windows.MultiDataTrigger objects.

Get: Binding(self: Condition) -> BindingBase

Set: Binding(self: Condition)=value
"""

 Property=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the property of the condition. This is only applicable to System.Windows.MultiTrigger objects.

Get: Property(self: Condition) -> DependencyProperty

Set: Property(self: Condition)=value
"""

 SourceName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the object with the property that causes the associated setters to be applied. This is only applicable to System.Windows.MultiTrigger objects.

Get: SourceName(self: Condition) -> str

Set: SourceName(self: Condition)=value
"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value of the condition.

Get: Value(self: Condition) -> object

Set: Value(self: Condition)=value
"""


