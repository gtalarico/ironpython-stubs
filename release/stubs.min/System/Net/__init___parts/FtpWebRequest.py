class FtpWebRequest(WebRequest,ISerializable):
 """ Implements a File Transfer Protocol (FTP) client. """
 def Abort(self):
  """
  Abort(self: FtpWebRequest)

   Terminates an asynchronous FTP operation.
  """
  pass
 def BeginGetRequestStream(self,callback,state):
  """
  BeginGetRequestStream(self: FtpWebRequest,callback: AsyncCallback,state: object) -> IAsyncResult

  

   Begins asynchronously opening a request's content stream for writing.

  

   callback: An System.AsyncCallback delegate that references the method to invoke when the operation is 

    complete.

  

   state: A user-defined object that contains information about the operation. This object is passed to 

    the callback delegate when the operation completes.

  

   Returns: An System.IAsyncResult instance that indicates the status of the operation.
  """
  pass
 def BeginGetResponse(self,callback,state):
  """
  BeginGetResponse(self: FtpWebRequest,callback: AsyncCallback,state: object) -> IAsyncResult

  

   Begins sending a request and receiving a response from an FTP server asynchronously.

  

   callback: An System.AsyncCallback delegate that references the method to invoke when the operation is 

    complete.

  

   state: A user-defined object that contains information about the operation. This object is passed to 

    the callback delegate when the operation completes.

  

   Returns: An System.IAsyncResult instance that indicates the status of the operation.
  """
  pass
 def EndGetRequestStream(self,asyncResult):
  """
  EndGetRequestStream(self: FtpWebRequest,asyncResult: IAsyncResult) -> Stream

  

   Ends a pending asynchronous operation started with 

    System.Net.FtpWebRequest.BeginGetRequestStream(System.AsyncCallback,System.Object).

  

  

   asyncResult: The System.IAsyncResult object that was returned when the operation started.

   Returns: A writable System.IO.Stream instance associated with this instance.
  """
  pass
 def EndGetResponse(self,asyncResult):
  """
  EndGetResponse(self: FtpWebRequest,asyncResult: IAsyncResult) -> WebResponse

  

   Ends a pending asynchronous operation started with 

    System.Net.FtpWebRequest.BeginGetResponse(System.AsyncCallback,System.Object).

  

  

   asyncResult: The System.IAsyncResult that was returned when the operation started.

   Returns: A System.Net.WebResponse reference that contains an System.Net.FtpWebResponse instance. This 

    object contains the FTP server's response to the request.
  """
  pass
 def GetObjectData(self,*args):
  """
  GetObjectData(self: WebRequest,serializationInfo: SerializationInfo,streamingContext: StreamingContext)

   Populates a System.Runtime.Serialization.SerializationInfo with the data needed to serialize the 

    target object.

  

  

   serializationInfo: The System.Runtime.Serialization.SerializationInfo to populate with data.

   streamingContext: A System.Runtime.Serialization.StreamingContext that specifies the destination for this 

    serialization.
  """
  pass
 def GetRequestStream(self):
  """
  GetRequestStream(self: FtpWebRequest) -> Stream

  

   Retrieves the stream used to upload data to an FTP server.

   Returns: A writable System.IO.Stream instance used to store data to be sent to the server by the current 

    request.
  """
  pass
 def GetResponse(self):
  """
  GetResponse(self: FtpWebRequest) -> WebResponse

  

   Returns the FTP server response.

   Returns: A System.Net.WebResponse reference that contains an System.Net.FtpWebResponse instance. This 

    object contains the FTP server's response to the request.
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
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 ClientCertificates=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the certificates used for establishing an encrypted connection to the FTP server.



Get: ClientCertificates(self: FtpWebRequest) -> X509CertificateCollection



Set: ClientCertificates(self: FtpWebRequest)=value

"""

 ConnectionGroupName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the connection group that contains the service point used to send the current request.



Get: ConnectionGroupName(self: FtpWebRequest) -> str



Set: ConnectionGroupName(self: FtpWebRequest)=value

"""

 ContentLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that is ignored by the System.Net.FtpWebRequest class.



Get: ContentLength(self: FtpWebRequest) -> Int64



Set: ContentLength(self: FtpWebRequest)=value

"""

 ContentOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a byte offset into the file being downloaded by this request.



Get: ContentOffset(self: FtpWebRequest) -> Int64



Set: ContentOffset(self: FtpWebRequest)=value

"""

 ContentType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Always throws a System.NotSupportedException.



Get: ContentType(self: FtpWebRequest) -> str



Set: ContentType(self: FtpWebRequest)=value

"""

 Credentials=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the credentials used to communicate with the FTP server.



Get: Credentials(self: FtpWebRequest) -> ICredentials



Set: Credentials(self: FtpWebRequest)=value

"""

 EnableSsl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Boolean that specifies that an SSL connection should be used.



Get: EnableSsl(self: FtpWebRequest) -> bool



Set: EnableSsl(self: FtpWebRequest)=value

"""

 Headers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an empty System.Net.WebHeaderCollection object.



Get: Headers(self: FtpWebRequest) -> WebHeaderCollection



Set: Headers(self: FtpWebRequest)=value

"""

 KeepAlive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Boolean value that specifies whether the control connection to the FTP server is closed after the request completes.



Get: KeepAlive(self: FtpWebRequest) -> bool



Set: KeepAlive(self: FtpWebRequest)=value

"""

 Method=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the command to send to the FTP server.



Get: Method(self: FtpWebRequest) -> str



Set: Method(self: FtpWebRequest)=value

"""

 PreAuthenticate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Always throws a System.NotSupportedException.



Get: PreAuthenticate(self: FtpWebRequest) -> bool



Set: PreAuthenticate(self: FtpWebRequest)=value

"""

 Proxy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the proxy used to communicate with the FTP server.



Get: Proxy(self: FtpWebRequest) -> IWebProxy



Set: Proxy(self: FtpWebRequest)=value

"""

 ReadWriteTimeout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a time-out when reading from or writing to a stream.



Get: ReadWriteTimeout(self: FtpWebRequest) -> int



Set: ReadWriteTimeout(self: FtpWebRequest)=value

"""

 RenameTo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the new name of a file being renamed.



Get: RenameTo(self: FtpWebRequest) -> str



Set: RenameTo(self: FtpWebRequest)=value

"""

 RequestUri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the URI requested by this instance.



Get: RequestUri(self: FtpWebRequest) -> Uri



"""

 ServicePoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Net.ServicePoint object used to connect to the FTP server.



Get: ServicePoint(self: FtpWebRequest) -> ServicePoint



"""

 Timeout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of milliseconds to wait for a request.



Get: Timeout(self: FtpWebRequest) -> int



Set: Timeout(self: FtpWebRequest)=value

"""

 UseBinary=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Boolean value that specifies the data type for file transfers.



Get: UseBinary(self: FtpWebRequest) -> bool



Set: UseBinary(self: FtpWebRequest)=value

"""

 UseDefaultCredentials=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Always throws a System.NotSupportedException.



Get: UseDefaultCredentials(self: FtpWebRequest) -> bool



Set: UseDefaultCredentials(self: FtpWebRequest)=value

"""

 UsePassive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the behavior of a client application's data transfer process.



Get: UsePassive(self: FtpWebRequest) -> bool



Set: UsePassive(self: FtpWebRequest)=value

"""


 DefaultCachePolicy=None

