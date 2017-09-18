class RecommendedAsConfigurableAttribute(Attribute,_Attribute):
 """
 Specifies that the property can be used as an application setting.

 

 RecommendedAsConfigurableAttribute(recommendedAsConfigurable: bool)
 """
 def Equals(self,obj):
  """
  Equals(self: RecommendedAsConfigurableAttribute,obj: object) -> bool

  

   Indicates whether this instance and a specified object are equal.

  

   obj: Another object to compare to.

   Returns: true if obj is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: RecommendedAsConfigurableAttribute) -> int

  

   Returns the hash code for this instance.

   Returns: A hash code for the current System.ComponentModel.RecommendedAsConfigurableAttribute.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: RecommendedAsConfigurableAttribute) -> bool

  

   Indicates whether the value of this instance is the default value for the class.

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
 def __new__(self,recommendedAsConfigurable):
  """ __new__(cls: type,recommendedAsConfigurable: bool) """
  pass
 def __ne__(self,*args):
  pass
 RecommendedAsConfigurable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the property this attribute is bound to can be used as an application setting.



Get: RecommendedAsConfigurable(self: RecommendedAsConfigurableAttribute) -> bool



"""


 Default=None
 No=None
 Yes=None

