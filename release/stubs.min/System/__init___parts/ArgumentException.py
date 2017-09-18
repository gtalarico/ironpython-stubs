class ArgumentException(SystemException,ISerializable,_Exception):
 """
 The exception that is thrown when one of the arguments provided to a method is not valid.

 

 ArgumentException()

 ArgumentException(message: str)

 ArgumentException(message: str,innerException: Exception)

 ArgumentException(message: str,paramName: str,innerException: Exception)

 ArgumentException(message: str,paramName: str)
 """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: ArgumentException,info: SerializationInfo,context: StreamingContext)

   Sets the System.Runtime.Serialization.SerializationInfo object with the parameter name and 

    additional exception information.

  

  

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
 def __new__(self,message=None,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,message: str)

  __new__(cls: type,message: str,innerException: Exception)

  __new__(cls: type,message: str,paramName: str,innerException: Exception)

  __new__(cls: type,message: str,paramName: str)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the error message and the parameter name,or only the error message if no parameter name is set.



Get: Message(self: ArgumentException) -> str



"""

 ParamName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the parameter that causes this exception.



Get: ParamName(self: ArgumentException) -> str



"""


