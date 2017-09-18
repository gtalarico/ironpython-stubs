class ObsoleteAttribute(Attribute,_Attribute):
 """
 Marks the program elements that are no longer in use. This class cannot be inherited.

 

 ObsoleteAttribute()

 ObsoleteAttribute(message: str)

 ObsoleteAttribute(message: str,error: bool)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message=None,error=None):
  """
  __new__(cls: type)

  __new__(cls: type,message: str)

  __new__(cls: type,message: str,error: bool)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 IsError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a Boolean value indicating whether the compiler will treat usage of the obsolete program element as an error.



Get: IsError(self: ObsoleteAttribute) -> bool



"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the workaround message,including a description of the alternative program elements.



Get: Message(self: ObsoleteAttribute) -> str



"""


