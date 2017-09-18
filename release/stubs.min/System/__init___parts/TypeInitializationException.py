class TypeInitializationException(SystemException,ISerializable,_Exception):
 """
 The exception that is thrown as a wrapper around the exception thrown by the class initializer. This class cannot be inherited.

 

 TypeInitializationException(fullTypeName: str,innerException: Exception)
 """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: TypeInitializationException,info: SerializationInfo,context: StreamingContext)

   Sets the System.Runtime.Serialization.SerializationInfo object with the type name and additional 

    exception information.

  

  

   info: The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about 

    the exception being thrown.

  

   context: The System.Runtime.Serialization.StreamingContext that contains contextual information about the 

    source or destination.
  """
  pass
 def remove_SerializeObjectState(self,*args):
  """ remove_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,fullTypeName,innerException):
  """ __new__(cls: type,fullTypeName: str,innerException: Exception) """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 TypeName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the fully qualified name of the type that fails to initialize.



Get: TypeName(self: TypeInitializationException) -> str



"""


