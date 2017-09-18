class EditorAttribute(Attribute,_Attribute):
 """
 Specifies the editor to use to change a property. This class cannot be inherited.

 

 EditorAttribute()

 EditorAttribute(typeName: str,baseTypeName: str)

 EditorAttribute(typeName: str,baseType: Type)

 EditorAttribute(type: Type,baseType: Type)
 """
 def Equals(self,obj):
  """
  Equals(self: EditorAttribute,obj: object) -> bool

  

   Returns whether the value of the given object is equal to the current 

    System.ComponentModel.EditorAttribute.

  

  

   obj: The object to test the value equality of.

   Returns: true if the value of the given object is equal to that of the current object; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: EditorAttribute) -> int """
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
  __new__(cls: type)

  __new__(cls: type,typeName: str,baseTypeName: str)

  __new__(cls: type,typeName: str,baseType: Type)

  __new__(cls: type,type: Type,baseType: Type)
  """
  pass
 def __ne__(self,*args):
  pass
 EditorBaseTypeName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the base class or interface serving as a lookup key for this editor.



Get: EditorBaseTypeName(self: EditorAttribute) -> str



"""

 EditorTypeName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the editor class in the System.Type.AssemblyQualifiedName format.



Get: EditorTypeName(self: EditorAttribute) -> str



"""

 TypeId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a unique ID for this attribute type.



Get: TypeId(self: EditorAttribute) -> object



"""


