class TypeUnloadedException:
 """
 The exception that is thrown when there is an attempt to access an unloaded class.
 
 TypeUnloadedException()
 TypeUnloadedException(message: str)
 TypeUnloadedException(message: str,innerException: Exception)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message=None,innerException=None):
  """
  __new__(cls: type)
  __new__(cls: type,message: str)
  __new__(cls: type,message: str,innerException: Exception)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 SerializeObjectState=None

