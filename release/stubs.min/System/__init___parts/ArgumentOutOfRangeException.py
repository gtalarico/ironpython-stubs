class ArgumentOutOfRangeException(ArgumentException,ISerializable,_Exception):
 """
 The exception that is thrown when the value of an argument is outside the allowable range of values as defined by the invoked method.

 

 ArgumentOutOfRangeException()

 ArgumentOutOfRangeException(paramName: str)

 ArgumentOutOfRangeException(paramName: str,message: str)

 ArgumentOutOfRangeException(message: str,innerException: Exception)

 ArgumentOutOfRangeException(paramName: str,actualValue: object,message: str)
 """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: ArgumentOutOfRangeException,info: SerializationInfo,context: StreamingContext)

   Sets the System.Runtime.Serialization.SerializationInfo object with the invalid argument value 

    and additional exception information.

  

  

   info: The object that holds the serialized object data.

   context: An object that describes the source or destination of the serialized data.
  """
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

  __new__(cls: type,paramName: str)

  __new__(cls: type,paramName: str,message: str)

  __new__(cls: type,message: str,innerException: Exception)

  __new__(cls: type,paramName: str,actualValue: object,message: str)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 ActualValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the argument value that causes this exception.



Get: ActualValue(self: ArgumentOutOfRangeException) -> object



"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the error message and the string representation of the invalid argument value,or only the error message if the argument value is null.



Get: Message(self: ArgumentOutOfRangeException) -> str



"""


