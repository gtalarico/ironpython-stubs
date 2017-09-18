class MergablePropertyAttribute(Attribute,_Attribute):
 """
 Specifies that this property can be combined with properties belonging to other objects in a Properties window.

 

 MergablePropertyAttribute(allowMerge: bool)
 """
 def Equals(self,obj):
  """
  Equals(self: MergablePropertyAttribute,obj: object) -> bool

  

   Indicates whether this instance and a specified object are equal.

  

   obj: Another object to compare to.

   Returns: true if obj is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: MergablePropertyAttribute) -> int

  

   Returns the hash code for this instance.

   Returns: A hash code for the current System.ComponentModel.MergablePropertyAttribute.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: MergablePropertyAttribute) -> bool

  

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
 def __new__(self,allowMerge):
  """ __new__(cls: type,allowMerge: bool) """
  pass
 def __ne__(self,*args):
  pass
 AllowMerge=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this property can be combined with properties belonging to other objects in a Properties window.



Get: AllowMerge(self: MergablePropertyAttribute) -> bool



"""


 Default=None
 No=None
 Yes=None

