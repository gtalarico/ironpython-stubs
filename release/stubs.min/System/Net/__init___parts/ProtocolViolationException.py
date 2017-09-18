class ProtocolViolationException(InvalidOperationException,ISerializable,_Exception):
 """
 The exception that is thrown when an error is made while using a network protocol.

 

 ProtocolViolationException()

 ProtocolViolationException(message: str)
 """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def GetObjectData(self,serializationInfo,streamingContext):
  """
  GetObjectData(self: ProtocolViolationException,serializationInfo: SerializationInfo,streamingContext: StreamingContext)

   Populates a System.Runtime.Serialization.SerializationInfo with the data required to serialize 

    the target object.

  

  

   serializationInfo: The System.Runtime.Serialization.SerializationInfo to populate with data.

   streamingContext: A System.Runtime.Serialization.StreamingContext that specifies the destination for this 

    serialization.
  """
  pass
 def remove_SerializeObjectState(self,*args):
  """ remove_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message=None):
  """
  __new__(cls: type)

  __new__(cls: type,message: str)

  __new__(cls: type,serializationInfo: SerializationInfo,streamingContext: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
