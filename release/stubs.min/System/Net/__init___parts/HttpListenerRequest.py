class HttpListenerRequest(object):
 """ Describes an incoming HTTP request to an System.Net.HttpListener object. This class cannot be inherited. """
 def BeginGetClientCertificate(self,requestCallback,state):
  """
  BeginGetClientCertificate(self: HttpListenerRequest,requestCallback: AsyncCallback,state: object) -> IAsyncResult

  

   Begins an asynchronous request for the client's X.509 v.3 certificate.

  

   requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is 

    complete.

  

   state: A user-defined object that contains information about the operation. This object is passed to 

    the callback delegate when the operation completes.

  

   Returns: An System.IAsyncResult that indicates the status of the operation.
  """
  pass
 def EndGetClientCertificate(self,asyncResult):
  """
  EndGetClientCertificate(self: HttpListenerRequest,asyncResult: IAsyncResult) -> X509Certificate2

  

   Ends an asynchronous request for the client's X.509 v.3 certificate.

  

   asyncResult: The pending request for the certificate.

   Returns: The System.IAsyncResult object that is returned when the operation started.
  """
  pass
 def GetClientCertificate(self):
  """
  GetClientCertificate(self: HttpListenerRequest) -> X509Certificate2

  

   Retrieves the client's X.509 v.3 certificate.

   Returns: A System.Security.Cryptography.X509Certificates object that contains the client's X.509 v.3 

    certificate.
  """
  pass
 def GetClientCertificateAsync(self):
  """ GetClientCertificateAsync(self: HttpListenerRequest) -> Task[X509Certificate2] """
  pass
 AcceptTypes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the MIME types accepted by the client.



Get: AcceptTypes(self: HttpListenerRequest) -> Array[str]



"""

 ClientCertificateError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an error code that identifies a problem with the System.Security.Cryptography.X509Certificates.X509Certificate provided by the client.



Get: ClientCertificateError(self: HttpListenerRequest) -> int



"""

 ContentEncoding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the content encoding that can be used with data sent with the request



Get: ContentEncoding(self: HttpListenerRequest) -> Encoding



"""

 ContentLength64=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length of the body data included in the request.



Get: ContentLength64(self: HttpListenerRequest) -> Int64



"""

 ContentType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the MIME type of the body data included in the request.



Get: ContentType(self: HttpListenerRequest) -> str



"""

 Cookies=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the cookies sent with the request.



Get: Cookies(self: HttpListenerRequest) -> CookieCollection



"""

 HasEntityBody=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Boolean value that indicates whether the request has associated body data.



Get: HasEntityBody(self: HttpListenerRequest) -> bool



"""

 Headers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of header name/value pairs sent in the request.



Get: Headers(self: HttpListenerRequest) -> NameValueCollection



"""

 HttpMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the HTTP method specified by the client.



Get: HttpMethod(self: HttpListenerRequest) -> str



"""

 InputStream=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a stream that contains the body data sent by the client.



Get: InputStream(self: HttpListenerRequest) -> Stream



"""

 IsAuthenticated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Boolean value that indicates whether the client sending this request is authenticated.



Get: IsAuthenticated(self: HttpListenerRequest) -> bool



"""

 IsLocal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Boolean value that indicates whether the request is sent from the local computer.



Get: IsLocal(self: HttpListenerRequest) -> bool



"""

 IsSecureConnection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Boolean value that indicates whether the TCP connection used to send the request is using the Secure Sockets Layer (SSL) protocol.



Get: IsSecureConnection(self: HttpListenerRequest) -> bool



"""

 IsWebSocketRequest=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsWebSocketRequest(self: HttpListenerRequest) -> bool



"""

 KeepAlive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Boolean value that indicates whether the client requests a persistent connection.



Get: KeepAlive(self: HttpListenerRequest) -> bool



"""

 LocalEndPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get the server IP address and port number to which the request is directed.



Get: LocalEndPoint(self: HttpListenerRequest) -> IPEndPoint



"""

 ProtocolVersion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the HTTP version used by the requesting client.



Get: ProtocolVersion(self: HttpListenerRequest) -> Version



"""

 QueryString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the query string included in the request.



Get: QueryString(self: HttpListenerRequest) -> NameValueCollection



"""

 RawUrl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the URL information (without the host and port) requested by the client.



Get: RawUrl(self: HttpListenerRequest) -> str



"""

 RemoteEndPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the client IP address and port number from which the request originated.



Get: RemoteEndPoint(self: HttpListenerRequest) -> IPEndPoint



"""

 RequestTraceIdentifier=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the request identifier of the incoming HTTP request.



Get: RequestTraceIdentifier(self: HttpListenerRequest) -> Guid



"""

 ServiceName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Service Provider Name (SPN) that the client sent on the request.



Get: ServiceName(self: HttpListenerRequest) -> str



"""

 TransportContext=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Net.TransportContext for the client request.



Get: TransportContext(self: HttpListenerRequest) -> TransportContext



"""

 Url=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Uri object requested by the client.



Get: Url(self: HttpListenerRequest) -> Uri



"""

 UrlReferrer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Uniform Resource Identifier (URI) of the resource that referred the client to the server.



Get: UrlReferrer(self: HttpListenerRequest) -> Uri



"""

 UserAgent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the user agent presented by the client.



Get: UserAgent(self: HttpListenerRequest) -> str



"""

 UserHostAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the server IP address and port number to which the request is directed.



Get: UserHostAddress(self: HttpListenerRequest) -> str



"""

 UserHostName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the DNS name and,if provided,the port number specified by the client.



Get: UserHostName(self: HttpListenerRequest) -> str



"""

 UserLanguages=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the natural languages that are preferred for the response.



Get: UserLanguages(self: HttpListenerRequest) -> Array[str]



"""


