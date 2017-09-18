class COMException(ExternalException,ISerializable,_Exception):
 """
 The exception that is thrown when an unrecognized HRESULT is returned from a COM method call.

 

 COMException()

 COMException(message: str)

 COMException(message: str,inner: Exception)

 COMException(message: str,errorCode: int)
 """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def remove_SerializeObjectState(self,*args):
  """ remove_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def ToString(self):
  """
  ToString(self: COMException) -> str

  

   Converts the contents of the exception to a string.

   Returns: A string containing the System.Exception.HResult,System.Exception.Message,

    System.Exception.InnerException,and System.Exception.StackTrace properties of the exception.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message=None,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,message: str)

  __new__(cls: type,message: str,inner: Exception)

  __new__(cls: type,message: str,errorCode: int)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
