class ImmutableObjectAttribute(Attribute,_Attribute):
 """
 Specifies that an object has no subproperties capable of being edited. This class cannot be inherited.

 

 ImmutableObjectAttribute(immutable: bool)
 """
 def Equals(self,obj):
  """
  Equals(self: ImmutableObjectAttribute,obj: object) -> bool

  

   obj: An System.Object to compare with this instance or null.

   Returns: true if obj equals the type and value of this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ImmutableObjectAttribute) -> int

  

   Returns the hash code for this instance.

   Returns: A hash code for the current System.ComponentModel.ImmutableObjectAttribute.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: ImmutableObjectAttribute) -> bool

  

   Indicates whether the value of this instance is the default value.

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
 def __new__(self,immutable):
  """ __new__(cls: type,immutable: bool) """
  pass
 def __ne__(self,*args):
  pass
 Immutable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether the object is immutable.



Get: Immutable(self: ImmutableObjectAttribute) -> bool



"""


 Default=None
 No=None
 Yes=None

