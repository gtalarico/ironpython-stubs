class ArrayWithOffset(object):
 """
 Encapsulates an array and an offset within the specified array.

 

 ArrayWithOffset(array: object,offset: int)
 """
 def Equals(self,obj):
  """
  Equals(self: ArrayWithOffset,obj: ArrayWithOffset) -> bool

  

   Indicates whether the specified System.Runtime.InteropServices.ArrayWithOffset object matches 

    the current instance.

  

  

   obj: An System.Runtime.InteropServices.ArrayWithOffset object to compare with this instance.

   Returns: true if the specified System.Runtime.InteropServices.ArrayWithOffset object matches the current 

    instance; otherwise,false.

  

  Equals(self: ArrayWithOffset,obj: object) -> bool

  

   Indicates whether the specified object matches the current 

    System.Runtime.InteropServices.ArrayWithOffset object.

  

  

   obj: Object to compare with this instance.

   Returns: true if the object matches this System.Runtime.InteropServices.ArrayWithOffset; otherwise,false.
  """
  pass
 def GetArray(self):
  """
  GetArray(self: ArrayWithOffset) -> object

  

   Returns the managed array referenced by this System.Runtime.InteropServices.ArrayWithOffset.

   Returns: The managed array this instance references.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ArrayWithOffset) -> int

  

   Returns a hash code for this value type.

   Returns: The hash code for this instance.
  """
  pass
 def GetOffset(self):
  """
  GetOffset(self: ArrayWithOffset) -> int

  

   Returns the offset provided when this System.Runtime.InteropServices.ArrayWithOffset was 

    constructed.

  

   Returns: The offset for this instance.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,array,offset):
  """
  __new__(cls: type,array: object,offset: int)

  __new__[ArrayWithOffset]() -> ArrayWithOffset
  """
  pass
 def __ne__(self,*args):
  pass
