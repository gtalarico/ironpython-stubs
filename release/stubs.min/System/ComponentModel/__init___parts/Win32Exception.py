class Win32Exception(ExternalException,ISerializable,_Exception):
 """
 Throws an exception for a Win32 error code.

 

 Win32Exception()

 Win32Exception(error: int)

 Win32Exception(error: int,message: str)

 Win32Exception(message: str)

 Win32Exception(message: str,innerException: Exception)
 """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: Win32Exception,info: SerializationInfo,context: StreamingContext)

   Sets the System.Runtime.Serialization.SerializationInfo object with the file name and line 

    number at which this System.ComponentModel.Win32Exception occurred.

  

  

   info: A System.Runtime.Serialization.SerializationInfo.

   context: The contextual information about the source or destination.
  """
  pass
 def remove_SerializeObjectState(self,*args):
  """ remove_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,error: int)

  __new__(cls: type,error: int,message: str)

  __new__(cls: type,message: str)

  __new__(cls: type,message: str,innerException: Exception)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 NativeErrorCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Win32 error code associated with this exception.



Get: NativeErrorCode(self: Win32Exception) -> int



"""



# variables with complex values

