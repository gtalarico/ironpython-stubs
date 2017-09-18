class UIntPtr(object,ISerializable):
 """
 A platform-specific type that is used to represent a pointer or a handle.

 

 UIntPtr(value: UInt32)

 UIntPtr(value: UInt64)

 UIntPtr(value: Void*)
 """
 @staticmethod
 def Add(pointer,offset):
  """
  Add(pointer: UIntPtr,offset: int) -> UIntPtr

  

   Adds an offset to the value of an unsigned pointer.

  

   pointer: The unsigned pointer to add the offset to.

   offset: The offset to add.

   Returns: A new unsigned pointer that reflects the addition of offset to pointer.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: UIntPtr,obj: object) -> bool

  

   Returns a value indicating whether this instance is equal to a specified object.

  

   obj: An object to compare with this instance or null.

   Returns: true if obj is an instance of System.UIntPtr and equals the value of this instance; otherwise,

    false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: UIntPtr) -> int

  

   Returns the hash code for this instance.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 @staticmethod
 def Subtract(pointer,offset):
  """
  Subtract(pointer: UIntPtr,offset: int) -> UIntPtr

  

   Subtracts an offset from the value of an unsigned pointer.

  

   pointer: The unsigned pointer to subtract the offset from.

   offset: The offset to subtract.

   Returns: A new unsigned pointer that reflects the subtraction of offset from pointer.
  """
  pass
 def ToPointer(self):
  """
  ToPointer(self: UIntPtr) -> Void*

  

   Converts the value of this instance to a pointer to an unspecified type.

   Returns: A pointer to System.Void; that is,a pointer to memory containing data of an unspecified type.
  """
  pass
 def ToString(self):
  """
  ToString(self: UIntPtr) -> str

  

   Converts the numeric value of this instance to its equivalent string representation.

   Returns: The string representation of the value of this instance.
  """
  pass
 def ToUInt32(self):
  """
  ToUInt32(self: UIntPtr) -> UInt32

  

   Converts the value of this instance to a 32-bit unsigned integer.

   Returns: A 32-bit unsigned integer equal to the value of this instance.
  """
  pass
 def ToUInt64(self):
  """
  ToUInt64(self: UIntPtr) -> UInt64

  

   Converts the value of this instance to a 64-bit unsigned integer.

   Returns: A 64-bit unsigned integer equal to the value of this instance.
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
 @staticmethod
 def __new__(self,value):
  """
  __new__(cls: type,value: UInt32)

  __new__(cls: type,value: UInt64)

  __new__(cls: type,value: Void*)

  __new__[UIntPtr]() -> UIntPtr
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

