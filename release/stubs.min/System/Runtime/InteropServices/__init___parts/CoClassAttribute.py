class CoClassAttribute:
 """
 Specifies the class identifier of a coclass imported from a type library.
 
 CoClassAttribute(coClass: Type)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return CoClassAttribute()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,coClass):
  """ __new__(cls: type,coClass: Type) """
  pass
 CoClass=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the class identifier of the original coclass.

Get: CoClass(self: CoClassAttribute) -> Type

"""


