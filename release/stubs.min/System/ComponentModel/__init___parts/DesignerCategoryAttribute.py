class DesignerCategoryAttribute(Attribute,_Attribute):
 """
 Specifies that the designer for a class belongs to a certain category.

 

 DesignerCategoryAttribute()

 DesignerCategoryAttribute(category: str)
 """
 def Equals(self,obj):
  """
  Equals(self: DesignerCategoryAttribute,obj: object) -> bool

  

   Returns whether the value of the given object is equal to the current 

    System.ComponentModel.DesignOnlyAttribute.

  

  

   obj: The object to test the value equality of.

   Returns: true if the value of the given object is equal to that of the current; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DesignerCategoryAttribute) -> int

  

   Returns the hash code for this instance.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: DesignerCategoryAttribute) -> bool

  

   Determines if this attribute is the default.

   Returns: true if the attribute is the default value for this attribute class; otherwise,false.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,category=None):
  """
  __new__(cls: type)

  __new__(cls: type,category: str)
  """
  pass
 def __ne__(self,*args):
  pass
 Category=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the category.



Get: Category(self: DesignerCategoryAttribute) -> str



"""

 TypeId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a unique identifier for this attribute.



Get: TypeId(self: DesignerCategoryAttribute) -> object



"""


 Component=None
 Default=None
 Form=None
 Generic=None

