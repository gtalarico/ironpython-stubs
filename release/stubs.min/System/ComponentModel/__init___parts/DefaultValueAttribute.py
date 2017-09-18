class DefaultValueAttribute(Attribute,_Attribute):
 """
 Specifies the default value for a property.

 

 DefaultValueAttribute(type: Type,value: str)

 DefaultValueAttribute(value: Char)

 DefaultValueAttribute(value: Byte)

 DefaultValueAttribute(value: Int16)

 DefaultValueAttribute(value: int)

 DefaultValueAttribute(value: Int64)

 DefaultValueAttribute(value: Single)

 DefaultValueAttribute(value: float)

 DefaultValueAttribute(value: bool)

 DefaultValueAttribute(value: str)

 DefaultValueAttribute(value: object)
 """
 def Equals(self,obj):
  """
  Equals(self: DefaultValueAttribute,obj: object) -> bool

  

   Returns whether the value of the given object is equal to the current 

    System.ComponentModel.DefaultValueAttribute.

  

  

   obj: The object to test the value equality of.

   Returns: true if the value of the given object is equal to that of the current; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: DefaultValueAttribute) -> int """
  pass
 def SetValue(self,*args):
  """
  SetValue(self: DefaultValueAttribute,value: object)

   Sets the default value for the property to which this attribute is bound.

  

   value: The default value.
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
 """Gets the default value of the property this attribute is bound to.



Get: Value(self: DefaultValueAttribute) -> object



"""


