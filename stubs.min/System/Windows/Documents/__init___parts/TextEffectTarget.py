class TextEffectTarget(object):
 """ Result from using System.Windows.Documents.TextEffectResolver to set an effect on text. This consists of the System.Windows.Media.TextEffect created and the System.Windows.DependencyObject to which the System.Windows.Media.TextEffect should be set. """
 def Disable(self):
  """
  Disable(self: TextEffectTarget)
   Disables the System.Windows.Media.TextEffect on the effect target.
  """
  pass
 def Enable(self):
  """
  Enable(self: TextEffectTarget)
   Enables the System.Windows.Media.TextEffect on the target text.
  """
  pass
 Element=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.DependencyObject that the System.Windows.Media.TextEffect is targeting.

Get: Element(self: TextEffectTarget) -> DependencyObject

"""

 IsEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines whether the text effect is enabled on the target element

Get: IsEnabled(self: TextEffectTarget) -> bool

"""

 TextEffect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Media.TextEffect of the System.Windows.Documents.TextEffectTarget.

Get: TextEffect(self: TextEffectTarget) -> TextEffect

"""


