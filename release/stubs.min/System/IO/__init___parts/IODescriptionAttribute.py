class IODescriptionAttribute(DescriptionAttribute):
 """
 Sets the description visual designers can display when referencing an event,extender,or property.
 
 IODescriptionAttribute(description: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IODescriptionAttribute()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,description):
  """ __new__(cls: type,description: str) """
  pass
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the description.

Get: Description(self: IODescriptionAttribute) -> str

"""

 DescriptionValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the string stored as the description.

"""


