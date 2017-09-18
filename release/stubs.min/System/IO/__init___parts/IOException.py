class IOException(SystemException,ISerializable,_Exception):
 """
 The exception that is thrown when an I/O error occurs.

 

 IOException()

 IOException(message: str)

 IOException(message: str,hresult: int)

 IOException(message: str,innerException: Exception)
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
 def __new__(self,message=None,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,message: str)

  __new__(cls: type,message: str,hresult: int)

  __new__(cls: type,message: str,innerException: Exception)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
