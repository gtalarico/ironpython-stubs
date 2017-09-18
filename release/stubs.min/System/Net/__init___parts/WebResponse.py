class WebResponse(MarshalByRefObject,ISerializable,IDisposable):
 """ Provides a response from a Uniform Resource Identifier (URI). This is an abstract class. """
 def Close(self):
  """
  Close(self: WebResponse)

   When overridden by a descendant class,closes the response stream.
  """
  pass
 def Dispose(self):
  """ Dispose(self: WebResponse) """
  pass
 def GetObjectData(self,*args):
  """
  GetObjectData(self: WebResponse,serializationInfo: SerializationInfo,streamingContext: StreamingContext)

   Populates a System.Runtime.Serialization.SerializationInfo with the data that is needed to 

    serialize the target object.

  

  

   serializationInfo: The System.Runtime.Serialization.SerializationInfo to populate with data.

   streamingContext: A System.Runtime.Serialization.StreamingContext that specifies the destination for this 

    serialization.
  """
  pass
 def GetResponseStream(self):
  """
  GetResponseStream(self: WebResponse) -> Stream

  

   When overridden in a descendant class,returns the data stream from the Internet resource.

   Returns: An instance of the System.IO.Stream class for reading data from the Internet resource.
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
  """
  __new__(cls: type)

  __new__(cls: type,serializationInfo: SerializationInfo,streamingContext: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 ContentLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a descendant class,gets or sets the content length of data being received.



Get: ContentLength(self: WebResponse) -> Int64



Set: ContentLength(self: WebResponse)=value

"""

 ContentType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets or sets the content type of the data being received.



Get: ContentType(self: WebResponse) -> str



Set: ContentType(self: WebResponse)=value

"""

 Headers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets a collection of header name-value pairs associated with this request.



Get: Headers(self: WebResponse) -> WebHeaderCollection



"""

 IsFromCache=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Boolean value that indicates whether this response was obtained from the cache.



Get: IsFromCache(self: WebResponse) -> bool



"""

 IsMutuallyAuthenticated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Boolean value that indicates whether mutual authentication occurred.



Get: IsMutuallyAuthenticated(self: WebResponse) -> bool



"""

 ResponseUri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets the URI of the Internet resource that actually responded to the request.



Get: ResponseUri(self: WebResponse) -> Uri



"""

 SupportsHeaders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SupportsHeaders(self: WebResponse) -> bool



"""


