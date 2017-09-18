class ErrorWrapper(object):
 """
 Wraps objects the marshaler should marshal as a VT_ERROR.

 

 ErrorWrapper(errorCode: int)

 ErrorWrapper(errorCode: object)

 ErrorWrapper(e: Exception)
 """
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,errorCode: int)

  __new__(cls: type,errorCode: object)

  __new__(cls: type,e: Exception)
  """
  pass
 ErrorCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the error code of the wrapper.



Get: ErrorCode(self: ErrorWrapper) -> int



"""


