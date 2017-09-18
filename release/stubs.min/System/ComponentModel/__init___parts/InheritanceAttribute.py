class InheritanceAttribute(Attribute,_Attribute):
 """
 Indicates whether the component associated with this attribute has been inherited from a base class. This class cannot be inherited.

 

 InheritanceAttribute()

 InheritanceAttribute(inheritanceLevel: InheritanceLevel)
 """
 def Equals(self,value):
  """
  Equals(self: InheritanceAttribute,value: object) -> bool

  

   Override to test for equality.

  

   value: The object to test.

   Returns: true if the object is the same; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: InheritanceAttribute) -> int

  

   Returns the hashcode for this object.

   Returns: A hash code for the current System.ComponentModel.InheritanceAttribute.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: InheritanceAttribute) -> bool

  

   Gets a value indicating whether the current value of the attribute is the default value for the 

    attribute.

  

   Returns: true if the current value of the attribute is the default; otherwise,false.
  """
  pass
 def ToString(self):
  """
  ToString(self: InheritanceAttribute) -> str

  

   Converts this attribute to a string.

   Returns: A string that represents this System.ComponentModel.InheritanceAttribute.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,inheritanceLevel=None):
  """
  __new__(cls: type)

  __new__(cls: type,inheritanceLevel: InheritanceLevel)
  """
  pass
 def __ne__(self,*args):
  pass
 def __str__(self,*args):
  pass
 InheritanceLevel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current inheritance level stored in this attribute.



Get: InheritanceLevel(self: InheritanceAttribute) -> InheritanceLevel



"""


 Default=None
 Inherited=None
 InheritedReadOnly=None
 NotInherited=None

