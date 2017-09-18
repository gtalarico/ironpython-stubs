class TypeLoadException(SystemException,ISerializable,_Exception):
 """
 The exception that is thrown when type-loading failures occur.

 

 TypeLoadException()

 TypeLoadException(message: str)

 TypeLoadException(message: str,inner: Exception)
 """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: TypeLoadException,info: SerializationInfo,context: StreamingContext)

   Sets the System.Runtime.Serialization.SerializationInfo object with the class name,method name,

    resource ID,and additional exception information.

  

  

   info: The object that holds the serialized object data.

   context: The contextual information about the source or destination.
  """
  pass
 def remove_SerializeObjectState(self,*args):
  """ remove_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
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
 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the error message for this exception.



Get: Message(self: TypeLoadException) -> str



"""

 TypeName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the fully qualified name of the type that causes the exception.



Get: TypeName(self: TypeLoadException) -> str



"""


