class BrowsableAttribute(Attribute,_Attribute):
 """
 Specifies whether a property or event should be displayed in a Properties window.

 

 BrowsableAttribute(browsable: bool)
 """
 def Equals(self,obj):
  """
  Equals(self: BrowsableAttribute,obj: object) -> bool

  

   Indicates whether this instance and a specified object are equal.

  

   obj: Another object to compare to.

   Returns: true if obj is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: BrowsableAttribute) -> int

  

   Returns the hash code for this instance.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: BrowsableAttribute) -> bool

  

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
 def __new__(self,browsable):
  """ __new__(cls: type,browsable: bool) """
  pass
 def __ne__(self,*args):
  pass
 Browsable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether an object is browsable.



Get: Browsable(self: BrowsableAttribute) -> bool



"""


 Default=None
 No=None
 Yes=None

