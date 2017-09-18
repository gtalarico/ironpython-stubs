class AttributeProviderAttribute(Attribute,_Attribute):
 """
 Enables attribute redirection. This class cannot be inherited.

 

 AttributeProviderAttribute(typeName: str)

 AttributeProviderAttribute(typeName: str,propertyName: str)

 AttributeProviderAttribute(type: Type)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,typeName: str)

  __new__(cls: type,typeName: str,propertyName: str)

  __new__(cls: type,type: Type)
  """
  pass
 PropertyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the property for which attributes will be retrieved.



Get: PropertyName(self: AttributeProviderAttribute) -> str



"""

 TypeName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the assembly qualified type name passed into the constructor.



Get: TypeName(self: AttributeProviderAttribute) -> str



"""


