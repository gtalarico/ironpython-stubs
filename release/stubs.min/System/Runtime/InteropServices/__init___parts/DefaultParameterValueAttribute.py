class DefaultParameterValueAttribute(Attribute,_Attribute):
 """
 Sets the default value of a parameter when called from a language that supports default parameters. This class cannot be inherited.

 

 DefaultParameterValueAttribute(value: object)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,value):
  """ __new__(cls: type,value: object) """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the default value of a parameter.



Get: Value(self: DefaultParameterValueAttribute) -> object



"""


