# encoding: utf-8
# module System.Net.Sockets calls itself Sockets
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class AddressFamily(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the addressing scheme that an instance of the System.Net.Sockets.Socket class can use.
    
    enum AddressFamily, values: AppleTalk (16), Atm (22), Banyan (21), Ccitt (10), Chaos (5), Cluster (24), DataKit (9), DataLink (13), DecNet (12), Ecma (8), FireFox (19), HyperChannel (15), Ieee12844 (25), ImpLink (3), InterNetwork (2), InterNetworkV6 (23), Ipx (6), Irda (26), Iso (7), Lat (14), Max (29), NetBios (17), NetworkDesigners (28), NS (6), Osi (7), Pup (4), Sna (11), Unix (1), Unknown (-1), Unspecified (0), VoiceView (18)
    """
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

    AppleTalk = None
    Atm = None
    Banyan = None
    Ccitt = None
    Chaos = None
    Cluster = None
    DataKit = None
    DataLink = None
    DecNet = None
    Ecma = None
    FireFox = None
    HyperChannel = None
    Ieee12844 = None
    ImpLink = None
    InterNetwork = None
    InterNetworkV6 = None
    Ipx = None
    Irda = None
    Iso = None
    Lat = None
    Max = None
    NetBios = None
    NetworkDesigners = None
    NS = None
    Osi = None
    Pup = None
    Sna = None
    Unix = None
    Unknown = None
    Unspecified = None
    value__ = None
    VoiceView = None


class IOControlCode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the IO control codes supported by the System.Net.Sockets.Socket.IOControl(System.Int32,System.Byte[],System.Byte[]) method.
    
    enum IOControlCode, values: AbsorbRouterAlert (2550136837), AddMulticastGroupOnInterface (2550136842), AddressListChange (671088663), AddressListQuery (1207959574), AddressListSort (3355443225), AssociateHandle (2281701377), AsyncIO (2147772029), BindToInterface (2550136840), DataToRead (1074030207), DeleteMulticastGroupFromInterface (2550136843), EnableCircularQueuing (671088642), Flush (671088644), GetBroadcastAddress (1207959557), GetExtensionFunctionPointer (3355443206), GetGroupQos (3355443208), GetQos (3355443207), KeepAliveValues (2550136836), LimitBroadcasts (2550136839), MulticastInterface (2550136841), MulticastScope (2281701386), MultipointLoopback (2281701385), NamespaceChange (2281701401), NonBlockingIO (2147772030), OobDataRead (1074033415), QueryTargetPnpHandle (1207959576), ReceiveAll (2550136833), ReceiveAllIgmpMulticast (2550136835), ReceiveAllMulticast (2550136834), RoutingInterfaceChange (2281701397), RoutingInterfaceQuery (3355443220), SetGroupQos (2281701388), SetQos (2281701387), TranslateHandle (3355443213), UnicastInterface (2550136838)
    """
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

    AbsorbRouterAlert = None
    AddMulticastGroupOnInterface = None
    AddressListChange = None
    AddressListQuery = None
    AddressListSort = None
    AssociateHandle = None
    AsyncIO = None
    BindToInterface = None
    DataToRead = None
    DeleteMulticastGroupFromInterface = None
    EnableCircularQueuing = None
    Flush = None
    GetBroadcastAddress = None
    GetExtensionFunctionPointer = None
    GetGroupQos = None
    GetQos = None
    KeepAliveValues = None
    LimitBroadcasts = None
    MulticastInterface = None
    MulticastScope = None
    MultipointLoopback = None
    NamespaceChange = None
    NonBlockingIO = None
    OobDataRead = None
    QueryTargetPnpHandle = None
    ReceiveAll = None
    ReceiveAllIgmpMulticast = None
    ReceiveAllMulticast = None
    RoutingInterfaceChange = None
    RoutingInterfaceQuery = None
    SetGroupQos = None
    SetQos = None
    TranslateHandle = None
    UnicastInterface = None
    value__ = None


class IPPacketInformation(object):
    """ Presents the packet information from a call to System.Net.Sockets.Socket.ReceiveMessageFrom(System.Byte[],System.Int32,System.Int32,System.Net.Sockets.SocketFlags@,System.Net.EndPoint@,System.Net.Sockets.IPPacketInformation@) or System.Net.Sockets.Socket.EndReceiveMessageFrom(System.IAsyncResult,System.Net.Sockets.SocketFlags@,System.Net.EndPoint@,System.Net.Sockets.IPPacketInformation@). """
    def Equals(self, comparand):
        """
        Equals(self: IPPacketInformation, comparand: object) -> bool
        
            Returns a value that indicates whether this instance is equal to a specified object.
        
            comparand: The object to compare with this instance.
            Returns: true if comparand is an instance of System.Net.Sockets.IPPacketInformation and equals the value 
             of the instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: IPPacketInformation) -> int
        
            Returns the hash code for this instance.
            Returns: An Int32 hash code.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the origin information of the packet that was received as a result of calling the System.Net.Sockets.Socket.ReceiveMessageFrom(System.Byte[],System.Int32,System.Int32,System.Net.Sockets.SocketFlags@,System.Net.EndPoint@,System.Net.Sockets.IPPacketInformation@) method or System.Net.Sockets.Socket.EndReceiveMessageFrom(System.IAsyncResult,System.Net.Sockets.SocketFlags@,System.Net.EndPoint@,System.Net.Sockets.IPPacketInformation@) method.

Get: Address(self: IPPacketInformation) -> IPAddress

"""

    Interface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the network interface information that is associated with a call to System.Net.Sockets.Socket.ReceiveMessageFrom(System.Byte[],System.Int32,System.Int32,System.Net.Sockets.SocketFlags@,System.Net.EndPoint@,System.Net.Sockets.IPPacketInformation@) or System.Net.Sockets.Socket.EndReceiveMessageFrom(System.IAsyncResult,System.Net.Sockets.SocketFlags@,System.Net.EndPoint@,System.Net.Sockets.IPPacketInformation@).

Get: Interface(self: IPPacketInformation) -> int

"""



class IPProtectionLevel(Enum, IComparable, IFormattable, IConvertible):
    """
    A value that enables restriction of an IPv6 socket to a specified scope, such as addresses with the same link local or site local prefix.
    
    enum IPProtectionLevel, values: EdgeRestricted (20), Restricted (30), Unrestricted (10), Unspecified (-1)
    """
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

    EdgeRestricted = None
    Restricted = None
    Unrestricted = None
    Unspecified = None
    value__ = None


class IPv6MulticastOption(object):
    """
    Contains option values for joining an IPv6 multicast group.
    
    IPv6MulticastOption(group: IPAddress, ifindex: Int64)
    IPv6MulticastOption(group: IPAddress)
    """
    @staticmethod # known case of __new__
    def __new__(self, group, ifindex=None):
        """
        __new__(cls: type, group: IPAddress, ifindex: Int64)
        __new__(cls: type, group: IPAddress)
        """
        pass

    Group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the IP address of a multicast group.

Get: Group(self: IPv6MulticastOption) -> IPAddress

Set: Group(self: IPv6MulticastOption) = value
"""

    InterfaceIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the interface index that is associated with a multicast group.

Get: InterfaceIndex(self: IPv6MulticastOption) -> Int64

Set: InterfaceIndex(self: IPv6MulticastOption) = value
"""



class LingerOption(object):
    """
    Specifies whether a System.Net.Sockets.Socket will remain connected after a call to the System.Net.Sockets.Socket.Close or System.Net.Sockets.TcpClient.Close methods and the length of time it will remain connected, if data remains to be sent.
    
    LingerOption(enable: bool, seconds: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, enable, seconds):
        """ __new__(cls: type, enable: bool, seconds: int) """
        pass

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether to linger after the System.Net.Sockets.Socket is closed.

Get: Enabled(self: LingerOption) -> bool

Set: Enabled(self: LingerOption) = value
"""

    LingerTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the amount of time to remain connected after calling the System.Net.Sockets.Socket.Close method if data remains to be sent.

Get: LingerTime(self: LingerOption) -> int

Set: LingerTime(self: LingerOption) = value
"""



class MulticastOption(object):
    """
    Contains System.Net.IPAddress values used to join and drop multicast groups.
    
    MulticastOption(group: IPAddress, mcint: IPAddress)
    MulticastOption(group: IPAddress, interfaceIndex: int)
    MulticastOption(group: IPAddress)
    """
    @staticmethod # known case of __new__
    def __new__(self, group, *__args):
        """
        __new__(cls: type, group: IPAddress, mcint: IPAddress)
        __new__(cls: type, group: IPAddress, interfaceIndex: int)
        __new__(cls: type, group: IPAddress)
        """
        pass

    Group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the IP address of a multicast group.

Get: Group(self: MulticastOption) -> IPAddress

Set: Group(self: MulticastOption) = value
"""

    InterfaceIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the index of the interface that is used to send and receive multicast packets.

Get: InterfaceIndex(self: MulticastOption) -> int

Set: InterfaceIndex(self: MulticastOption) = value
"""

    LocalAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the local address associated with a multicast group.

Get: LocalAddress(self: MulticastOption) -> IPAddress

Set: LocalAddress(self: MulticastOption) = value
"""



class NetworkStream(Stream, IDisposable):
    """
    Provides the underlying stream of data for network access.
    
    NetworkStream(socket: Socket)
    NetworkStream(socket: Socket, ownsSocket: bool)
    NetworkStream(socket: Socket, access: FileAccess)
    NetworkStream(socket: Socket, access: FileAccess, ownsSocket: bool)
    """
    def BeginRead(self, buffer, offset, size, callback, state):
        """
        BeginRead(self: NetworkStream, buffer: Array[Byte], offset: int, size: int, callback: AsyncCallback, state: object) -> IAsyncResult
        
            Begins an asynchronous read from the System.Net.Sockets.NetworkStream.
        
            buffer: An array of type System.Byte that is the location in memory to store data read from the 
             System.Net.Sockets.NetworkStream.
        
            offset: The location in buffer to begin storing the data.
            size: The number of bytes to read from the System.Net.Sockets.NetworkStream.
            callback: The System.AsyncCallback delegate that is executed when 
             System.Net.Sockets.NetworkStream.BeginRead(System.Byte[],System.Int32,System.Int32,System.AsyncCa
             llback,System.Object) completes.
        
            state: An object that contains any additional user-defined data.
            Returns: An System.IAsyncResult that represents the asynchronous call.
        """
        pass

    def BeginWrite(self, buffer, offset, size, callback, state):
        """
        BeginWrite(self: NetworkStream, buffer: Array[Byte], offset: int, size: int, callback: AsyncCallback, state: object) -> IAsyncResult
        
            Begins an asynchronous write to a stream.
        
            buffer: An array of type System.Byte that contains the data to write to the 
             System.Net.Sockets.NetworkStream.
        
            offset: The location in buffer to begin sending the data.
            size: The number of bytes to write to the System.Net.Sockets.NetworkStream.
            callback: The System.AsyncCallback delegate that is executed when 
             System.Net.Sockets.NetworkStream.BeginWrite(System.Byte[],System.Int32,System.Int32,System.AsyncC
             allback,System.Object) completes.
        
            state: An object that contains any additional user-defined data.
            Returns: An System.IAsyncResult that represents the asynchronous call.
        """
        pass

    def Close(self, timeout=None):
        """
        Close(self: NetworkStream, timeout: int)
            Closes the System.Net.Sockets.NetworkStream after waiting the specified time to allow data to be 
             sent.
        
        
            timeout: A 32-bit signed integer that specifies the number of milliseconds to wait to send any remaining 
             data before closing.
        """
        pass

    def CreateWaitHandle(self, *args): #cannot find CLR method
        """
        CreateWaitHandle(self: Stream) -> WaitHandle
        
            Allocates a System.Threading.WaitHandle object.
            Returns: A reference to the allocated WaitHandle.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: NetworkStream, disposing: bool)
            Releases the unmanaged resources used by the System.Net.Sockets.NetworkStream and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def EndRead(self, asyncResult):
        """
        EndRead(self: NetworkStream, asyncResult: IAsyncResult) -> int
        
            Handles the end of an asynchronous read.
        
            asyncResult: An System.IAsyncResult that represents an asynchronous call.
            Returns: The number of bytes read from the System.Net.Sockets.NetworkStream.
        """
        pass

    def EndWrite(self, asyncResult):
        """
        EndWrite(self: NetworkStream, asyncResult: IAsyncResult)
            Handles the end of an asynchronous write.
        
            asyncResult: The System.IAsyncResult that represents the asynchronous call.
        """
        pass

    def Flush(self):
        """
        Flush(self: NetworkStream)
            Flushes data from the stream. This method is reserved for future use.
        """
        pass

    def FlushAsync(self, cancellationToken=None):
        """ FlushAsync(self: NetworkStream, cancellationToken: CancellationToken) -> Task """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def ObjectInvariant(self, *args): #cannot find CLR method
        """
        ObjectInvariant(self: Stream)
            Provides support for a System.Diagnostics.Contracts.Contract.
        """
        pass

    def Read(self, buffer, offset, size):
        """
        Read(self: NetworkStream, offset: int, size: int) -> (int, Array[Byte])
        
            Reads data from the System.Net.Sockets.NetworkStream.
        
            offset: The location in buffer to begin storing the data to.
            size: The number of bytes to read from the System.Net.Sockets.NetworkStream.
            Returns: The number of bytes read from the System.Net.Sockets.NetworkStream.
        """
        pass

    def Seek(self, offset, origin):
        """
        Seek(self: NetworkStream, offset: Int64, origin: SeekOrigin) -> Int64
        
            Sets the current position of the stream to the given value. This method is not currently 
             supported and always throws a System.NotSupportedException.
        
        
            offset: This parameter is not used.
            origin: This parameter is not used.
            Returns: The position in the stream.
        """
        pass

    def SetLength(self, value):
        """
        SetLength(self: NetworkStream, value: Int64)
            Sets the length of the stream. This method always throws a System.NotSupportedException.
        
            value: This parameter is not used.
        """
        pass

    def Write(self, buffer, offset, size):
        """
        Write(self: NetworkStream, buffer: Array[Byte], offset: int, size: int)
            Writes data to the System.Net.Sockets.NetworkStream.
        
            buffer: An array of type System.Byte that contains the data to write to the 
             System.Net.Sockets.NetworkStream.
        
            offset: The location in buffer from which to start writing data.
            size: The number of bytes to write to the System.Net.Sockets.NetworkStream.
        """
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

    @staticmethod # known case of __new__
    def __new__(self, socket, *__args):
        """
        __new__(cls: type, socket: Socket)
        __new__(cls: type, socket: Socket, ownsSocket: bool)
        __new__(cls: type, socket: Socket, access: FileAccess)
        __new__(cls: type, socket: Socket, access: FileAccess, ownsSocket: bool)
        """
        pass

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Net.Sockets.NetworkStream supports reading.

Get: CanRead(self: NetworkStream) -> bool

"""

    CanSeek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the stream supports seeking. This property is not currently supported.This property always returns false.

Get: CanSeek(self: NetworkStream) -> bool

"""

    CanTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether timeout properties are usable for System.Net.Sockets.NetworkStream.

Get: CanTimeout(self: NetworkStream) -> bool

"""

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Net.Sockets.NetworkStream supports writing.

Get: CanWrite(self: NetworkStream) -> bool

"""

    DataAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether data is available on the System.Net.Sockets.NetworkStream to be read.

Get: DataAvailable(self: NetworkStream) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length of the data available on the stream. This property is not currently supported and always throws a System.NotSupportedException.

Get: Length(self: NetworkStream) -> Int64

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current position in the stream. This property is not currently supported and always throws a System.NotSupportedException.

Get: Position(self: NetworkStream) -> Int64

Set: Position(self: NetworkStream) = value
"""

    Readable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the System.Net.Sockets.NetworkStream can be read.

"""

    ReadTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the amount of time that a read operation blocks waiting for data.

Get: ReadTimeout(self: NetworkStream) -> int

Set: ReadTimeout(self: NetworkStream) = value
"""

    Socket = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the underlying System.Net.Sockets.Socket.

"""

    Writeable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Net.Sockets.NetworkStream is writable.

"""

    WriteTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the amount of time that a write operation blocks waiting for data.

Get: WriteTimeout(self: NetworkStream) -> int

Set: WriteTimeout(self: NetworkStream) = value
"""



class ProtocolFamily(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of protocol that an instance of the System.Net.Sockets.Socket class can use.
    
    enum ProtocolFamily, values: AppleTalk (16), Atm (22), Banyan (21), Ccitt (10), Chaos (5), Cluster (24), DataKit (9), DataLink (13), DecNet (12), Ecma (8), FireFox (19), HyperChannel (15), Ieee12844 (25), ImpLink (3), InterNetwork (2), InterNetworkV6 (23), Ipx (6), Irda (26), Iso (7), Lat (14), Max (29), NetBios (17), NetworkDesigners (28), NS (6), Osi (7), Pup (4), Sna (11), Unix (1), Unknown (-1), Unspecified (0), VoiceView (18)
    """
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

    AppleTalk = None
    Atm = None
    Banyan = None
    Ccitt = None
    Chaos = None
    Cluster = None
    DataKit = None
    DataLink = None
    DecNet = None
    Ecma = None
    FireFox = None
    HyperChannel = None
    Ieee12844 = None
    ImpLink = None
    InterNetwork = None
    InterNetworkV6 = None
    Ipx = None
    Irda = None
    Iso = None
    Lat = None
    Max = None
    NetBios = None
    NetworkDesigners = None
    NS = None
    Osi = None
    Pup = None
    Sna = None
    Unix = None
    Unknown = None
    Unspecified = None
    value__ = None
    VoiceView = None


class ProtocolType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the protocols that the System.Net.Sockets.Socket class supports.
    
    enum ProtocolType, values: Ggp (3), Icmp (1), IcmpV6 (58), Idp (22), Igmp (2), IP (0), IPSecAuthenticationHeader (51), IPSecEncapsulatingSecurityPayload (50), IPv4 (4), IPv6 (41), IPv6DestinationOptions (60), IPv6FragmentHeader (44), IPv6HopByHopOptions (0), IPv6NoNextHeader (59), IPv6RoutingHeader (43), Ipx (1000), ND (77), Pup (12), Raw (255), Spx (1256), SpxII (1257), Tcp (6), Udp (17), Unknown (-1), Unspecified (0)
    """
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

    Ggp = None
    Icmp = None
    IcmpV6 = None
    Idp = None
    Igmp = None
    IP = None
    IPSecAuthenticationHeader = None
    IPSecEncapsulatingSecurityPayload = None
    IPv4 = None
    IPv6 = None
    IPv6DestinationOptions = None
    IPv6FragmentHeader = None
    IPv6HopByHopOptions = None
    IPv6NoNextHeader = None
    IPv6RoutingHeader = None
    Ipx = None
    ND = None
    Pup = None
    Raw = None
    Spx = None
    SpxII = None
    Tcp = None
    Udp = None
    Unknown = None
    Unspecified = None
    value__ = None


class SelectMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines the polling modes for the System.Net.Sockets.Socket.Poll(System.Int32,System.Net.Sockets.SelectMode) method.
    
    enum SelectMode, values: SelectError (2), SelectRead (0), SelectWrite (1)
    """
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

    SelectError = None
    SelectRead = None
    SelectWrite = None
    value__ = None


class SendPacketsElement(object):
    """
    Represents an element in a System.Net.Sockets.SendPacketsElement array.
    
    SendPacketsElement(filepath: str)
    SendPacketsElement(filepath: str, offset: int, count: int)
    SendPacketsElement(filepath: str, offset: int, count: int, endOfPacket: bool)
    SendPacketsElement(buffer: Array[Byte])
    SendPacketsElement(buffer: Array[Byte], offset: int, count: int)
    SendPacketsElement(buffer: Array[Byte], offset: int, count: int, endOfPacket: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, filepath: str)
        __new__(cls: type, filepath: str, offset: int, count: int)
        __new__(cls: type, filepath: str, offset: int, count: int, endOfPacket: bool)
        __new__(cls: type, buffer: Array[Byte])
        __new__(cls: type, buffer: Array[Byte], offset: int, count: int)
        __new__(cls: type, buffer: Array[Byte], offset: int, count: int, endOfPacket: bool)
        """
        pass

    Buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the buffer to be sent if the System.Net.Sockets.SendPacketsElement class was initialized with a buffer parameter.

Get: Buffer(self: SendPacketsElement) -> Array[Byte]

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the count of bytes to be sent.

Get: Count(self: SendPacketsElement) -> int

"""

    EndOfPacket = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that indicates if this element should not be combined with the next element in a single send request from the sockets layer to the transport.

Get: EndOfPacket(self: SendPacketsElement) -> bool

"""

    FilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the filename of the file to send if the System.Net.Sockets.SendPacketsElement class was initialized with a filepath parameter.

Get: FilePath(self: SendPacketsElement) -> str

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the offset, in bytes, from the beginning of the data buffer or file to the location in the buffer or file to start sending the data.

Get: Offset(self: SendPacketsElement) -> int

"""



class Socket(object, IDisposable):
    """
    Implements the Berkeley sockets interface.
    
    Socket(socketType: SocketType, protocolType: ProtocolType)
    Socket(addressFamily: AddressFamily, socketType: SocketType, protocolType: ProtocolType)
    Socket(socketInformation: SocketInformation)
    """
    def Accept(self):
        """
        Accept(self: Socket) -> Socket
        
            Creates a new System.Net.Sockets.Socket for a newly created connection.
            Returns: A System.Net.Sockets.Socket for a newly created connection.
        """
        pass

    def AcceptAsync(self, e):
        """
        AcceptAsync(self: Socket, e: SocketAsyncEventArgs) -> bool
        
            Begins an asynchronous operation to accept an incoming connection attempt.
        
            e: The System.Net.Sockets.SocketAsyncEventArgs object to use for this asynchronous socket operation.
            Returns: Returns true if the I/O operation is pending. The 
             System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will be raised upon 
             completion of the operation.Returns false if the I/O operation completed synchronously. The 
             System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will not be raised 
             and the e object passed as a parameter may be examined immediately after the method call returns 
             to retrieve the result of the operation.
        """
        pass

    def BeginAccept(self, *__args):
        """
        BeginAccept(self: Socket, acceptSocket: Socket, receiveSize: int, callback: AsyncCallback, state: object) -> IAsyncResult
        
            Begins an asynchronous operation to accept an incoming connection attempt from a specified 
             socket and receives the first block of data sent by the client application.
        
        
            acceptSocket: The accepted System.Net.Sockets.Socket object. This value may be null.
            receiveSize: The maximum number of bytes to receive.
            callback: The System.AsyncCallback delegate.
            state: An object that contains state information for this request.
            Returns: An System.IAsyncResult object that references the asynchronous System.Net.Sockets.Socket object 
             creation.
        
        BeginAccept(self: Socket, receiveSize: int, callback: AsyncCallback, state: object) -> IAsyncResult
        
            Begins an asynchronous operation to accept an incoming connection attempt and receives the first 
             block of data sent by the client application.
        
        
            receiveSize: The number of bytes to accept from the sender.
            callback: The System.AsyncCallback delegate.
            state: An object that contains state information for this request.
            Returns: An System.IAsyncResult that references the asynchronous System.Net.Sockets.Socket creation.
        BeginAccept(self: Socket, callback: AsyncCallback, state: object) -> IAsyncResult
        
            Begins an asynchronous operation to accept an incoming connection attempt.
        
            callback: The System.AsyncCallback delegate.
            state: An object that contains state information for this request.
            Returns: An System.IAsyncResult that references the asynchronous System.Net.Sockets.Socket creation.
        """
        pass

    def BeginConnect(self, *__args):
        """
        BeginConnect(self: Socket, address: IPAddress, port: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult
        
            Begins an asynchronous request for a remote host connection. The host is specified by an 
             System.Net.IPAddress and a port number.
        
        
            address: The System.Net.IPAddress of the remote host.
            port: The port number of the remote host.
            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the connect operation 
             is complete.
        
            state: A user-defined object that contains information about the connect operation. This object is 
             passed to the requestCallback delegate when the operation is complete.
        
            Returns: An System.IAsyncResult that references the asynchronous connection.
        BeginConnect(self: Socket, addresses: Array[IPAddress], port: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult
        
            Begins an asynchronous request for a remote host connection. The host is specified by an 
             System.Net.IPAddress array and a port number.
        
        
            addresses: At least one System.Net.IPAddress, designating the remote host.
            port: The port number of the remote host.
            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the connect operation 
             is complete.
        
            state: A user-defined object that contains information about the connect operation. This object is 
             passed to the requestCallback delegate when the operation is complete.
        
            Returns: An System.IAsyncResult that references the asynchronous connections.
        BeginConnect(self: Socket, remoteEP: EndPoint, callback: AsyncCallback, state: object) -> IAsyncResult
        
            Begins an asynchronous request for a remote host connection.
        
            remoteEP: An System.Net.EndPoint that represents the remote host.
            callback: The System.AsyncCallback delegate.
            state: An object that contains state information for this request.
            Returns: An System.IAsyncResult that references the asynchronous connection.
        BeginConnect(self: Socket, host: str, port: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult
        
            Begins an asynchronous request for a remote host connection. The host is specified by a host 
             name and a port number.
        
        
            host: The name of the remote host.
            port: The port number of the remote host.
            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the connect operation 
             is complete.
        
            state: A user-defined object that contains information about the connect operation. This object is 
             passed to the requestCallback delegate when the operation is complete.
        
            Returns: An System.IAsyncResult that references the asynchronous connection.
        """
        pass

    def BeginDisconnect(self, reuseSocket, callback, state):
        """
        BeginDisconnect(self: Socket, reuseSocket: bool, callback: AsyncCallback, state: object) -> IAsyncResult
        
            Begins an asynchronous request to disconnect from a remote endpoint.
        
            reuseSocket: true if this socket can be reused after the connection is closed; otherwise, false.
            callback: The System.AsyncCallback delegate.
            state: An object that contains state information for this request.
            Returns: An System.IAsyncResult object that references the asynchronous operation.
        """
        pass

    def BeginReceive(self, *__args):
        """
        BeginReceive(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginReceive(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> (IAsyncResult, SocketError)
        BeginReceive(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> IAsyncResult
        
            Begins to asynchronously receive data from a connected System.Net.Sockets.Socket.
        
            buffer: An array of type System.Byte that is the storage location for the received data.
            offset: The zero-based position in the buffer parameter at which to store the received data.
            size: The number of bytes to receive.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            callback: An System.AsyncCallback delegate that references the method to invoke when the operation is 
             complete.
        
            state: A user-defined object that contains information about the receive operation. This object is 
             passed to the System.Net.Sockets.Socket.EndReceive(System.IAsyncResult) delegate when the 
             operation is complete.
        
            Returns: An System.IAsyncResult that references the asynchronous read.
        BeginReceive(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> (IAsyncResult, SocketError)
        
            Begins to asynchronously receive data from a connected System.Net.Sockets.Socket.
        
            buffer: An array of type System.Byte that is the storage location for the received data.
            offset: The location in buffer to store the received data.
            size: The number of bytes to receive.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            callback: An System.AsyncCallback delegate that references the method to invoke when the operation is 
             complete.
        
            state: A user-defined object that contains information about the receive operation. This object is 
             passed to the System.Net.Sockets.Socket.EndReceive(System.IAsyncResult) delegate when the 
             operation is complete.
        
            Returns: An System.IAsyncResult that references the asynchronous read.
        """
        pass

    def BeginReceiveFrom(self, buffer, offset, size, socketFlags, remoteEP, callback, state):
        """
        BeginReceiveFrom(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, remoteEP: EndPoint, callback: AsyncCallback, state: object) -> (IAsyncResult, EndPoint)
        
            Begins to asynchronously receive data from a specified network device.
        
            buffer: An array of type System.Byte that is the storage location for the received data.
            offset: The zero-based position in the buffer parameter at which to store the data.
            size: The number of bytes to receive.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            remoteEP: An System.Net.EndPoint that represents the source of the data.
            callback: The System.AsyncCallback delegate.
            state: An object that contains state information for this request.
            Returns: An System.IAsyncResult that references the asynchronous read.
        """
        pass

    def BeginReceiveMessageFrom(self, buffer, offset, size, socketFlags, remoteEP, callback, state):
        """
        BeginReceiveMessageFrom(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, remoteEP: EndPoint, callback: AsyncCallback, state: object) -> (IAsyncResult, EndPoint)
        
            Begins to asynchronously receive the specified number of bytes of data into the specified 
             location of the data buffer, using the specified System.Net.Sockets.SocketFlags, and stores the 
             endpoint and packet information..
        
        
            buffer: An array of type System.Byte that is the storage location for the received data.
            offset: The zero-based position in the buffer parameter at which to store the data.
            size: The number of bytes to receive.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            remoteEP: An System.Net.EndPoint that represents the source of the data.
            callback: The System.AsyncCallback delegate.
            state: An object that contains state information for this request.
            Returns: An System.IAsyncResult that references the asynchronous read.
        """
        pass

    def BeginSend(self, *__args):
        """
        BeginSend(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginSend(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> (IAsyncResult, SocketError)
        BeginSend(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> IAsyncResult
        
            Sends data asynchronously to a connected System.Net.Sockets.Socket.
        
            buffer: An array of type System.Byte that contains the data to send.
            offset: The zero-based position in the buffer parameter at which to begin sending data.
            size: The number of bytes to send.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            callback: The System.AsyncCallback delegate.
            state: An object that contains state information for this request.
            Returns: An System.IAsyncResult that references the asynchronous send.
        BeginSend(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> (IAsyncResult, SocketError)
        
            Sends data asynchronously to a connected System.Net.Sockets.Socket.
        
            buffer: An array of type System.Byte that contains the data to send.
            offset: The zero-based position in the buffer parameter at which to begin sending data.
            size: The number of bytes to send.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            callback: The System.AsyncCallback delegate.
            state: An object that contains state information for this request.
            Returns: An System.IAsyncResult that references the asynchronous send.
        """
        pass

    def BeginSendFile(self, fileName, *__args):
        """
        BeginSendFile(self: Socket, fileName: str, preBuffer: Array[Byte], postBuffer: Array[Byte], flags: TransmitFileOptions, callback: AsyncCallback, state: object) -> IAsyncResult
        
            Sends a file and buffers of data asynchronously to a connected System.Net.Sockets.Socket object.
        
            fileName: A string that contains the path and name of the file to be sent. This parameter can be null.
            preBuffer: A System.Byte array that contains data to be sent before the file is sent. This parameter can be 
             null.
        
            postBuffer: A System.Byte array that contains data to be sent after the file is sent. This parameter can be 
             null.
        
            flags: A bitwise combination of System.Net.Sockets.TransmitFileOptions values.
            callback: An System.AsyncCallback delegate to be invoked when this operation completes. This parameter can 
             be null.
        
            state: A user-defined object that contains state information for this request. This parameter can be 
             null.
        
            Returns: An System.IAsyncResult object that represents the asynchronous operation.
        BeginSendFile(self: Socket, fileName: str, callback: AsyncCallback, state: object) -> IAsyncResult
        
            Sends the file fileName to a connected System.Net.Sockets.Socket object using the 
             System.Net.Sockets.TransmitFileOptions.UseDefaultWorkerThread flag.
        
        
            fileName: A string that contains the path and name of the file to send. This parameter can be null.
            callback: The System.AsyncCallback delegate.
            state: An object that contains state information for this request.
            Returns: An System.IAsyncResult object that represents the asynchronous send.
        """
        pass

    def BeginSendTo(self, buffer, offset, size, socketFlags, remoteEP, callback, state):
        """
        BeginSendTo(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, remoteEP: EndPoint, callback: AsyncCallback, state: object) -> IAsyncResult
        
            Sends data asynchronously to a specific remote host.
        
            buffer: An array of type System.Byte that contains the data to send.
            offset: The zero-based position in buffer at which to begin sending data.
            size: The number of bytes to send.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            remoteEP: An System.Net.EndPoint that represents the remote device.
            callback: The System.AsyncCallback delegate.
            state: An object that contains state information for this request.
            Returns: An System.IAsyncResult that references the asynchronous send.
        """
        pass

    def Bind(self, localEP):
        """
        Bind(self: Socket, localEP: EndPoint)
            Associates a System.Net.Sockets.Socket with a local endpoint.
        
            localEP: The local System.Net.EndPoint to associate with the System.Net.Sockets.Socket.
        """
        pass

    @staticmethod
    def CancelConnectAsync(e):
        """
        CancelConnectAsync(e: SocketAsyncEventArgs)
            Cancels an asynchronous request for a remote host connection.
        
            e: The System.Net.Sockets.SocketAsyncEventArgs object used to request the connection to the remote 
             host by calling one of the 
             System.Net.Sockets.Socket.ConnectAsync(System.Net.Sockets.SocketType,System.Net.Sockets.ProtocolT
             ype,System.Net.Sockets.SocketAsyncEventArgs) methods.
        """
        pass

    def Close(self, timeout=None):
        """
        Close(self: Socket, timeout: int)
            Closes the System.Net.Sockets.Socket connection and releases all associated resources with a 
             specified timeout to allow queued data to be sent.
        
        
            timeout: Wait up to timeout seconds to send any remaining data, then close the socket.
        Close(self: Socket)
            Closes the System.Net.Sockets.Socket connection and releases all associated resources.
        """
        pass

    def Connect(self, *__args):
        """
        Connect(self: Socket, host: str, port: int)
            Establishes a connection to a remote host. The host is specified by a host name and a port 
             number.
        
        
            host: The name of the remote host.
            port: The port number of the remote host.
        Connect(self: Socket, addresses: Array[IPAddress], port: int)
            Establishes a connection to a remote host. The host is specified by an array of IP addresses and 
             a port number.
        
        
            addresses: The IP addresses of the remote host.
            port: The port number of the remote host.
        Connect(self: Socket, remoteEP: EndPoint)
            Establishes a connection to a remote host.
        
            remoteEP: An System.Net.EndPoint that represents the remote device.
        Connect(self: Socket, address: IPAddress, port: int)
            Establishes a connection to a remote host. The host is specified by an IP address and a port 
             number.
        
        
            address: The IP address of the remote host.
            port: The port number of the remote host.
        """
        pass

    def ConnectAsync(self, *__args):
        """
        ConnectAsync(socketType: SocketType, protocolType: ProtocolType, e: SocketAsyncEventArgs) -> bool
        
            Begins an asynchronous request for a remote host connection.
        
            socketType: One of the System.Net.Sockets.SocketType values.
            protocolType: One of the System.Net.Sockets.ProtocolType values.
            e: The System.Net.Sockets.SocketAsyncEventArgs object to use for this asynchronous socket operation.
            Returns: Returns true if the I/O operation is pending. The 
             System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will be raised upon 
             completion of the operation. Returns false if the I/O operation completed synchronously. In this 
             case, The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will not be 
             raised and the e object passed as a parameter may be examined immediately after the method call 
             returns to retrieve the result of the operation.
        
        ConnectAsync(self: Socket, e: SocketAsyncEventArgs) -> bool
        
            Begins an asynchronous request for a remote host connection.
        
            e: The System.Net.Sockets.SocketAsyncEventArgs object to use for this asynchronous socket operation.
            Returns: Returns true if the I/O operation is pending. The 
             System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will be raised upon 
             completion of the operation. Returns false if the I/O operation completed synchronously. In this 
             case, The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will not be 
             raised and the e object passed as a parameter may be examined immediately after the method call 
             returns to retrieve the result of the operation.
        """
        pass

    def Disconnect(self, reuseSocket):
        """
        Disconnect(self: Socket, reuseSocket: bool)
            Closes the socket connection and allows reuse of the socket.
        
            reuseSocket: true if this socket can be reused after the current connection is closed; otherwise, false.
        """
        pass

    def DisconnectAsync(self, e):
        """
        DisconnectAsync(self: Socket, e: SocketAsyncEventArgs) -> bool
        
            Begins an asynchronous request to disconnect from a remote endpoint.
        
            e: The System.Net.Sockets.SocketAsyncEventArgs object to use for this asynchronous socket operation.
            Returns: Returns true if the I/O operation is pending. The 
             System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will be raised upon 
             completion of the operation. Returns false if the I/O operation completed synchronously. In this 
             case, The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will not be 
             raised and the e object passed as a parameter may be examined immediately after the method call 
             returns to retrieve the result of the operation.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Socket)
            Releases all resources used by the current instance of the System.Net.Sockets.Socket class.
        """
        pass

    def DuplicateAndClose(self, targetProcessId):
        """
        DuplicateAndClose(self: Socket, targetProcessId: int) -> SocketInformation
        
            Duplicates the socket reference for the target process, and closes the socket for this process.
        
            targetProcessId: The ID of the target process where a duplicate of the socket reference is created.
            Returns: The socket reference to be passed to the target process.
        """
        pass

    def EndAccept(self, *__args):
        """
        EndAccept(self: Socket, asyncResult: IAsyncResult) -> (Socket, Array[Byte], int)
        
            Asynchronously accepts an incoming connection attempt and creates a new 
             System.Net.Sockets.Socket object to handle remote host communication. This method returns a 
             buffer that contains the initial data and the number of bytes transferred.
        
        
            asyncResult: An System.IAsyncResult object that stores state information for this asynchronous operation as 
             well as any user defined data.
        
            Returns: A System.Net.Sockets.Socket object to handle communication with the remote host.
        EndAccept(self: Socket, asyncResult: IAsyncResult) -> (Socket, Array[Byte])
        
            Asynchronously accepts an incoming connection attempt and creates a new 
             System.Net.Sockets.Socket object to handle remote host communication. This method returns a 
             buffer that contains the initial data transferred.
        
        
            asyncResult: An System.IAsyncResult object that stores state information for this asynchronous operation as 
             well as any user defined data.
        
            Returns: A System.Net.Sockets.Socket object to handle communication with the remote host.
        EndAccept(self: Socket, asyncResult: IAsyncResult) -> Socket
        
            Asynchronously accepts an incoming connection attempt and creates a new 
             System.Net.Sockets.Socket to handle remote host communication.
        
        
            asyncResult: An System.IAsyncResult that stores state information for this asynchronous operation as well as 
             any user defined data.
        
            Returns: A System.Net.Sockets.Socket to handle communication with the remote host.
        """
        pass

    def EndConnect(self, asyncResult):
        """
        EndConnect(self: Socket, asyncResult: IAsyncResult)
            Ends a pending asynchronous connection request.
        
            asyncResult: An System.IAsyncResult that stores state information and any user defined data for this 
             asynchronous operation.
        """
        pass

    def EndDisconnect(self, asyncResult):
        """
        EndDisconnect(self: Socket, asyncResult: IAsyncResult)
            Ends a pending asynchronous disconnect request.
        
            asyncResult: An System.IAsyncResult object that stores state information and any user-defined data for this 
             asynchronous operation.
        """
        pass

    def EndReceive(self, asyncResult, errorCode=None):
        """
        EndReceive(self: Socket, asyncResult: IAsyncResult) -> (int, SocketError)
        
            Ends a pending asynchronous read.
        
            asyncResult: An System.IAsyncResult that stores state information and any user defined data for this 
             asynchronous operation.
        
            Returns: The number of bytes received.
        EndReceive(self: Socket, asyncResult: IAsyncResult) -> int
        
            Ends a pending asynchronous read.
        
            asyncResult: An System.IAsyncResult that stores state information and any user defined data for this 
             asynchronous operation.
        
            Returns: The number of bytes received.
        """
        pass

    def EndReceiveFrom(self, asyncResult, endPoint):
        """
        EndReceiveFrom(self: Socket, asyncResult: IAsyncResult, endPoint: EndPoint) -> (int, EndPoint)
        
            Ends a pending asynchronous read from a specific endpoint.
        
            asyncResult: An System.IAsyncResult that stores state information and any user defined data for this 
             asynchronous operation.
        
            endPoint: The source System.Net.EndPoint.
            Returns: If successful, the number of bytes received. If unsuccessful, returns 0.
        """
        pass

    def EndReceiveMessageFrom(self, asyncResult, socketFlags, endPoint, ipPacketInformation):
        """
        EndReceiveMessageFrom(self: Socket, asyncResult: IAsyncResult, socketFlags: SocketFlags, endPoint: EndPoint) -> (int, SocketFlags, EndPoint, IPPacketInformation)
        
            Ends a pending asynchronous read from a specific endpoint. This method also reveals more 
             information about the packet than 
             System.Net.Sockets.Socket.EndReceiveFrom(System.IAsyncResult,System.Net.EndPoint@).
        
        
            asyncResult: An System.IAsyncResult that stores state information and any user defined data for this 
             asynchronous operation.
        
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values for the received packet.
            endPoint: The source System.Net.EndPoint.
            Returns: If successful, the number of bytes received. If unsuccessful, returns 0.
        """
        pass

    def EndSend(self, asyncResult, errorCode=None):
        """
        EndSend(self: Socket, asyncResult: IAsyncResult) -> (int, SocketError)
        
            Ends a pending asynchronous send.
        
            asyncResult: An System.IAsyncResult that stores state information for this asynchronous operation.
            Returns: If successful, the number of bytes sent to the System.Net.Sockets.Socket; otherwise, an invalid 
             System.Net.Sockets.Socket error.
        
        EndSend(self: Socket, asyncResult: IAsyncResult) -> int
        
            Ends a pending asynchronous send.
        
            asyncResult: An System.IAsyncResult that stores state information for this asynchronous operation.
            Returns: If successful, the number of bytes sent to the System.Net.Sockets.Socket; otherwise, an invalid 
             System.Net.Sockets.Socket error.
        """
        pass

    def EndSendFile(self, asyncResult):
        """
        EndSendFile(self: Socket, asyncResult: IAsyncResult)
            Ends a pending asynchronous send of a file.
        
            asyncResult: An System.IAsyncResult object that stores state information for this asynchronous operation.
        """
        pass

    def EndSendTo(self, asyncResult):
        """
        EndSendTo(self: Socket, asyncResult: IAsyncResult) -> int
        
            Ends a pending asynchronous send to a specific location.
        
            asyncResult: An System.IAsyncResult that stores state information and any user defined data for this 
             asynchronous operation.
        
            Returns: If successful, the number of bytes sent; otherwise, an invalid System.Net.Sockets.Socket error.
        """
        pass

    def GetSocketOption(self, optionLevel, optionName, *__args):
        """
        GetSocketOption(self: Socket, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionLength: int) -> Array[Byte]
        
            Returns the value of the specified System.Net.Sockets.Socket option in an array.
        
            optionLevel: One of the System.Net.Sockets.SocketOptionLevel values.
            optionName: One of the System.Net.Sockets.SocketOptionName values.
            optionLength: The length, in bytes, of the expected return value.
            Returns: An array of type System.Byte that contains the value of the socket option.
        GetSocketOption(self: Socket, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: Array[Byte])
            Returns the specified System.Net.Sockets.Socket option setting, represented as a byte array.
        
            optionLevel: One of the System.Net.Sockets.SocketOptionLevel values.
            optionName: One of the System.Net.Sockets.SocketOptionName values.
            optionValue: An array of type System.Byte that is to receive the option setting.
        GetSocketOption(self: Socket, optionLevel: SocketOptionLevel, optionName: SocketOptionName) -> object
        
            Returns the value of a specified System.Net.Sockets.Socket option, represented as an object.
        
            optionLevel: One of the System.Net.Sockets.SocketOptionLevel values.
            optionName: One of the System.Net.Sockets.SocketOptionName values.
            Returns: An object that represents the value of the option. When the optionName parameter is set to 
             System.Net.Sockets.SocketOptionName.Linger the return value is an instance of the 
             System.Net.Sockets.LingerOption class. When optionName is set to 
             System.Net.Sockets.SocketOptionName.AddMembership or 
             System.Net.Sockets.SocketOptionName.DropMembership, the return value is an instance of the 
             System.Net.Sockets.MulticastOption class. When optionName is any other value, the return value 
             is an integer.
        """
        pass

    def IOControl(self, ioControlCode, optionInValue, optionOutValue):
        """
        IOControl(self: Socket, ioControlCode: IOControlCode, optionInValue: Array[Byte], optionOutValue: Array[Byte]) -> int
        
            Sets low-level operating modes for the System.Net.Sockets.Socket using the 
             System.Net.Sockets.IOControlCode enumeration to specify control codes.
        
        
            ioControlCode: A System.Net.Sockets.IOControlCode value that specifies the control code of the operation to 
             perform.
        
            optionInValue: An array of type System.Byte that contains the input data required by the operation.
            optionOutValue: An array of type System.Byte that contains the output data returned by the operation.
            Returns: The number of bytes in the optionOutValue parameter.
        IOControl(self: Socket, ioControlCode: int, optionInValue: Array[Byte], optionOutValue: Array[Byte]) -> int
        
            Sets low-level operating modes for the System.Net.Sockets.Socket using numerical control codes.
        
            ioControlCode: An System.Int32 value that specifies the control code of the operation to perform.
            optionInValue: A System.Byte array that contains the input data required by the operation.
            optionOutValue: A System.Byte array that contains the output data returned by the operation.
            Returns: The number of bytes in the optionOutValue parameter.
        """
        pass

    def Listen(self, backlog):
        """
        Listen(self: Socket, backlog: int)
            Places a System.Net.Sockets.Socket in a listening state.
        
            backlog: The maximum length of the pending connections queue.
        """
        pass

    def Poll(self, microSeconds, mode):
        """
        Poll(self: Socket, microSeconds: int, mode: SelectMode) -> bool
        
            Determines the status of the System.Net.Sockets.Socket.
        
            microSeconds: The time to wait for a response, in microseconds.
            mode: One of the System.Net.Sockets.SelectMode values.
            Returns: The status of the System.Net.Sockets.Socket based on the polling mode value passed in the mode 
             parameter.Mode Return Value System.Net.Sockets.SelectMode.SelectReadtrue if 
             System.Net.Sockets.Socket.Listen(System.Int32) has been called and a connection is pending; -or- 
             true if data is available for reading; -or- true if the connection has been closed, reset, or 
             terminated; otherwise, returns false. System.Net.Sockets.SelectMode.SelectWritetrue, if 
             processing a System.Net.Sockets.Socket.Connect(System.Net.EndPoint), and the connection has 
             succeeded; -or- true if data can be sent; otherwise, returns false. 
             System.Net.Sockets.SelectMode.SelectErrortrue if processing a 
             System.Net.Sockets.Socket.Connect(System.Net.EndPoint) that does not block, and the connection 
             has failed; -or- true if System.Net.Sockets.SocketOptionName.OutOfBandInline is not set and 
             out-of-band data is available; otherwise, returns false.
        """
        pass

    def Receive(self, *__args):
        """
        Receive(self: Socket, buffers: IList[ArraySegment[Byte]]) -> int
        Receive(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags) -> (int, SocketError)
        
            Receives data from a bound System.Net.Sockets.Socket into a receive buffer, using the specified 
             System.Net.Sockets.SocketFlags.
        
        
            buffer: An array of type System.Byte that is the storage location for the received data.
            offset: The position in the buffer parameter to store the received data.
            size: The number of bytes to receive.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            Returns: The number of bytes received.
        Receive(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags) -> (int, SocketError)
        Receive(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags) -> int
        Receive(self: Socket, buffer: Array[Byte], socketFlags: SocketFlags) -> int
        
            Receives data from a bound System.Net.Sockets.Socket into a receive buffer, using the specified 
             System.Net.Sockets.SocketFlags.
        
        
            buffer: An array of type System.Byte that is the storage location for the received data.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            Returns: The number of bytes received.
        Receive(self: Socket, buffer: Array[Byte], size: int, socketFlags: SocketFlags) -> int
        
            Receives the specified number of bytes of data from a bound System.Net.Sockets.Socket into a 
             receive buffer, using the specified System.Net.Sockets.SocketFlags.
        
        
            buffer: An array of type System.Byte that is the storage location for the received data.
            size: The number of bytes to receive.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            Returns: The number of bytes received.
        Receive(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags) -> int
        
            Receives the specified number of bytes from a bound System.Net.Sockets.Socket into the specified 
             offset position of the receive buffer, using the specified System.Net.Sockets.SocketFlags.
        
        
            buffer: An array of type System.Byte that is the storage location for received data.
            offset: The location in buffer to store the received data.
            size: The number of bytes to receive.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            Returns: The number of bytes received.
        Receive(self: Socket, buffer: Array[Byte]) -> int
        
            Receives data from a bound System.Net.Sockets.Socket into a receive buffer.
        
            buffer: An array of type System.Byte that is the storage location for the received data.
            Returns: The number of bytes received.
        """
        pass

    def ReceiveAsync(self, e):
        """
        ReceiveAsync(self: Socket, e: SocketAsyncEventArgs) -> bool
        
            Begins an asynchronous request to receive data from a connected System.Net.Sockets.Socket object.
        
            e: The System.Net.Sockets.SocketAsyncEventArgs object to use for this asynchronous socket operation.
            Returns: Returns true if the I/O operation is pending. The 
             System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will be raised upon 
             completion of the operation. Returns false if the I/O operation completed synchronously. In this 
             case, The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will not be 
             raised and the e object passed as a parameter may be examined immediately after the method call 
             returns to retrieve the result of the operation.
        """
        pass

    def ReceiveFrom(self, buffer, *__args):
        """
        ReceiveFrom(self: Socket, buffer: Array[Byte], socketFlags: SocketFlags, remoteEP: EndPoint) -> (int, EndPoint)
        
            Receives a datagram into the data buffer, using the specified System.Net.Sockets.SocketFlags, 
             and stores the endpoint.
        
        
            buffer: An array of type System.Byte that is the storage location for the received data.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            remoteEP: An System.Net.EndPoint, passed by reference, that represents the remote server.
            Returns: The number of bytes received.
        ReceiveFrom(self: Socket, buffer: Array[Byte], remoteEP: EndPoint) -> (int, EndPoint)
        
            Receives a datagram into the data buffer and stores the endpoint.
        
            buffer: An array of type System.Byte that is the storage location for received data.
            remoteEP: An System.Net.EndPoint, passed by reference, that represents the remote server.
            Returns: The number of bytes received.
        ReceiveFrom(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, remoteEP: EndPoint) -> (int, EndPoint)
        
            Receives the specified number of bytes of data into the specified location of the data buffer, 
             using the specified System.Net.Sockets.SocketFlags, and stores the endpoint.
        
        
            buffer: An array of type System.Byte that is the storage location for received data.
            offset: The position in the buffer parameter to store the received data.
            size: The number of bytes to receive.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            remoteEP: An System.Net.EndPoint, passed by reference, that represents the remote server.
            Returns: The number of bytes received.
        ReceiveFrom(self: Socket, buffer: Array[Byte], size: int, socketFlags: SocketFlags, remoteEP: EndPoint) -> (int, EndPoint)
        
            Receives the specified number of bytes into the data buffer, using the specified 
             System.Net.Sockets.SocketFlags, and stores the endpoint.
        
        
            buffer: An array of type System.Byte that is the storage location for received data.
            size: The number of bytes to receive.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            remoteEP: An System.Net.EndPoint, passed by reference, that represents the remote server.
            Returns: The number of bytes received.
        """
        pass

    def ReceiveFromAsync(self, e):
        """
        ReceiveFromAsync(self: Socket, e: SocketAsyncEventArgs) -> bool
        
            Begins to asynchronously receive data from a specified network device.
        
            e: The System.Net.Sockets.SocketAsyncEventArgs object to use for this asynchronous socket operation.
            Returns: Returns true if the I/O operation is pending. The 
             System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will be raised upon 
             completion of the operation. Returns false if the I/O operation completed synchronously. In this 
             case, The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will not be 
             raised and the e object passed as a parameter may be examined immediately after the method call 
             returns to retrieve the result of the operation.
        """
        pass

    def ReceiveMessageFrom(self, buffer, offset, size, socketFlags, remoteEP, ipPacketInformation):
        """
        ReceiveMessageFrom(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, remoteEP: EndPoint) -> (int, SocketFlags, EndPoint, IPPacketInformation)
        
            Receives the specified number of bytes of data into the specified location of the data buffer, 
             using the specified System.Net.Sockets.SocketFlags, and stores the endpoint and packet 
             information.
        
        
            buffer: An array of type System.Byte that is the storage location for received data.
            offset: The position in the buffer parameter to store the received data.
            size: The number of bytes to receive.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            remoteEP: An System.Net.EndPoint, passed by reference, that represents the remote server.
            Returns: The number of bytes received.
        """
        pass

    def ReceiveMessageFromAsync(self, e):
        """
        ReceiveMessageFromAsync(self: Socket, e: SocketAsyncEventArgs) -> bool
        
            Begins to asynchronously receive the specified number of bytes of data into the specified 
             location in the data buffer, using the specified 
             System.Net.Sockets.SocketAsyncEventArgs.SocketFlags, and stores the endpoint and packet 
             information.
        
        
            e: The System.Net.Sockets.SocketAsyncEventArgs object to use for this asynchronous socket operation.
            Returns: Returns true if the I/O operation is pending. The 
             System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will be raised upon 
             completion of the operation. Returns false if the I/O operation completed synchronously. In this 
             case, The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will not be 
             raised and the e object passed as a parameter may be examined immediately after the method call 
             returns to retrieve the result of the operation.
        """
        pass

    @staticmethod
    def Select(checkRead, checkWrite, checkError, microSeconds):
        """
        Select(checkRead: IList, checkWrite: IList, checkError: IList, microSeconds: int)
            Determines the status of one or more sockets.
        
            checkRead: An System.Collections.IList of System.Net.Sockets.Socket instances to check for readability.
            checkWrite: An System.Collections.IList of System.Net.Sockets.Socket instances to check for writability.
            checkError: An System.Collections.IList of System.Net.Sockets.Socket instances to check for errors.
            microSeconds: The time-out value, in microseconds. A -1 value indicates an infinite time-out.
        """
        pass

    def Send(self, *__args):
        """
        Send(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags) -> (int, SocketError)
        Send(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags) -> int
        Send(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags) -> (int, SocketError)
        
            Sends the specified number of bytes of data to a connected System.Net.Sockets.Socket, starting 
             at the specified offset, and using the specified System.Net.Sockets.SocketFlags
        
        
            buffer: An array of type System.Byte that contains the data to be sent.
            offset: The position in the data buffer at which to begin sending data.
            size: The number of bytes to send.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            Returns: The number of bytes sent to the System.Net.Sockets.Socket.
        Send(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags) -> int
        
            Sends the specified number of bytes of data to a connected System.Net.Sockets.Socket, starting 
             at the specified offset, and using the specified System.Net.Sockets.SocketFlags.
        
        
            buffer: An array of type System.Byte that contains the data to be sent.
            offset: The position in the data buffer at which to begin sending data.
            size: The number of bytes to send.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            Returns: The number of bytes sent to the System.Net.Sockets.Socket.
        Send(self: Socket, buffer: Array[Byte], socketFlags: SocketFlags) -> int
        
            Sends data to a connected System.Net.Sockets.Socket using the specified 
             System.Net.Sockets.SocketFlags.
        
        
            buffer: An array of type System.Byte that contains the data to be sent.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            Returns: The number of bytes sent to the System.Net.Sockets.Socket.
        Send(self: Socket, buffer: Array[Byte], size: int, socketFlags: SocketFlags) -> int
        
            Sends the specified number of bytes of data to a connected System.Net.Sockets.Socket, using the 
             specified System.Net.Sockets.SocketFlags.
        
        
            buffer: An array of type System.Byte that contains the data to be sent.
            size: The number of bytes to send.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            Returns: The number of bytes sent to the System.Net.Sockets.Socket.
        Send(self: Socket, buffers: IList[ArraySegment[Byte]]) -> int
        Send(self: Socket, buffer: Array[Byte]) -> int
        
            Sends data to a connected System.Net.Sockets.Socket.
        
            buffer: An array of type System.Byte that contains the data to be sent.
            Returns: The number of bytes sent to the System.Net.Sockets.Socket.
        """
        pass

    def SendAsync(self, e):
        """
        SendAsync(self: Socket, e: SocketAsyncEventArgs) -> bool
        
            Sends data asynchronously to a connected System.Net.Sockets.Socket object.
        
            e: The System.Net.Sockets.SocketAsyncEventArgs object to use for this asynchronous socket operation.
            Returns: Returns true if the I/O operation is pending. The 
             System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will be raised upon 
             completion of the operation. Returns false if the I/O operation completed synchronously. In this 
             case, The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will not be 
             raised and the e object passed as a parameter may be examined immediately after the method call 
             returns to retrieve the result of the operation.
        """
        pass

    def SendFile(self, fileName, preBuffer=None, postBuffer=None, flags=None):
        """
        SendFile(self: Socket, fileName: str, preBuffer: Array[Byte], postBuffer: Array[Byte], flags: TransmitFileOptions)
            Sends the file fileName and buffers of data to a connected System.Net.Sockets.Socket object 
             using the specified System.Net.Sockets.TransmitFileOptions value.
        
        
            fileName: A System.String that contains the path and name of the file to be sent. This parameter can be 
             null.
        
            preBuffer: A System.Byte array that contains data to be sent before the file is sent. This parameter can be 
             null.
        
            postBuffer: A System.Byte array that contains data to be sent after the file is sent. This parameter can be 
             null.
        
            flags: One or more of System.Net.Sockets.TransmitFileOptions values.
        SendFile(self: Socket, fileName: str)
            Sends the file fileName to a connected System.Net.Sockets.Socket object with the 
             System.Net.Sockets.TransmitFileOptions.UseDefaultWorkerThread transmit flag.
        
        
            fileName: A System.String that contains the path and name of the file to be sent. This parameter can be 
             null.
        """
        pass

    def SendPacketsAsync(self, e):
        """
        SendPacketsAsync(self: Socket, e: SocketAsyncEventArgs) -> bool
        
            Sends a collection of files or in memory data buffers asynchronously to a connected 
             System.Net.Sockets.Socket object.
        
        
            e: The System.Net.Sockets.SocketAsyncEventArgs object to use for this asynchronous socket operation.
            Returns: Returns true if the I/O operation is pending. The 
             System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will be raised upon 
             completion of the operation. Returns false if the I/O operation completed synchronously. In this 
             case, The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will not be 
             raised and the e object passed as a parameter may be examined immediately after the method call 
             returns to retrieve the result of the operation.
        """
        pass

    def SendTo(self, buffer, *__args):
        """
        SendTo(self: Socket, buffer: Array[Byte], socketFlags: SocketFlags, remoteEP: EndPoint) -> int
        
            Sends data to a specific endpoint using the specified System.Net.Sockets.SocketFlags.
        
            buffer: An array of type System.Byte that contains the data to be sent.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            remoteEP: The System.Net.EndPoint that represents the destination location for the data.
            Returns: The number of bytes sent.
        SendTo(self: Socket, buffer: Array[Byte], remoteEP: EndPoint) -> int
        
            Sends data to the specified endpoint.
        
            buffer: An array of type System.Byte that contains the data to be sent.
            remoteEP: The System.Net.EndPoint that represents the destination for the data.
            Returns: The number of bytes sent.
        SendTo(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, remoteEP: EndPoint) -> int
        
            Sends the specified number of bytes of data to the specified endpoint, starting at the specified 
             location in the buffer, and using the specified System.Net.Sockets.SocketFlags.
        
        
            buffer: An array of type System.Byte that contains the data to be sent.
            offset: The position in the data buffer at which to begin sending data.
            size: The number of bytes to send.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            remoteEP: The System.Net.EndPoint that represents the destination location for the data.
            Returns: The number of bytes sent.
        SendTo(self: Socket, buffer: Array[Byte], size: int, socketFlags: SocketFlags, remoteEP: EndPoint) -> int
        
            Sends the specified number of bytes of data to the specified endpoint using the specified 
             System.Net.Sockets.SocketFlags.
        
        
            buffer: An array of type System.Byte that contains the data to be sent.
            size: The number of bytes to send.
            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.
            remoteEP: The System.Net.EndPoint that represents the destination location for the data.
            Returns: The number of bytes sent.
        """
        pass

    def SendToAsync(self, e):
        """
        SendToAsync(self: Socket, e: SocketAsyncEventArgs) -> bool
        
            Sends data asynchronously to a specific remote host.
        
            e: The System.Net.Sockets.SocketAsyncEventArgs object to use for this asynchronous socket operation.
            Returns: Returns true if the I/O operation is pending. The 
             System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will be raised upon 
             completion of the operation. Returns false if the I/O operation completed synchronously. In this 
             case, The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will not be 
             raised and the e object passed as a parameter may be examined immediately after the method call 
             returns to retrieve the result of the operation.
        """
        pass

    def SetIPProtectionLevel(self, level):
        """
        SetIPProtectionLevel(self: Socket, level: IPProtectionLevel)
            Set the IP protection level on a socket.
        
            level: The IP protection level to set on this socket.
        """
        pass

    def SetSocketOption(self, optionLevel, optionName, optionValue):
        """
        SetSocketOption(self: Socket, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: bool)
            Sets the specified System.Net.Sockets.Socket option to the specified System.Boolean value.
        
            optionLevel: One of the System.Net.Sockets.SocketOptionLevel values.
            optionName: One of the System.Net.Sockets.SocketOptionName values.
            optionValue: The value of the option, represented as a System.Boolean.
        SetSocketOption(self: Socket, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: object)
            Sets the specified System.Net.Sockets.Socket option to the specified value, represented as an 
             object.
        
        
            optionLevel: One of the System.Net.Sockets.SocketOptionLevel values.
            optionName: One of the System.Net.Sockets.SocketOptionName values.
            optionValue: A System.Net.Sockets.LingerOption or System.Net.Sockets.MulticastOption that contains the value 
             of the option.
        
        SetSocketOption(self: Socket, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: int)
            Sets the specified System.Net.Sockets.Socket option to the specified integer value.
        
            optionLevel: One of the System.Net.Sockets.SocketOptionLevel values.
            optionName: One of the System.Net.Sockets.SocketOptionName values.
            optionValue: A value of the option.
        SetSocketOption(self: Socket, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: Array[Byte])
            Sets the specified System.Net.Sockets.Socket option to the specified value, represented as a 
             byte array.
        
        
            optionLevel: One of the System.Net.Sockets.SocketOptionLevel values.
            optionName: One of the System.Net.Sockets.SocketOptionName values.
            optionValue: An array of type System.Byte that represents the value of the option.
        """
        pass

    def Shutdown(self, how):
        """
        Shutdown(self: Socket, how: SocketShutdown)
            Disables sends and receives on a System.Net.Sockets.Socket.
        
            how: One of the System.Net.Sockets.SocketShutdown values that specifies the operation that will no 
             longer be allowed.
        """
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, socketType: SocketType, protocolType: ProtocolType)
        __new__(cls: type, addressFamily: AddressFamily, socketType: SocketType, protocolType: ProtocolType)
        __new__(cls: type, socketInformation: SocketInformation)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AddressFamily = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the address family of the System.Net.Sockets.Socket.

Get: AddressFamily(self: Socket) -> AddressFamily

"""

    Available = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of data that has been received from the network and is available to be read.

Get: Available(self: Socket) -> int

"""

    Blocking = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the System.Net.Sockets.Socket is in blocking mode.

Get: Blocking(self: Socket) -> bool

Set: Blocking(self: Socket) = value
"""

    Connected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a System.Net.Sockets.Socket is connected to a remote host as of the last erload:System.Net.Sockets.Socket.Send or erload:System.Net.Sockets.Socket.Receive operation.

Get: Connected(self: Socket) -> bool

"""

    DontFragment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Boolean value that specifies whether the System.Net.Sockets.Socket allows Internet Protocol (IP) datagrams to be fragmented.

Get: DontFragment(self: Socket) -> bool

Set: DontFragment(self: Socket) = value
"""

    DualMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DualMode(self: Socket) -> bool

Set: DualMode(self: Socket) = value
"""

    EnableBroadcast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Boolean value that specifies whether the System.Net.Sockets.Socket can send or receive broadcast packets.

Get: EnableBroadcast(self: Socket) -> bool

Set: EnableBroadcast(self: Socket) = value
"""

    ExclusiveAddressUse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Boolean value that specifies whether the System.Net.Sockets.Socket allows only one process to bind to a port.

Get: ExclusiveAddressUse(self: Socket) -> bool

Set: ExclusiveAddressUse(self: Socket) = value
"""

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the operating system handle for the System.Net.Sockets.Socket.

Get: Handle(self: Socket) -> IntPtr

"""

    IsBound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Net.Sockets.Socket is bound to a specific local port.

Get: IsBound(self: Socket) -> bool

"""

    LingerState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that specifies whether the System.Net.Sockets.Socket will delay closing a socket in an attempt to send all pending data.

Get: LingerState(self: Socket) -> LingerOption

Set: LingerState(self: Socket) = value
"""

    LocalEndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the local endpoint.

Get: LocalEndPoint(self: Socket) -> EndPoint

"""

    MulticastLoopback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that specifies whether outgoing multicast packets are delivered to the sending application.

Get: MulticastLoopback(self: Socket) -> bool

Set: MulticastLoopback(self: Socket) = value
"""

    NoDelay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Boolean value that specifies whether the stream System.Net.Sockets.Socket is using the Nagle algorithm.

Get: NoDelay(self: Socket) -> bool

Set: NoDelay(self: Socket) = value
"""

    ProtocolType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the protocol type of the System.Net.Sockets.Socket.

Get: ProtocolType(self: Socket) -> ProtocolType

"""

    ReceiveBufferSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that specifies the size of the receive buffer of the System.Net.Sockets.Socket.

Get: ReceiveBufferSize(self: Socket) -> int

Set: ReceiveBufferSize(self: Socket) = value
"""

    ReceiveTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that specifies the amount of time after which a synchronous erload:System.Net.Sockets.Socket.Receive call will time out.

Get: ReceiveTimeout(self: Socket) -> int

Set: ReceiveTimeout(self: Socket) = value
"""

    RemoteEndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the remote endpoint.

Get: RemoteEndPoint(self: Socket) -> EndPoint

"""

    SendBufferSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that specifies the size of the send buffer of the System.Net.Sockets.Socket.

Get: SendBufferSize(self: Socket) -> int

Set: SendBufferSize(self: Socket) = value
"""

    SendTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that specifies the amount of time after which a synchronous erload:System.Net.Sockets.Socket.Send call will time out.

Get: SendTimeout(self: Socket) -> int

Set: SendTimeout(self: Socket) = value
"""

    SocketType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of the System.Net.Sockets.Socket.

Get: SocketType(self: Socket) -> SocketType

"""

    Ttl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that specifies the Time To Live (TTL) value of Internet Protocol (IP) packets sent by the System.Net.Sockets.Socket.

Get: Ttl(self: Socket) -> Int16

Set: Ttl(self: Socket) = value
"""

    UseOnlyOverlappedIO = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the socket should only use Overlapped I/O mode.

Get: UseOnlyOverlappedIO(self: Socket) -> bool

Set: UseOnlyOverlappedIO(self: Socket) = value
"""


    OSSupportsIPv4 = True
    OSSupportsIPv6 = True
    SupportsIPv4 = True
    SupportsIPv6 = False


class SocketAsyncEventArgs(EventArgs, IDisposable):
    """
    Represents an asynchronous socket operation.
    
    SocketAsyncEventArgs()
    """
    def Dispose(self):
        """
        Dispose(self: SocketAsyncEventArgs)
            Releases the unmanaged resources used by the System.Net.Sockets.SocketAsyncEventArgs instance 
             and optionally disposes of the managed resources.
        """
        pass

    def OnCompleted(self, *args): #cannot find CLR method
        """
        OnCompleted(self: SocketAsyncEventArgs, e: SocketAsyncEventArgs)
            Represents a method that is called when an asynchronous operation completes.
        
            e: The event that is signaled.
        """
        pass

    def SetBuffer(self, *__args):
        """
        SetBuffer(self: SocketAsyncEventArgs, offset: int, count: int)
            Sets the data buffer to use with an asynchronous socket method.
        
            offset: The offset, in bytes, in the data buffer where the operation starts.
            count: The maximum amount of data, in bytes, to send or receive in the buffer.
        SetBuffer(self: SocketAsyncEventArgs, buffer: Array[Byte], offset: int, count: int)
            Sets the data buffer to use with an asynchronous socket method.
        
            buffer: The data buffer to use with an asynchronous socket method.
            offset: The offset, in bytes, in the data buffer where the operation starts.
            count: The maximum amount of data, in bytes, to send or receive in the buffer.
        """
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

    AcceptSocket = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the socket to use or the socket created for accepting a connection with an asynchronous socket method.

Get: AcceptSocket(self: SocketAsyncEventArgs) -> Socket

Set: AcceptSocket(self: SocketAsyncEventArgs) = value
"""

    Buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the data buffer to use with an asynchronous socket method.

Get: Buffer(self: SocketAsyncEventArgs) -> Array[Byte]

"""

    BufferList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of data buffers to use with an asynchronous socket method.

Get: BufferList(self: SocketAsyncEventArgs) -> IList[ArraySegment[Byte]]

Set: BufferList(self: SocketAsyncEventArgs) = value
"""

    BytesTransferred = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of bytes transferred in the socket operation.

Get: BytesTransferred(self: SocketAsyncEventArgs) -> int

"""

    ConnectByNameError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the exception in the case of a connection failure when a System.Net.DnsEndPoint was used.

Get: ConnectByNameError(self: SocketAsyncEventArgs) -> Exception

"""

    ConnectSocket = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The created and connected System.Net.Sockets.Socket object after successful completion of the erload:System.Net.Sockets.Socket.ConnectAsync method.

Get: ConnectSocket(self: SocketAsyncEventArgs) -> Socket

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the maximum amount of data, in bytes, to send or receive in an asynchronous operation.

Get: Count(self: SocketAsyncEventArgs) -> int

"""

    DisconnectReuseSocket = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that specifies if socket can be reused after a disconnect operation.

Get: DisconnectReuseSocket(self: SocketAsyncEventArgs) -> bool

Set: DisconnectReuseSocket(self: SocketAsyncEventArgs) = value
"""

    LastOperation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of socket operation most recently performed with this context object.

Get: LastOperation(self: SocketAsyncEventArgs) -> SocketAsyncOperation

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the offset, in bytes, into the data buffer referenced by the System.Net.Sockets.SocketAsyncEventArgs.Buffer property.

Get: Offset(self: SocketAsyncEventArgs) -> int

"""

    ReceiveMessageFromPacketInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the IP address and interface of a received packet.

Get: ReceiveMessageFromPacketInfo(self: SocketAsyncEventArgs) -> IPPacketInformation

"""

    RemoteEndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the remote IP endpoint for an asynchronous operation.

Get: RemoteEndPoint(self: SocketAsyncEventArgs) -> EndPoint

Set: RemoteEndPoint(self: SocketAsyncEventArgs) = value
"""

    SendPacketsElements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of buffers to be sent for an asynchronous operation used by the System.Net.Sockets.Socket.SendPacketsAsync(System.Net.Sockets.SocketAsyncEventArgs) method.

Get: SendPacketsElements(self: SocketAsyncEventArgs) -> Array[SendPacketsElement]

Set: SendPacketsElements(self: SocketAsyncEventArgs) = value
"""

    SendPacketsFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a bitwise combination of System.Net.Sockets.TransmitFileOptions values for an asynchronous operation used by the System.Net.Sockets.Socket.SendPacketsAsync(System.Net.Sockets.SocketAsyncEventArgs) method.

Get: SendPacketsFlags(self: SocketAsyncEventArgs) -> TransmitFileOptions

Set: SendPacketsFlags(self: SocketAsyncEventArgs) = value
"""

    SendPacketsSendSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the size, in bytes, of the data block used in the send operation.

Get: SendPacketsSendSize(self: SocketAsyncEventArgs) -> int

Set: SendPacketsSendSize(self: SocketAsyncEventArgs) = value
"""

    SocketClientAccessPolicyProtocol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SocketClientAccessPolicyProtocol(self: SocketAsyncEventArgs) -> SocketClientAccessPolicyProtocol

Set: SocketClientAccessPolicyProtocol(self: SocketAsyncEventArgs) = value
"""

    SocketError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the result of the asynchronous socket operation.

Get: SocketError(self: SocketAsyncEventArgs) -> SocketError

Set: SocketError(self: SocketAsyncEventArgs) = value
"""

    SocketFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the results of an asynchronous socket operation or sets the behavior of an asynchronous operation.

Get: SocketFlags(self: SocketAsyncEventArgs) -> SocketFlags

Set: SocketFlags(self: SocketAsyncEventArgs) = value
"""

    UserToken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a user or application object associated with this asynchronous socket operation.

Get: UserToken(self: SocketAsyncEventArgs) -> object

Set: UserToken(self: SocketAsyncEventArgs) = value
"""


    Completed = None


class SocketAsyncOperation(Enum, IComparable, IFormattable, IConvertible):
    """
    The type of asynchronous socket operation most recently performed with this context object.
    
    enum SocketAsyncOperation, values: Accept (1), Connect (2), Disconnect (3), None (0), Receive (4), ReceiveFrom (5), ReceiveMessageFrom (6), Send (7), SendPackets (8), SendTo (9)
    """
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

    Accept = None
    Connect = None
    Disconnect = None
    None = None
    Receive = None
    ReceiveFrom = None
    ReceiveMessageFrom = None
    Send = None
    SendPackets = None
    SendTo = None
    value__ = None


class SocketClientAccessPolicyProtocol(Enum, IComparable, IFormattable, IConvertible):
    """ enum SocketClientAccessPolicyProtocol, values: Http (1), Tcp (0) """
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

    Http = None
    Tcp = None
    value__ = None


class SocketError(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines error codes for the System.Net.Sockets.Socket class.
    
    enum SocketError, values: AccessDenied (10013), AddressAlreadyInUse (10048), AddressFamilyNotSupported (10047), AddressNotAvailable (10049), AlreadyInProgress (10037), ConnectionAborted (10053), ConnectionRefused (10061), ConnectionReset (10054), DestinationAddressRequired (10039), Disconnecting (10101), Fault (10014), HostDown (10064), HostNotFound (11001), HostUnreachable (10065), InProgress (10036), Interrupted (10004), InvalidArgument (10022), IOPending (997), IsConnected (10056), MessageSize (10040), NetworkDown (10050), NetworkReset (10052), NetworkUnreachable (10051), NoBufferSpaceAvailable (10055), NoData (11004), NoRecovery (11003), NotConnected (10057), NotInitialized (10093), NotSocket (10038), OperationAborted (995), OperationNotSupported (10045), ProcessLimit (10067), ProtocolFamilyNotSupported (10046), ProtocolNotSupported (10043), ProtocolOption (10042), ProtocolType (10041), Shutdown (10058), SocketError (-1), SocketNotSupported (10044), Success (0), SystemNotReady (10091), TimedOut (10060), TooManyOpenSockets (10024), TryAgain (11002), TypeNotFound (10109), VersionNotSupported (10092), WouldBlock (10035)
    """
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

    AccessDenied = None
    AddressAlreadyInUse = None
    AddressFamilyNotSupported = None
    AddressNotAvailable = None
    AlreadyInProgress = None
    ConnectionAborted = None
    ConnectionRefused = None
    ConnectionReset = None
    DestinationAddressRequired = None
    Disconnecting = None
    Fault = None
    HostDown = None
    HostNotFound = None
    HostUnreachable = None
    InProgress = None
    Interrupted = None
    InvalidArgument = None
    IOPending = None
    IsConnected = None
    MessageSize = None
    NetworkDown = None
    NetworkReset = None
    NetworkUnreachable = None
    NoBufferSpaceAvailable = None
    NoData = None
    NoRecovery = None
    NotConnected = None
    NotInitialized = None
    NotSocket = None
    OperationAborted = None
    OperationNotSupported = None
    ProcessLimit = None
    ProtocolFamilyNotSupported = None
    ProtocolNotSupported = None
    ProtocolOption = None
    ProtocolType = None
    Shutdown = None
    SocketError = None
    SocketNotSupported = None
    Success = None
    SystemNotReady = None
    TimedOut = None
    TooManyOpenSockets = None
    TryAgain = None
    TypeNotFound = None
    value__ = None
    VersionNotSupported = None
    WouldBlock = None


class SocketException(Win32Exception, ISerializable, _Exception):
    """
    The exception that is thrown when a socket error occurs.
    
    SocketException()
    SocketException(errorCode: int)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, errorCode=None):
        """
        __new__(cls: type)
        __new__(cls: type, errorCode: int)
        __new__(cls: type, serializationInfo: SerializationInfo, streamingContext: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ErrorCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the error code that is associated with this exception.

Get: ErrorCode(self: SocketException) -> int

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the error message that is associated with this exception.

Get: Message(self: SocketException) -> str

"""

    SocketErrorCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the error code that is associated with this exception.

Get: SocketErrorCode(self: SocketException) -> SocketError

"""



class SocketFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies socket send and receive behaviors.
    
    enum (flags) SocketFlags, values: Broadcast (1024), ControlDataTruncated (512), DontRoute (4), MaxIOVectorLength (16), Multicast (2048), None (0), OutOfBand (1), Partial (32768), Peek (2), Truncated (256)
    """
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

    Broadcast = None
    ControlDataTruncated = None
    DontRoute = None
    MaxIOVectorLength = None
    Multicast = None
    None = None
    OutOfBand = None
    Partial = None
    Peek = None
    Truncated = None
    value__ = None


class SocketInformation(object):
    """ Encapsulates the information that is necessary to duplicate a System.Net.Sockets.Socket. """
    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the options for a System.Net.Sockets.Socket.

Get: Options(self: SocketInformation) -> SocketInformationOptions

Set: Options(self: SocketInformation) = value
"""

    ProtocolInformation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the protocol information for a System.Net.Sockets.Socket.

Get: ProtocolInformation(self: SocketInformation) -> Array[Byte]

Set: ProtocolInformation(self: SocketInformation) = value
"""



class SocketInformationOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes states for a System.Net.Sockets.Socket.
    
    enum (flags) SocketInformationOptions, values: Connected (2), Listening (4), NonBlocking (1), UseOnlyOverlappedIO (8)
    """
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

    Connected = None
    Listening = None
    NonBlocking = None
    UseOnlyOverlappedIO = None
    value__ = None


class SocketOptionLevel(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines socket option levels for the System.Net.Sockets.Socket.SetSocketOption(System.Net.Sockets.SocketOptionLevel,System.Net.Sockets.SocketOptionName,System.Int32) and System.Net.Sockets.Socket.GetSocketOption(System.Net.Sockets.SocketOptionLevel,System.Net.Sockets.SocketOptionName) methods.
    
    enum SocketOptionLevel, values: IP (0), IPv6 (41), Socket (65535), Tcp (6), Udp (17)
    """
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

    IP = None
    IPv6 = None
    Socket = None
    Tcp = None
    Udp = None
    value__ = None


class SocketOptionName(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines configuration option names.
    
    enum SocketOptionName, values: AcceptConnection (2), AddMembership (12), AddSourceMembership (15), BlockSource (17), Broadcast (32), BsdUrgent (2), ChecksumCoverage (20), Debug (1), DontFragment (14), DontLinger (-129), DontRoute (16), DropMembership (13), DropSourceMembership (16), Error (4103), ExclusiveAddressUse (-5), Expedited (2), HeaderIncluded (2), HopLimit (21), IPOptions (1), IPProtectionLevel (23), IpTimeToLive (4), IPv6Only (27), KeepAlive (8), Linger (128), MaxConnections (2147483647), MulticastInterface (9), MulticastLoopback (11), MulticastTimeToLive (10), NoChecksum (1), NoDelay (1), OutOfBandInline (256), PacketInformation (19), ReceiveBuffer (4098), ReceiveLowWater (4100), ReceiveTimeout (4102), ReuseAddress (4), ReuseUnicastPort (12295), SendBuffer (4097), SendLowWater (4099), SendTimeout (4101), Type (4104), TypeOfService (3), UnblockSource (18), UpdateAcceptContext (28683), UpdateConnectContext (28688), UseLoopback (64)
    """
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

    AcceptConnection = None
    AddMembership = None
    AddSourceMembership = None
    BlockSource = None
    Broadcast = None
    BsdUrgent = None
    ChecksumCoverage = None
    Debug = None
    DontFragment = None
    DontLinger = None
    DontRoute = None
    DropMembership = None
    DropSourceMembership = None
    Error = None
    ExclusiveAddressUse = None
    Expedited = None
    HeaderIncluded = None
    HopLimit = None
    IPOptions = None
    IPProtectionLevel = None
    IpTimeToLive = None
    IPv6Only = None
    KeepAlive = None
    Linger = None
    MaxConnections = None
    MulticastInterface = None
    MulticastLoopback = None
    MulticastTimeToLive = None
    NoChecksum = None
    NoDelay = None
    OutOfBandInline = None
    PacketInformation = None
    ReceiveBuffer = None
    ReceiveLowWater = None
    ReceiveTimeout = None
    ReuseAddress = None
    ReuseUnicastPort = None
    SendBuffer = None
    SendLowWater = None
    SendTimeout = None
    Type = None
    TypeOfService = None
    UnblockSource = None
    UpdateAcceptContext = None
    UpdateConnectContext = None
    UseLoopback = None
    value__ = None


class SocketShutdown(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines constants that are used by the System.Net.Sockets.Socket.Shutdown(System.Net.Sockets.SocketShutdown) method.
    
    enum SocketShutdown, values: Both (2), Receive (0), Send (1)
    """
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

    Both = None
    Receive = None
    Send = None
    value__ = None


class SocketType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of socket that an instance of the System.Net.Sockets.Socket class represents.
    
    enum SocketType, values: Dgram (2), Raw (3), Rdm (4), Seqpacket (5), Stream (1), Unknown (-1)
    """
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

    Dgram = None
    Raw = None
    Rdm = None
    Seqpacket = None
    Stream = None
    Unknown = None
    value__ = None


class TcpClient(object, IDisposable):
    """
    Provides client connections for TCP network services.
    
    TcpClient(localEP: IPEndPoint)
    TcpClient()
    TcpClient(family: AddressFamily)
    TcpClient(hostname: str, port: int)
    """
    def BeginConnect(self, *__args):
        """
        BeginConnect(self: TcpClient, addresses: Array[IPAddress], port: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult
        
            Begins an asynchronous request for a remote host connection. The remote host is specified by an 
             System.Net.IPAddress array and a port number (System.Int32).
        
        
            addresses: At least one System.Net.IPAddress that designates the remote hosts.
            port: The port number of the remote hosts.
            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is 
             complete.
        
            state: A user-defined object that contains information about the connect operation. This object is 
             passed to the requestCallback delegate when the operation is complete.
        
            Returns: An System.IAsyncResult object that references the asynchronous connection.
        BeginConnect(self: TcpClient, address: IPAddress, port: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult
        
            Begins an asynchronous request for a remote host connection. The remote host is specified by an 
             System.Net.IPAddress and a port number (System.Int32).
        
        
            address: The System.Net.IPAddress of the remote host.
            port: The port number of the remote host.
            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is 
             complete.
        
            state: A user-defined object that contains information about the connect operation. This object is 
             passed to the requestCallback delegate when the operation is complete.
        
            Returns: An System.IAsyncResult object that references the asynchronous connection.
        BeginConnect(self: TcpClient, host: str, port: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult
        
            Begins an asynchronous request for a remote host connection. The remote host is specified by a 
             host name (System.String) and a port number (System.Int32).
        
        
            host: The name of the remote host.
            port: The port number of the remote host.
            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is 
             complete.
        
            state: A user-defined object that contains information about the connect operation. This object is 
             passed to the requestCallback delegate when the operation is complete.
        
            Returns: An System.IAsyncResult object that references the asynchronous connection.
        """
        pass

    def Close(self):
        """
        Close(self: TcpClient)
            Disposes this System.Net.Sockets.TcpClient instance and requests that the underlying TCP 
             connection be closed.
        """
        pass

    def Connect(self, *__args):
        """
        Connect(self: TcpClient, remoteEP: IPEndPoint)
            Connects the client to a remote TCP host using the specified remote network endpoint.
        
            remoteEP: The System.Net.IPEndPoint to which you intend to connect.
        Connect(self: TcpClient, ipAddresses: Array[IPAddress], port: int)
            Connects the client to a remote TCP host using the specified IP addresses and port number.
        
            ipAddresses: The System.Net.IPAddress array of the host to which you intend to connect.
            port: The port number to which you intend to connect.
        Connect(self: TcpClient, hostname: str, port: int)
            Connects the client to the specified port on the specified host.
        
            hostname: The DNS name of the remote host to which you intend to connect.
            port: The port number of the remote host to which you intend to connect.
        Connect(self: TcpClient, address: IPAddress, port: int)
            Connects the client to a remote TCP host using the specified IP address and port number.
        
            address: The System.Net.IPAddress of the host to which you intend to connect.
            port: The port number to which you intend to connect.
        """
        pass

    def ConnectAsync(self, *__args):
        """
        ConnectAsync(self: TcpClient, addresses: Array[IPAddress], port: int) -> Task
        ConnectAsync(self: TcpClient, host: str, port: int) -> Task
        ConnectAsync(self: TcpClient, address: IPAddress, port: int) -> Task
        """
        pass

    def Dispose(self):
        """ Dispose(self: TcpClient) """
        pass

    def EndConnect(self, asyncResult):
        """
        EndConnect(self: TcpClient, asyncResult: IAsyncResult)
            Asynchronously accepts an incoming connection attempt.
        
            asyncResult: An System.IAsyncResult object returned by a call to 
             erload:System.Net.Sockets.TcpClient.BeginConnect.
        """
        pass

    def GetStream(self):
        """
        GetStream(self: TcpClient) -> NetworkStream
        
            Returns the System.Net.Sockets.NetworkStream used to send and receive data.
            Returns: The underlying System.Net.Sockets.NetworkStream.
        """
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, localEP: IPEndPoint)
        __new__(cls: type)
        __new__(cls: type, family: AddressFamily)
        __new__(cls: type, hostname: str, port: int)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or set a value that indicates whether a connection has been made.

"""

    Available = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of data that has been received from the network and is available to be read.

Get: Available(self: TcpClient) -> int

"""

    Client = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the underlying System.Net.Sockets.Socket.

Get: Client(self: TcpClient) -> Socket

Set: Client(self: TcpClient) = value
"""

    Connected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the underlying System.Net.Sockets.Socket for a System.Net.Sockets.TcpClient is connected to a remote host.

Get: Connected(self: TcpClient) -> bool

"""

    ExclusiveAddressUse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Boolean value that specifies whether the System.Net.Sockets.TcpClient allows only one client to use a port.

Get: ExclusiveAddressUse(self: TcpClient) -> bool

Set: ExclusiveAddressUse(self: TcpClient) = value
"""

    LingerState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets information about the linger state of the associated socket.

Get: LingerState(self: TcpClient) -> LingerOption

Set: LingerState(self: TcpClient) = value
"""

    NoDelay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that disables a delay when send or receive buffers are not full.

Get: NoDelay(self: TcpClient) -> bool

Set: NoDelay(self: TcpClient) = value
"""

    ReceiveBufferSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the size of the receive buffer.

Get: ReceiveBufferSize(self: TcpClient) -> int

Set: ReceiveBufferSize(self: TcpClient) = value
"""

    ReceiveTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the amount of time a System.Net.Sockets.TcpClient will wait to receive data once a read operation is initiated.

Get: ReceiveTimeout(self: TcpClient) -> int

Set: ReceiveTimeout(self: TcpClient) = value
"""

    SendBufferSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the size of the send buffer.

Get: SendBufferSize(self: TcpClient) -> int

Set: SendBufferSize(self: TcpClient) = value
"""

    SendTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the amount of time a System.Net.Sockets.TcpClient will wait for a send operation to complete successfully.

Get: SendTimeout(self: TcpClient) -> int

Set: SendTimeout(self: TcpClient) = value
"""



class TcpListener(object):
    """
    Listens for connections from TCP network clients.
    
    TcpListener(localEP: IPEndPoint)
    TcpListener(localaddr: IPAddress, port: int)
    TcpListener(port: int)
    """
    def AcceptSocket(self):
        """
        AcceptSocket(self: TcpListener) -> Socket
        
            Accepts a pending connection request.
            Returns: A System.Net.Sockets.Socket used to send and receive data.
        """
        pass

    def AcceptSocketAsync(self):
        """ AcceptSocketAsync(self: TcpListener) -> Task[Socket] """
        pass

    def AcceptTcpClient(self):
        """
        AcceptTcpClient(self: TcpListener) -> TcpClient
        
            Accepts a pending connection request
            Returns: A System.Net.Sockets.TcpClient used to send and receive data.
        """
        pass

    def AcceptTcpClientAsync(self):
        """ AcceptTcpClientAsync(self: TcpListener) -> Task[TcpClient] """
        pass

    def AllowNatTraversal(self, allowed):
        """
        AllowNatTraversal(self: TcpListener, allowed: bool)
            Enables or disables Network Address Translation (NAT) traversal on a 
             System.Net.Sockets.TcpListener instance.
        
        
            allowed: A Boolean value that specifies whether to enable or disable NAT traversal.
        """
        pass

    def BeginAcceptSocket(self, callback, state):
        """
        BeginAcceptSocket(self: TcpListener, callback: AsyncCallback, state: object) -> IAsyncResult
        
            Begins an asynchronous operation to accept an incoming connection attempt.
        
            callback: An System.AsyncCallback delegate that references the method to invoke when the operation is 
             complete.
        
            state: A user-defined object containing information about the accept operation. This object is passed 
             to the callback delegate when the operation is complete.
        
            Returns: An System.IAsyncResult that references the asynchronous creation of the 
             System.Net.Sockets.Socket.
        """
        pass

    def BeginAcceptTcpClient(self, callback, state):
        """
        BeginAcceptTcpClient(self: TcpListener, callback: AsyncCallback, state: object) -> IAsyncResult
        
            Begins an asynchronous operation to accept an incoming connection attempt.
        
            callback: An System.AsyncCallback delegate that references the method to invoke when the operation is 
             complete.
        
            state: A user-defined object containing information about the accept operation. This object is passed 
             to the callback delegate when the operation is complete.
        
            Returns: An System.IAsyncResult that references the asynchronous creation of the 
             System.Net.Sockets.TcpClient.
        """
        pass

    @staticmethod
    def Create(port):
        """ Create(port: int) -> TcpListener """
        pass

    def EndAcceptSocket(self, asyncResult):
        """
        EndAcceptSocket(self: TcpListener, asyncResult: IAsyncResult) -> Socket
        
            Asynchronously accepts an incoming connection attempt and creates a new 
             System.Net.Sockets.Socket to handle remote host communication.
        
        
            asyncResult: An System.IAsyncResult returned by a call to the 
             System.Net.Sockets.TcpListener.BeginAcceptSocket(System.AsyncCallback,System.Object)  method.
        
            Returns: A System.Net.Sockets.Socket.
        """
        pass

    def EndAcceptTcpClient(self, asyncResult):
        """
        EndAcceptTcpClient(self: TcpListener, asyncResult: IAsyncResult) -> TcpClient
        
            Asynchronously accepts an incoming connection attempt and creates a new 
             System.Net.Sockets.TcpClient to handle remote host communication.
        
        
            asyncResult: An System.IAsyncResult returned by a call to the 
             System.Net.Sockets.TcpListener.BeginAcceptTcpClient(System.AsyncCallback,System.Object) method.
        
            Returns: A System.Net.Sockets.TcpClient.
        """
        pass

    def Pending(self):
        """
        Pending(self: TcpListener) -> bool
        
            Determines if there are pending connection requests.
            Returns: true if connections are pending; otherwise, false.
        """
        pass

    def Start(self, backlog=None):
        """
        Start(self: TcpListener, backlog: int)
            Starts listening for incoming connection requests with a maximum number of pending connection.
        
            backlog: The maximum length of the pending connections queue.
        Start(self: TcpListener)
            Starts listening for incoming connection requests.
        """
        pass

    def Stop(self):
        """
        Stop(self: TcpListener)
            Closes the listener.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, localEP: IPEndPoint)
        __new__(cls: type, localaddr: IPAddress, port: int)
        __new__(cls: type, port: int)
        """
        pass

    Active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether System.Net.Sockets.TcpListener is actively listening for client connections.

"""

    ExclusiveAddressUse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Boolean value that specifies whether the System.Net.Sockets.TcpListener allows only one underlying socket to listen to a specific port.

Get: ExclusiveAddressUse(self: TcpListener) -> bool

Set: ExclusiveAddressUse(self: TcpListener) = value
"""

    LocalEndpoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the underlying System.Net.EndPoint of the current System.Net.Sockets.TcpListener.

Get: LocalEndpoint(self: TcpListener) -> EndPoint

"""

    Server = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the underlying network System.Net.Sockets.Socket.

Get: Server(self: TcpListener) -> Socket

"""



class TransmitFileOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    The System.Net.Sockets.TransmitFileOptions enumeration defines values used in file transfer requests.
    
    enum (flags) TransmitFileOptions, values: Disconnect (1), ReuseSocket (2), UseDefaultWorkerThread (0), UseKernelApc (32), UseSystemThread (16), WriteBehind (4)
    """
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

    Disconnect = None
    ReuseSocket = None
    UseDefaultWorkerThread = None
    UseKernelApc = None
    UseSystemThread = None
    value__ = None
    WriteBehind = None


class UdpClient(object, IDisposable):
    """
    Provides User Datagram Protocol (UDP) network services.
    
    UdpClient()
    UdpClient(family: AddressFamily)
    UdpClient(port: int)
    UdpClient(port: int, family: AddressFamily)
    UdpClient(localEP: IPEndPoint)
    UdpClient(hostname: str, port: int)
    """
    def AllowNatTraversal(self, allowed):
        """
        AllowNatTraversal(self: UdpClient, allowed: bool)
            Enables or disables Network Address Translation (NAT) traversal on a 
             System.Net.Sockets.UdpClient instance.
        
        
            allowed: A Boolean value that specifies whether to enable or disable NAT traversal.
        """
        pass

    def BeginReceive(self, requestCallback, state):
        """
        BeginReceive(self: UdpClient, requestCallback: AsyncCallback, state: object) -> IAsyncResult
        
            Receives a datagram from a remote host asynchronously.
        
            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is 
             complete.
        
            state: A user-defined object that contains information about the receive operation. This object is 
             passed to the requestCallback delegate when the operation is complete.
        
            Returns: An System.IAsyncResult object that references the asynchronous receive.
        """
        pass

    def BeginSend(self, datagram, bytes, *__args):
        """
        BeginSend(self: UdpClient, datagram: Array[Byte], bytes: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult
        
            Sends a datagram to a remote host asynchronously. The destination was specified previously by a 
             call to erload:System.Net.Sockets.UdpClient.Connect.
        
        
            datagram: A System.Byte array that contains the data to be sent.
            bytes: The number of bytes to send.
            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is 
             complete.
        
            state: A user-defined object that contains information about the send operation. This object is passed 
             to the requestCallback delegate when the operation is complete.
        
            Returns: An System.IAsyncResult object that references the asynchronous send.
        BeginSend(self: UdpClient, datagram: Array[Byte], bytes: int, hostname: str, port: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult
        
            Sends a datagram to a destination asynchronously. The destination is specified by the host name 
             and port number.
        
        
            datagram: A System.Byte array that contains the data to be sent.
            bytes: The number of bytes to send.
            hostname: The destination host.
            port: The destination port number.
            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is 
             complete.
        
            state: A user-defined object that contains information about the send operation. This object is passed 
             to the requestCallback delegate when the operation is complete.
        
            Returns: An System.IAsyncResult object that references the asynchronous send.
        BeginSend(self: UdpClient, datagram: Array[Byte], bytes: int, endPoint: IPEndPoint, requestCallback: AsyncCallback, state: object) -> IAsyncResult
        
            Sends a datagram to a destination asynchronously. The destination is specified by a 
             System.Net.EndPoint.
        
        
            datagram: A System.Byte array that contains the data to be sent.
            bytes: The number of bytes to send.
            endPoint: The System.Net.EndPoint that represents the destination for the data.
            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is 
             complete.
        
            state: A user-defined object that contains information about the send operation. This object is passed 
             to the requestCallback delegate when the operation is complete.
        
            Returns: An System.IAsyncResult object that references the asynchronous send.
        """
        pass

    def Close(self):
        """
        Close(self: UdpClient)
            Closes the UDP connection.
        """
        pass

    def Connect(self, *__args):
        """
        Connect(self: UdpClient, endPoint: IPEndPoint)
            Establishes a default remote host using the specified network endpoint.
        
            endPoint: An System.Net.IPEndPoint that specifies the network endpoint to which you intend to send data.
        Connect(self: UdpClient, addr: IPAddress, port: int)
            Establishes a default remote host using the specified IP address and port number.
        
            addr: The System.Net.IPAddress of the remote host to which you intend to send data.
            port: The port number to which you intend send data.
        Connect(self: UdpClient, hostname: str, port: int)
            Establishes a default remote host using the specified host name and port number.
        
            hostname: The DNS name of the remote host to which you intend send data.
            port: The port number on the remote host to which you intend to send data.
        """
        pass

    def Dispose(self):
        """ Dispose(self: UdpClient) """
        pass

    def DropMulticastGroup(self, multicastAddr, ifindex=None):
        """
        DropMulticastGroup(self: UdpClient, multicastAddr: IPAddress, ifindex: int)
            Leaves a multicast group.
        
            multicastAddr: The System.Net.IPAddress of the multicast group to leave.
            ifindex: The interface index associated with the local IP address joined to the multicast group.
        DropMulticastGroup(self: UdpClient, multicastAddr: IPAddress)
            Leaves a multicast group.
        
            multicastAddr: The System.Net.IPAddress of the multicast group to leave.
        """
        pass

    def EndReceive(self, asyncResult, remoteEP):
        """
        EndReceive(self: UdpClient, asyncResult: IAsyncResult, remoteEP: IPEndPoint) -> (Array[Byte], IPEndPoint)
        
            Ends a pending asynchronous receive.
        
            asyncResult: An System.IAsyncResult object returned by a call to 
             System.Net.Sockets.UdpClient.BeginReceive(System.AsyncCallback,System.Object).
        
            remoteEP: The specified remote endpoint.
            Returns: If successful, the number of bytes received. If unsuccessful, this method returns 0.
        """
        pass

    def EndSend(self, asyncResult):
        """
        EndSend(self: UdpClient, asyncResult: IAsyncResult) -> int
        
            Ends a pending asynchronous send.
        
            asyncResult: An System.IAsyncResult object returned by a call to 
             erload:System.Net.Sockets.UdpClient.BeginSend.
        
            Returns: If successful, the number of bytes sent to the System.Net.Sockets.UdpClient.
        """
        pass

    def JoinMulticastGroup(self, *__args):
        """
        JoinMulticastGroup(self: UdpClient, ifindex: int, multicastAddr: IPAddress)
            Adds a System.Net.Sockets.UdpClient to a multicast group.
        
            ifindex: The interface index associated with the local IP address on which to join the multicast group.
            multicastAddr: The multicast System.Net.IPAddress of the group you want to join.
        JoinMulticastGroup(self: UdpClient, multicastAddr: IPAddress, timeToLive: int)
            Adds a System.Net.Sockets.UdpClient to a multicast group with the specified Time to Live (TTL).
        
            multicastAddr: The System.Net.IPAddress of the multicast group to join.
            timeToLive: The Time to Live (TTL), measured in router hops.
        JoinMulticastGroup(self: UdpClient, multicastAddr: IPAddress)
            Adds a System.Net.Sockets.UdpClient to a multicast group.
        
            multicastAddr: The multicast System.Net.IPAddress of the group you want to join.
        JoinMulticastGroup(self: UdpClient, multicastAddr: IPAddress, localAddress: IPAddress)
            Adds a System.Net.Sockets.UdpClient to a multicast group.
        
            multicastAddr: The multicast System.Net.IPAddress of the group you want to join.
            localAddress: The local System.Net.IPAddress.
        """
        pass

    def Receive(self, remoteEP):
        """
        Receive(self: UdpClient, remoteEP: IPEndPoint) -> (Array[Byte], IPEndPoint)
        
            Returns a UDP datagram that was sent by a remote host.
        
            remoteEP: An System.Net.IPEndPoint that represents the remote host from which the data was sent.
            Returns: An array of type System.Byte that contains datagram data.
        """
        pass

    def ReceiveAsync(self):
        """ ReceiveAsync(self: UdpClient) -> Task[UdpReceiveResult] """
        pass

    def Send(self, dgram, bytes, *__args):
        """
        Send(self: UdpClient, dgram: Array[Byte], bytes: int) -> int
        
            Sends a UDP datagram to a remote host.
        
            dgram: An array of type System.Byte that specifies the UDP datagram that you intend to send represented 
             as an array of bytes.
        
            bytes: The number of bytes in the datagram.
            Returns: The number of bytes sent.
        Send(self: UdpClient, dgram: Array[Byte], bytes: int, hostname: str, port: int) -> int
        
            Sends a UDP datagram to a specified port on a specified remote host.
        
            dgram: An array of type System.Byte that specifies the UDP datagram that you intend to send represented 
             as an array of bytes.
        
            bytes: The number of bytes in the datagram.
            hostname: The name of the remote host to which you intend to send the datagram.
            port: The remote port number with which you intend to communicate.
            Returns: The number of bytes sent.
        Send(self: UdpClient, dgram: Array[Byte], bytes: int, endPoint: IPEndPoint) -> int
        
            Sends a UDP datagram to the host at the specified remote endpoint.
        
            dgram: An array of type System.Byte that specifies the UDP datagram that you intend to send, 
             represented as an array of bytes.
        
            bytes: The number of bytes in the datagram.
            endPoint: An System.Net.IPEndPoint that represents the host and port to which to send the datagram.
            Returns: The number of bytes sent.
        """
        pass

    def SendAsync(self, datagram, bytes, *__args):
        """
        SendAsync(self: UdpClient, datagram: Array[Byte], bytes: int, hostname: str, port: int) -> Task[int]
        SendAsync(self: UdpClient, datagram: Array[Byte], bytes: int, endPoint: IPEndPoint) -> Task[int]
        SendAsync(self: UdpClient, datagram: Array[Byte], bytes: int) -> Task[int]
        """
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, family: AddressFamily)
        __new__(cls: type, port: int)
        __new__(cls: type, port: int, family: AddressFamily)
        __new__(cls: type, localEP: IPEndPoint)
        __new__(cls: type, hostname: str, port: int)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether a default remote host has been established.

"""

    Available = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of data received from the network that is available to read.

Get: Available(self: UdpClient) -> int

"""

    Client = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the underlying network System.Net.Sockets.Socket.

Get: Client(self: UdpClient) -> Socket

Set: Client(self: UdpClient) = value
"""

    DontFragment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Boolean value that specifies whether the System.Net.Sockets.UdpClient allows Internet Protocol (IP) datagrams to be fragmented.

Get: DontFragment(self: UdpClient) -> bool

Set: DontFragment(self: UdpClient) = value
"""

    EnableBroadcast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Boolean value that specifies whether the System.Net.Sockets.UdpClient may send or receive broadcast packets.

Get: EnableBroadcast(self: UdpClient) -> bool

Set: EnableBroadcast(self: UdpClient) = value
"""

    ExclusiveAddressUse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Boolean value that specifies whether the System.Net.Sockets.UdpClient allows only one client to use a port.

Get: ExclusiveAddressUse(self: UdpClient) -> bool

Set: ExclusiveAddressUse(self: UdpClient) = value
"""

    MulticastLoopback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Boolean value that specifies whether outgoing multicast packets are delivered to the sending application.

Get: MulticastLoopback(self: UdpClient) -> bool

Set: MulticastLoopback(self: UdpClient) = value
"""

    Ttl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that specifies the Time to Live (TTL) value of Internet Protocol (IP) packets sent by the System.Net.Sockets.UdpClient.

Get: Ttl(self: UdpClient) -> Int16

Set: Ttl(self: UdpClient) = value
"""



class UdpReceiveResult(object, IEquatable[UdpReceiveResult]):
    """ UdpReceiveResult(buffer: Array[Byte], remoteEndPoint: IPEndPoint) """
    def Equals(self, *__args):
        """
        Equals(self: UdpReceiveResult, other: UdpReceiveResult) -> bool
        Equals(self: UdpReceiveResult, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: UdpReceiveResult) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, buffer, remoteEndPoint):
        """
        __new__[UdpReceiveResult]() -> UdpReceiveResult
        
        __new__(cls: type, buffer: Array[Byte], remoteEndPoint: IPEndPoint)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Buffer(self: UdpReceiveResult) -> Array[Byte]

"""

    RemoteEndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RemoteEndPoint(self: UdpReceiveResult) -> IPEndPoint

"""



