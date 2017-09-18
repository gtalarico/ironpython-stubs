class FtpWebResponse(WebResponse,ISerializable,IDisposable):
 """ Encapsulates a File Transfer Protocol (FTP) server's response to a request. """
 def Close(self):
  """
  Close(self: FtpWebResponse)

   Frees the resources held by the response.
  """
  pass
 def Dispose(self):
  """ Dispose(self: WebResponse,disposing: bool) """
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
  GetResponseStream(self: FtpWebResponse) -> Stream

  

   Retrieves the stream that contains response data sent from an FTP server.

   Returns: A readable System.IO.Stream instance that contains data returned with the response; otherwise,

    System.IO.Stream.Null if no response data was returned by the server.
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
 BannerMessage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the message sent by the FTP server when a connection is established prior to logon.



Get: BannerMessage(self: FtpWebResponse) -> str



"""

 ContentLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length of the data received from the FTP server.



Get: ContentLength(self: FtpWebResponse) -> Int64



"""

 ExitMessage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the message sent by the server when the FTP session is ending.



Get: ExitMessage(self: FtpWebResponse) -> str



"""

 Headers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an empty System.Net.WebHeaderCollection object.



Get: Headers(self: FtpWebResponse) -> WebHeaderCollection



"""

 LastModified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the date and time that a file on an FTP server was last modified.



Get: LastModified(self: FtpWebResponse) -> DateTime



"""

 ResponseUri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the URI that sent the response to the request.



Get: ResponseUri(self: FtpWebResponse) -> Uri



"""

 StatusCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the most recent status code sent from the FTP server.



Get: StatusCode(self: FtpWebResponse) -> FtpStatusCode



"""

 StatusDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets text that describes a status code sent from the FTP server.



Get: StatusDescription(self: FtpWebResponse) -> str



"""

 SupportsHeaders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SupportsHeaders(self: FtpWebResponse) -> bool



"""

 WelcomeMessage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the message sent by the FTP server when authentication is complete.



Get: WelcomeMessage(self: FtpWebResponse) -> str



"""


