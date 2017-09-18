class HttpListener(object,IDisposable):
 """
 Provides a simple,programmatically controlled HTTP protocol listener. This class cannot be inherited.

 

 HttpListener()
 """
 def Abort(self):
  """
  Abort(self: HttpListener)

   Shuts down the System.Net.HttpListener object immediately,discarding all currently queued 

    requests.
  """
  pass
 def BeginGetContext(self,callback,state):
  """
  BeginGetContext(self: HttpListener,callback: AsyncCallback,state: object) -> IAsyncResult

  

   Begins asynchronously retrieving an incoming request.

  

   callback: An System.AsyncCallback delegate that references the method to invoke when a client request is 

    available.

  

   state: A user-defined object that contains information about the operation. This object is passed to 

    the callback delegate when the operation completes.

  

   Returns: An System.IAsyncResult object that indicates the status of the asynchronous operation.
  """
  pass
 def Close(self):
  """
  Close(self: HttpListener)

   Shuts down the System.Net.HttpListener.
  """
  pass
 def EndGetContext(self,asyncResult):
  """
  EndGetContext(self: HttpListener,asyncResult: IAsyncResult) -> HttpListenerContext

  

   Completes an asynchronous operation to retrieve an incoming client request.

  

   asyncResult: An System.IAsyncResult object that was obtained when the asynchronous operation was started.

   Returns: An System.Net.HttpListenerContext object that represents the client request.
  """
  pass
 def GetContext(self):
  """
  GetContext(self: HttpListener) -> HttpListenerContext

  

   Waits for an incoming request and returns when one is received.

   Returns: An System.Net.HttpListenerContext object that represents a client request.
  """
  pass
 def GetContextAsync(self):
  """ GetContextAsync(self: HttpListener) -> Task[HttpListenerContext] """
  pass
 def Start(self):
  """
  Start(self: HttpListener)

   Allows this instance to receive incoming requests.
  """
  pass
 def Stop(self):
  """
  Stop(self: HttpListener)

   Causes this instance to stop receiving incoming requests.
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 AuthenticationSchemes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the scheme used to authenticate clients.



Get: AuthenticationSchemes(self: HttpListener) -> AuthenticationSchemes



Set: AuthenticationSchemes(self: HttpListener)=value

"""

 AuthenticationSchemeSelectorDelegate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the delegate called to determine the protocol used to authenticate clients.



Get: AuthenticationSchemeSelectorDelegate(self: HttpListener) -> AuthenticationSchemeSelector



Set: AuthenticationSchemeSelectorDelegate(self: HttpListener)=value

"""

 DefaultServiceNames=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a default list of Service Provider Names (SPNs) as determined by registered prefixes.



Get: DefaultServiceNames(self: HttpListener) -> ServiceNameCollection



"""

 ExtendedProtectionPolicy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or set the System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy to use for extended protection for a session.



Get: ExtendedProtectionPolicy(self: HttpListener) -> ExtendedProtectionPolicy



Set: ExtendedProtectionPolicy(self: HttpListener)=value

"""

 ExtendedProtectionSelectorDelegate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or set the delegate called to determine the System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy to use for each request.



Get: ExtendedProtectionSelectorDelegate(self: HttpListener) -> ExtendedProtectionSelector



Set: ExtendedProtectionSelectorDelegate(self: HttpListener)=value

"""

 IgnoreWriteExceptions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Boolean value that specifies whether your application receives exceptions that occur when an System.Net.HttpListener sends the response to the client.



Get: IgnoreWriteExceptions(self: HttpListener) -> bool



Set: IgnoreWriteExceptions(self: HttpListener)=value

"""

 IsListening=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether System.Net.HttpListener has been started.



Get: IsListening(self: HttpListener) -> bool



"""

 Prefixes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Uniform Resource Identifier (URI) prefixes handled by this System.Net.HttpListener object.



Get: Prefixes(self: HttpListener) -> HttpListenerPrefixCollection



"""

 Realm=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the realm,or resource partition,associated with this System.Net.HttpListener object.



Get: Realm(self: HttpListener) -> str



Set: Realm(self: HttpListener)=value

"""

 TimeoutManager=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TimeoutManager(self: HttpListener) -> HttpListenerTimeoutManager



"""

 UnsafeConnectionNtlmAuthentication=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Boolean value that controls whether,when NTLM is used,additional requests using the same Transmission Control Protocol (TCP) connection are required to authenticate.



Get: UnsafeConnectionNtlmAuthentication(self: HttpListener) -> bool



Set: UnsafeConnectionNtlmAuthentication(self: HttpListener)=value

"""


 ExtendedProtectionSelector=None
 IsSupported=True

