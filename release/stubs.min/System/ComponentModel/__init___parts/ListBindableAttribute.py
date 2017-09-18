class ListBindableAttribute(Attribute,_Attribute):
 """
 Specifies that a list can be used as a data source. A visual designer should use this attribute to determine whether to display a particular list in a data-binding picker. This class cannot be inherited.

 

 ListBindableAttribute(listBindable: bool)

 ListBindableAttribute(flags: BindableSupport)
 """
 def Equals(self,obj):
  """
  Equals(self: ListBindableAttribute,obj: object) -> bool

  

   Returns whether the object passed is equal to this System.ComponentModel.ListBindableAttribute.

  

   obj: The object to test equality with.

   Returns: true if the object passed is equal to this System.ComponentModel.ListBindableAttribute; 

    otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ListBindableAttribute) -> int

  

   Returns the hash code for this instance.

   Returns: A hash code for the current System.ComponentModel.ListBindableAttribute.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: ListBindableAttribute) -> bool

  

   Returns whether System.ComponentModel.ListBindableAttribute.ListBindable is set to the default 

    value.

  

   Returns: true if System.ComponentModel.ListBindableAttribute.ListBindable is set to the default value; 

    otherwise,false.
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
  __new__(cls: type,listBindable: bool)

  __new__(cls: type,flags: BindableSupport)
  """
  pass
 def __ne__(self,*args):
  pass
 ListBindable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether the list is bindable.



Get: ListBindable(self: ListBindableAttribute) -> bool



"""


 Default=None
 No=None
 Yes=None

