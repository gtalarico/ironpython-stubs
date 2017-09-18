class FileFormatException(FormatException,ISerializable,_Exception):
 """
 The exception that is thrown when an input file or a data stream that is supposed to conform to a certain file format specification is malformed.
 
 FileFormatException()
 FileFormatException(message: str)
 FileFormatException(message: str,innerException: Exception)
 FileFormatException(sourceUri: Uri)
 FileFormatException(sourceUri: Uri,message: str)
 FileFormatException(sourceUri: Uri,innerException: Exception)
 FileFormatException(sourceUri: Uri,message: str,innerException: Exception)
 """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: FileFormatException,info: SerializationInfo,context: StreamingContext)
   Sets the System.Runtime.Serialization.SerializationInfo object with the file 
    name and additional exception information.
  
  
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
 def __new__(self,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,message: str)
  __new__(cls: type,message: str,innerException: Exception)
  __new__(cls: type,sourceUri: Uri)
  __new__(cls: type,sourceUri: Uri,message: str)
  __new__(cls: type,sourceUri: Uri,innerException: Exception)
  __new__(cls: type,sourceUri: Uri,message: str,innerException: Exception)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 SourceUri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of a file that caused the System.IO.FileFormatException.

Get: SourceUri(self: FileFormatException) -> Uri

"""


