class SEHException(ExternalException):
 """
 Represents structured exception handling (SEH) errors.
 
 SEHException()
 SEHException(message: str)
 SEHException(message: str,inner: Exception)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return SEHException()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def CanResume(self):
  """
  CanResume(self: SEHException) -> bool
  
   Indicates whether the exception can be recovered from,and whether the code can continue from the point at which the exception was thrown.
   Returns: Always false,because resumable exceptions are not implemented.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message=None,inner=None):
  """
  __new__(cls: type)
  __new__(cls: type,message: str)
  __new__(cls: type,message: str,inner: Exception)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 SerializeObjectState=None

