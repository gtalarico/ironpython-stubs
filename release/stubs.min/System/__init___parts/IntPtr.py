class IntPtr(object,ISerializable):
 """
 A platform-specific type that is used to represent a pointer or a handle.

 

 IntPtr(value: int)

 IntPtr(value: Int64)

 IntPtr(value: Void*)
 """
 @staticmethod
 def Add(pointer,offset):
  """
  Add(pointer: IntPtr,offset: int) -> IntPtr

  

   Adds an offset to the value of a pointer.

  

   pointer: The pointer to add the offset to.

   offset: The offset to add.

   Returns: A new pointer that reflects the addition of offset to pointer.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: IntPtr,obj: object) -> bool

  

   Returns a value indicating whether this instance is equal to a specified object.

  

   obj: An object to compare with this instance or null.

   Returns: true if obj is an instance of System.IntPtr and equals the value of this instance; otherwise,

    false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: IntPtr) -> int

  

   Returns the hash code for this instance.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 @staticmethod
 def Subtract(pointer,offset):
  """
  Subtract(pointer: IntPtr,offset: int) -> IntPtr

  

   Subtracts an offset from the value of a pointer.

  

   pointer: The pointer to subtract the offset from.

   offset: The offset to subtract.

   Returns: A new pointer that reflects the subtraction of offset from pointer.
  """
  pass
 def ToInt32(self):
  """
  ToInt32(self: IntPtr) -> int

  

   Converts the value of this instance to a 32-bit signed integer.

   Returns: A 32-bit signed integer equal to the value of this instance.
  """
  pass
 def ToInt64(self):
  """
  ToInt64(self: IntPtr) -> Int64

  

   Converts the value of this instance to a 64-bit signed integer.

   Returns: A 64-bit signed integer equal to the value of this instance.
  """
  pass
 def ToPointer(self):
  """
  ToPointer(self: IntPtr) -> Void*

  

   Converts the value of this instance to a pointer to an unspecified type.

   Returns: A pointer to System.Void; that is,a pointer to memory containing data of an unspecified type.
  """
  pass
 def ToString(self,format=None):
  """
  ToString(self: IntPtr,format: str) -> str

  

   Converts the numeric value of the current System.IntPtr object to its equivalent string 

    representation.

  

  

   format: A format specification that governs how the current System.IntPtr object is converted.

   Returns: The string representation of the value of the current System.IntPtr object.

  ToString(self: IntPtr) -> str

  

   Converts the numeric value of the current System.IntPtr object to its equivalent string 

    representation.

  

   Returns: The string representation of the value of this instance.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __int__(self,*args):
  """ __int__(value: IntPtr) -> int """
  pass
 def __long__(self,*args):
  """ __int__(value: IntPtr) -> int """
  pass
 @staticmethod
 def __new__(self,value):
  """
  __new__(cls: type,value: int)

  __new__(cls: type,value: Int64)

  __new__(cls: type,value: Void*)

  __new__[IntPtr]() -> IntPtr
  """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-y """
  pass
 Size=4
 Zero=None

