class TemplatePartAttribute(Attribute,_Attribute):
 """
 Represents an attribute that is applied to the class definition to identify the types of the named parts that are used for templating.
 
 TemplatePartAttribute()
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the pre-defined name of the part.

Get: Name(self: TemplatePartAttribute) -> str

Set: Name(self: TemplatePartAttribute)=value
"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the type of the named part this attribute is identifying.

Get: Type(self: TemplatePartAttribute) -> Type

Set: Type(self: TemplatePartAttribute)=value
"""


