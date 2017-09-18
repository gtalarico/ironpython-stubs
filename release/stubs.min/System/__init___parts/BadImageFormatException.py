class BadImageFormatException(SystemException,ISerializable,_Exception):
 """
 The exception that is thrown when the file image of a dynamic link library (DLL) or an executable program is invalid.

 

 BadImageFormatException()

 BadImageFormatException(message: str)

 BadImageFormatException(message: str,inner: Exception)

 BadImageFormatException(message: str,fileName: str)

 BadImageFormatException(message: str,fileName: str,inner: Exception)
 """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: BadImageFormatException,info: SerializationInfo,context: StreamingContext)

   Sets the System.Runtime.Serialization.SerializationInfo object with the file name,assembly 

    cache log,and additional exception information.

  

  

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
  ToString(self: BadImageFormatException) -> str

  

   Returns the fully qualified name of this exception and possibly the error message,the name of 

    the inner exception,and the stack trace.

  

   Returns: A string containing the fully qualified name of this exception and possibly the error message,

    the name of the inner exception,and the stack trace.
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



Get: FileName(self: BadImageFormatException) -> str



"""

 FusionLog=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the log file that describes why an assembly load failed.



Get: FusionLog(self: BadImageFormatException) -> str



"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the error message and the name of the file that caused this exception.



Get: Message(self: BadImageFormatException) -> str



"""


