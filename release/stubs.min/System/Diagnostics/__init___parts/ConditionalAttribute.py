class ConditionalAttribute:
 """
 Indicates to compilers that a method call or attribute should be ignored unless a specified conditional compilation symbol is defined.
 
 ConditionalAttribute(conditionString: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ConditionalAttribute()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,conditionString):
  """ __new__(cls: type,conditionString: str) """
  pass
 def __reduce_ex__(self,*args):
  pass
 ConditionString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the conditional compilation symbol that is associated with the System.Diagnostics.ConditionalAttribute attribute.

Get: ConditionString(self: ConditionalAttribute) -> str

"""


