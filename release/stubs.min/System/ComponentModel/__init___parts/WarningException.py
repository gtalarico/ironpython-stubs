class WarningException(SystemException,ISerializable,_Exception):
 """
 Specifies an exception that is handled as a warning instead of an error.

 

 WarningException()

 WarningException(message: str)

 WarningException(message: str,helpUrl: str)

 WarningException(message: str,innerException: Exception)

 WarningException(message: str,helpUrl: str,helpTopic: str)
 """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: WarningException,info: SerializationInfo,context: StreamingContext)

   Sets the System.Runtime.Serialization.SerializationInfo with the parameter name and additional 

    exception information.

  

  

   info: Stores the data that was being used to serialize or deserialize the object that the 

    System.ComponentModel.Design.Serialization.CodeDomSerializer was serializing or deserializing.

  

   context: Describes the source and destination of the stream that generated the exception,as well as a 

    means for serialization to retain that context and an additional caller-defined context.
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

  __new__(cls: type,message: str,helpUrl: str)

  __new__(cls: type,message: str,innerException: Exception)

  __new__(cls: type,message: str,helpUrl: str,helpTopic: str)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 HelpTopic=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Help topic associated with the warning.



Get: HelpTopic(self: WarningException) -> str



"""

 HelpUrl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Help file associated with the warning.



Get: HelpUrl(self: WarningException) -> str



"""


