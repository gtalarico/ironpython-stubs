class OperationCanceledException(SystemException,ISerializable,_Exception):
 """
 The exception that is thrown in a thread upon cancellation of an operation that the thread was executing.

 

 OperationCanceledException()

 OperationCanceledException(message: str)

 OperationCanceledException(message: str,innerException: Exception)

 OperationCanceledException(token: CancellationToken)

 OperationCanceledException(message: str,token: CancellationToken)

 OperationCanceledException(message: str,innerException: Exception,token: CancellationToken)
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
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,message: str)

  __new__(cls: type,message: str,innerException: Exception)

  __new__(cls: type,token: CancellationToken)

  __new__(cls: type,message: str,token: CancellationToken)

  __new__(cls: type,message: str,innerException: Exception,token: CancellationToken)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 CancellationToken=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a token associated with the operation that was canceled.



Get: CancellationToken(self: OperationCanceledException) -> CancellationToken



"""


