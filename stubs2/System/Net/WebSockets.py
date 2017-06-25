# encoding: utf-8
# module System.Net.WebSockets calls itself WebSockets
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class WebSocket(object, IDisposable):
    # no doc
    def Abort(self):
        """ Abort(self: WebSocket) """
        pass

    def CloseAsync(self, closeStatus, statusDescription, cancellationToken):
        """ CloseAsync(self: WebSocket, closeStatus: WebSocketCloseStatus, statusDescription: str, cancellationToken: CancellationToken) -> Task """
        pass

    def CloseOutputAsync(self, closeStatus, statusDescription, cancellationToken):
        """ CloseOutputAsync(self: WebSocket, closeStatus: WebSocketCloseStatus, statusDescription: str, cancellationToken: CancellationToken) -> Task """
        pass

    @staticmethod
    def CreateClientBuffer(receiveBufferSize, sendBufferSize):
        """ CreateClientBuffer(receiveBufferSize: int, sendBufferSize: int) -> ArraySegment[Byte] """
        pass

    @staticmethod
    def CreateClientWebSocket(innerStream, subProtocol, receiveBufferSize, sendBufferSize, keepAliveInterval, useZeroMaskingKey, internalBuffer):
        """ CreateClientWebSocket(innerStream: Stream, subProtocol: str, receiveBufferSize: int, sendBufferSize: int, keepAliveInterval: TimeSpan, useZeroMaskingKey: bool, internalBuffer: ArraySegment[Byte]) -> WebSocket """
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

    def IsStateTerminal(self, *args): #cannot find CLR method
        """ IsStateTerminal(state: WebSocketState) -> bool """
        pass

    def ReceiveAsync(self, buffer, cancellationToken):
        """ ReceiveAsync(self: WebSocket, buffer: ArraySegment[Byte], cancellationToken: CancellationToken) -> Task[WebSocketReceiveResult] """
        pass

    @staticmethod
    def RegisterPrefixes():
        """ RegisterPrefixes() """
        pass

    def SendAsync(self, buffer, messageType, endOfMessage, cancellationToken):
        """ SendAsync(self: WebSocket, buffer: ArraySegment[Byte], messageType: WebSocketMessageType, endOfMessage: bool, cancellationToken: CancellationToken) -> Task """
        pass

    def ThrowOnInvalidState(self, *args): #cannot find CLR method
        """ ThrowOnInvalidState(state: WebSocketState, *validStates: Array[WebSocketState]) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CloseStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CloseStatus(self: WebSocket) -> Nullable[WebSocketCloseStatus]

"""

    CloseStatusDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CloseStatusDescription(self: WebSocket) -> str

"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: State(self: WebSocket) -> WebSocketState

"""

    SubProtocol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubProtocol(self: WebSocket) -> str

"""


    DefaultKeepAliveInterval = None


class ClientWebSocket(WebSocket, IDisposable):
    """ ClientWebSocket() """
    def Abort(self):
        """ Abort(self: ClientWebSocket) """
        pass

    def CloseAsync(self, closeStatus, statusDescription, cancellationToken):
        """ CloseAsync(self: ClientWebSocket, closeStatus: WebSocketCloseStatus, statusDescription: str, cancellationToken: CancellationToken) -> Task """
        pass

    def CloseOutputAsync(self, closeStatus, statusDescription, cancellationToken):
        """ CloseOutputAsync(self: ClientWebSocket, closeStatus: WebSocketCloseStatus, statusDescription: str, cancellationToken: CancellationToken) -> Task """
        pass

    def ConnectAsync(self, uri, cancellationToken):
        """ ConnectAsync(self: ClientWebSocket, uri: Uri, cancellationToken: CancellationToken) -> Task """
        pass

    def Dispose(self):
        """ Dispose(self: ClientWebSocket) """
        pass

    def ReceiveAsync(self, buffer, cancellationToken):
        """ ReceiveAsync(self: ClientWebSocket, buffer: ArraySegment[Byte], cancellationToken: CancellationToken) -> Task[WebSocketReceiveResult] """
        pass

    def SendAsync(self, buffer, messageType, endOfMessage, cancellationToken):
        """ SendAsync(self: ClientWebSocket, buffer: ArraySegment[Byte], messageType: WebSocketMessageType, endOfMessage: bool, cancellationToken: CancellationToken) -> Task """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CloseStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CloseStatus(self: ClientWebSocket) -> Nullable[WebSocketCloseStatus]

"""

    CloseStatusDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CloseStatusDescription(self: ClientWebSocket) -> str

"""

    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Options(self: ClientWebSocket) -> ClientWebSocketOptions

"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: State(self: ClientWebSocket) -> WebSocketState

"""

    SubProtocol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubProtocol(self: ClientWebSocket) -> str

"""



class ClientWebSocketOptions(object):
    # no doc
    def AddSubProtocol(self, subProtocol):
        """ AddSubProtocol(self: ClientWebSocketOptions, subProtocol: str) """
        pass

    def SetBuffer(self, receiveBufferSize, sendBufferSize, buffer=None):
        """ SetBuffer(self: ClientWebSocketOptions, receiveBufferSize: int, sendBufferSize: int, buffer: ArraySegment[Byte])SetBuffer(self: ClientWebSocketOptions, receiveBufferSize: int, sendBufferSize: int) """
        pass

    def SetRequestHeader(self, headerName, headerValue):
        """ SetRequestHeader(self: ClientWebSocketOptions, headerName: str, headerValue: str) """
        pass

    ClientCertificates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClientCertificates(self: ClientWebSocketOptions) -> X509CertificateCollection

Set: ClientCertificates(self: ClientWebSocketOptions) = value
"""

    Cookies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cookies(self: ClientWebSocketOptions) -> CookieContainer

Set: Cookies(self: ClientWebSocketOptions) = value
"""

    Credentials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Credentials(self: ClientWebSocketOptions) -> ICredentials

Set: Credentials(self: ClientWebSocketOptions) = value
"""

    KeepAliveInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeepAliveInterval(self: ClientWebSocketOptions) -> TimeSpan

Set: KeepAliveInterval(self: ClientWebSocketOptions) = value
"""

    Proxy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Proxy(self: ClientWebSocketOptions) -> IWebProxy

Set: Proxy(self: ClientWebSocketOptions) = value
"""

    UseDefaultCredentials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseDefaultCredentials(self: ClientWebSocketOptions) -> bool

Set: UseDefaultCredentials(self: ClientWebSocketOptions) = value
"""



class WebSocketContext(object):
    # no doc
    CookieCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CookieCollection(self: WebSocketContext) -> CookieCollection

"""

    Headers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Headers(self: WebSocketContext) -> NameValueCollection

"""

    IsAuthenticated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAuthenticated(self: WebSocketContext) -> bool

"""

    IsLocal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLocal(self: WebSocketContext) -> bool

"""

    IsSecureConnection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSecureConnection(self: WebSocketContext) -> bool

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Origin(self: WebSocketContext) -> str

"""

    RequestUri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RequestUri(self: WebSocketContext) -> Uri

"""

    SecWebSocketKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecWebSocketKey(self: WebSocketContext) -> str

"""

    SecWebSocketProtocols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecWebSocketProtocols(self: WebSocketContext) -> IEnumerable[str]

"""

    SecWebSocketVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecWebSocketVersion(self: WebSocketContext) -> str

"""

    User = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: User(self: WebSocketContext) -> IPrincipal

"""

    WebSocket = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WebSocket(self: WebSocketContext) -> WebSocket

"""



class HttpListenerWebSocketContext(WebSocketContext):
    # no doc
    CookieCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CookieCollection(self: HttpListenerWebSocketContext) -> CookieCollection

"""

    Headers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Headers(self: HttpListenerWebSocketContext) -> NameValueCollection

"""

    IsAuthenticated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAuthenticated(self: HttpListenerWebSocketContext) -> bool

"""

    IsLocal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLocal(self: HttpListenerWebSocketContext) -> bool

"""

    IsSecureConnection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSecureConnection(self: HttpListenerWebSocketContext) -> bool

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Origin(self: HttpListenerWebSocketContext) -> str

"""

    RequestUri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RequestUri(self: HttpListenerWebSocketContext) -> Uri

"""

    SecWebSocketKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecWebSocketKey(self: HttpListenerWebSocketContext) -> str

"""

    SecWebSocketProtocols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecWebSocketProtocols(self: HttpListenerWebSocketContext) -> IEnumerable[str]

"""

    SecWebSocketVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecWebSocketVersion(self: HttpListenerWebSocketContext) -> str

"""

    User = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: User(self: HttpListenerWebSocketContext) -> IPrincipal

"""

    WebSocket = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WebSocket(self: HttpListenerWebSocketContext) -> WebSocket

"""



class WebSocketCloseStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum WebSocketCloseStatus, values: Empty (1005), EndpointUnavailable (1001), InternalServerError (1011), InvalidMessageType (1003), InvalidPayloadData (1007), MandatoryExtension (1010), MessageTooBig (1009), NormalClosure (1000), PolicyViolation (1008), ProtocolError (1002) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Empty = None
    EndpointUnavailable = None
    InternalServerError = None
    InvalidMessageType = None
    InvalidPayloadData = None
    MandatoryExtension = None
    MessageTooBig = None
    NormalClosure = None
    PolicyViolation = None
    ProtocolError = None
    value__ = None


class WebSocketError(Enum, IComparable, IFormattable, IConvertible):
    """ enum WebSocketError, values: ConnectionClosedPrematurely (8), Faulted (2), HeaderError (7), InvalidMessageType (1), InvalidState (9), NativeError (3), NotAWebSocket (4), Success (0), UnsupportedProtocol (6), UnsupportedVersion (5) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ConnectionClosedPrematurely = None
    Faulted = None
    HeaderError = None
    InvalidMessageType = None
    InvalidState = None
    NativeError = None
    NotAWebSocket = None
    Success = None
    UnsupportedProtocol = None
    UnsupportedVersion = None
    value__ = None


class WebSocketException(Win32Exception, ISerializable, _Exception):
    """
    WebSocketException()
    WebSocketException(error: WebSocketError)
    WebSocketException(error: WebSocketError, message: str)
    WebSocketException(error: WebSocketError, innerException: Exception)
    WebSocketException(error: WebSocketError, message: str, innerException: Exception)
    WebSocketException(nativeError: int)
    WebSocketException(nativeError: int, message: str)
    WebSocketException(nativeError: int, innerException: Exception)
    WebSocketException(error: WebSocketError, nativeError: int)
    WebSocketException(error: WebSocketError, nativeError: int, message: str)
    WebSocketException(error: WebSocketError, nativeError: int, innerException: Exception)
    WebSocketException(error: WebSocketError, nativeError: int, message: str, innerException: Exception)
    WebSocketException(message: str)
    WebSocketException(message: str, innerException: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: WebSocketException, info: SerializationInfo, context: StreamingContext) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, error: WebSocketError)
        __new__(cls: type, error: WebSocketError, message: str)
        __new__(cls: type, error: WebSocketError, innerException: Exception)
        __new__(cls: type, error: WebSocketError, message: str, innerException: Exception)
        __new__(cls: type, nativeError: int)
        __new__(cls: type, nativeError: int, message: str)
        __new__(cls: type, nativeError: int, innerException: Exception)
        __new__(cls: type, error: WebSocketError, nativeError: int)
        __new__(cls: type, error: WebSocketError, nativeError: int, message: str)
        __new__(cls: type, error: WebSocketError, nativeError: int, innerException: Exception)
        __new__(cls: type, error: WebSocketError, nativeError: int, message: str, innerException: Exception)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ErrorCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorCode(self: WebSocketException) -> int

"""

    WebSocketErrorCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WebSocketErrorCode(self: WebSocketException) -> WebSocketError

"""



class WebSocketMessageType(Enum, IComparable, IFormattable, IConvertible):
    """ enum WebSocketMessageType, values: Binary (1), Close (2), Text (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Binary = None
    Close = None
    Text = None
    value__ = None


class WebSocketReceiveResult(object):
    """
    WebSocketReceiveResult(count: int, messageType: WebSocketMessageType, endOfMessage: bool)
    WebSocketReceiveResult(count: int, messageType: WebSocketMessageType, endOfMessage: bool, closeStatus: Nullable[WebSocketCloseStatus], closeStatusDescription: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, count, messageType, endOfMessage, closeStatus=None, closeStatusDescription=None):
        """
        __new__(cls: type, count: int, messageType: WebSocketMessageType, endOfMessage: bool)
        __new__(cls: type, count: int, messageType: WebSocketMessageType, endOfMessage: bool, closeStatus: Nullable[WebSocketCloseStatus], closeStatusDescription: str)
        """
        pass

    CloseStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CloseStatus(self: WebSocketReceiveResult) -> Nullable[WebSocketCloseStatus]

"""

    CloseStatusDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CloseStatusDescription(self: WebSocketReceiveResult) -> str

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: WebSocketReceiveResult) -> int

"""

    EndOfMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndOfMessage(self: WebSocketReceiveResult) -> bool

"""

    MessageType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MessageType(self: WebSocketReceiveResult) -> WebSocketMessageType

"""



class WebSocketState(Enum, IComparable, IFormattable, IConvertible):
    """ enum WebSocketState, values: Aborted (6), Closed (5), CloseReceived (4), CloseSent (3), Connecting (1), None (0), Open (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Aborted = None
    Closed = None
    CloseReceived = None
    CloseSent = None
    Connecting = None
    None = None
    Open = None
    value__ = None


