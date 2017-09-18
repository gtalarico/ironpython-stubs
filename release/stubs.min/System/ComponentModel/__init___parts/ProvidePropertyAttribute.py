class ProvidePropertyAttribute(Attribute,_Attribute):
 """
 Specifies the name of the property that an implementer of System.ComponentModel.IExtenderProvider offers to other components. This class cannot be inherited

 

 ProvidePropertyAttribute(propertyName: str,receiverType: Type)

 ProvidePropertyAttribute(propertyName: str,receiverTypeName: str)
 """
 def Equals(self,obj):
  """
  Equals(self: ProvidePropertyAttribute,obj: object) -> bool

  

   Returns whether the value of the given object is equal to the current 

    System.ComponentModel.ProvidePropertyAttribute.

  

  

   obj: The object to test the value equality of.

   Returns: true if the value of the given object is equal to that of the current; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ProvidePropertyAttribute) -> int

  

   Returns the hash code for this instance.

   Returns: A hash code for the current System.ComponentModel.ProvidePropertyAttribute.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,propertyName,*__args):
  """
  __new__(cls: type,propertyName: str,receiverType: Type)

  __new__(cls: type,propertyName: str,receiverTypeName: str)
  """
  pass
 def __ne__(self,*args):
  pass
 PropertyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of a property that this class provides.



Get: PropertyName(self: ProvidePropertyAttribute) -> str



"""

 ReceiverTypeName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the data type this property can extend.



Get: ReceiverTypeName(self: ProvidePropertyAttribute) -> str



"""

 TypeId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a unique identifier for this attribute.



Get: TypeId(self: ProvidePropertyAttribute) -> object



"""


