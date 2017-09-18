class WebProxy(object,IAutoWebProxy,IWebProxy,ISerializable):
 """
 Contains HTTP proxy settings for the System.Net.WebRequest class.

 

 WebProxy()

 WebProxy(Address: Uri)

 WebProxy(Address: Uri,BypassOnLocal: bool)

 WebProxy(Address: Uri,BypassOnLocal: bool,BypassList: Array[str])

 WebProxy(Address: Uri,BypassOnLocal: bool,BypassList: Array[str],Credentials: ICredentials)

 WebProxy(Host: str,Port: int)

 WebProxy(Address: str)

 WebProxy(Address: str,BypassOnLocal: bool)

 WebProxy(Address: str,BypassOnLocal: bool,BypassList: Array[str])

 WebProxy(Address: str,BypassOnLocal: bool,BypassList: Array[str],Credentials: ICredentials)
 """
 @staticmethod
 def GetDefaultProxy():
  """
  GetDefaultProxy() -> WebProxy

  

   Reads the Internet Explorer nondynamic proxy settings.

   Returns: A System.Net.WebProxy instance that contains the nondynamic proxy settings from Internet 

    Explorer 5.5 and later.
  """
  pass
 def GetObjectData(self,*args):
  """
  GetObjectData(self: WebProxy,serializationInfo: SerializationInfo,streamingContext: StreamingContext)

   Populates a System.Runtime.Serialization.SerializationInfo with the data that is needed to 

    serialize the target object.

  

  

   serializationInfo: The System.Runtime.Serialization.SerializationInfo to populate with data.

   streamingContext: A System.Runtime.Serialization.StreamingContext that specifies the destination for this 

    serialization.
  """
  pass
 def GetProxy(self,destination):
  """
  GetProxy(self: WebProxy,destination: Uri) -> Uri

  

   Returns the proxied URI for a request.

  

   destination: The System.Uri instance of the requested Internet resource.

   Returns: The System.Uri instance of the Internet resource,if the resource is on the bypass list; 

    otherwise,the System.Uri instance of the proxy.
  """
  pass
 def IsBypassed(self,host):
  """
  IsBypassed(self: WebProxy,host: Uri) -> bool

  

   Indicates whether to use the proxy server for the specified host.

  

   host: The System.Uri instance of the host to check for proxy use.

   Returns: true if the proxy server should not be used for host; otherwise,false.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,Address: Uri)

  __new__(cls: type,Address: Uri,BypassOnLocal: bool)

  __new__(cls: type,Address: Uri,BypassOnLocal: bool,BypassList: Array[str])

  __new__(cls: type,Address: Uri,BypassOnLocal: bool,BypassList: Array[str],Credentials: ICredentials)

  __new__(cls: type,Host: str,Port: int)

  __new__(cls: type,Address: str)

  __new__(cls: type,Address: str,BypassOnLocal: bool)

  __new__(cls: type,Address: str,BypassOnLocal: bool,BypassList: Array[str])

  __new__(cls: type,Address: str,BypassOnLocal: bool,BypassList: Array[str],Credentials: ICredentials)

  __new__(cls: type,serializationInfo: SerializationInfo,streamingContext: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Address=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the address of the proxy server.



Get: Address(self: WebProxy) -> Uri



Set: Address(self: WebProxy)=value

"""

 BypassArrayList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a list of addresses that do not use the proxy server.



Get: BypassArrayList(self: WebProxy) -> ArrayList



"""

 BypassList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an array of addresses that do not use the proxy server.



Get: BypassList(self: WebProxy) -> Array[str]



Set: BypassList(self: WebProxy)=value

"""

 BypassProxyOnLocal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether to bypass the proxy server for local addresses.



Get: BypassProxyOnLocal(self: WebProxy) -> bool



Set: BypassProxyOnLocal(self: WebProxy)=value

"""

 Credentials=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the credentials to submit to the proxy server for authentication.



Get: Credentials(self: WebProxy) -> ICredentials



Set: Credentials(self: WebProxy)=value

"""

 UseDefaultCredentials=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Boolean value that controls whether the System.Net.CredentialCache.DefaultCredentials are sent with requests.



Get: UseDefaultCredentials(self: WebProxy) -> bool



Set: UseDefaultCredentials(self: WebProxy)=value

"""


