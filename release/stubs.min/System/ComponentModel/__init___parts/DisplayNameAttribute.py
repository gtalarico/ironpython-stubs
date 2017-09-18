class DisplayNameAttribute(Attribute,_Attribute):
 """
 Specifies the display name for a property,event,or public void method which takes no arguments.

 

 DisplayNameAttribute()

 DisplayNameAttribute(displayName: str)
 """
 def Equals(self,obj):
  """
  Equals(self: DisplayNameAttribute,obj: object) -> bool

  

   Determines whether two System.ComponentModel.DisplayNameAttribute instances are equal.

  

   obj: The System.ComponentModel.DisplayNameAttribute to test the value equality of.

   Returns: true if the value of the given object is equal to that of the current object; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DisplayNameAttribute) -> int

  

   Returns the hash code for this instance.

   Returns: A hash code for the current System.ComponentModel.DisplayNameAttribute.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: DisplayNameAttribute) -> bool

  

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
 def __new__(self,displayName=None):
  """
  __new__(cls: type)

  __new__(cls: type,displayName: str)
  """
  pass
 def __ne__(self,*args):
  pass
 DisplayName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the display name for a property,event,or public void method that takes no arguments stored in this attribute.



Get: DisplayName(self: DisplayNameAttribute) -> str



"""

 DisplayNameValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the display name.



"""


 Default=None

