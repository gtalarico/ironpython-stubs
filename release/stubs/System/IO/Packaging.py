# encoding: utf-8
# module System.IO.Packaging calls itself Packaging
# from PresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class PackageStore(object):
    """ Represents a collection of application-specific System.IO.Packaging.Package instances used in combination with System.IO.Packaging.PackWebRequest. """
    @staticmethod
    def AddPackage(uri, package):
        """
        AddPackage(uri: Uri, package: Package)
            Adds a System.IO.Packaging.Package to the store.
        
            uri: The key URI of the package to compare in a System.IO.Packaging.PackWebRequest.
            package: The package to add to the store.
        """
        pass

    @staticmethod
    def GetPackage(uri):
        """
        GetPackage(uri: Uri) -> Package
        
            Returns the System.IO.Packaging.Package with a specified URI from the store.
        
            uri: The uniform resource identifier (URI) of the package to return.
            Returns: The package with a specified packageUri; or null, if a package with the specified packageUri is 
             not in the store.
        """
        pass

    @staticmethod
    def RemovePackage(uri):
        """
        RemovePackage(uri: Uri)
            Removes the System.IO.Packaging.Package with a specified URI from the store.
        
            uri: The uniform resource identifier (URI) of the package to remove.
        """
        pass

    __all__ = [
        'AddPackage',
        'GetPackage',
        'RemovePackage',
    ]


class PackWebRequest(WebRequest, ISerializable):
    """ Makes a request to an entire System.IO.Packaging.PackagePart or to a System.IO.Packaging.PackagePart in a package, identified by a pack URI. """
    def GetInnerRequest(self):
        """
        GetInnerRequest(self: PackWebRequest) -> WebRequest
        
            Gets the inner System.Net.WebRequest.
            Returns: A System.Net.WebRequest created from the inner-URI if the request resolves to a valid transport 
             protocol such http or ftp; or a System.Net.WebRequest created with a null-URI if the request 
             resolves from the System.IO.Packaging.PackageStore cache.
        """
        pass

    def GetObjectData(self, *args): #cannot find CLR method
        """
        GetObjectData(self: WebRequest, serializationInfo: SerializationInfo, streamingContext: StreamingContext)
            Populates a System.Runtime.Serialization.SerializationInfo with the data needed to serialize the 
             target object.
        
        
            serializationInfo: The System.Runtime.Serialization.SerializationInfo to populate with data.
            streamingContext: A System.Runtime.Serialization.StreamingContext that specifies the destination for this 
             serialization.
        """
        pass

    def GetRequestStream(self):
        """
        GetRequestStream(self: PackWebRequest) -> Stream
        
                     System.IO.Packaging.PackWebRequest.
        
            Returns: If System.IO.Packaging.PackWebRequest.GetRequestStream is called, a System.NotSupportedException 
             is thrown.
        """
        pass

    def GetResponse(self):
        """
        GetResponse(self: PackWebRequest) -> WebResponse
        
            Returns the response stream for the request.
            Returns: The response stream for the request.
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CachePolicy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Net.Cache.RequestCachePolicy.

Get: CachePolicy(self: PackWebRequest) -> RequestCachePolicy

Set: CachePolicy(self: PackWebRequest) = value
"""

    ConnectionGroupName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the connection group.

Get: ConnectionGroupName(self: PackWebRequest) -> str

Set: ConnectionGroupName(self: PackWebRequest) = value
"""

    ContentLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Content-length�HTTP header.

Get: ContentLength(self: PackWebRequest) -> Int64

Set: ContentLength(self: PackWebRequest) = value
"""

    ContentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Content-type�HTTP header.

Get: ContentType(self: PackWebRequest) -> str

Set: ContentType(self: PackWebRequest) = value
"""

    Credentials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the authentication credentials.

Get: Credentials(self: PackWebRequest) -> ICredentials

Set: Credentials(self: PackWebRequest) = value
"""

    Headers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the collection of header name/value pairs associated with the request.

Get: Headers(self: PackWebRequest) -> WebHeaderCollection

Set: Headers(self: PackWebRequest) = value
"""

    Method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the protocol method to use with the pack URI request.

Get: Method(self: PackWebRequest) -> str

Set: Method(self: PackWebRequest) = value
"""

    PreAuthenticate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether to preauthenticate the request.

Get: PreAuthenticate(self: PackWebRequest) -> bool

Set: PreAuthenticate(self: PackWebRequest) = value
"""

    Proxy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the network proxy for Internet access.

Get: Proxy(self: PackWebRequest) -> IWebProxy

Set: Proxy(self: PackWebRequest) = value
"""

    RequestUri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the URI of the resource associated with the request.

Get: RequestUri(self: PackWebRequest) -> Uri

"""

    Timeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the length of time before the request times out.

Get: Timeout(self: PackWebRequest) -> int

Set: Timeout(self: PackWebRequest) = value
"""

    UseDefaultCredentials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the default authentication credentials.

Get: UseDefaultCredentials(self: PackWebRequest) -> bool

Set: UseDefaultCredentials(self: PackWebRequest) = value
"""



class PackWebRequestFactory(object, IWebRequestCreate):
    """
    Represents the class that is invoked when an instance of a pack URI�System.IO.Packaging.PackWebRequest is created.
    
    PackWebRequestFactory()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class PackWebResponse(WebResponse, ISerializable, IDisposable):
    """ Represents a response of a System.IO.Packaging.PackWebRequest. """
    def Close(self):
        """
        Close(self: PackWebResponse)
            Closes the stream for this request.
        """
        pass

    def Dispose(self):
        """ Dispose(self: PackWebResponse, disposing: bool) """
        pass

    def GetObjectData(self, *args): #cannot find CLR method
        """
        GetObjectData(self: WebResponse, serializationInfo: SerializationInfo, streamingContext: StreamingContext)
            Populates a System.Runtime.Serialization.SerializationInfo with the data that is needed to 
             serialize the target object.
        
        
            serializationInfo: The System.Runtime.Serialization.SerializationInfo to populate with data.
            streamingContext: A System.Runtime.Serialization.StreamingContext that specifies the destination for this 
             serialization.
        """
        pass

    def GetResponseStream(self):
        """
        GetResponseStream(self: PackWebResponse) -> Stream
        
            Gets the response stream that is contained in the System.IO.Packaging.PackWebResponse.
            Returns: The response stream.
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

    ContentLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the content length of the response.

Get: ContentLength(self: PackWebResponse) -> Int64

"""

    ContentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Multipurpose Internet Mail Extensions (MIME) content type of the response stream's content.

Get: ContentType(self: PackWebResponse) -> str

"""

    Headers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of Web System.Net.WebResponse.Headers for this response.

Get: Headers(self: PackWebResponse) -> WebHeaderCollection

"""

    InnerResponse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the inner System.Net.WebResponse object for the response.

Get: InnerResponse(self: PackWebResponse) -> WebResponse

"""

    IsFromCache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the response is from the package cache or from a Web request.

Get: IsFromCache(self: PackWebResponse) -> bool

"""

    ResponseUri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the uniform resource identifier (URI) of the response.

Get: ResponseUri(self: PackWebResponse) -> Uri

"""



