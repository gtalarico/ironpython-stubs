class LocalizableAttribute(Attribute,_Attribute):
 """
 Specifies whether a property should be localized. This class cannot be inherited.

 

 LocalizableAttribute(isLocalizable: bool)
 """
 def Equals(self,obj):
  """
  Equals(self: LocalizableAttribute,obj: object) -> bool

  

   Returns whether the value of the given object is equal to the current 

    System.ComponentModel.LocalizableAttribute.

  

  

   obj: The object to test the value equality of.

   Returns: true if the value of the given object is equal to that of the current; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: LocalizableAttribute) -> int

  

   Returns the hash code for this instance.

   Returns: A hash code for the current System.ComponentModel.LocalizableAttribute.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: LocalizableAttribute) -> bool

  

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
 def __new__(self,isLocalizable):
  """ __new__(cls: type,isLocalizable: bool) """
  pass
 def __ne__(self,*args):
  pass
 IsLocalizable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether a property should be localized.



Get: IsLocalizable(self: LocalizableAttribute) -> bool



"""


 Default=None
 No=None
 Yes=None

