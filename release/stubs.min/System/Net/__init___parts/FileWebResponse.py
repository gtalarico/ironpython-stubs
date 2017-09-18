class FileWebResponse(WebResponse,ISerializable,IDisposable,ICloseEx):
 """ Provides a file system implementation of the System.Net.WebResponse class. """
 def Close(self):
  """
  Close(self: FileWebResponse)

   Closes the response stream.
  """
  pass
 def Dispose(self):
  """ Dispose(self: WebResponse,disposing: bool) """
  pass
 def GetObjectData(self,*args):
  """
  GetObjectData(self: FileWebResponse,serializationInfo: SerializationInfo,streamingContext: StreamingContext)

   Populates a System.Runtime.Serialization.SerializationInfo with the data needed to serialize the 

    target object.

  

  

   serializationInfo: The System.Runtime.Serialization.SerializationInfo to populate with data.

   streamingContext: A System.Runtime.Serialization.StreamingContext that specifies the destination for this 

    serialization.
  """
  pass
 def GetResponseStream(self):
  """
  GetResponseStream(self: FileWebResponse) -> Stream

  

   Returns the data stream from the file system resource.

   Returns: A System.IO.Stream for reading data from the file system resource.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject

  

   Creates a shallow copy of the current System.MarshalByRefObject object.

  

   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the 

    object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 

    false is usually appropriate. true to copy the current System.MarshalByRefObject object's 

    identity to its clone,which will cause remoting client calls to be routed to the remote server 

    object.

  

   Returns: A shallow copy of the current System.MarshalByRefObject object.

  MemberwiseClone(self: object) -> object

  

   Creates a shallow copy of the current System.Object.

   Returns: A shallow copy of the current System.Object.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,serializationInfo: SerializationInfo,streamingContext: StreamingContext) """
  pass
 def __reduce_ex__(self,*args):
  pass
 ContentLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length of the content in the file system resource.



Get: ContentLength(self: FileWebResponse) -> Int64



"""

 ContentType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the content type of the file system resource.



Get: ContentType(self: FileWebResponse) -> str



"""

 Headers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of header name/value pairs associated with the response.



Get: Headers(self: FileWebResponse) -> WebHeaderCollection



"""

 ResponseUri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the URI of the file system resource that provided the response.



Get: ResponseUri(self: FileWebResponse) -> Uri



"""

 SupportsHeaders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SupportsHeaders(self: FileWebResponse) -> bool



"""


