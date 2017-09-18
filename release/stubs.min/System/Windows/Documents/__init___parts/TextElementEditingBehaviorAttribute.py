class TextElementEditingBehaviorAttribute(Attribute,_Attribute):
 """
 Specifies how a System.Windows.Controls.RichTextBox should handle a custom text element.
 
 TextElementEditingBehaviorAttribute()
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 IsMergeable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Controls.RichTextBox can merge two adjacent text elements.

Get: IsMergeable(self: TextElementEditingBehaviorAttribute) -> bool

Set: IsMergeable(self: TextElementEditingBehaviorAttribute)=value
"""

 IsTypographicOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the text element provides formatting on a character basis,or if the formatting applies to the entire element.

Get: IsTypographicOnly(self: TextElementEditingBehaviorAttribute) -> bool

Set: IsTypographicOnly(self: TextElementEditingBehaviorAttribute)=value
"""


