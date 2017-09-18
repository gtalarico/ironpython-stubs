class DefaultBindingPropertyAttribute(Attribute,_Attribute):
 """
 Specifies the default binding property for a component. This class cannot be inherited.

 

 DefaultBindingPropertyAttribute()

 DefaultBindingPropertyAttribute(name: str)
 """
 def Equals(self,obj):
  """
  Equals(self: DefaultBindingPropertyAttribute,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to the current 

    System.ComponentModel.DefaultBindingPropertyAttribute instance.

  

  

   obj: The System.Object to compare with the current 

    System.ComponentModel.DefaultBindingPropertyAttribute instance

  

   Returns: true if the object is equal to the current instance; otherwise,false,indicating they are not 

    equal.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DefaultBindingPropertyAttribute) -> int

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,name=None):
  """
  __new__(cls: type)

  __new__(cls: type,name: str)
  """
  pass
 def __ne__(self,*args):
  pass
 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the default binding property for the component to which the System.ComponentModel.DefaultBindingPropertyAttribute is bound.



Get: Name(self: DefaultBindingPropertyAttribute) -> str



"""


 Default=None

