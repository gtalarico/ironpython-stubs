class BindableAttribute(Attribute,_Attribute):
 """
 Specifies whether a member is typically used for binding. This class cannot be inherited.

 

 BindableAttribute(bindable: bool)

 BindableAttribute(bindable: bool,direction: BindingDirection)

 BindableAttribute(flags: BindableSupport)

 BindableAttribute(flags: BindableSupport,direction: BindingDirection)
 """
 def Equals(self,obj):
  """
  Equals(self: BindableAttribute,obj: object) -> bool

  

   Determines whether two System.ComponentModel.BindableAttribute objects are equal.

  

   obj: The object to compare.

   Returns: true if the specified System.ComponentModel.BindableAttribute is equal to the current 

    System.ComponentModel.BindableAttribute; false if it is not equal.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: BindableAttribute) -> int

  

   Serves as a hash function for the System.ComponentModel.BindableAttribute class.

   Returns: A hash code for the current System.ComponentModel.BindableAttribute.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: BindableAttribute) -> bool

  

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
 def __new__(self,*__args):
  """
  __new__(cls: type,bindable: bool)

  __new__(cls: type,bindable: bool,direction: BindingDirection)

  __new__(cls: type,flags: BindableSupport)

  __new__(cls: type,flags: BindableSupport,direction: BindingDirection)
  """
  pass
 def __ne__(self,*args):
  pass
 Bindable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating that a property is typically used for binding.



Get: Bindable(self: BindableAttribute) -> bool



"""

 Direction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating the direction or directions of this property's data binding.



Get: Direction(self: BindableAttribute) -> BindingDirection



"""


 Default=None
 No=None
 Yes=None

