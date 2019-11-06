class MissingMemberException(MemberAccessException):
 """
 The exception that is thrown when there is an attempt to dynamically access a class member that does not exist.
 
 MissingMemberException()
 MissingMemberException(message: str)
 MissingMemberException(message: str,inner: Exception)
 MissingMemberException(className: str,memberName: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MissingMemberException()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: MissingMemberException,info: SerializationInfo,context: StreamingContext)
   Sets the System.Runtime.Serialization.SerializationInfo object with the class name,the member name,the signature of the missing member,and additional exception 
    information.
  
  
   info: The object that holds the serialized object data.
   context: The contextual information about the source or destination.
  """
  pass
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
  __new__(cls: type,className: str,memberName: str)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the text string showing the class name,the member name,and the signature of the missing member.

Get: Message(self: MissingMemberException) -> str

"""


 ClassName=None
 MemberName=None
 SerializeObjectState=None
 Signature=None

