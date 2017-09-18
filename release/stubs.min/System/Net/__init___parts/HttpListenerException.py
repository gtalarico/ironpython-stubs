class HttpListenerException(Win32Exception,ISerializable,_Exception):
 """
 The exception that is thrown when an error occurs processing an HTTP request.

 

 HttpListenerException()

 HttpListenerException(errorCode: int)

 HttpListenerException(errorCode: int,message: str)
 """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def remove_SerializeObjectState(self,*args):
  """ remove_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,errorCode=None,message=None):
  """
  __new__(cls: type)

  __new__(cls: type,errorCode: int)

  __new__(cls: type,errorCode: int,message: str)

  __new__(cls: type,serializationInfo: SerializationInfo,streamingContext: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 ErrorCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that identifies the error that occurred.



Get: ErrorCode(self: HttpListenerException) -> int



"""


