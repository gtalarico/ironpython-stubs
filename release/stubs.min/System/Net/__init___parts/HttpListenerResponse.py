class HttpListenerResponse(object,IDisposable):
 """ Represents a response to a request being handled by an System.Net.HttpListener object. """
 def Abort(self):
  """
  Abort(self: HttpListenerResponse)

   Closes the connection to the client without sending a response.
  """
  pass
 def AddHeader(self,name,value):
  """
  AddHeader(self: HttpListenerResponse,name: str,value: str)

   Adds the specified header and value to the HTTP headers for this response.

  

   name: The name of the HTTP header to set.

   value: The value for the name header.
  """
  pass
 def AppendCookie(self,cookie):
  """
  AppendCookie(self: HttpListenerResponse,cookie: Cookie)

   Adds the specified System.Net.Cookie to the collection of cookies for this response.

  

   cookie: The System.Net.Cookie to add to the collection to be sent with this response
  """
  pass
 def AppendHeader(self,name,value):
  """
  AppendHeader(self: HttpListenerResponse,name: str,value: str)

   Appends a value to the specified HTTP header to be sent with this response.

  

   name: The name of the HTTP header to append value to.

   value: The value to append to the name header.
  """
  pass
 def Close(self,responseEntity=None,willBlock=None):
  """
  Close(self: HttpListenerResponse)

   Sends the response to the client and releases the resources held by this 

    System.Net.HttpListenerResponse instance.

  

  Close(self: HttpListenerResponse,responseEntity: Array[Byte],willBlock: bool)

   Returns the specified byte array to the client and releases the resources held by this 

    System.Net.HttpListenerResponse instance.

  

  

   responseEntity: A System.Byte array that contains the response to send to the client.

   willBlock: true to block execution while flushing the stream to the client; otherwise,false.
  """
  pass
 def CopyFrom(self,templateResponse):
  """
  CopyFrom(self: HttpListenerResponse,templateResponse: HttpListenerResponse)

   Copies properties from the specified System.Net.HttpListenerResponse to this response.

  

   templateResponse: The System.Net.HttpListenerResponse instance to copy.
  """
  pass
 def Redirect(self,url):
  """
  Redirect(self: HttpListenerResponse,url: str)

   Configures the response to redirect the client to the specified URL.

  

   url: The URL that the client should use to locate the requested resource.
  """
  pass
 def SetCookie(self,cookie):
  """
  SetCookie(self: HttpListenerResponse,cookie: Cookie)

   Adds or updates a System.Net.Cookie in the collection of cookies sent with this response.

  

   cookie: A System.Net.Cookie for this response.
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
 ContentEncoding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Text.Encoding for this response's System.Net.HttpListenerResponse.OutputStream.



Get: ContentEncoding(self: HttpListenerResponse) -> Encoding



Set: ContentEncoding(self: HttpListenerResponse)=value

"""

 ContentLength64=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of bytes in the body data included in the response.



Get: ContentLength64(self: HttpListenerResponse) -> Int64



Set: ContentLength64(self: HttpListenerResponse)=value

"""

 ContentType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the MIME type of the content returned.



Get: ContentType(self: HttpListenerResponse) -> str



Set: ContentType(self: HttpListenerResponse)=value

"""

 Cookies=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the collection of cookies returned with the response.



Get: Cookies(self: HttpListenerResponse) -> CookieCollection



Set: Cookies(self: HttpListenerResponse)=value

"""

 Headers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the collection of header name/value pairs returned by the server.



Get: Headers(self: HttpListenerResponse) -> WebHeaderCollection



Set: Headers(self: HttpListenerResponse)=value

"""

 KeepAlive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the server requests a persistent connection.



Get: KeepAlive(self: HttpListenerResponse) -> bool



Set: KeepAlive(self: HttpListenerResponse)=value

"""

 OutputStream=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.IO.Stream object to which a response can be written.



Get: OutputStream(self: HttpListenerResponse) -> Stream



"""

 ProtocolVersion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the HTTP version used for the response.



Get: ProtocolVersion(self: HttpListenerResponse) -> Version



Set: ProtocolVersion(self: HttpListenerResponse)=value

"""

 RedirectLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value of the HTTP Location header in this response.



Get: RedirectLocation(self: HttpListenerResponse) -> str



Set: RedirectLocation(self: HttpListenerResponse)=value

"""

 SendChunked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether the response uses chunked transfer encoding.



Get: SendChunked(self: HttpListenerResponse) -> bool



Set: SendChunked(self: HttpListenerResponse)=value

"""

 StatusCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the HTTP status code to be returned to the client.



Get: StatusCode(self: HttpListenerResponse) -> int



Set: StatusCode(self: HttpListenerResponse)=value

"""

 StatusDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a text description of the HTTP status code returned to the client.



Get: StatusDescription(self: HttpListenerResponse) -> str



Set: StatusDescription(self: HttpListenerResponse)=value

"""


