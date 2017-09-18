class WebRequest(MarshalByRefObject,ISerializable):
 """ Makes a request to a Uniform Resource Identifier (URI). This is an abstract class. """
 def Abort(self):
  """
  Abort(self: WebRequest)

   Aborts the Request
  """
  pass
 def BeginGetRequestStream(self,callback,state):
  """
  BeginGetRequestStream(self: WebRequest,callback: AsyncCallback,state: object) -> IAsyncResult

  

   When overridden in a descendant class,provides an asynchronous version of the 

    System.Net.WebRequest.GetRequestStream method.

  

  

   callback: The System.AsyncCallback delegate.

   state: An object containing state information for this asynchronous request.

   Returns: An System.IAsyncResult that references the asynchronous request.
  """
  pass
 def BeginGetResponse(self,callback,state):
  """
  BeginGetResponse(self: WebRequest,callback: AsyncCallback,state: object) -> IAsyncResult

  

   When overridden in a descendant class,begins an asynchronous request for an Internet resource.

  

   callback: The System.AsyncCallback delegate.

   state: An object containing state information for this asynchronous request.

   Returns: An System.IAsyncResult that references the asynchronous request.
  """
  pass
 @staticmethod
 def Create(*__args):
  """
  Create(requestUri: Uri) -> WebRequest

  

   Initializes a new System.Net.WebRequest instance for the specified URI scheme.

  

   requestUri: A System.Uri containing the URI of the requested resource.

   Returns: A System.Net.WebRequest descendant for the specified URI scheme.

  Create(requestUriString: str) -> WebRequest

  

   Initializes a new System.Net.WebRequest instance for the specified URI scheme.

  

   requestUriString: The URI that identifies the Internet resource.

   Returns: A System.Net.WebRequest descendant for the specific URI scheme.
  """
  pass
 @staticmethod
 def CreateDefault(requestUri):
  """
  CreateDefault(requestUri: Uri) -> WebRequest

  

   Initializes a new System.Net.WebRequest instance for the specified URI scheme.

  

   requestUri: A System.Uri containing the URI of the requested resource.

   Returns: A System.Net.WebRequest descendant for the specified URI scheme.
  """
  pass
 @staticmethod
 def CreateHttp(*__args):
  """
  CreateHttp(requestUri: Uri) -> HttpWebRequest

  CreateHttp(requestUriString: str) -> HttpWebRequest
  """
  pass
 def EndGetRequestStream(self,asyncResult):
  """
  EndGetRequestStream(self: WebRequest,asyncResult: IAsyncResult) -> Stream

  

   When overridden in a descendant class,returns a System.IO.Stream for writing data to the 

    Internet resource.

  

  

   asyncResult: An System.IAsyncResult that references a pending request for a stream.

   Returns: A System.IO.Stream to write data to.
  """
  pass
 def EndGetResponse(self,asyncResult):
  """
  EndGetResponse(self: WebRequest,asyncResult: IAsyncResult) -> WebResponse

  

   When overridden in a descendant class,returns a System.Net.WebResponse.

  

   asyncResult: An System.IAsyncResult that references a pending request for a response.

   Returns: A System.Net.WebResponse that contains a response to the Internet request.
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
  GetRequestStream(self: WebRequest) -> Stream

  

   When overridden in a descendant class,returns a System.IO.Stream for writing data to the 

    Internet resource.

  

   Returns: A System.IO.Stream for writing data to the Internet resource.
  """
  pass
 def GetRequestStreamAsync(self):
  """ GetRequestStreamAsync(self: WebRequest) -> Task[Stream] """
  pass
 def GetResponse(self):
  """
  GetResponse(self: WebRequest) -> WebResponse

  

   When overridden in a descendant class,returns a response to an Internet request.

   Returns: A System.Net.WebResponse containing the response to the Internet request.
  """
  pass
 def GetResponseAsync(self):
  """ GetResponseAsync(self: WebRequest) -> Task[WebResponse] """
  pass
 @staticmethod
 def GetSystemWebProxy():
  """
  GetSystemWebProxy() -> IWebProxy

  

   Returns a proxy configured with the Internet Explorer settings of the currently impersonated 

    user.

  

   Returns: An System.Net.IWebProxy used by every call to instances of System.Net.WebRequest.
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
 @staticmethod
 def RegisterPortableWebRequestCreator(creator):
  """ RegisterPortableWebRequestCreator(creator: IWebRequestCreate) """
  pass
 @staticmethod
 def RegisterPrefix(prefix,creator):
  """
  RegisterPrefix(prefix: str,creator: IWebRequestCreate) -> bool

  

   Registers a System.Net.WebRequest descendant for the specified URI.

  

   prefix: The complete URI or URI prefix that the System.Net.WebRequest descendant services.

   creator: The create method that the System.Net.WebRequest calls to create the System.Net.WebRequest 

    descendant.

  

   Returns: true if registration is successful; otherwise,false.
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
 AuthenticationLevel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets values indicating the level of authentication and impersonation used for this request.



Get: AuthenticationLevel(self: WebRequest) -> AuthenticationLevel



Set: AuthenticationLevel(self: WebRequest)=value

"""

 CachePolicy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the cache policy for this request.



Get: CachePolicy(self: WebRequest) -> RequestCachePolicy



Set: CachePolicy(self: WebRequest)=value

"""

 ConnectionGroupName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a descendant class,gets or sets the name of the connection group for the request.



Get: ConnectionGroupName(self: WebRequest) -> str



Set: ConnectionGroupName(self: WebRequest)=value

"""

 ContentLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a descendant class,gets or sets the content length of the request data being sent.



Get: ContentLength(self: WebRequest) -> Int64



Set: ContentLength(self: WebRequest)=value

"""

 ContentType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a descendant class,gets or sets the content type of the request data being sent.



Get: ContentType(self: WebRequest) -> str



Set: ContentType(self: WebRequest)=value

"""

 CreatorInstance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatorInstance(self: WebRequest) -> IWebRequestCreate



"""

 Credentials=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a descendant class,gets or sets the network credentials used for authenticating the request with the Internet resource.



Get: Credentials(self: WebRequest) -> ICredentials



Set: Credentials(self: WebRequest)=value

"""

 Headers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a descendant class,gets or sets the collection of header name/value pairs associated with the request.



Get: Headers(self: WebRequest) -> WebHeaderCollection



Set: Headers(self: WebRequest)=value

"""

 ImpersonationLevel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the impersonation level for the current request.



Get: ImpersonationLevel(self: WebRequest) -> TokenImpersonationLevel



Set: ImpersonationLevel(self: WebRequest)=value

"""

 Method=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a descendant class,gets or sets the protocol method to use in this request.



Get: Method(self: WebRequest) -> str



Set: Method(self: WebRequest)=value

"""

 PreAuthenticate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a descendant class,indicates whether to pre-authenticate the request.



Get: PreAuthenticate(self: WebRequest) -> bool



Set: PreAuthenticate(self: WebRequest)=value

"""

 Proxy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a descendant class,gets or sets the network proxy to use to access this Internet resource.



Get: Proxy(self: WebRequest) -> IWebProxy



Set: Proxy(self: WebRequest)=value

"""

 RequestUri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a descendant class,gets the URI of the Internet resource associated with the request.



Get: RequestUri(self: WebRequest) -> Uri



"""

 Timeout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the length of time,in milliseconds,before the request times out.



Get: Timeout(self: WebRequest) -> int



Set: Timeout(self: WebRequest)=value

"""

 UseDefaultCredentials=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a descendant class,gets or sets a System.Boolean value that controls whether System.Net.CredentialCache.DefaultCredentials are sent with requests.



Get: UseDefaultCredentials(self: WebRequest) -> bool



Set: UseDefaultCredentials(self: WebRequest)=value

"""


 DefaultCachePolicy=None
 DefaultWebProxy=None

