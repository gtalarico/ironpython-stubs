class MethodAccessException(MemberAccessException):
 """
 The exception that is thrown when there is an invalid attempt to access a method,such as accessing a private method from partially trusted code.
 
 MethodAccessException()
 MethodAccessException(message: str)
 MethodAccessException(message: str,inner: Exception)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MethodAccessException()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
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

