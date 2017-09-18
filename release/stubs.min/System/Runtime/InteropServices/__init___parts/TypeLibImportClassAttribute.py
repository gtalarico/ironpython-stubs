class TypeLibImportClassAttribute(Attribute,_Attribute):
 """
 Specifies which System.Type exclusively uses an interface. This class cannot be inherited.

 

 TypeLibImportClassAttribute(importClass: Type)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,importClass):
  """ __new__(cls: type,importClass: Type) """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of a System.Type object that exclusively uses an interface.



Get: Value(self: TypeLibImportClassAttribute) -> str



"""


