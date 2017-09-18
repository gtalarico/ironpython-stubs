class ObjectDisposedException(InvalidOperationException,ISerializable,_Exception):
 """
 The exception that is thrown when an operation is performed on a disposed object.

 

 ObjectDisposedException(objectName: str)

 ObjectDisposedException(objectName: str,message: str)

 ObjectDisposedException(message: str,innerException: Exception)
 """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: ObjectDisposedException,info: SerializationInfo,context: StreamingContext)

   Retrieves the System.Runtime.Serialization.SerializationInfo object with the parameter name and 

    additional exception information.

  

  

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
 def __new__(self,*__args):
  """
  __new__(cls: type,objectName: str)

  __new__(cls: type,objectName: str,message: str)

  __new__(cls: type,message: str,innerException: Exception)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the message that describes the error.



Get: Message(self: ObjectDisposedException) -> str



"""

 ObjectName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the disposed object.



Get: ObjectName(self: ObjectDisposedException) -> str



"""


