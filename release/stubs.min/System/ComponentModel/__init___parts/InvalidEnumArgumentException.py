class InvalidEnumArgumentException(ArgumentException,ISerializable,_Exception):
 """
 The exception thrown when using invalid arguments that are enumerators.

 

 InvalidEnumArgumentException()

 InvalidEnumArgumentException(message: str)

 InvalidEnumArgumentException(message: str,innerException: Exception)

 InvalidEnumArgumentException(argumentName: str,invalidValue: int,enumClass: Type)
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

  __new__(cls: type,argumentName: str,invalidValue: int,enumClass: Type)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
