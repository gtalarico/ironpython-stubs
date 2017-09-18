class RuntimeTypeHandle(object,ISerializable):
 """ Represents a type using an internal metadata token. """
 def Equals(self,*__args):
  """
  Equals(self: RuntimeTypeHandle,handle: RuntimeTypeHandle) -> bool

  

   Indicates whether the specified System.RuntimeTypeHandle structure is equal to the current 

    System.RuntimeTypeHandle structure.

  

  

   handle: The System.RuntimeTypeHandle structure to compare to the current instance.

   Returns: true if the value of handle is equal to the value of this instance; otherwise,false.

  Equals(self: RuntimeTypeHandle,obj: object) -> bool

  

   Indicates whether the specified object is equal to the current System.RuntimeTypeHandle 

    structure.

  

  

   obj: An object to compare to the current instance.

   Returns: true if obj is a System.RuntimeTypeHandle structure and is equal to the value of this instance; 

    otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: RuntimeTypeHandle) -> int

  

   Returns the hash code for the current instance.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def GetModuleHandle(self):
  """
  GetModuleHandle(self: RuntimeTypeHandle) -> ModuleHandle

  

   Gets a handle to the module that contains the type represented by the current instance.

   Returns: A System.ModuleHandle structure representing a handle to the module that contains the type 

    represented by the current instance.
  """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: RuntimeTypeHandle,info: SerializationInfo,context: StreamingContext)

   Populates a System.Runtime.Serialization.SerializationInfo with the data necessary to 

    deserialize the type represented by the current instance.

  

  

   info: The object to be populated with serialization information.

   context: (Reserved) The location where serialized data will be stored and retrieved.
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
 """Gets a handle to the type represented by this instance.



Get: Value(self: RuntimeTypeHandle) -> IntPtr



"""


