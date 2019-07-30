# encoding: utf-8
# module System.Net.WebSockets calls itself WebSockets
# from System,Version=4.0.0.0,Culture=neutral,PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no important

# no functions
# classes

class WebSocket(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return WebSocket()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Abort(self):
  """ Abort(self: WebSocket) """
  pass
 def CloseAsync(self,closeStatus,statusDescription,cancellationToken):
  """ CloseAsync(self: WebSocket,closeStatus: WebSocketCloseStatus,statusDescription: str,cancellationToken: CancellationToken) -> Task """
  pass
 def CloseOutputAsync(self,closeStatus,statusDescription,cancellationToken):
  """ CloseOutputAsync(self: WebSocket,closeStatus: WebSocketCloseStatus,statusDescription: str,cancellationToken: CancellationToken) -> Task """
  pass
 @staticmethod
 def CreateClientBuffer(receiveBufferSize,sendBufferSize):
  """ CreateClientBuffer(receiveBufferSize: int,sendBufferSize: int) -> ArraySegment[Byte] """
  pass
 @staticmethod
 def CreateClientWebSocket(innerStream,subProtocol,receiveBufferSize,sendBufferSize,keepAliveInterval,useZeroMaskingKey,internalBuffer):
  """ CreateClientWebSocket(innerStream: Stream,subProtocol: str,receiveBufferSize: int,sendBufferSize: int,keepAliveInterval: TimeSpan,useZeroMaskingKey: bool,internalBuffer: ArraySegment[Byte]) -> WebSocket """
  pass
 @staticmethod
 def CreateServerBuffer(receiveBufferSize):
  """ CreateServerBuffer(receiveBufferSize: int) -> ArraySegment[Byte] """
  pass
 def Dispose(self):
  """ Dispose(self: WebSocket) """
  pass
 @staticmethod
 def IsApplicationTargeting45():
  """ IsApplicationTargeting45() -> bool """
  pass
 def IsStateTerminal(self,*args):
  """ IsStateTerminal(state: WebSocketState) -> bool """
  pass
 def ReceiveAsync(self,buffer,cancellationToken):
  """ ReceiveAsync(self: WebSocket,buffer: ArraySegment[Byte],cancellationToken: CancellationToken) -> Task[WebSocketReceiveResult] """
  pass
 @staticmethod
 def RegisterPrefixes():
  """ RegisterPrefixes() """
  pass
 def SendAsync(self,buffer,messageType,endOfMessage,cancellationToken):
  """ SendAsync(self: WebSocket,buffer: ArraySegment[Byte],messageType: WebSocketMessageType,endOfMessage: bool,cancellationToken: CancellationToken) -> Task """
  pass
 def ThrowOnInvalidState(self,*args):
  """ ThrowOnInvalidState(state: WebSocketState,*validStates: Array[WebSocketState]) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 CloseStatus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CloseStatus(self: WebSocket) -> Nullable[WebSocketCloseStatus]

"""

 CloseStatusDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CloseStatusDescription(self: WebSocket) -> str

"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: State(self: WebSocket) -> WebSocketState

"""

 SubProtocol=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SubProtocol(self: WebSocket) -> str

"""


 DefaultKeepAliveInterval=None


class ClientWebSocket(WebSocket):
 """ ClientWebSocket() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ClientWebSocket()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Abort(self):
  """ Abort(self: ClientWebSocket) """
  pass
 def CloseAsync(self,closeStatus,statusDescription,cancellationToken):
  """ CloseAsync(self: ClientWebSocket,closeStatus: WebSocketCloseStatus,statusDescription: str,cancellationToken: CancellationToken) -> Task """
  pass
 def CloseOutputAsync(self,closeStatus,statusDescription,cancellationToken):
  """ CloseOutputAsync(self: ClientWebSocket,closeStatus: WebSocketCloseStatus,statusDescription: str,cancellationToken: CancellationToken) -> Task """
  pass
 def ConnectAsync(self,uri,cancellationToken):
  """ ConnectAsync(self: ClientWebSocket,uri: Uri,cancellationToken: CancellationToken) -> Task """
  pass
 def Dispose(self):
  """ Dispose(self: ClientWebSocket) """
  pass
 def ReceiveAsync(self,buffer,cancellationToken):
  """ ReceiveAsync(self: ClientWebSocket,buffer: ArraySegment[Byte],cancellationToken: CancellationToken) -> Task[WebSocketReceiveResult] """
  pass
 def SendAsync(self,buffer,messageType,endOfMessage,cancellationToken):
  """ SendAsync(self: ClientWebSocket,buffer: ArraySegment[Byte],messageType: WebSocketMessageType,endOfMessage: bool,cancellationToken: CancellationToken) -> Task """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 CloseStatus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CloseStatus(self: ClientWebSocket) -> Nullable[WebSocketCloseStatus]

"""

 CloseStatusDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CloseStatusDescription(self: ClientWebSocket) -> str

"""

 Options=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Options(self: ClientWebSocket) -> ClientWebSocketOptions

"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: State(self: ClientWebSocket) -> WebSocketState

"""

 SubProtocol=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SubProtocol(self: ClientWebSocket) -> str

"""



class ClientWebSocketOptions(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ClientWebSocketOptions()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def AddSubProtocol(self,subProtocol):
  """ AddSubProtocol(self: ClientWebSocketOptions,subProtocol: str) """
  pass
 def SetBuffer(self,receiveBufferSize,sendBufferSize,buffer=None):
  """ SetBuffer(self: ClientWebSocketOptions,receiveBufferSize: int,sendBufferSize: int)SetBuffer(self: ClientWebSocketOptions,receiveBufferSize: int,sendBufferSize: int,buffer: ArraySegment[Byte]) """
  pass
 def SetRequestHeader(self,headerName,headerValue):
  """ SetRequestHeader(self: ClientWebSocketOptions,headerName: str,headerValue: str) """
  pass
 ClientCertificates=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ClientCertificates(self: ClientWebSocketOptions) -> X509CertificateCollection

Set: ClientCertificates(self: ClientWebSocketOptions)=value
"""

 Cookies=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Cookies(self: ClientWebSocketOptions) -> CookieContainer

Set: Cookies(self: ClientWebSocketOptions)=value
"""

 Credentials=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Credentials(self: ClientWebSocketOptions) -> ICredentials

Set: Credentials(self: ClientWebSocketOptions)=value
"""

 KeepAliveInterval=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: KeepAliveInterval(self: ClientWebSocketOptions) -> TimeSpan

Set: KeepAliveInterval(self: ClientWebSocketOptions)=value
"""

 Proxy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Proxy(self: ClientWebSocketOptions) -> IWebProxy

Set: Proxy(self: ClientWebSocketOptions)=value
"""

 UseDefaultCredentials=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UseDefaultCredentials(self: ClientWebSocketOptions) -> bool

Set: UseDefaultCredentials(self: ClientWebSocketOptions)=value
"""



class WebSocketContext(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return WebSocketContext()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 CookieCollection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CookieCollection(self: WebSocketContext) -> CookieCollection

"""

 Headers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Headers(self: WebSocketContext) -> NameValueCollection

"""

 IsAuthenticated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsAuthenticated(self: WebSocketContext) -> bool

"""

 IsLocal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsLocal(self: WebSocketContext) -> bool

"""

 IsSecureConnection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsSecureConnection(self: WebSocketContext) -> bool

"""

 Origin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Origin(self: WebSocketContext) -> str

"""

 RequestUri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: RequestUri(self: WebSocketContext) -> Uri

"""

 SecWebSocketKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SecWebSocketKey(self: WebSocketContext) -> str

"""

 SecWebSocketProtocols=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SecWebSocketProtocols(self: WebSocketContext) -> IEnumerable[str]

"""

 SecWebSocketVersion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SecWebSocketVersion(self: WebSocketContext) -> str

"""

 User=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: User(self: WebSocketContext) -> IPrincipal

"""

 WebSocket=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WebSocket(self: WebSocketContext) -> WebSocket

"""



class HttpListenerWebSocketContext(WebSocketContext):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HttpListenerWebSocketContext()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 CookieCollection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CookieCollection(self: HttpListenerWebSocketContext) -> CookieCollection

"""

 Headers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Headers(self: HttpListenerWebSocketContext) -> NameValueCollection

"""

 IsAuthenticated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsAuthenticated(self: HttpListenerWebSocketContext) -> bool

"""

 IsLocal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsLocal(self: HttpListenerWebSocketContext) -> bool

"""

 IsSecureConnection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsSecureConnection(self: HttpListenerWebSocketContext) -> bool

"""

 Origin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Origin(self: HttpListenerWebSocketContext) -> str

"""

 RequestUri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: RequestUri(self: HttpListenerWebSocketContext) -> Uri

"""

 SecWebSocketKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SecWebSocketKey(self: HttpListenerWebSocketContext) -> str

"""

 SecWebSocketProtocols=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SecWebSocketProtocols(self: HttpListenerWebSocketContext) -> IEnumerable[str]

"""

 SecWebSocketVersion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SecWebSocketVersion(self: HttpListenerWebSocketContext) -> str

"""

 User=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: User(self: HttpListenerWebSocketContext) -> IPrincipal

"""

 WebSocket=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WebSocket(self: HttpListenerWebSocketContext) -> WebSocket

"""



class WebSocketCloseStatus:
 """ enum WebSocketCloseStatus,values: Empty (1005),EndpointUnavailable (1001),InternalServerError (1011),InvalidMessageType (1003),InvalidPayloadData (1007),MandatoryExtension (1010),MessageTooBig (1009),NormalClosure (1000),PolicyViolation (1008),ProtocolError (1002) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return WebSocketCloseStatus()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Empty=None
 EndpointUnavailable=None
 InternalServerError=None
 InvalidMessageType=None
 InvalidPayloadData=None
 MandatoryExtension=None
 MessageTooBig=None
 NormalClosure=None
 PolicyViolation=None
 ProtocolError=None
 value__=None


class WebSocketError:
 """ enum WebSocketError,values: ConnectionClosedPrematurely (8),Faulted (2),HeaderError (7),InvalidMessageType (1),InvalidState (9),NativeError (3),NotAWebSocket (4),Success (0),UnsupportedProtocol (6),UnsupportedVersion (5) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return WebSocketError()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 ConnectionClosedPrematurely=None
 Faulted=None
 HeaderError=None
 InvalidMessageType=None
 InvalidState=None
 NativeError=None
 NotAWebSocket=None
 Success=None
 UnsupportedProtocol=None
 UnsupportedVersion=None
 value__=None


class WebSocketException(Win32Exception):
 """
 WebSocketException()
 WebSocketException(error: WebSocketError)
 WebSocketException(error: WebSocketError,message: str)
 WebSocketException(error: WebSocketError,innerException: Exception)
 WebSocketException(error: WebSocketError,message: str,innerException: Exception)
 WebSocketException(nativeError: int)
 WebSocketException(nativeError: int,message: str)
 WebSocketException(nativeError: int,innerException: Exception)
 WebSocketException(error: WebSocketError,nativeError: int)
 WebSocketException(error: WebSocketError,nativeError: int,message: str)
 WebSocketException(error: WebSocketError,nativeError: int,innerException: Exception)
 WebSocketException(error: WebSocketError,nativeError: int,message: str,innerException: Exception)
 WebSocketException(message: str)
 WebSocketException(message: str,innerException: Exception)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return WebSocketException()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetObjectData(self,info,context):
  """ GetObjectData(self: WebSocketException,info: SerializationInfo,context: StreamingContext) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,error: WebSocketError)
  __new__(cls: type,error: WebSocketError,message: str)
  __new__(cls: type,error: WebSocketError,innerException: Exception)
  __new__(cls: type,error: WebSocketError,message: str,innerException: Exception)
  __new__(cls: type,nativeError: int)
  __new__(cls: type,nativeError: int,message: str)
  __new__(cls: type,nativeError: int,innerException: Exception)
  __new__(cls: type,error: WebSocketError,nativeError: int)
  __new__(cls: type,error: WebSocketError,nativeError: int,message: str)
  __new__(cls: type,error: WebSocketError,nativeError: int,innerException: Exception)
  __new__(cls: type,error: WebSocketError,nativeError: int,message: str,innerException: Exception)
  __new__(cls: type,message: str)
  __new__(cls: type,message: str,innerException: Exception)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 ErrorCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ErrorCode(self: WebSocketException) -> int

"""

 WebSocketErrorCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WebSocketErrorCode(self: WebSocketException) -> WebSocketError

"""


 SerializeObjectState=None


class WebSocketMessageType:
 """ enum WebSocketMessageType,values: Binary (1),Close (2),Text (0) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return WebSocketMessageType()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Binary=None
 Close=None
 Text=None
 value__=None


class WebSocketReceiveResult(object):
 """
 WebSocketReceiveResult(count: int,messageType: WebSocketMessageType,endOfMessage: bool)
 WebSocketReceiveResult(count: int,messageType: WebSocketMessageType,endOfMessage: bool,closeStatus: Nullable[WebSocketCloseStatus],closeStatusDescription: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return WebSocketReceiveResult()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,count,messageType,endOfMessage,closeStatus=None,closeStatusDescription=None):
  """
  __new__(cls: type,count: int,messageType: WebSocketMessageType,endOfMessage: bool)
  __new__(cls: type,count: int,messageType: WebSocketMessageType,endOfMessage: bool,closeStatus: Nullable[WebSocketCloseStatus],closeStatusDescription: str)
  """
  pass
 CloseStatus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CloseStatus(self: WebSocketReceiveResult) -> Nullable[WebSocketCloseStatus]

"""

 CloseStatusDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CloseStatusDescription(self: WebSocketReceiveResult) -> str

"""

 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Count(self: WebSocketReceiveResult) -> int

"""

 EndOfMessage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: EndOfMessage(self: WebSocketReceiveResult) -> bool

"""

 MessageType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MessageType(self: WebSocketReceiveResult) -> WebSocketMessageType

"""



class WebSocketState:
 """ enum WebSocketState,values: Aborted (6),Closed (5),CloseReceived (4),CloseSent (3),Connecting (1),None (0),Open (2) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return WebSocketState()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Aborted=None
 Closed=None
 CloseReceived=None
 CloseSent=None
 Connecting=None
 None_ =None
 Open=None
 value__=None


