class DesignerAttribute(Attribute,_Attribute):
 """
 Specifies the class used to implement design-time services for a component.

 

 DesignerAttribute(designerTypeName: str)

 DesignerAttribute(designerType: Type)

 DesignerAttribute(designerTypeName: str,designerBaseTypeName: str)

 DesignerAttribute(designerTypeName: str,designerBaseType: Type)

 DesignerAttribute(designerType: Type,designerBaseType: Type)
 """
 def Equals(self,obj):
  """
  Equals(self: DesignerAttribute,obj: object) -> bool

  

   Returns whether the value of the given object is equal to the current 

    System.ComponentModel.DesignerAttribute.

  

  

   obj: The object to test the value equality of.

   Returns: true if the value of the given object is equal to that of the current; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: DesignerAttribute) -> int """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,designerTypeName: str)

  __new__(cls: type,designerType: Type)

  __new__(cls: type,designerTypeName: str,designerBaseTypeName: str)

  __new__(cls: type,designerTypeName: str,designerBaseType: Type)

  __new__(cls: type,designerType: Type,designerBaseType: Type)
  """
  pass
 def __ne__(self,*args):
  pass
 DesignerBaseTypeName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the base type of this designer.



Get: DesignerBaseTypeName(self: DesignerAttribute) -> str



"""

 DesignerTypeName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the designer type associated with this designer attribute.



Get: DesignerTypeName(self: DesignerAttribute) -> str



"""

 TypeId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a unique ID for this attribute type.



Get: TypeId(self: DesignerAttribute) -> object



"""


