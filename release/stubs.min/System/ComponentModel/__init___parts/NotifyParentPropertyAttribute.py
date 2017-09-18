class NotifyParentPropertyAttribute(Attribute,_Attribute):
 """
 Indicates that the parent property is notified when the value of the property that this attribute is applied to is modified. This class cannot be inherited.

 

 NotifyParentPropertyAttribute(notifyParent: bool)
 """
 def Equals(self,obj):
  """
  Equals(self: NotifyParentPropertyAttribute,obj: object) -> bool

  

   Gets a value indicating whether the specified object is the same as the current object.

  

   obj: The object to test for equality.

   Returns: true if the object is the same as this object; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: NotifyParentPropertyAttribute) -> int

  

   Gets the hash code for this object.

   Returns: The hash code for the object the attribute belongs to.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: NotifyParentPropertyAttribute) -> bool

  

   Gets a value indicating whether the current value of the attribute is the default value for the 

    attribute.

  

   Returns: true if the current value of the attribute is the default value of the attribute; otherwise,

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
 def __new__(self,notifyParent):
  """ __new__(cls: type,notifyParent: bool) """
  pass
 def __ne__(self,*args):
  pass
 NotifyParent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the parent property should be notified of changes to the value of the property.



Get: NotifyParent(self: NotifyParentPropertyAttribute) -> bool



"""


 Default=None
 No=None
 Yes=None

