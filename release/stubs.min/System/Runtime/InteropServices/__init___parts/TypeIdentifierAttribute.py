class TypeIdentifierAttribute(Attribute,_Attribute):
 """
 Provides support for type equivalence.

 

 TypeIdentifierAttribute()

 TypeIdentifierAttribute(scope: str,identifier: str)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,scope=None,identifier=None):
  """
  __new__(cls: type)

  __new__(cls: type,scope: str,identifier: str)
  """
  pass
 Identifier=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value of the identifier parameter that was passed to the System.Runtime.InteropServices.TypeIdentifierAttribute.#ctor(System.String,System.String) constructor.



Get: Identifier(self: TypeIdentifierAttribute) -> str



"""

 Scope=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value of the scope parameter that was passed to the System.Runtime.InteropServices.TypeIdentifierAttribute.#ctor(System.String,System.String) constructor.



Get: Scope(self: TypeIdentifierAttribute) -> str



"""


