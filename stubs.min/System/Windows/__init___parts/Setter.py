class Setter(SetterBase,ISupportInitialize):
 """
 Represents a setter that applies a property value.
 
 Setter()
 Setter(property: DependencyProperty,value: object)
 Setter(property: DependencyProperty,value: object,targetName: str)
 """
 def CheckSealed(self,*args):
  """
  CheckSealed(self: SetterBase)
   Checks whether this object is read-only and cannot be changed.
  """
  pass
 @staticmethod
 def ReceiveMarkupExtension(targetObject,eventArgs):
  """
  ReceiveMarkupExtension(targetObject: object,eventArgs: XamlSetMarkupExtensionEventArgs)
   Handles cases where a markup extension provides a value for a property of 
    System.Windows.Setter object.
  
  
   targetObject: The object where the markup extension sets the value.
   eventArgs: Data that is relevant for markup extension processing.
  """
  pass
 @staticmethod
 def ReceiveTypeConverter(targetObject,eventArgs):
  """
  ReceiveTypeConverter(targetObject: object,eventArgs: XamlSetTypeConverterEventArgs)
   Handles cases where a type converter provides a value for a property of a 
    System.Windows.Setter object.
  
  
   targetObject: The object where the type converter sets the value.
   eventArgs: Data that is relevant for type converter processing.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,property=None,value=None,targetName=None):
  """
  __new__(cls: type)
  __new__(cls: type,property: DependencyProperty,value: object)
  __new__(cls: type,property: DependencyProperty,value: object,targetName: str)
  """
  pass
 Property=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the property to which the System.Windows.Setter.Value will be applied.

Get: Property(self: Setter) -> DependencyProperty

Set: Property(self: Setter)=value
"""

 TargetName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the object this System.Windows.Setter is intended for.

Get: TargetName(self: Setter) -> str

Set: TargetName(self: Setter)=value
"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value to apply to the property that is specified by this System.Windows.Setter.

Get: Value(self: Setter) -> object

Set: Value(self: Setter)=value
"""


