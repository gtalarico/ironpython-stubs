class CLSCompliantAttribute:
 """
 Indicates whether a program element is compliant with the Common Language Specification (CLS). This class cannot be inherited.
 
 CLSCompliantAttribute(isCompliant: bool)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return CLSCompliantAttribute()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,isCompliant):
  """ __new__(cls: type,isCompliant: bool) """
  pass
 def __reduce_ex__(self,*args):
  pass
 IsCompliant=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Boolean value indicating whether the indicated program element is CLS-compliant.

Get: IsCompliant(self: CLSCompliantAttribute) -> bool

"""


