class HttpWebResponse(WebResponse,ISerializable,IDisposable):
 """
 Provides an HTTP-specific implementation of the System.Net.WebResponse class.

 

 HttpWebResponse()
 """
 def Close(self):
  """
  Close(self: HttpWebResponse)

   Closes the response stream.
  """
  pass
 def Dispose(self):
  """ Dispose(self: HttpWebResponse,disposing: bool) """
  pass
 def GetObjectData(self,*args):
  """
  GetObjectData(self: HttpWebResponse,serializationInfo: SerializationInfo,streamingContext: StreamingContext)

   Populates a System.Runtime.Serialization.SerializationInfo with the data needed to serialize the 

    target object.

  

  

   serializationInfo: The System.Runtime.Serialization.SerializationInfo to populate with data.

   streamingContext: A System.Runtime.Serialization.StreamingContext that specifies the destination for this 

    serialization.
  """
  pass
 def GetResponseHeader(self,headerName):
  """
  GetResponseHeader(self: HttpWebResponse,headerName: str) -> str

  

   Gets the contents of a header that was returned with the response.

  

   headerName: The header value to return.

   Returns: The contents of the specified header.
  """
  pass
 def GetResponseStream(self):
  """
  GetResponseStream(self: HttpWebResponse) -> Stream

  

   Gets the stream that is used to read the body of the response from the server.

   Returns: A System.IO.Stream containing the body of the response.
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
 def __new__(self):
  """
  __new__(cls: type)

  __new__(cls: type,serializationInfo: SerializationInfo,streamingContext: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 CharacterSet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the character set of the response.



Get: CharacterSet(self: HttpWebResponse) -> str



"""

 ContentEncoding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the method that is used to encode the body of the response.



Get: ContentEncoding(self: HttpWebResponse) -> str



"""

 ContentLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length of the content returned by the request.



Get: ContentLength(self: HttpWebResponse) -> Int64



"""

 ContentType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the content type of the response.



Get: ContentType(self: HttpWebResponse) -> str



"""

 Cookies=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the cookies that are associated with this response.



Get: Cookies(self: HttpWebResponse) -> CookieCollection



Set: Cookies(self: HttpWebResponse)=value

"""

 Headers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the headers that are associated with this response from the server.



Get: Headers(self: HttpWebResponse) -> WebHeaderCollection



"""

 IsMutuallyAuthenticated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Boolean value that indicates whether both client and server were authenticated.



Get: IsMutuallyAuthenticated(self: HttpWebResponse) -> bool



"""

 LastModified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the last date and time that the contents of the response were modified.



Get: LastModified(self: HttpWebResponse) -> DateTime



"""

 Method=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the method that is used to return the response.



Get: Method(self: HttpWebResponse) -> str



"""

 ProtocolVersion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the version of the HTTP protocol that is used in the response.



Get: ProtocolVersion(self: HttpWebResponse) -> Version



"""

 ResponseUri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the URI of the Internet resource that responded to the request.



Get: ResponseUri(self: HttpWebResponse) -> Uri



"""

 Server=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the server that sent the response.



Get: Server(self: HttpWebResponse) -> str



"""

 StatusCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the status of the response.



Get: StatusCode(self: HttpWebResponse) -> HttpStatusCode



"""

 StatusDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the status description returned with the response.



Get: StatusDescription(self: HttpWebResponse) -> str



"""

 SupportsHeaders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SupportsHeaders(self: HttpWebResponse) -> bool



"""


