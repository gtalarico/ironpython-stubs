class DataObjectMethodAttribute(Attribute,_Attribute):
 """
 Identifies a data operation method exposed by a type,what type of operation the method performs,and whether the method is the default data method. This class cannot be inherited.

 

 DataObjectMethodAttribute(methodType: DataObjectMethodType)

 DataObjectMethodAttribute(methodType: DataObjectMethodType,isDefault: bool)
 """
 def Equals(self,obj):
  """
  Equals(self: DataObjectMethodAttribute,obj: object) -> bool

  

   Returns a value indicating whether this instance is equal to a specified object.

  

   obj: An object to compare with this instance of System.ComponentModel.DataObjectMethodAttribute.

   Returns: true if this instance is the same as the instance specified by the obj parameter; otherwise,

    false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DataObjectMethodAttribute) -> int

  

   Returns the hash code for this instance.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def Match(self,obj):
  """
  Match(self: DataObjectMethodAttribute,obj: object) -> bool

  

   Gets a value indicating whether this instance shares a common pattern with a specified attribute.

  

   obj: An object to compare with this instance of System.ComponentModel.DataObjectMethodAttribute.

   Returns: true if this instance is the same as the instance specified by the obj parameter; otherwise,

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
 def __new__(self,methodType,isDefault=None):
  """
  __new__(cls: type,methodType: DataObjectMethodType)

  __new__(cls: type,methodType: DataObjectMethodType,isDefault: bool)
  """
  pass
 def __ne__(self,*args):
  pass
 IsDefault=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the method that the System.ComponentModel.DataObjectMethodAttribute is applied to is the default data method exposed by the data object for a specific method type.



Get: IsDefault(self: DataObjectMethodAttribute) -> bool



"""

 MethodType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.ComponentModel.DataObjectMethodType value indicating the type of data operation the method performs.



Get: MethodType(self: DataObjectMethodAttribute) -> DataObjectMethodType



"""


