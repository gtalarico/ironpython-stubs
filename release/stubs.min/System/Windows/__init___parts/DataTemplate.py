class DataTemplate(FrameworkTemplate,INameScope,ISealable,IHaveResources,IQueryAmbient):
 """
 Describes the visual structure of a data object.
 
 DataTemplate()
 DataTemplate(dataType: object)
 """
 def ValidateTemplatedParent(self,*args):
  """
  ValidateTemplatedParent(self: DataTemplate,templatedParent: FrameworkElement)
   Checks the templated parent against a set of rules.
  
   templatedParent: The element this template is applied to.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,dataType=None):
  """
  __new__(cls: type)
  __new__(cls: type,dataType: object)
  """
  pass
 DataTemplateKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the default key of the System.Windows.DataTemplate.

Get: DataTemplateKey(self: DataTemplate) -> object

"""

 DataType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the type for which this System.Windows.DataTemplate is intended.

Get: DataType(self: DataTemplate) -> object

Set: DataType(self: DataTemplate)=value
"""

 Triggers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of triggers that apply property values or perform actions based on one or more conditions.

Get: Triggers(self: DataTemplate) -> TriggerCollection

"""


