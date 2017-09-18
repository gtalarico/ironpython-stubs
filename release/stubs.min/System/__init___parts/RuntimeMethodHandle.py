class RuntimeMethodHandle(object,ISerializable):
 """ System.RuntimeMethodHandle is a handle to the internal metadata representation of a method. """
 def Equals(self,*__args):
  """
  Equals(self: RuntimeMethodHandle,handle: RuntimeMethodHandle) -> bool

  

   Indicates whether this instance is equal to a specified System.RuntimeMethodHandle.

  

   handle: A System.RuntimeMethodHandle to compare to this instance.

   Returns: true if handle is equal to the value of this instance; otherwise,false.

  Equals(self: RuntimeMethodHandle,obj: object) -> bool

  

   Indicates whether this instance is equal to a specified object.

  

   obj: A System.Object to compare to this instance.

   Returns: true if obj is a System.RuntimeMethodHandle and equal to the value of this instance; otherwise,

    false.
  """
  pass
 def GetFunctionPointer(self):
  """
  GetFunctionPointer(self: RuntimeMethodHandle) -> IntPtr

  

   Obtains a pointer to the method represented by this instance.

   Returns: A pointer to the method represented by this instance.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: RuntimeMethodHandle) -> int

  

   Returns the hash code for this instance.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: RuntimeMethodHandle,info: SerializationInfo,context: StreamingContext)

   Populates a System.Runtime.Serialization.SerializationInfo with the data necessary to 

    deserialize the field represented by this instance.

  

  

   info: The object to populate with serialization information.

   context: (Reserved) The place to store and retrieve serialized data.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
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
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value of this instance.



Get: Value(self: RuntimeMethodHandle) -> IntPtr



"""


