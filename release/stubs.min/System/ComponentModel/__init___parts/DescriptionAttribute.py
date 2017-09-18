class DescriptionAttribute(Attribute,_Attribute):
 """
 Specifies a description for a property or event.

 

 DescriptionAttribute()

 DescriptionAttribute(description: str)
 """
 def Equals(self,obj):
  """
  Equals(self: DescriptionAttribute,obj: object) -> bool

  

   Returns whether the value of the given object is equal to the current 

    System.ComponentModel.DescriptionAttribute.

  

  

   obj: The object to test the value equality of.

   Returns: true if the value of the given object is equal to that of the current; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: DescriptionAttribute) -> int """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: DescriptionAttribute) -> bool

  

   Returns a value indicating whether this is the default 

    System.ComponentModel.DescriptionAttribute instance.

  

   Returns: true,if this is the default System.ComponentModel.DescriptionAttribute instance; otherwise,

    false.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,description=None):
  """
  __new__(cls: type)

  __new__(cls: type,description: str)
  """
  pass
 def __ne__(self,*args):
  pass
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the description stored in this attribute.



Get: Description(self: DescriptionAttribute) -> str



"""

 DescriptionValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the string stored as the description.



"""


 Default=None

