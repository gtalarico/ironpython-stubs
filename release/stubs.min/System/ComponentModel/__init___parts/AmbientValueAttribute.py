class AmbientValueAttribute(Attribute,_Attribute):
 """
 Specifies the value to pass to a property to cause the property to get its value from another source. This is known as ambience. This class cannot be inherited.

 

 AmbientValueAttribute(type: Type,value: str)

 AmbientValueAttribute(value: Char)

 AmbientValueAttribute(value: Byte)

 AmbientValueAttribute(value: Int16)

 AmbientValueAttribute(value: int)

 AmbientValueAttribute(value: Int64)

 AmbientValueAttribute(value: Single)

 AmbientValueAttribute(value: float)

 AmbientValueAttribute(value: bool)

 AmbientValueAttribute(value: str)

 AmbientValueAttribute(value: object)
 """
 def Equals(self,obj):
  """
  Equals(self: AmbientValueAttribute,obj: object) -> bool

  

   Determines whether the specified System.ComponentModel.AmbientValueAttribute is equal to the 

    current System.ComponentModel.AmbientValueAttribute.

  

  

   obj: The System.ComponentModel.AmbientValueAttribute to compare with the current 

    System.ComponentModel.AmbientValueAttribute.

  

   Returns: true if the specified System.ComponentModel.AmbientValueAttribute is equal to the current 

    System.ComponentModel.AmbientValueAttribute; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: AmbientValueAttribute) -> int

  

   Returns the hash code for this instance.

   Returns: A hash code for the current System.ComponentModel.AmbientValueAttribute.
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
  __new__(cls: type,type: Type,value: str)

  __new__(cls: type,value: Char)

  __new__(cls: type,value: Byte)

  __new__(cls: type,value: Int16)

  __new__(cls: type,value: int)

  __new__(cls: type,value: Int64)

  __new__(cls: type,value: Single)

  __new__(cls: type,value: float)

  __new__(cls: type,value: bool)

  __new__(cls: type,value: str)

  __new__(cls: type,value: object)
  """
  pass
 def __ne__(self,*args):
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the object that is the value of this System.ComponentModel.AmbientValueAttribute.



Get: Value(self: AmbientValueAttribute) -> object



"""


