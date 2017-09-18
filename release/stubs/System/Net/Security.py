# encoding: utf-8
# module System.Net.Security calls itself Security
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class AuthenticatedStream(Stream, IDisposable):
    """ Provides methods for passing credentials across a stream and requesting or performing authentication for client-server applications. """
    def CreateWaitHandle(self, *args): #cannot find CLR method
        """
        CreateWaitHandle(self: Stream) -> WaitHandle
        
            Allocates a System.Threading.WaitHandle object.
            Returns: A reference to the allocated WaitHandle.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: AuthenticatedStream, disposing: bool)
            Releases the unmanaged resources used by the System.Net.Security.AuthenticatedStream and 
             optionally releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
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
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, innerStream: Stream, leaveInnerStreamOpen: bool) """
        pass

    InnerStream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the stream used by this System.Net.Security.AuthenticatedStream for sending and receiving data.

"""

    IsAuthenticated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether authentication was successful.

Get: IsAuthenticated(self: AuthenticatedStream) -> bool

"""

    IsEncrypted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether data sent using this System.Net.Security.AuthenticatedStream is encrypted.

Get: IsEncrypted(self: AuthenticatedStream) -> bool

"""

    IsMutuallyAuthenticated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether both server and client have been authenticated.

Get: IsMutuallyAuthenticated(self: AuthenticatedStream) -> bool

"""

    IsServer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether the local side of the connection was authenticated as the server.

Get: IsServer(self: AuthenticatedStream) -> bool

"""

    IsSigned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether the data sent using this stream is signed.

Get: IsSigned(self: AuthenticatedStream) -> bool

"""

    LeaveInnerStreamOpen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether the stream used by this System.Net.Security.AuthenticatedStream for sending and receiving data has been left open.

Get: LeaveInnerStreamOpen(self: AuthenticatedStream) -> bool

"""



class AuthenticationLevel(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies client requirements for authentication and impersonation when using the System.Net.WebRequest class and derived classes to request a resource.
    
    enum AuthenticationLevel, values: MutualAuthRequested (1), MutualAuthRequired (2), None (0)
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

    MutualAuthRequested = None
    MutualAuthRequired = None
    None = None
    value__ = None


class EncryptionPolicy(Enum, IComparable, IFormattable, IConvertible):
    """
    The EncryptionPolicy to use.
    
    enum EncryptionPolicy, values: AllowNoEncryption (1), NoEncryption (2), RequireEncryption (0)
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

    AllowNoEncryption = None
    NoEncryption = None
    RequireEncryption = None
    value__ = None


class LocalCertificateSelectionCallback(MulticastDelegate, ICloneable, ISerializable):
    """
    Selects the local Secure Sockets Layer (SSL) certificate used for authentication.
    
    LocalCertificateSelectionCallback(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, targetHost, localCertificates, remoteCertificate, acceptableIssuers, callback, object):
        """ BeginInvoke(self: LocalCertificateSelectionCallback, sender: object, targetHost: str, localCertificates: X509CertificateCollection, remoteCertificate: X509Certificate, acceptableIssuers: Array[str], callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: LocalCertificateSelectionCallback, result: IAsyncResult) -> X509Certificate """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, targetHost, localCertificates, remoteCertificate, acceptableIssuers):
        """ Invoke(self: LocalCertificateSelectionCallback, sender: object, targetHost: str, localCertificates: X509CertificateCollection, remoteCertificate: X509Certificate, acceptableIssuers: Array[str]) -> X509Certificate """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class NegotiateStream(AuthenticatedStream, IDisposable):
    """
    Provides a stream that uses the Negotiate security protocol to authenticate the client, and optionally the server, in client-server communication.
    
    NegotiateStream(innerStream: Stream)
    NegotiateStream(innerStream: Stream, leaveInnerStreamOpen: bool)
    """
    def AuthenticateAsClient(self, credential=None, *__args):
        """
        AuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel)
            Called by clients to authenticate the client, and optionally the server, in a client-server 
             connection. The authentication process uses the specified credentials and authentication 
             options.
        
        
            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.
            targetName: The Service Principal Name (SPN) that uniquely identifies the server to authenticate.
            requiredProtectionLevel: One of the System.Net.Security.ProtectionLevel values, indicating the security services for the 
             stream.
        
            allowedImpersonationLevel: One of the System.Security.Principal.TokenImpersonationLevel values, indicating how the server 
             can use the client's credentials to access resources.
        
        AuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, binding: ChannelBinding, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel)
            Called by clients to authenticate the client, and optionally the server, in a client-server 
             connection. The authentication process uses the specified credential, authentication options, 
             and channel binding.
        
        
            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.
            binding: The System.Security.Authentication.ExtendedProtection.ChannelBinding that is used for extended 
             protection.
        
            targetName: The Service Principal Name (SPN) that uniquely identifies the server to authenticate.
            requiredProtectionLevel: One of the System.Net.Security.ProtectionLevel values, indicating the security services for the 
             stream.
        
            allowedImpersonationLevel: One of the System.Security.Principal.TokenImpersonationLevel values, indicating how the server 
             can use the client's credentials to access resources.
        
        AuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, binding: ChannelBinding, targetName: str)
            Called by clients to authenticate the client, and optionally the server, in a client-server 
             connection. The authentication process uses the specified client credential and the channel 
             binding.
        
        
            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.
            binding: The System.Security.Authentication.ExtendedProtection.ChannelBinding that is used for extended 
             protection.
        
            targetName: The Service Principal Name (SPN) that uniquely identifies the server to authenticate.
        AuthenticateAsClient(self: NegotiateStream)
            Called by clients to authenticate the client, and optionally the server, in a client-server 
             connection.
        
        AuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, targetName: str)
            Called by clients to authenticate the client, and optionally the server, in a client-server 
             connection. The authentication process uses the specified client credential.
        
        
            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.
            targetName: The Service Principal Name (SPN) that uniquely identifies the server to authenticate.
        """
        pass

    def AuthenticateAsClientAsync(self, credential=None, *__args):
        """
        AuthenticateAsClientAsync(self: NegotiateStream, credential: NetworkCredential, binding: ChannelBinding, targetName: str) -> Task
        AuthenticateAsClientAsync(self: NegotiateStream, credential: NetworkCredential, binding: ChannelBinding, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel) -> Task
        AuthenticateAsClientAsync(self: NegotiateStream, credential: NetworkCredential, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel) -> Task
        AuthenticateAsClientAsync(self: NegotiateStream) -> Task
        AuthenticateAsClientAsync(self: NegotiateStream, credential: NetworkCredential, targetName: str) -> Task
        """
        pass

    def AuthenticateAsServer(self, *__args):
        """
        AuthenticateAsServer(self: NegotiateStream, credential: NetworkCredential, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel)
            Called by servers to authenticate the client, and optionally the server, in a client-server 
             connection. The authentication process uses the specified server credentials and authentication 
             options.
        
        
            credential: The System.Net.NetworkCredential that is used to establish the identity of the server.
            requiredProtectionLevel: One of the System.Net.Security.ProtectionLevel values, indicating the security services for the 
             stream.
        
            requiredImpersonationLevel: One of the System.Security.Principal.TokenImpersonationLevel values, indicating how the server 
             can use the client's credentials to access resources.
        
        AuthenticateAsServer(self: NegotiateStream, credential: NetworkCredential, policy: ExtendedProtectionPolicy, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel)
            Called by servers to authenticate the client, and optionally the server, in a client-server 
             connection. The authentication process uses the specified server credentials, authentication 
             options, and extended protection policy.
        
        
            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.
            policy: The System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy that is used for 
             extended protection.
        
            requiredProtectionLevel: One of the System.Net.Security.ProtectionLevel values, indicating the security services for the 
             stream.
        
            requiredImpersonationLevel: One of the System.Security.Principal.TokenImpersonationLevel values, indicating how the server 
             can use the client's credentials to access resources.
        
        AuthenticateAsServer(self: NegotiateStream)
            Called by servers to authenticate the client, and optionally the server, in a client-server 
             connection.
        
        AuthenticateAsServer(self: NegotiateStream, policy: ExtendedProtectionPolicy)
            Called by servers to authenticate the client, and optionally the server, in a client-server 
             connection. The authentication process uses the specified extended protection policy.
        
        
            policy: The System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy that is used for 
             extended protection.
        """
        pass

    def AuthenticateAsServerAsync(self, *__args):
        """
        AuthenticateAsServerAsync(self: NegotiateStream, credential: NetworkCredential, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel) -> Task
        AuthenticateAsServerAsync(self: NegotiateStream, credential: NetworkCredential, policy: ExtendedProtectionPolicy, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel) -> Task
        AuthenticateAsServerAsync(self: NegotiateStream) -> Task
        AuthenticateAsServerAsync(self: NegotiateStream, policy: ExtendedProtectionPolicy) -> Task
        """
        pass

    def BeginAuthenticateAsClient(self, *__args):
        """
        BeginAuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        
            Called by clients to begin an asynchronous operation to authenticate the client, and optionally 
             the server, in a client-server connection. The authentication process uses the specified 
             credentials and authentication options. This method does not block.
        
        
            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.
            targetName: The Service Principal Name (SPN) that uniquely identifies the server to authenticate.
            requiredProtectionLevel: One of the System.Net.Security.ProtectionLevel values, indicating the security services for the 
             stream.
        
            allowedImpersonationLevel: One of the System.Security.Principal.TokenImpersonationLevel values, indicating how the server 
             can use the client's credentials to access resources.
        
            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is 
             complete.
        
            asyncState: A user-defined object containing information about the write operation. This object is passed to 
             the asyncCallback delegate when the operation completes.
        
            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.
        BeginAuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, binding: ChannelBinding, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        
            Called by clients to begin an asynchronous operation to authenticate the client, and optionally 
             the server, in a client-server connection. The authentication process uses the specified 
             credentials, authentication options, and channel binding. This method does not block.
        
        
            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.
            binding: The System.Security.Authentication.ExtendedProtection.ChannelBinding that is used for extended 
             protection.
        
            targetName: The Service Principal Name (SPN) that uniquely identifies the server to authenticate.
            requiredProtectionLevel: One of the System.Net.Security.ProtectionLevel values, indicating the security services for the 
             stream.
        
            allowedImpersonationLevel: One of the System.Security.Principal.TokenImpersonationLevel values, indicating how the server 
             can use the client's credentials to access resources.
        
            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is 
             complete.
        
            asyncState: A user-defined object containing information about the write operation. This object is passed to 
             the asyncCallback delegate when the operation completes.
        
            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.
        BeginAuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, binding: ChannelBinding, targetName: str, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        
            Called by clients to begin an asynchronous operation to authenticate the client, and optionally 
             the server, in a client-server connection. The authentication process uses the specified 
             credentials and channel binding. This method does not block.
        
        
            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.
            binding: The System.Security.Authentication.ExtendedProtection.ChannelBinding that is used for extended 
             protection.
        
            targetName: The Service Principal Name (SPN) that uniquely identifies the server to authenticate.
            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is 
             complete.
        
            asyncState: A user-defined object containing information about the write operation. This object is passed to 
             the asyncCallback delegate when the operation completes.
        
            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.
        BeginAuthenticateAsClient(self: NegotiateStream, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        
            Called by clients to begin an asynchronous operation to authenticate the client, and optionally 
             the server, in a client-server connection. This method does not block.
        
        
            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is 
             complete.
        
            asyncState: A user-defined object containing information about the operation. This object is passed to the 
             asyncCallback delegate when the operation completes.
        
            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.
        BeginAuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, targetName: str, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        
            Called by clients to begin an asynchronous operation to authenticate the client, and optionally 
             the server, in a client-server connection. The authentication process uses the specified 
             credentials. This method does not block.
        
        
            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.
            targetName: The Service Principal Name (SPN) that uniquely identifies the server to authenticate.
            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is 
             complete.
        
            asyncState: A user-defined object containing information about the write operation. This object is passed to 
             the asyncCallback delegate when the operation completes.
        
            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.
        """
        pass

    def BeginAuthenticateAsServer(self, *__args):
        """
        BeginAuthenticateAsServer(self: NegotiateStream, credential: NetworkCredential, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        
            Called by servers to begin an asynchronous operation to authenticate the client, and optionally 
             the server, in a client-server connection. The authentication process uses the specified server 
             credentials and authentication options. This method does not block.
        
        
            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.
            requiredProtectionLevel: One of the System.Net.Security.ProtectionLevel values, indicating the security services for the 
             stream.
        
            requiredImpersonationLevel: One of the System.Security.Principal.TokenImpersonationLevel values, indicating how the server 
             can use the client's credentials to access resources.
        
            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is 
             complete.
        
            asyncState: A user-defined object containing information about the operation. This object is passed to the 
             asyncCallback delegate when the operation completes.
        
            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.
        BeginAuthenticateAsServer(self: NegotiateStream, credential: NetworkCredential, policy: ExtendedProtectionPolicy, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        
            Called by servers to begin an asynchronous operation to authenticate the client, and optionally 
             the server, in a client-server connection. The authentication process uses the specified server 
             credentials, authentication options, and extended protection policy. This method does not block.
        
        
            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.
            policy: The System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy that is used for 
             extended protection.
        
            requiredProtectionLevel: One of the System.Net.Security.ProtectionLevel values, indicating the security services for the 
             stream.
        
            requiredImpersonationLevel: One of the System.Security.Principal.TokenImpersonationLevel values, indicating how the server 
             can use the client's credentials to access resources.
        
            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is 
             complete.
        
            asyncState: A user-defined object containing information about the write operation. This object is passed to 
             the asyncCallback delegate when the operation completes.
        
            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.
        BeginAuthenticateAsServer(self: NegotiateStream, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        
            Called by servers to begin an asynchronous operation to authenticate the client, and optionally 
             the server, in a client-server connection. This method does not block.
        
        
            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is 
             complete.
        
            asyncState: A user-defined object containing information about the operation. This object is passed to the 
             asyncCallback delegate when the operation completes.
        
            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.
        BeginAuthenticateAsServer(self: NegotiateStream, policy: ExtendedProtectionPolicy, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        
            Called by servers to begin an asynchronous operation to authenticate the client, and optionally 
             the server, in a client-server connection. The authentication process uses the specified 
             extended protection policy. This method does not block.
        
        
            policy: The System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy that is used for 
             extended protection.
        
            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is 
             complete.
        
            asyncState: A user-defined object containing information about the write operation. This object is passed to 
             the asyncCallback delegate when the operation completes.
        
            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.
        """
        pass

    def BeginRead(self, buffer, offset, count, asyncCallback, asyncState):
        """
        BeginRead(self: NegotiateStream, buffer: Array[Byte], offset: int, count: int, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        
            Begins an asynchronous read operation that reads data from the stream and stores it in the 
             specified array.
        
        
            buffer: A System.Byte array that receives the bytes read from the stream.
            offset: The zero-based location in buffer at which to begin storing the data read from this stream.
            count: The maximum number of bytes to read from the stream.
            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the read operation is 
             complete.
        
            asyncState: A user-defined object containing information about the read operation. This object is passed to 
             the asyncCallback delegate when the operation completes.
        
            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.
        """
        pass

    def BeginWrite(self, buffer, offset, count, asyncCallback, asyncState):
        """
        BeginWrite(self: NegotiateStream, buffer: Array[Byte], offset: int, count: int, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        
            Begins an asynchronous write operation that writes System.Bytes from the specified buffer to the 
             stream.
        
        
            buffer: A System.Byte array that supplies the bytes to be written to the stream.
            offset: The zero-based location in buffer at which to begin reading bytes to be written to the stream.
            count: An System.Int32 value that specifies the number of bytes to read from buffer.
            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the write operation 
             is complete.
        
            asyncState: A user-defined object containing information about the write operation. This object is passed to 
             the asyncCallback delegate when the operation completes.
        
            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.
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
        Dispose(self: NegotiateStream, disposing: bool)
            Releases the unmanaged resources used by the System.Net.Security.NegotiateStream and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def EndAuthenticateAsClient(self, asyncResult):
        """
        EndAuthenticateAsClient(self: NegotiateStream, asyncResult: IAsyncResult)
            Ends a pending asynchronous client authentication operation that was started with a call to 
             erload:System.Net.Security.NegotiateStream.BeginAuthenticateAsClient.
        
        
            asyncResult: An System.IAsyncResult instance returned by a call to 
             erload:System.Net.Security.NegotiateStream.BeginAuthenticateAsClient.
        """
        pass

    def EndAuthenticateAsServer(self, asyncResult):
        """
        EndAuthenticateAsServer(self: NegotiateStream, asyncResult: IAsyncResult)
            Ends a pending asynchronous client authentication operation that was started with a call to 
             erload:System.Net.Security.NegotiateStream.BeginAuthenticateAsServer.
        
        
            asyncResult: An System.IAsyncResult instance returned by a call to 
             erload:System.Net.Security.NegotiateStream.BeginAuthenticateAsServer.
        """
        pass

    def EndRead(self, asyncResult):
        """
        EndRead(self: NegotiateStream, asyncResult: IAsyncResult) -> int
        
            Ends an asynchronous read operation that was started with a call to 
             System.Net.Security.NegotiateStream.BeginRead(System.Byte[],System.Int32,System.Int32,System.Asyn
             cCallback,System.Object).
        
        
            asyncResult: An System.IAsyncResult instance returned by a call to 
             System.Net.Security.NegotiateStream.BeginRead(System.Byte[],System.Int32,System.Int32,System.Asyn
             cCallback,System.Object)
        
            Returns: A System.Int32 value that specifies the number of bytes read from the underlying stream.
        """
        pass

    def EndWrite(self, asyncResult):
        """
        EndWrite(self: NegotiateStream, asyncResult: IAsyncResult)
            Ends an asynchronous write operation that was started with a call to 
             System.Net.Security.NegotiateStream.BeginWrite(System.Byte[],System.Int32,System.Int32,System.Asy
             ncCallback,System.Object).
        
        
            asyncResult: An System.IAsyncResult instance returned by a call to 
             System.Net.Security.NegotiateStream.BeginWrite(System.Byte[],System.Int32,System.Int32,System.Asy
             ncCallback,System.Object)
        """
        pass

    def Flush(self):
        """
        Flush(self: NegotiateStream)
            Causes any buffered data to be written to the underlying device.
        """
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

    def Read(self, buffer, offset, count):
        """
        Read(self: NegotiateStream, buffer: Array[Byte], offset: int, count: int) -> int
        
            Reads data from this stream and stores it in the specified array.
        
            buffer: A System.Byte array that receives the bytes read from the stream.
            offset: A System.Int32 containing the zero-based location in buffer at which to begin storing the data 
             read from this stream.
        
            count: A System.Int32 containing the maximum number of bytes to read from the stream.
            Returns: A System.Int32 value that specifies the number of bytes read from the underlying stream. When 
             there is no more data to be read, returns 0.
        """
        pass

    def Seek(self, offset, origin):
        """
        Seek(self: NegotiateStream, offset: Int64, origin: SeekOrigin) -> Int64
        
            Throws System.NotSupportedException.
        
            offset: This value is ignored.
            origin: This value is ignored.
            Returns: Always throws a System.NotSupportedException.
        """
        pass

    def SetLength(self, value):
        """
        SetLength(self: NegotiateStream, value: Int64)
            Sets the length of the underlying stream.
        
            value: An System.Int64 value that specifies the length of the stream.
        """
        pass

    def Write(self, buffer, offset, count):
        """
        Write(self: NegotiateStream, buffer: Array[Byte], offset: int, count: int)
            Write the specified number of System.Bytes to the underlying stream using the specified buffer 
             and offset.
        
        
            buffer: A System.Byte array that supplies the bytes written to the stream.
            offset: An System.Int32 containing the zero-based location in buffer at which to begin reading bytes to 
             be written to the stream.
        
            count: A System.Int32 containing the number of bytes to read from buffer.
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
    def __new__(self, innerStream, leaveInnerStreamOpen=None):
        """
        __new__(cls: type, innerStream: Stream)
        __new__(cls: type, innerStream: Stream, leaveInnerStreamOpen: bool)
        """
        pass

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether the underlying stream is readable.

Get: CanRead(self: NegotiateStream) -> bool

"""

    CanSeek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether the underlying stream is seekable.

Get: CanSeek(self: NegotiateStream) -> bool

"""

    CanTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether the underlying stream supports time-outs.

Get: CanTimeout(self: NegotiateStream) -> bool

"""

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether the underlying stream is writable.

Get: CanWrite(self: NegotiateStream) -> bool

"""

    ImpersonationLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates how the server can use the client's credentials.

Get: ImpersonationLevel(self: NegotiateStream) -> TokenImpersonationLevel

"""

    InnerStream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the stream used by this System.Net.Security.AuthenticatedStream for sending and receiving data.

"""

    IsAuthenticated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether authentication was successful.

Get: IsAuthenticated(self: NegotiateStream) -> bool

"""

    IsEncrypted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether this System.Net.Security.NegotiateStream uses data encryption.

Get: IsEncrypted(self: NegotiateStream) -> bool

"""

    IsMutuallyAuthenticated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether both the server and the client have been authenticated.

Get: IsMutuallyAuthenticated(self: NegotiateStream) -> bool

"""

    IsServer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether the local side of the connection used by this System.Net.Security.NegotiateStream was authenticated as the server.

Get: IsServer(self: NegotiateStream) -> bool

"""

    IsSigned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether the data sent using this stream is signed.

Get: IsSigned(self: NegotiateStream) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length of the underlying stream.

Get: Length(self: NegotiateStream) -> Int64

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current position in the underlying stream.

Get: Position(self: NegotiateStream) -> Int64

Set: Position(self: NegotiateStream) = value
"""

    ReadTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the amount of time a read operation blocks waiting for data.

Get: ReadTimeout(self: NegotiateStream) -> int

Set: ReadTimeout(self: NegotiateStream) = value
"""

    RemoteIdentity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets information about the identity of the remote party sharing this authenticated stream.

Get: RemoteIdentity(self: NegotiateStream) -> IIdentity

"""

    WriteTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the amount of time a write operation blocks waiting for data.

Get: WriteTimeout(self: NegotiateStream) -> int

Set: WriteTimeout(self: NegotiateStream) = value
"""



class ProtectionLevel(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates the security services requested for an authenticated stream.
    
    enum ProtectionLevel, values: EncryptAndSign (2), None (0), Sign (1)
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

    EncryptAndSign = None
    None = None
    Sign = None
    value__ = None


class RemoteCertificateValidationCallback(MulticastDelegate, ICloneable, ISerializable):
    """
    Verifies the remote Secure Sockets Layer (SSL) certificate used for authentication.
    
    RemoteCertificateValidationCallback(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, certificate, chain, sslPolicyErrors, callback, object):
        """ BeginInvoke(self: RemoteCertificateValidationCallback, sender: object, certificate: X509Certificate, chain: X509Chain, sslPolicyErrors: SslPolicyErrors, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: RemoteCertificateValidationCallback, result: IAsyncResult) -> bool """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, certificate, chain, sslPolicyErrors):
        """ Invoke(self: RemoteCertificateValidationCallback, sender: object, certificate: X509Certificate, chain: X509Chain, sslPolicyErrors: SslPolicyErrors) -> bool """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class SslPolicyErrors(Enum, IComparable, IFormattable, IConvertible):
    """
    Enumerates Secure Socket Layer (SSL) policy errors.
    
    enum (flags) SslPolicyErrors, values: None (0), RemoteCertificateChainErrors (4), RemoteCertificateNameMismatch (2), RemoteCertificateNotAvailable (1)
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

    None = None
    RemoteCertificateChainErrors = None
    RemoteCertificateNameMismatch = None
    RemoteCertificateNotAvailable = None
    value__ = None


class SslStream(AuthenticatedStream, IDisposable):
    """
    Provides a stream used for client-server communication that uses the Secure Socket Layer (SSL) security protocol to authenticate the server and optionally the client.
    
    SslStream(innerStream: Stream, leaveInnerStreamOpen: bool, userCertificateValidationCallback: RemoteCertificateValidationCallback, userCertificateSelectionCallback: LocalCertificateSelectionCallback)
    SslStream(innerStream: Stream, leaveInnerStreamOpen: bool, userCertificateValidationCallback: RemoteCertificateValidationCallback, userCertificateSelectionCallback: LocalCertificateSelectionCallback, encryptionPolicy: EncryptionPolicy)
    SslStream(innerStream: Stream)
    SslStream(innerStream: Stream, leaveInnerStreamOpen: bool)
    SslStream(innerStream: Stream, leaveInnerStreamOpen: bool, userCertificateValidationCallback: RemoteCertificateValidationCallback)
    """
    def AuthenticateAsClient(self, targetHost, clientCertificates=None, *__args):
        """
        AuthenticateAsClient(self: SslStream, targetHost: str, clientCertificates: X509CertificateCollection, checkCertificateRevocation: bool)AuthenticateAsClient(self: SslStream, targetHost: str)
            Called by clients to authenticate the server and optionally the client in a client-server 
             connection.
        
        
            targetHost: The name of the server that shares this System.Net.Security.SslStream.
        AuthenticateAsClient(self: SslStream, targetHost: str, clientCertificates: X509CertificateCollection, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool)
            Called by clients to authenticate the server and optionally the client in a client-server 
             connection. The authentication process uses the specified certificate collection and SSL 
             protocol.
        
        
            targetHost: The name of the server that will share this System.Net.Security.SslStream.
            clientCertificates: The System.Security.Cryptography.X509Certificates.X509CertificateCollection that contains client 
             certificates.
        
            enabledSslProtocols: The System.Security.Authentication.SslProtocols value that represents the protocol used for 
             authentication.
        
            checkCertificateRevocation: A System.Boolean value that specifies whether the certificate revocation list is checked during 
             authentication.
        """
        pass

    def AuthenticateAsClientAsync(self, targetHost, clientCertificates=None, *__args):
        """
        AuthenticateAsClientAsync(self: SslStream, targetHost: str, clientCertificates: X509CertificateCollection, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool) -> Task
        AuthenticateAsClientAsync(self: SslStream, targetHost: str, clientCertificates: X509CertificateCollection, checkCertificateRevocation: bool) -> Task
        AuthenticateAsClientAsync(self: SslStream, targetHost: str) -> Task
        """
        pass

    def AuthenticateAsServer(self, serverCertificate, clientCertificateRequired=None, *__args):
        """
        AuthenticateAsServer(self: SslStream, serverCertificate: X509Certificate, clientCertificateRequired: bool, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool)
            Called by servers to begin an asynchronous operation to authenticate the server and optionally 
             the client using the specified certificates, requirements and security protocol.
        
        
            serverCertificate: The X509Certificate used to authenticate the server.
            clientCertificateRequired: A System.Boolean value that specifies whether the client must supply a certificate for 
             authentication.
        
            enabledSslProtocols: The System.Security.Authentication.SslProtocols  value that represents the protocol used for 
             authentication.
        
            checkCertificateRevocation: A System.Boolean value that specifies whether the certificate revocation list is checked during 
             authentication.
        
        AuthenticateAsServer(self: SslStream, serverCertificate: X509Certificate, clientCertificateRequired: bool, checkCertificateRevocation: bool)AuthenticateAsServer(self: SslStream, serverCertificate: X509Certificate)
            Called by servers to authenticate the server and optionally the client in a client-server 
             connection using the specified certificate.
        
        
            serverCertificate: The certificate used to authenticate the server.
        """
        pass

    def AuthenticateAsServerAsync(self, serverCertificate, clientCertificateRequired=None, *__args):
        """
        AuthenticateAsServerAsync(self: SslStream, serverCertificate: X509Certificate, clientCertificateRequired: bool, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool) -> Task
        AuthenticateAsServerAsync(self: SslStream, serverCertificate: X509Certificate, clientCertificateRequired: bool, checkCertificateRevocation: bool) -> Task
        AuthenticateAsServerAsync(self: SslStream, serverCertificate: X509Certificate) -> Task
        """
        pass

    def BeginAuthenticateAsClient(self, targetHost, *__args):
        """
        BeginAuthenticateAsClient(self: SslStream, targetHost: str, clientCertificates: X509CertificateCollection, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        
            Called by clients to begin an asynchronous operation to authenticate the server and optionally 
             the client using the specified certificates and security protocol.
        
        
            targetHost: The name of the server that shares this System.Net.Security.SslStream.
            clientCertificates: The System.Security.Cryptography.X509Certificates.X509CertificateCollection containing client 
             certificates.
        
            enabledSslProtocols: The System.Security.Authentication.SslProtocols value that represents the protocol used for 
             authentication.
        
            checkCertificateRevocation: A System.Boolean value that specifies whether the certificate revocation list is checked during 
             authentication.
        
            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is 
             complete.
        
            asyncState: A user-defined object that contains information about the operation. This object is passed to 
             the asyncCallback delegate when the operation completes.
        
            Returns: An System.IAsyncResult object that indicates the status of the asynchronous operation.
        BeginAuthenticateAsClient(self: SslStream, targetHost: str, clientCertificates: X509CertificateCollection, checkCertificateRevocation: bool, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        BeginAuthenticateAsClient(self: SslStream, targetHost: str, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        
            Called by clients to begin an asynchronous operation to authenticate the server and optionally 
             the client.
        
        
            targetHost: The name of the server that shares this System.Net.Security.SslStream.
            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is 
             complete.
        
            asyncState: A user-defined object that contains information about the operation. This object is passed to 
             the asyncCallback delegate when the operation completes.
        
            Returns: An System.IAsyncResult object that indicates the status of the asynchronous operation.
        """
        pass

    def BeginAuthenticateAsServer(self, serverCertificate, *__args):
        """
        BeginAuthenticateAsServer(self: SslStream, serverCertificate: X509Certificate, clientCertificateRequired: bool, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        
            Called by servers to begin an asynchronous operation to authenticate the server and optionally 
             the client using the specified certificates, requirements and security protocol.
        
        
            serverCertificate: The X509Certificate used to authenticate the server.
            clientCertificateRequired: A System.Boolean value that specifies whether the client must supply a certificate for 
             authentication.
        
            enabledSslProtocols: The System.Security.Authentication.SslProtocols  value that represents the protocol used for 
             authentication.
        
            checkCertificateRevocation: A System.Boolean value that specifies whether the certificate revocation list is checked during 
             authentication.
        
            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is 
             complete.
        
            asyncState: A user-defined object that contains information about the operation. This object is passed to 
             the asyncCallback delegate when the operation completes.
        
            Returns: An System.IAsyncResult object that indicates the status of the asynchronous operation.
        BeginAuthenticateAsServer(self: SslStream, serverCertificate: X509Certificate, clientCertificateRequired: bool, checkCertificateRevocation: bool, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        BeginAuthenticateAsServer(self: SslStream, serverCertificate: X509Certificate, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        
            Called by servers to begin an asynchronous operation to authenticate the client and optionally 
             the server in a client-server connection.
        
        
            serverCertificate: The X509Certificate used to authenticate the server.
            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is 
             complete.
        
            asyncState: A user-defined object that contains information about the operation. This object is passed to 
             the asyncCallback delegate when the operation completes.
        
            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.
        """
        pass

    def BeginRead(self, buffer, offset, count, asyncCallback, asyncState):
        """
        BeginRead(self: SslStream, buffer: Array[Byte], offset: int, count: int, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        
            Begins an asynchronous read operation that reads data from the stream and stores it in the 
             specified array.
        
        
            buffer: A System.Byte array that receives the bytes read from the stream.
            offset: The zero-based location in buffer at which to begin storing the data read from this stream.
            count: The maximum number of bytes to read from the stream.
            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the read operation is 
             complete.
        
            asyncState: A user-defined object that contains information about the read operation. This object is passed 
             to the asyncCallback delegate when the operation completes.
        
            Returns: An System.IAsyncResult object that indicates the status of the asynchronous operation.
        """
        pass

    def BeginWrite(self, buffer, offset, count, asyncCallback, asyncState):
        """
        BeginWrite(self: SslStream, buffer: Array[Byte], offset: int, count: int, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        
            Begins an asynchronous write operation that writes System.Bytes from the specified buffer to the 
             stream.
        
        
            buffer: A System.Byte array that supplies the bytes to be written to the stream.
            offset: The zero-based location in buffer at which to begin reading bytes to be written to the stream.
            count: An System.Int32 value that specifies the number of bytes to read from buffer.
            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the write operation 
             is complete.
        
            asyncState: A user-defined object that contains information about the write operation. This object is passed 
             to the asyncCallback delegate when the operation completes.
        
            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.
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
        Dispose(self: SslStream, disposing: bool)
            Releases the unmanaged resources used by the System.Net.Security.SslStream and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def EndAuthenticateAsClient(self, asyncResult):
        """
        EndAuthenticateAsClient(self: SslStream, asyncResult: IAsyncResult)
            Ends a pending asynchronous server authentication operation started with a previous call to 
             erload:System.Net.Security.SslStream.BeginAuthenticateAsServer.
        
        
            asyncResult: An System.IAsyncResult instance returned by a call to 
             erload:System.Net.Security.SslStream.BeginAuthenticateAsServer.
        """
        pass

    def EndAuthenticateAsServer(self, asyncResult):
        """
        EndAuthenticateAsServer(self: SslStream, asyncResult: IAsyncResult)
            Ends a pending asynchronous client authentication operation started with a previous call to 
             erload:System.Net.Security.SslStream.BeginAuthenticateAsClient.
        
        
            asyncResult: An System.IAsyncResult instance returned by a call to 
             erload:System.Net.Security.SslStream.BeginAuthenticateAsClient.
        """
        pass

    def EndRead(self, asyncResult):
        """
        EndRead(self: SslStream, asyncResult: IAsyncResult) -> int
        
            Ends an asynchronous read operation started with a previous call to 
             System.Net.Security.SslStream.BeginRead(System.Byte[],System.Int32,System.Int32,System.AsyncCallb
             ack,System.Object).
        
        
            asyncResult: An System.IAsyncResult instance returned by a call to 
             System.Net.Security.SslStream.BeginRead(System.Byte[],System.Int32,System.Int32,System.AsyncCallb
             ack,System.Object)
        
            Returns: A System.Int32 value that specifies the number of bytes read from the underlying stream.
        """
        pass

    def EndWrite(self, asyncResult):
        """
        EndWrite(self: SslStream, asyncResult: IAsyncResult)
            Ends an asynchronous write operation started with a previous call to 
             System.Net.Security.SslStream.BeginWrite(System.Byte[],System.Int32,System.Int32,System.AsyncCall
             back,System.Object).
        
        
            asyncResult: An System.IAsyncResult instance returned by a call to 
             System.Net.Security.SslStream.BeginWrite(System.Byte[],System.Int32,System.Int32,System.AsyncCall
             back,System.Object)
        """
        pass

    def Flush(self):
        """
        Flush(self: SslStream)
            Causes any buffered data to be written to the underlying device.
        """
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

    def Read(self, buffer, offset, count):
        """
        Read(self: SslStream, buffer: Array[Byte], offset: int, count: int) -> int
        
            Reads data from this stream and stores it in the specified array.
        
            buffer: A System.Byte array that receives the bytes read from this stream.
            offset: A System.Int32 that contains the zero-based location in buffer at which to begin storing the 
             data read from this stream.
        
            count: A System.Int32 that contains the maximum number of bytes to read from this stream.
            Returns: A System.Int32 value that specifies the number of bytes read. When there is no more data to be 
             read, returns 0.
        """
        pass

    def Seek(self, offset, origin):
        """
        Seek(self: SslStream, offset: Int64, origin: SeekOrigin) -> Int64
        
            Throws a System.NotSupportedException.
        
            offset: This value is ignored.
            origin: This value is ignored.
            Returns: Always throws a System.NotSupportedException.
        """
        pass

    def SetLength(self, value):
        """
        SetLength(self: SslStream, value: Int64)
            Sets the length of the underlying stream.
        
            value: An System.Int64 value that specifies the length of the stream.
        """
        pass

    def ShutdownAsync(self):
        """ ShutdownAsync(self: SslStream) -> Task """
        pass

    def Write(self, buffer, offset=None, count=None):
        """
        Write(self: SslStream, buffer: Array[Byte], offset: int, count: int)
            Write the specified number of System.Bytes to the underlying stream using the specified buffer 
             and offset.
        
        
            buffer: A System.Byte array that supplies the bytes written to the stream.
            offset: A System.Int32 that contains the zero-based location in buffer at which to begin reading bytes 
             to be written to the stream.
        
            count: A System.Int32 that contains the number of bytes to read from buffer.
        Write(self: SslStream, buffer: Array[Byte])
            Writes the specified data to this stream.
        
            buffer: A System.Byte array that supplies the bytes written to the stream.
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
    def __new__(self, innerStream, leaveInnerStreamOpen=None, userCertificateValidationCallback=None, userCertificateSelectionCallback=None, encryptionPolicy=None):
        """
        __new__(cls: type, innerStream: Stream)
        __new__(cls: type, innerStream: Stream, leaveInnerStreamOpen: bool)
        __new__(cls: type, innerStream: Stream, leaveInnerStreamOpen: bool, userCertificateValidationCallback: RemoteCertificateValidationCallback)
        __new__(cls: type, innerStream: Stream, leaveInnerStreamOpen: bool, userCertificateValidationCallback: RemoteCertificateValidationCallback, userCertificateSelectionCallback: LocalCertificateSelectionCallback)
        __new__(cls: type, innerStream: Stream, leaveInnerStreamOpen: bool, userCertificateValidationCallback: RemoteCertificateValidationCallback, userCertificateSelectionCallback: LocalCertificateSelectionCallback, encryptionPolicy: EncryptionPolicy)
        """
        pass

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether the underlying stream is readable.

Get: CanRead(self: SslStream) -> bool

"""

    CanSeek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether the underlying stream is seekable.

Get: CanSeek(self: SslStream) -> bool

"""

    CanTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether the underlying stream supports time-outs.

Get: CanTimeout(self: SslStream) -> bool

"""

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether the underlying stream is writable.

Get: CanWrite(self: SslStream) -> bool

"""

    CheckCertRevocationStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether the certificate revocation list is checked during the certificate validation process.

Get: CheckCertRevocationStatus(self: SslStream) -> bool

"""

    CipherAlgorithm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that identifies the bulk encryption algorithm used by this System.Net.Security.SslStream.

Get: CipherAlgorithm(self: SslStream) -> CipherAlgorithmType

"""

    CipherStrength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that identifies the strength of the cipher algorithm used by this System.Net.Security.SslStream.

Get: CipherStrength(self: SslStream) -> int

"""

    HashAlgorithm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the algorithm used for generating message authentication codes (MACs).

Get: HashAlgorithm(self: SslStream) -> HashAlgorithmType

"""

    HashStrength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that identifies the strength of the hash algorithm used by this instance.

Get: HashStrength(self: SslStream) -> int

"""

    InnerStream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the stream used by this System.Net.Security.AuthenticatedStream for sending and receiving data.

"""

    IsAuthenticated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether authentication was successful.

Get: IsAuthenticated(self: SslStream) -> bool

"""

    IsEncrypted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether this System.Net.Security.SslStream uses data encryption.

Get: IsEncrypted(self: SslStream) -> bool

"""

    IsMutuallyAuthenticated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether both server and client have been authenticated.

Get: IsMutuallyAuthenticated(self: SslStream) -> bool

"""

    IsServer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether the local side of the connection used by this System.Net.Security.SslStream was authenticated as the server.

Get: IsServer(self: SslStream) -> bool

"""

    IsSigned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether the data sent using this stream is signed.

Get: IsSigned(self: SslStream) -> bool

"""

    KeyExchangeAlgorithm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the key exchange algorithm used by this System.Net.Security.SslStream.

Get: KeyExchangeAlgorithm(self: SslStream) -> ExchangeAlgorithmType

"""

    KeyExchangeStrength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that identifies the strength of the key exchange algorithm used by this instance.

Get: KeyExchangeStrength(self: SslStream) -> int

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length of the underlying stream.

Get: Length(self: SslStream) -> Int64

"""

    LocalCertificate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the certificate used to authenticate the local endpoint.

Get: LocalCertificate(self: SslStream) -> X509Certificate

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current position in the underlying stream.

Get: Position(self: SslStream) -> Int64

Set: Position(self: SslStream) = value
"""

    ReadTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the amount of time a read operation blocks waiting for data.

Get: ReadTimeout(self: SslStream) -> int

Set: ReadTimeout(self: SslStream) = value
"""

    RemoteCertificate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the certificate used to authenticate the remote endpoint.

Get: RemoteCertificate(self: SslStream) -> X509Certificate

"""

    SslProtocol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates the security protocol used to authenticate this connection.

Get: SslProtocol(self: SslStream) -> SslProtocols

"""

    TransportContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Net.TransportContext used for authentication using extended protection.

Get: TransportContext(self: SslStream) -> TransportContext

"""

    WriteTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the amount of time a write operation blocks waiting for data.

Get: WriteTimeout(self: SslStream) -> int

Set: WriteTimeout(self: SslStream) = value
"""



