class ReadOnlyAttribute(Attribute,_Attribute):
 """
 Specifies whether the property this attribute is bound to is read-only or read/write. This class cannot be inherited

 

 ReadOnlyAttribute(isReadOnly: bool)
 """
 def Equals(self,value):
  """
  Equals(self: ReadOnlyAttribute,value: object) -> bool

  

   Indicates whether this instance and a specified object are equal.

  

   value: Another object to compare to.

   Returns: true if value is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ReadOnlyAttribute) -> int

  

   Returns the hash code for this instance.

   Returns: A hash code for the current System.ComponentModel.ReadOnlyAttribute.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: ReadOnlyAttribute) -> bool

  

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
 def __new__(self,isReadOnly):
  """ __new__(cls: type,isReadOnly: bool) """
  pass
 def __ne__(self,*args):
  pass
 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the property this attribute is bound to is read-only.



Get: IsReadOnly(self: ReadOnlyAttribute) -> bool



"""


 Default=None
 No=None
 Yes=None

