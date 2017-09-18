class FileNotFoundException(IOException,ISerializable,_Exception):
 """
 The exception that is thrown when an attempt to access a file that does not exist on disk fails.

 

 FileNotFoundException()

 FileNotFoundException(message: str)

 FileNotFoundException(message: str,innerException: Exception)

 FileNotFoundException(message: str,fileName: str)

 FileNotFoundException(message: str,fileName: str,innerException: Exception)
 """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: FileNotFoundException,info: SerializationInfo,context: StreamingContext)

   Sets the System.Runtime.Serialization.SerializationInfo object with the file name and additional 

    exception information.

  

  

   info: The object that holds the serialized object data about the exception being thrown.

   context: The object that contains contextual information about the source or destination.
  """
  pass
 def remove_SerializeObjectState(self,*args):
  """ remove_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def ToString(self):
  """
  ToString(self: FileNotFoundException) -> str

  

   Returns the fully qualified name of this exception and possibly the error message,the name of 

    the inner exception,and the stack trace.

  

   Returns: The fully qualified name of this exception and possibly the error message,the name of the inner 

    exception,and the stack trace.
  """
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

  __new__(cls: type,message: str,fileName: str)

  __new__(cls: type,message: str,fileName: str,innerException: Exception)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 FileName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the file that cannot be found.



Get: FileName(self: FileNotFoundException) -> str



"""

 FusionLog=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the log file that describes why loading of an assembly failed.



Get: FusionLog(self: FileNotFoundException) -> str



"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the error message that explains the reason for the exception.



Get: Message(self: FileNotFoundException) -> str



"""


