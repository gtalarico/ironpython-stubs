class DesignOnlyAttribute(Attribute,_Attribute):
 """
 Specifies whether a property can only be set at design time.

 

 DesignOnlyAttribute(isDesignOnly: bool)
 """
 def Equals(self,obj):
  """
  Equals(self: DesignOnlyAttribute,obj: object) -> bool

  

   Returns whether the value of the given object is equal to the current 

    System.ComponentModel.DesignOnlyAttribute.

  

  

   obj: The object to test the value equality of.

   Returns: true if the value of the given object is equal to that of the current; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: DesignOnlyAttribute) -> int """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: DesignOnlyAttribute) -> bool

  

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
 def __new__(self,isDesignOnly):
  """ __new__(cls: type,isDesignOnly: bool) """
  pass
 def __ne__(self,*args):
  pass
 IsDesignOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether a property can be set only at design time.



Get: IsDesignOnly(self: DesignOnlyAttribute) -> bool



"""


 Default=None
 No=None
 Yes=None

