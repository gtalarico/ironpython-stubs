class RuntimeFieldHandle(object,ISerializable):
 """ Represents a field using an internal metadata token. """
 def Equals(self,*__args):
  """
  Equals(self: RuntimeFieldHandle,handle: RuntimeFieldHandle) -> bool

  

   Indicates whether the current instance is equal to the specified System.RuntimeFieldHandle.

  

   handle: The System.RuntimeFieldHandle to compare to the current instance.

   Returns: true if the value of handle is equal to the value of the current instance; otherwise,false.

  Equals(self: RuntimeFieldHandle,obj: object) -> bool

  

   Indicates whether the current instance is equal to the specified object.

  

   obj: The object to compare to the current instance.

   Returns: true if obj is a System.RuntimeFieldHandle and equal to the value of the current instance; 

    otherwise,false.
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: RuntimeFieldHandle) -> int """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: RuntimeFieldHandle,info: SerializationInfo,context: StreamingContext)

   Populates a System.Runtime.Serialization.SerializationInfo with the data necessary to 

    deserialize the field represented by the current instance.

  

  

   info: The System.Runtime.Serialization.SerializationInfo object to populate with serialization 

    information.

  

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
 """Gets a handle to the field represented by the current instance.



Get: Value(self: RuntimeFieldHandle) -> IntPtr



"""


