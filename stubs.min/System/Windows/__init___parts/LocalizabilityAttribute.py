class LocalizabilityAttribute(Attribute,_Attribute):
 """
 Specifies the localization attributes for a binary XAML (BAML) class or class member.
 
 LocalizabilityAttribute(category: LocalizationCategory)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,category):
  """ __new__(cls: type,category: LocalizationCategory) """
  pass
 Category=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the category setting of the localization attribute's targeted value.

Get: Category(self: LocalizabilityAttribute) -> LocalizationCategory

"""

 Modifiability=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the modifiability setting of the localization attribute's targeted value.

Get: Modifiability(self: LocalizabilityAttribute) -> Modifiability

Set: Modifiability(self: LocalizabilityAttribute)=value
"""

 Readability=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the readability setting of the localization attribute's targeted value.

Get: Readability(self: LocalizabilityAttribute) -> Readability

Set: Readability(self: LocalizabilityAttribute)=value
"""


