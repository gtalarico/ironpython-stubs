class ControlTemplate(FrameworkTemplate,INameScope,ISealable,IHaveResources,IQueryAmbient):
 """
 Specifies the visual structure and behavioral aspects of a System.Windows.Controls.Control that can be shared across multiple instances of the control.

 

 ControlTemplate()

 ControlTemplate(targetType: Type)
 """
 def ValidateTemplatedParent(self,*args):
  """
  ValidateTemplatedParent(self: ControlTemplate,templatedParent: FrameworkElement)

   Checks the templated parent against a set of rules.

  

   templatedParent: The element this template is applied to.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,targetType=None):
  """
  __new__(cls: type)

  __new__(cls: type,targetType: Type)
  """
  pass
 TargetType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the type for which this System.Windows.Controls.ControlTemplate is intended.



Get: TargetType(self: ControlTemplate) -> Type



Set: TargetType(self: ControlTemplate)=value

"""

 Triggers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of System.Windows.TriggerBase objects that apply property changes or perform actions based on specified conditions.



Get: Triggers(self: ControlTemplate) -> TriggerCollection



"""


