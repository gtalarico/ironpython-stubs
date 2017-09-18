class PasswordPropertyTextAttribute(Attribute,_Attribute):
 """
 Indicates that an object's text representation is obscured by characters such as asterisks. This class cannot be inherited.

 

 PasswordPropertyTextAttribute()

 PasswordPropertyTextAttribute(password: bool)
 """
 def Equals(self,o):
  """
  Equals(self: PasswordPropertyTextAttribute,o: object) -> bool

  

   Determines whether two System.ComponentModel.PasswordPropertyTextAttribute instances are equal.

  

   o: The System.ComponentModel.PasswordPropertyTextAttribute to compare with the current 

    System.ComponentModel.PasswordPropertyTextAttribute.

  

   Returns: true if the specified System.ComponentModel.PasswordPropertyTextAttribute is equal to the 

    current System.ComponentModel.PasswordPropertyTextAttribute; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PasswordPropertyTextAttribute) -> int

  

   Returns the hash code for this instance.

   Returns: A hash code for the current System.ComponentModel.PasswordPropertyTextAttribute.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: PasswordPropertyTextAttribute) -> bool

  

   Returns an indication whether the value of this instance is the default value.

   Returns: true if this instance is the default attribute for the class; otherwise,false.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,password=None):
  """
  __new__(cls: type)

  __new__(cls: type,password: bool)
  """
  pass
 def __ne__(self,*args):
  pass
 Password=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating if the property for which the System.ComponentModel.PasswordPropertyTextAttribute is defined should be shown as password text.



Get: Password(self: PasswordPropertyTextAttribute) -> bool



"""


 Default=None
 No=None
 Yes=None

