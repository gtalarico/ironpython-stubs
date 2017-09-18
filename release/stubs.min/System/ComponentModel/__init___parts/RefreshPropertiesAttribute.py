class RefreshPropertiesAttribute(Attribute,_Attribute):
 """
 Indicates that the property grid should refresh when the associated property value changes. This class cannot be inherited.

 

 RefreshPropertiesAttribute(refresh: RefreshProperties)
 """
 def Equals(self,value):
  """
  Equals(self: RefreshPropertiesAttribute,value: object) -> bool

  

   Overrides the object's erload:System.Object.Equals method.

  

   value: The object to test for equality.

   Returns: true if the specified object is the same; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: RefreshPropertiesAttribute) -> int

  

   Returns the hash code for this object.

   Returns: The hash code for the object that the attribute belongs to.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: RefreshPropertiesAttribute) -> bool

  

   Gets a value indicating whether the current value of the attribute is the default value for the 

    attribute.

  

   Returns: true if the current value of the attribute is the default; otherwise,false.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,refresh):
  """ __new__(cls: type,refresh: RefreshProperties) """
  pass
 def __ne__(self,*args):
  pass
 RefreshProperties=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the refresh properties for the member.



Get: RefreshProperties(self: RefreshPropertiesAttribute) -> RefreshProperties



"""


 All=None
 Default=None
 Repaint=None

