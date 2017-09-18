class TypeDescriptionProviderAttribute(Attribute,_Attribute):
 """
 Specifies the custom type description provider for a class. This class cannot be inherited.

 

 TypeDescriptionProviderAttribute(typeName: str)

 TypeDescriptionProviderAttribute(type: Type)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,typeName: str)

  __new__(cls: type,type: Type)
  """
  pass
 TypeName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type name for the type description provider.



Get: TypeName(self: TypeDescriptionProviderAttribute) -> str



"""


