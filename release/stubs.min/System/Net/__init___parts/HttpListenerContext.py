class HttpListenerContext(object):
 """ Provides access to the request and response objects used by the System.Net.HttpListener class. This class cannot be inherited. """
 def AcceptWebSocketAsync(self,subProtocol,*__args):
  """
  AcceptWebSocketAsync(self: HttpListenerContext,subProtocol: str,receiveBufferSize: int,keepAliveInterval: TimeSpan) -> Task[HttpListenerWebSocketContext]

  AcceptWebSocketAsync(self: HttpListenerContext,subProtocol: str,receiveBufferSize: int,keepAliveInterval: TimeSpan,internalBuffer: ArraySegment[Byte]) -> Task[HttpListenerWebSocketContext]

  AcceptWebSocketAsync(self: HttpListenerContext,subProtocol: str) -> Task[HttpListenerWebSocketContext]

  AcceptWebSocketAsync(self: HttpListenerContext,subProtocol: str,keepAliveInterval: TimeSpan) -> Task[HttpListenerWebSocketContext]
  """
  pass
 Request=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Net.HttpListenerRequest that represents a client's request for a resource.



Get: Request(self: HttpListenerContext) -> HttpListenerRequest



"""

 Response=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Net.HttpListenerResponse object that will be sent to the client in response to the client's request.



Get: Response(self: HttpListenerContext) -> HttpListenerResponse



"""

 User=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an object used to obtain identity,authentication information,and security roles for the client whose request is represented by this System.Net.HttpListenerContext object.



Get: User(self: HttpListenerContext) -> IPrincipal



"""


