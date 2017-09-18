# encoding: utf-8
# module System.IO.Compression calls itself Compression
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class CompressionLevel(Enum, IComparable, IFormattable, IConvertible):
    """ enum CompressionLevel, values: Fastest (1), NoCompression (2), Optimal (0) """
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

    Fastest = None
    NoCompression = None
    Optimal = None
    value__ = None


class CompressionMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies whether to compress or decompress the underlying stream.
    
    enum CompressionMode, values: Compress (1), Decompress (0)
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

    Compress = None
    Decompress = None
    value__ = None


class DeflateStream(Stream, IDisposable):
    """
    Provides methods and properties for compressing and decompressing streams using the Deflate algorithm.
    
    DeflateStream(stream: Stream, mode: CompressionMode)
    DeflateStream(stream: Stream, mode: CompressionMode, leaveOpen: bool)
    DeflateStream(stream: Stream, compressionLevel: CompressionLevel)
    DeflateStream(stream: Stream, compressionLevel: CompressionLevel, leaveOpen: bool)
    """
    def BeginRead(self, array, offset, count, asyncCallback, asyncState):
        """
        BeginRead(self: DeflateStream, array: Array[Byte], offset: int, count: int, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        
            Begins an asynchronous read operation.
        
            array: The byte array to read the data into.
            offset: The byte offset in array at which to begin writing data read from the stream.
            count: The maximum number of bytes to read.
            asyncCallback: An optional asynchronous callback, to be called when the read is complete.
            asyncState: A user-provided object that distinguishes this particular asynchronous read request from other 
             requests.
        
            Returns: An System.IAsyncResult object that represents the asynchronous read, which could still be 
             pending.
        """
        pass

    def BeginWrite(self, array, offset, count, asyncCallback, asyncState):
        """
        BeginWrite(self: DeflateStream, array: Array[Byte], offset: int, count: int, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        
            Begins an asynchronous write operation.
        
            array: The buffer to write data from.
            offset: The byte offset in buffer to begin writing from.
            count: The maximum number of bytes to write.
            asyncCallback: An optional asynchronous callback, to be called when the write is complete.
            asyncState: A user-provided object that distinguishes this particular asynchronous write request from other 
             requests.
        
            Returns: An System.IAsyncResult object that represents the asynchronous write, which could still be 
             pending.
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
        Dispose(self: DeflateStream, disposing: bool)
            Releases the unmanaged resources used by the System.IO.Compression.DeflateStream and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def EndRead(self, asyncResult):
        """
        EndRead(self: DeflateStream, asyncResult: IAsyncResult) -> int
        
            Waits for the pending asynchronous read to complete.
        
            asyncResult: The reference to the pending asynchronous request to finish.
            Returns: The number of bytes read from the stream, between zero (0) and the number of bytes you 
             requested. System.IO.Compression.DeflateStream returns zero (0) only at the end of the stream; 
             otherwise, it blocks until at least one byte is available.
        """
        pass

    def EndWrite(self, asyncResult):
        """
        EndWrite(self: DeflateStream, asyncResult: IAsyncResult)
            Ends an asynchronous write operation.
        
            asyncResult: A reference to the outstanding asynchronous I/O request.
        """
        pass

    def Flush(self):
        """
        Flush(self: DeflateStream)
            Flushes the contents of the internal buffer of the current stream object to the underlying 
             stream.
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

    def Read(self, array, offset, count):
        """
        Read(self: DeflateStream, array: Array[Byte], offset: int, count: int) -> int
        
            Reads a number of decompressed bytes into the specified byte array.
        
            array: The array to store decompressed bytes.
            offset: The byte offset in array at which the read bytes will be placed.
            count: The maximum number of decompressed bytes to read.
            Returns: The number of bytes that were read into the byte array.
        """
        pass

    def Seek(self, offset, origin):
        """
        Seek(self: DeflateStream, offset: Int64, origin: SeekOrigin) -> Int64
        
            This operation is not supported and always throws a System.NotSupportedException.
        
            offset: The location in the stream.
            origin: One of the System.IO.SeekOrigin values.
            Returns: A long value.
        """
        pass

    def SetLength(self, value):
        """
        SetLength(self: DeflateStream, value: Int64)
            This operation is not supported and always throws a System.NotSupportedException.
        
            value: The length of the stream.
        """
        pass

    def Write(self, array, offset, count):
        """
        Write(self: DeflateStream, array: Array[Byte], offset: int, count: int)
            Writes compressed bytes to the underlying stream from the specified byte array.
        
            array: The buffer that contains the data to compress.
            offset: The byte offset in array at which the compressed bytes will be placed.
            count: The maximum number of compressed bytes to write.
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
    def __new__(self, stream, *__args):
        """
        __new__(cls: type, stream: Stream, mode: CompressionMode)
        __new__(cls: type, stream: Stream, mode: CompressionMode, leaveOpen: bool)
        __new__(cls: type, stream: Stream, compressionLevel: CompressionLevel)
        __new__(cls: type, stream: Stream, compressionLevel: CompressionLevel, leaveOpen: bool)
        """
        pass

    BaseStream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a reference to the underlying stream.

Get: BaseStream(self: DeflateStream) -> Stream

"""

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the stream supports reading while decompressing a file.

Get: CanRead(self: DeflateStream) -> bool

"""

    CanSeek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the stream supports seeking.

Get: CanSeek(self: DeflateStream) -> bool

"""

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the stream supports writing.

Get: CanWrite(self: DeflateStream) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is not supported and always throws a System.NotSupportedException.

Get: Length(self: DeflateStream) -> Int64

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is not supported and always throws a System.NotSupportedException.

Get: Position(self: DeflateStream) -> Int64

Set: Position(self: DeflateStream) = value
"""



class GZipStream(Stream, IDisposable):
    """
    Provides methods and properties used to compress and decompress streams.
    
    GZipStream(stream: Stream, mode: CompressionMode)
    GZipStream(stream: Stream, mode: CompressionMode, leaveOpen: bool)
    GZipStream(stream: Stream, compressionLevel: CompressionLevel)
    GZipStream(stream: Stream, compressionLevel: CompressionLevel, leaveOpen: bool)
    """
    def BeginRead(self, array, offset, count, asyncCallback, asyncState):
        """
        BeginRead(self: GZipStream, array: Array[Byte], offset: int, count: int, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        
            Begins an asynchronous read operation.
        
            array: The byte array to read the data into.
            offset: The byte offset in array at which to begin writing data read from the stream.
            count: The maximum number of bytes to read.
            asyncCallback: An optional asynchronous callback, to be called when the read is complete.
            asyncState: A user-provided object that distinguishes this particular asynchronous read request from other 
             requests.
        
            Returns: An System.IAsyncResult object that represents the asynchronous read, which could still be 
             pending.
        """
        pass

    def BeginWrite(self, array, offset, count, asyncCallback, asyncState):
        """
        BeginWrite(self: GZipStream, array: Array[Byte], offset: int, count: int, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        
            Begins an asynchronous write operation.
        
            array: The buffer containing data to write to the current stream.
            offset: The byte offset in array at which to begin writing.
            count: The maximum number of bytes to write.
            asyncCallback: An optional asynchronous callback to be called when the write is complete.
            asyncState: A user-provided object that distinguishes this particular asynchronous write request from other 
             requests.
        
            Returns: An System.IAsyncResult object that represents the asynchronous write, which could still be 
             pending.
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
        Dispose(self: GZipStream, disposing: bool)
            Releases the unmanaged resources used by the System.IO.Compression.GZipStream and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def EndRead(self, asyncResult):
        """
        EndRead(self: GZipStream, asyncResult: IAsyncResult) -> int
        
            Waits for the pending asynchronous read to complete.
        
            asyncResult: The reference to the pending asynchronous request to finish.
            Returns: The number of bytes read from the stream, between zero (0) and the number of bytes you 
             requested. System.IO.Compression.GZipStream returns zero (0) only at the end of the stream; 
             otherwise, it blocks until at least one byte is available.
        """
        pass

    def EndWrite(self, asyncResult):
        """
        EndWrite(self: GZipStream, asyncResult: IAsyncResult)
            Handles the end of an asynchronous write operation.
        
            asyncResult: The System.IAsyncResult object that represents the asynchronous call.
        """
        pass

    def Flush(self):
        """
        Flush(self: GZipStream)
            Flushes the contents of the internal buffer of the current System.IO.Compression.GZipStream 
             object to the underlying stream.
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

    def Read(self, array, offset, count):
        """
        Read(self: GZipStream, array: Array[Byte], offset: int, count: int) -> int
        
            Reads a number of decompressed bytes into the specified byte array.
        
            array: The array used to store decompressed bytes.
            offset: The byte offset in array at which the read bytes will be placed.
            count: The maximum number of decompressed bytes to read.
            Returns: The number of bytes that were decompressed into the byte array. If the end of the stream has 
             been reached, zero or the number of bytes read is returned.
        """
        pass

    def Seek(self, offset, origin):
        """
        Seek(self: GZipStream, offset: Int64, origin: SeekOrigin) -> Int64
        
            This property is not supported and always throws a System.NotSupportedException.
        
            offset: The location in the stream.
            origin: One of the System.IO.SeekOrigin values.
            Returns: A long value.
        """
        pass

    def SetLength(self, value):
        """
        SetLength(self: GZipStream, value: Int64)
            This property is not supported and always throws a System.NotSupportedException.
        
            value: The length of the stream.
        """
        pass

    def Write(self, array, offset, count):
        """
        Write(self: GZipStream, array: Array[Byte], offset: int, count: int)
            Writes compressed bytes to the underlying stream from the specified byte array.
        
            array: The buffer that contains the data to compress.
            offset: The byte offset in array at which the compressed bytes will be placed.
            count: The maximum number of compressed bytes to write.
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
    def __new__(self, stream, *__args):
        """
        __new__(cls: type, stream: Stream, mode: CompressionMode)
        __new__(cls: type, stream: Stream, mode: CompressionMode, leaveOpen: bool)
        __new__(cls: type, stream: Stream, compressionLevel: CompressionLevel)
        __new__(cls: type, stream: Stream, compressionLevel: CompressionLevel, leaveOpen: bool)
        """
        pass

    BaseStream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a reference to the underlying stream.

Get: BaseStream(self: GZipStream) -> Stream

"""

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the stream supports reading while decompressing a file.

Get: CanRead(self: GZipStream) -> bool

"""

    CanSeek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the stream supports seeking.

Get: CanSeek(self: GZipStream) -> bool

"""

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the stream supports writing.

Get: CanWrite(self: GZipStream) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is not supported and always throws a System.NotSupportedException.

Get: Length(self: GZipStream) -> Int64

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is not supported and always throws a System.NotSupportedException.

Get: Position(self: GZipStream) -> Int64

Set: Position(self: GZipStream) = value
"""



