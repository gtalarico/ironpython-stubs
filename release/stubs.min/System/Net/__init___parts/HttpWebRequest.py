class HttpWebRequest(WebRequest,ISerializable):
 """
 Provides an HTTP-specific implementation of the System.Net.WebRequest class.

 

 HttpWebRequest()
 """
 def Abort(self):
  """
  Abort(self: HttpWebRequest)

   Cancels a request to an Internet resource.
  """
  pass
 def AddRange(self,*__args):
  """
  AddRange(self: HttpWebRequest,rangeSpecifier: str,from: Int64,to: Int64)

   Adds a range header to a request for a specified range.

  

   rangeSpecifier: The description of the range.

   from: The position at which to start sending data.

   to: The position at which to stop sending data.

  AddRange(self: HttpWebRequest,rangeSpecifier: str,from: int,to: int)

   Adds a range header to a request for a specified range.

  

   rangeSpecifier: The description of the range.

   from: The position at which to start sending data.

   to: The position at which to stop sending data.

  AddRange(self: HttpWebRequest,rangeSpecifier: str,range: Int64)

   Adds a Range header to a request for a specific range from the beginning or end of the requested 

    data.

  

  

   rangeSpecifier: The description of the range.

   range: The starting or ending point of the range.

  AddRange(self: HttpWebRequest,rangeSpecifier: str,range: int)

   Adds a Range header to a request for a specific range from the beginning or end of the requested 

    data.

  

  

   rangeSpecifier: The description of the range.

   range: The starting or ending point of the range.

  AddRange(self: HttpWebRequest,from: Int64,to: Int64)

   Adds a byte range header to the request for a specified range.

  

   from: The position at which to start sending data.

   to: The position at which to stop sending data.

  AddRange(self: HttpWebRequest,from: int,to: int)

   Adds a byte range header to the request for a specified range.

  

   from: The position at which to start sending data.

   to: The position at which to stop sending data.

  AddRange(self: HttpWebRequest,range: Int64)

   Adds a byte range header to a request for a specific range from the beginning or end of the 

    requested data.

  

  

   range: The starting or ending point of the range.

  AddRange(self: HttpWebRequest,range: int)

   Adds a byte range header to a request for a specific range from the beginning or end of the 

    requested data.

  

  

   range: The starting or ending point of the range.
  """
  pass
 def BeginGetRequestStream(self,callback,state):
  """
  BeginGetRequestStream(self: HttpWebRequest,callback: AsyncCallback,state: object) -> IAsyncResult

  

   Begins an asynchronous request for a System.IO.Stream object to use to write data.

  

   callback: The System.AsyncCallback delegate.

   state: The state object for this request.

   Returns: An System.IAsyncResult that references the asynchronous request.
  """
  pass
 def BeginGetResponse(self,callback,state):
  """
  BeginGetResponse(self: HttpWebRequest,callback: AsyncCallback,state: object) -> IAsyncResult

  

   Begins an asynchronous request to an Internet resource.

  

   callback: The System.AsyncCallback delegate

   state: The state object for this request.

   Returns: An System.IAsyncResult that references the asynchronous request for a response.
  """
  pass
 def EndGetRequestStream(self,asyncResult,context=None):
  """
  EndGetRequestStream(self: HttpWebRequest,asyncResult: IAsyncResult) -> (Stream,TransportContext)

  

   Ends an asynchronous request for a System.IO.Stream object to use to write data and outputs the 

    System.Net.TransportContext associated with the stream.

  

  

   asyncResult: The pending request for a stream.

   Returns: A System.IO.Stream to use to write request data.

  EndGetRequestStream(self: HttpWebRequest,asyncResult: IAsyncResult) -> Stream

  

   Ends an asynchronous request for a System.IO.Stream object to use to write data.

  

   asyncResult: The pending request for a stream.

   Returns: A System.IO.Stream to use to write request data.
  """
  pass
 def EndGetResponse(self,asyncResult):
  """
  EndGetResponse(self: HttpWebRequest,asyncResult: IAsyncResult) -> WebResponse

  

   Ends an asynchronous request to an Internet resource.

  

   asyncResult: The pending request for a response.

   Returns: A System.Net.WebResponse that contains the response from the Internet resource.
  """
  pass
 def GetObjectData(self,*args):
  """
  GetObjectData(self: HttpWebRequest,serializationInfo: SerializationInfo,streamingContext: StreamingContext)

   Populates a System.Runtime.Serialization.SerializationInfo with the data required to serialize 

    the target object.

  

  

   serializationInfo: The System.Runtime.Serialization.SerializationInfo to populate with data.

   streamingContext: A System.Runtime.Serialization.StreamingContext that specifies the destination for this 

    serialization.
  """
  pass
 def GetRequestStream(self,context=None):
  """
  GetRequestStream(self: HttpWebRequest) -> (Stream,TransportContext)

  

   Gets a System.IO.Stream object to use to write request data and outputs the 

    System.Net.TransportContext associated with the stream.

  

   Returns: A System.IO.Stream to use to write request data.

  GetRequestStream(self: HttpWebRequest) -> Stream

  

   Gets a System.IO.Stream object to use to write request data.

   Returns: A System.IO.Stream to use to write request data.
  """
  pass
 def GetResponse(self):
  """
  GetResponse(self: HttpWebRequest) -> WebResponse

  

   Returns a response from an Internet resource.

   Returns: A System.Net.WebResponse that contains the response from the Internet resource.
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
 @staticmethod
 def __new__(self):
  """
  __new__(cls: type)

  __new__(cls: type,serializationInfo: SerializationInfo,streamingContext: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 Accept=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value of the Accept HTTP header.



Get: Accept(self: HttpWebRequest) -> str



Set: Accept(self: HttpWebRequest)=value

"""

 Address=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Uniform Resource Identifier (URI) of the Internet resource that actually responds to the request.



Get: Address(self: HttpWebRequest) -> Uri



"""

 AllowAutoRedirect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the request should follow redirection responses.



Get: AllowAutoRedirect(self: HttpWebRequest) -> bool



Set: AllowAutoRedirect(self: HttpWebRequest)=value

"""

 AllowReadStreamBuffering=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AllowReadStreamBuffering(self: HttpWebRequest) -> bool



Set: AllowReadStreamBuffering(self: HttpWebRequest)=value

"""

 AllowWriteStreamBuffering=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether to buffer the data sent to the Internet resource.



Get: AllowWriteStreamBuffering(self: HttpWebRequest) -> bool



Set: AllowWriteStreamBuffering(self: HttpWebRequest)=value

"""

 AutomaticDecompression=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the type of decompression that is used.



Get: AutomaticDecompression(self: HttpWebRequest) -> DecompressionMethods



Set: AutomaticDecompression(self: HttpWebRequest)=value

"""

 ClientCertificates=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the collection of security certificates that are associated with this request.



Get: ClientCertificates(self: HttpWebRequest) -> X509CertificateCollection



Set: ClientCertificates(self: HttpWebRequest)=value

"""

 Connection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value of the Connection HTTP header.



Get: Connection(self: HttpWebRequest) -> str



Set: Connection(self: HttpWebRequest)=value

"""

 ConnectionGroupName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the connection group for the request.



Get: ConnectionGroupName(self: HttpWebRequest) -> str



Set: ConnectionGroupName(self: HttpWebRequest)=value

"""

 ContentLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Content-length HTTP header.



Get: ContentLength(self: HttpWebRequest) -> Int64



Set: ContentLength(self: HttpWebRequest)=value

"""

 ContentType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value of the Content-type HTTP header.



Get: ContentType(self: HttpWebRequest) -> str



Set: ContentType(self: HttpWebRequest)=value

"""

 ContinueDelegate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the delegate method called when an HTTP 100-continue response is received from the Internet resource.



Get: ContinueDelegate(self: HttpWebRequest) -> HttpContinueDelegate



Set: ContinueDelegate(self: HttpWebRequest)=value

"""

 ContinueTimeout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ContinueTimeout(self: HttpWebRequest) -> int



Set: ContinueTimeout(self: HttpWebRequest)=value

"""

 CookieContainer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the cookies associated with the request.



Get: CookieContainer(self: HttpWebRequest) -> CookieContainer



Set: CookieContainer(self: HttpWebRequest)=value

"""

 Credentials=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets authentication information for the request.



Get: Credentials(self: HttpWebRequest) -> ICredentials



Set: Credentials(self: HttpWebRequest)=value

"""

 Date=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or set the Date HTTP header value to use in an HTTP request.



Get: Date(self: HttpWebRequest) -> DateTime



Set: Date(self: HttpWebRequest)=value

"""

 Expect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value of the Expect HTTP header.



Get: Expect(self: HttpWebRequest) -> str



Set: Expect(self: HttpWebRequest)=value

"""

 HaveResponse=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether a response has been received from an Internet resource.



Get: HaveResponse(self: HttpWebRequest) -> bool



"""

 Headers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies a collection of the name/value pairs that make up the HTTP headers.



Get: Headers(self: HttpWebRequest) -> WebHeaderCollection



Set: Headers(self: HttpWebRequest)=value

"""

 Host=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or set the Host header value to use in an HTTP request independent from the request URI.



Get: Host(self: HttpWebRequest) -> str



Set: Host(self: HttpWebRequest)=value

"""

 IfModifiedSince=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value of the If-Modified-Since HTTP header.



Get: IfModifiedSince(self: HttpWebRequest) -> DateTime



Set: IfModifiedSince(self: HttpWebRequest)=value

"""

 KeepAlive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether to make a persistent connection to the Internet resource.



Get: KeepAlive(self: HttpWebRequest) -> bool



Set: KeepAlive(self: HttpWebRequest)=value

"""

 MaximumAutomaticRedirections=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum number of redirects that the request follows.



Get: MaximumAutomaticRedirections(self: HttpWebRequest) -> int



Set: MaximumAutomaticRedirections(self: HttpWebRequest)=value

"""

 MaximumResponseHeadersLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum allowed length of the response headers.



Get: MaximumResponseHeadersLength(self: HttpWebRequest) -> int



Set: MaximumResponseHeadersLength(self: HttpWebRequest)=value

"""

 MediaType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the media type of the request.



Get: MediaType(self: HttpWebRequest) -> str



Set: MediaType(self: HttpWebRequest)=value

"""

 Method=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the method for the request.



Get: Method(self: HttpWebRequest) -> str



Set: Method(self: HttpWebRequest)=value

"""

 Pipelined=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether to pipeline the request to the Internet resource.



Get: Pipelined(self: HttpWebRequest) -> bool



Set: Pipelined(self: HttpWebRequest)=value

"""

 PreAuthenticate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether to send an Authorization header with the request.



Get: PreAuthenticate(self: HttpWebRequest) -> bool



Set: PreAuthenticate(self: HttpWebRequest)=value

"""

 ProtocolVersion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the version of HTTP to use for the request.



Get: ProtocolVersion(self: HttpWebRequest) -> Version



Set: ProtocolVersion(self: HttpWebRequest)=value

"""

 Proxy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets proxy information for the request.



Get: Proxy(self: HttpWebRequest) -> IWebProxy



Set: Proxy(self: HttpWebRequest)=value

"""

 ReadWriteTimeout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a time-out in milliseconds when writing to or reading from a stream.



Get: ReadWriteTimeout(self: HttpWebRequest) -> int



Set: ReadWriteTimeout(self: HttpWebRequest)=value

"""

 Referer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value of the Referer HTTP header.



Get: Referer(self: HttpWebRequest) -> str



Set: Referer(self: HttpWebRequest)=value

"""

 RequestUri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the original Uniform Resource Identifier (URI) of the request.



Get: RequestUri(self: HttpWebRequest) -> Uri



"""

 SendChunked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether to send data in segments to the Internet resource.



Get: SendChunked(self: HttpWebRequest) -> bool



Set: SendChunked(self: HttpWebRequest)=value

"""

 ServerCertificateValidationCallback=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ServerCertificateValidationCallback(self: HttpWebRequest) -> RemoteCertificateValidationCallback



Set: ServerCertificateValidationCallback(self: HttpWebRequest)=value

"""

 ServicePoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the service point to use for the request.



Get: ServicePoint(self: HttpWebRequest) -> ServicePoint



"""

 SupportsCookieContainer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SupportsCookieContainer(self: HttpWebRequest) -> bool



"""

 Timeout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the time-out value in milliseconds for the System.Net.HttpWebRequest.GetResponse and System.Net.HttpWebRequest.GetRequestStream methods.



Get: Timeout(self: HttpWebRequest) -> int



Set: Timeout(self: HttpWebRequest)=value

"""

 TransferEncoding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value of the Transfer-encoding HTTP header.



Get: TransferEncoding(self: HttpWebRequest) -> str



Set: TransferEncoding(self: HttpWebRequest)=value

"""

 UnsafeAuthenticatedConnectionSharing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether to allow high-speed NTLM-authenticated connection sharing.



Get: UnsafeAuthenticatedConnectionSharing(self: HttpWebRequest) -> bool



Set: UnsafeAuthenticatedConnectionSharing(self: HttpWebRequest)=value

"""

 UseDefaultCredentials=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Boolean value that controls whether default credentials are sent with requests.



Get: UseDefaultCredentials(self: HttpWebRequest) -> bool



Set: UseDefaultCredentials(self: HttpWebRequest)=value

"""

 UserAgent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value of the User-agent HTTP header.



Get: UserAgent(self: HttpWebRequest) -> str



Set: UserAgent(self: HttpWebRequest)=value

"""


 DefaultCachePolicy=None
 DefaultMaximumErrorResponseLength=64
 DefaultMaximumResponseHeadersLength=64

