class MissingFieldException(MissingMemberException):
 """
 The exception that is thrown when there is an attempt to dynamically access a field that does not exist.
 
 MissingFieldException()
 MissingFieldException(message: str)
 MissingFieldException(message: str,inner: Exception)
 MissingFieldException(className: str,fieldName: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MissingFieldException()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,message: str)
  __new__(cls: type,message: str,inner: Exception)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  __new__(cls: type,className: str,fieldName: str)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the text string showing the signature of the missing field,the class name,and the field name. This property is read-only.

Get: Message(self: MissingFieldException) -> str

"""


 ClassName=None
 MemberName=None
 SerializeObjectState=None
 Signature=None

