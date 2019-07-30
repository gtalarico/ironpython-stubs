class InvalidCastException(SystemException):
 """
 The exception that is thrown for invalid casting or explicit conversion.
 
 InvalidCastException()
 InvalidCastException(message: str)
 InvalidCastException(message: str,innerException: Exception)
 InvalidCastException(message: str,errorCode: int)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return InvalidCastException()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message=None,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,message: str)
  __new__(cls: type,message: str,innerException: Exception)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  __new__(cls: type,message: str,errorCode: int)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 SerializeObjectState=None

