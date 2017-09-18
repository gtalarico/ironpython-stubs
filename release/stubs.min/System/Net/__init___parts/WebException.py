class WebException(InvalidOperationException,ISerializable,_Exception):
 """
 The exception that is thrown when an error occurs while accessing the network through a pluggable protocol.

 

 WebException()

 WebException(message: str)

 WebException(message: str,innerException: Exception)

 WebException(message: str,status: WebExceptionStatus)

 WebException(message: str,innerException: Exception,status: WebExceptionStatus,response: WebResponse)
 """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def GetObjectData(self,serializationInfo,streamingContext):
  """
  GetObjectData(self: WebException,serializationInfo: SerializationInfo,streamingContext: StreamingContext)

   Populates a System.Runtime.Serialization.SerializationInfo instance with the data needed to 

    serialize the System.Net.WebException.

  

  

   serializationInfo: The System.Runtime.Serialization.SerializationInfo to be used.

   streamingContext: The System.Runtime.Serialization.StreamingContext to be used.
  """
  pass
 def remove_SerializeObjectState(self,*args):
  """ remove_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message=None,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,message: str)

  __new__(cls: type,message: str,innerException: Exception)

  __new__(cls: type,message: str,status: WebExceptionStatus)

  __new__(cls: type,message: str,innerException: Exception,status: WebExceptionStatus,response: WebResponse)

  __new__(cls: type,serializationInfo: SerializationInfo,streamingContext: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Response=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the response that the remote host returned.



Get: Response(self: WebException) -> WebResponse



"""

 Status=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the status of the response.



Get: Status(self: WebException) -> WebExceptionStatus



"""


