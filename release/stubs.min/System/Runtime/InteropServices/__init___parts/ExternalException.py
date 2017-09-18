class ExternalException(SystemException,ISerializable,_Exception):
 """
 The base exception type for all COM interop exceptions and structured exception handling (SEH) exceptions.

 

 ExternalException()

 ExternalException(message: str)

 ExternalException(message: str,inner: Exception)

 ExternalException(message: str,errorCode: int)
 """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def remove_SerializeObjectState(self,*args):
  """ remove_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def ToString(self):
  """
  ToString(self: ExternalException) -> str

  

   Returns a string that contains the HRESULT of the error.

   Returns: A string that represents the HRESULT.
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
 ErrorCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the HRESULT of the error.



Get: ErrorCode(self: ExternalException) -> int



"""


