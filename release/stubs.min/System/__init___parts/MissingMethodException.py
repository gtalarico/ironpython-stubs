class MissingMethodException(MissingMemberException,ISerializable,_Exception):
 """
 The exception that is thrown when there is an attempt to dynamically access a method that does not exist.

 

 MissingMethodException()

 MissingMethodException(message: str)

 MissingMethodException(message: str,inner: Exception)

 MissingMethodException(className: str,methodName: str)
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

  __new__(cls: type,message: str,inner: Exception)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)

  __new__(cls: type,className: str,methodName: str)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the text string showing the class name,the method name,and the signature of the missing method. This property is read-only.



Get: Message(self: MissingMethodException) -> str



"""


 ClassName=None
 MemberName=None
 Signature=None

