class FileLoadException(IOException,ISerializable,_Exception):
 """
 The exception that is thrown when a managed assembly is found but cannot be loaded.

 

 FileLoadException()

 FileLoadException(message: str)

 FileLoadException(message: str,inner: Exception)

 FileLoadException(message: str,fileName: str)

 FileLoadException(message: str,fileName: str,inner: Exception)
 """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: FileLoadException,info: SerializationInfo,context: StreamingContext)

   Sets the System.Runtime.Serialization.SerializationInfo with the file name and additional 

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
 def ToString(self):
  """
  ToString(self: FileLoadException) -> str

  

   Returns the fully qualified name of the current exception,and possibly the error message,the 

    name of the inner exception,and the stack trace.

  

   Returns: A string containing the fully qualified name of this exception,and possibly the error message,

    the name of the inner exception,and the stack trace,depending on which 

    System.IO.FileLoadException constructor is used.
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

  __new__(cls: type,message: str,inner: Exception)

  __new__(cls: type,message: str,fileName: str)

  __new__(cls: type,message: str,fileName: str,inner: Exception)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 FileName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the file that causes this exception.



Get: FileName(self: FileLoadException) -> str



"""

 FusionLog=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the log file that describes why an assembly load failed.



Get: FusionLog(self: FileLoadException) -> str



"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the error message and the name of the file that caused this exception.



Get: Message(self: FileLoadException) -> str



"""


