# encoding: utf-8
# module System.IO calls itself IO
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class BinaryReader(object, IDisposable):
    """
    Reads primitive data types as binary values in a specific encoding.
    
    BinaryReader(input: Stream)
    BinaryReader(input: Stream, encoding: Encoding)
    BinaryReader(input: Stream, encoding: Encoding, leaveOpen: bool)
    """
    def Close(self):
        """
        Close(self: BinaryReader)
            Closes the current reader and the underlying stream.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: BinaryReader)
            Releases all resources used by the current instance of the System.IO.BinaryReader class.
        """
        pass

    def FillBuffer(self, *args): #cannot find CLR method
        """
        FillBuffer(self: BinaryReader, numBytes: int)
            Fills the internal buffer with the specified number of bytes read from the stream.
        
            numBytes: The number of bytes to be read.
        """
        pass

    def PeekChar(self):
        """
        PeekChar(self: BinaryReader) -> int
        
            Returns the next available character and does not advance the byte or character position.
            Returns: The next available character, or -1 if no more characters are available or the stream does not 
             support seeking.
        """
        pass

    def Read(self, buffer=None, index=None, count=None):
        """
        Read(self: BinaryReader, buffer: Array[Byte], index: int, count: int) -> int
        
            Reads the specified number of bytes from the stream, starting from a specified point in the byte 
             array.
        
        
            buffer: The buffer to read data into.
            index: The starting point in the buffer at which to begin reading into the buffer.
            count: The number of bytes to read.
            Returns: The number of bytes read into buffer. This might be less than the number of bytes requested if 
             that many bytes are not available, or it might be zero if the end of the stream is reached.
        
        Read(self: BinaryReader, buffer: Array[Char], index: int, count: int) -> int
        
            Reads the specified number of characters from the stream, starting from a specified point in the 
             character array.
        
        
            buffer: The buffer to read data into.
            index: The starting point in the buffer at which to begin reading into the buffer.
            count: The number of characters to read.
            Returns: The total number of characters read into the buffer. This might be less than the number of 
             characters requested if that many characters are not currently available, or it might be zero if 
             the end of the stream is reached.
        
        Read(self: BinaryReader) -> int
        
            Reads characters from the underlying stream and advances the current position of the stream in 
             accordance with the Encoding used and the specific character being read from the stream.
        
            Returns: The next character from the input stream, or -1 if no characters are currently available.
        """
        pass

    def Read7BitEncodedInt(self, *args): #cannot find CLR method
        """
        Read7BitEncodedInt(self: BinaryReader) -> int
        
            Reads in a 32-bit integer in compressed format.
            Returns: A 32-bit integer in compressed format.
        """
        pass

    def ReadBoolean(self):
        """
        ReadBoolean(self: BinaryReader) -> bool
        
            Reads a Boolean value from the current stream and advances the current position of the stream by 
             one byte.
        
            Returns: true if the byte is nonzero; otherwise, false.
        """
        pass

    def ReadByte(self):
        """
        ReadByte(self: BinaryReader) -> Byte
        
            Reads the next byte from the current stream and advances the current position of the stream by 
             one byte.
        
            Returns: The next byte read from the current stream.
        """
        pass

    def ReadBytes(self, count):
        """
        ReadBytes(self: BinaryReader, count: int) -> Array[Byte]
        
            Reads the specified number of bytes from the current stream into a byte array and advances the 
             current position by that number of bytes.
        
        
            count: The number of bytes to read.
            Returns: A byte array containing data read from the underlying stream. This might be less than the number 
             of bytes requested if the end of the stream is reached.
        """
        pass

    def ReadChar(self):
        """
        ReadChar(self: BinaryReader) -> Char
        
            Reads the next character from the current stream and advances the current position of the stream 
             in accordance with the Encoding used and the specific character being read from the stream.
        
            Returns: A character read from the current stream.
        """
        pass

    def ReadChars(self, count):
        """
        ReadChars(self: BinaryReader, count: int) -> Array[Char]
        
            Reads the specified number of characters from the current stream, returns the data in a 
             character array, and advances the current position in accordance with the Encoding used and the 
             specific character being read from the stream.
        
        
            count: The number of characters to read.
            Returns: A character array containing data read from the underlying stream. This might be less than the 
             number of characters requested if the end of the stream is reached.
        """
        pass

    def ReadDecimal(self):
        """
        ReadDecimal(self: BinaryReader) -> Decimal
        
            Reads a decimal value from the current stream and advances the current position of the stream by 
             sixteen bytes.
        
            Returns: A decimal value read from the current stream.
        """
        pass

    def ReadDouble(self):
        """
        ReadDouble(self: BinaryReader) -> float
        
            Reads an 8-byte floating point value from the current stream and advances the current position 
             of the stream by eight bytes.
        
            Returns: An 8-byte floating point value read from the current stream.
        """
        pass

    def ReadInt16(self):
        """
        ReadInt16(self: BinaryReader) -> Int16
        
            Reads a 2-byte signed integer from the current stream and advances the current position of the 
             stream by two bytes.
        
            Returns: A 2-byte signed integer read from the current stream.
        """
        pass

    def ReadInt32(self):
        """
        ReadInt32(self: BinaryReader) -> int
        
            Reads a 4-byte signed integer from the current stream and advances the current position of the 
             stream by four bytes.
        
            Returns: A 4-byte signed integer read from the current stream.
        """
        pass

    def ReadInt64(self):
        """
        ReadInt64(self: BinaryReader) -> Int64
        
            Reads an 8-byte signed integer from the current stream and advances the current position of the 
             stream by eight bytes.
        
            Returns: An 8-byte signed integer read from the current stream.
        """
        pass

    def ReadSByte(self):
        """
        ReadSByte(self: BinaryReader) -> SByte
        
            Reads a signed byte from this stream and advances the current position of the stream by one byte.
            Returns: A signed byte read from the current stream.
        """
        pass

    def ReadSingle(self):
        """
        ReadSingle(self: BinaryReader) -> Single
        
            Reads a 4-byte floating point value from the current stream and advances the current position of 
             the stream by four bytes.
        
            Returns: A 4-byte floating point value read from the current stream.
        """
        pass

    def ReadString(self):
        """
        ReadString(self: BinaryReader) -> str
        
            Reads a string from the current stream. The string is prefixed with the length, encoded as an 
             integer seven bits at a time.
        
            Returns: The string being read.
        """
        pass

    def ReadUInt16(self):
        """
        ReadUInt16(self: BinaryReader) -> UInt16
        
            Reads a 2-byte unsigned integer from the current stream using little-endian encoding and 
             advances the position of the stream by two bytes.
        
            Returns: A 2-byte unsigned integer read from this stream.
        """
        pass

    def ReadUInt32(self):
        """
        ReadUInt32(self: BinaryReader) -> UInt32
        
            Reads a 4-byte unsigned integer from the current stream and advances the position of the stream 
             by four bytes.
        
            Returns: A 4-byte unsigned integer read from this stream.
        """
        pass

    def ReadUInt64(self):
        """
        ReadUInt64(self: BinaryReader) -> UInt64
        
            Reads an 8-byte unsigned integer from the current stream and advances the position of the stream 
             by eight bytes.
        
            Returns: An 8-byte unsigned integer read from this stream.
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
    def __new__(self, input, encoding=None, leaveOpen=None):
        """
        __new__(cls: type, input: Stream)
        __new__(cls: type, input: Stream, encoding: Encoding)
        __new__(cls: type, input: Stream, encoding: Encoding, leaveOpen: bool)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BaseStream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Exposes access to the underlying stream of the System.IO.BinaryReader.

Get: BaseStream(self: BinaryReader) -> Stream

"""



class BinaryWriter(object, IDisposable):
    """
    Writes primitive types in binary to a stream and supports writing strings in a specific encoding.
    
    BinaryWriter(output: Stream)
    BinaryWriter(output: Stream, encoding: Encoding)
    BinaryWriter(output: Stream, encoding: Encoding, leaveOpen: bool)
    """
    def Close(self):
        """
        Close(self: BinaryWriter)
            Closes the current System.IO.BinaryWriter and the underlying stream.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: BinaryWriter)
            Releases all resources used by the current instance of the System.IO.BinaryWriter class.
        """
        pass

    def Flush(self):
        """
        Flush(self: BinaryWriter)
            Clears all buffers for the current writer and causes any buffered data to be written to the 
             underlying device.
        """
        pass

    def Seek(self, offset, origin):
        """
        Seek(self: BinaryWriter, offset: int, origin: SeekOrigin) -> Int64
        
            Sets the position within the current stream.
        
            offset: A byte offset relative to origin.
            origin: A field of System.IO.SeekOrigin indicating the reference point from which the new position is to 
             be obtained.
        
            Returns: The position with the current stream.
        """
        pass

    def Write(self, *__args):
        """
        Write(self: BinaryWriter, value: UInt16)
            Writes a two-byte unsigned integer to the current stream and advances the stream position by two 
             bytes.
        
        
            value: The two-byte unsigned integer to write.
        Write(self: BinaryWriter, value: int)
            Writes a four-byte signed integer to the current stream and advances the stream position by four 
             bytes.
        
        
            value: The four-byte signed integer to write.
        Write(self: BinaryWriter, value: Decimal)
            Writes a decimal value to the current stream and advances the stream position by sixteen bytes.
        
            value: The decimal value to write.
        Write(self: BinaryWriter, value: Int16)
            Writes a two-byte signed integer to the current stream and advances the stream position by two 
             bytes.
        
        
            value: The two-byte signed integer to write.
        Write(self: BinaryWriter, value: UInt32)
            Writes a four-byte unsigned integer to the current stream and advances the stream position by 
             four bytes.
        
        
            value: The four-byte unsigned integer to write.
        Write(self: BinaryWriter, value: Single)
            Writes a four-byte floating-point value to the current stream and advances the stream position 
             by four bytes.
        
        
            value: The four-byte floating-point value to write.
        Write(self: BinaryWriter, value: str)
            Writes a length-prefixed string to this stream in the current encoding of the 
             System.IO.BinaryWriter, and advances the current position of the stream in accordance with the 
             encoding used and the specific characters being written to the stream.
        
        
            value: The value to write.
        Write(self: BinaryWriter, value: Int64)
            Writes an eight-byte signed integer to the current stream and advances the stream position by 
             eight bytes.
        
        
            value: The eight-byte signed integer to write.
        Write(self: BinaryWriter, value: UInt64)
            Writes an eight-byte unsigned integer to the current stream and advances the stream position by 
             eight bytes.
        
        
            value: The eight-byte unsigned integer to write.
        Write(self: BinaryWriter, value: SByte)
            Writes a signed byte to the current stream and advances the stream position by one byte.
        
            value: The signed byte to write.
        Write(self: BinaryWriter, buffer: Array[Byte])
            Writes a byte array to the underlying stream.
        
            buffer: A byte array containing the data to write.
        Write(self: BinaryWriter, value: bool)
            Writes a one-byte Boolean value to the current stream, with 0 representing false and 1 
             representing true.
        
        
            value: The Boolean value to write (0 or 1).
        Write(self: BinaryWriter, value: Byte)
            Writes an unsigned byte to the current stream and advances the stream position by one byte.
        
            value: The unsigned byte to write.
        Write(self: BinaryWriter, buffer: Array[Byte], index: int, count: int)
            Writes a region of a byte array to the current stream.
        
            buffer: A byte array containing the data to write.
            index: The starting point in buffer at which to begin writing.
            count: The number of bytes to write.
        Write(self: BinaryWriter, chars: Array[Char], index: int, count: int)
            Writes a section of a character array to the current stream, and advances the current position 
             of the stream in accordance with the Encoding used and perhaps the specific characters being 
             written to the stream.
        
        
            chars: A character array containing the data to write.
            index: The starting point in chars from which to begin writing.
            count: The number of characters to write.
        Write(self: BinaryWriter, value: float)
            Writes an eight-byte floating-point value to the current stream and advances the stream position 
             by eight bytes.
        
        
            value: The eight-byte floating-point value to write.
        Write(self: BinaryWriter, ch: Char)
            Writes a Unicode character to the current stream and advances the current position of the stream 
             in accordance with the Encoding used and the specific characters being written to the stream.
        
        
            ch: The non-surrogate, Unicode character to write.
        Write(self: BinaryWriter, chars: Array[Char])
            Writes a character array to the current stream and advances the current position of the stream 
             in accordance with the Encoding used and the specific characters being written to the stream.
        
        
            chars: A character array containing the data to write.
        """
        pass

    def Write7BitEncodedInt(self, *args): #cannot find CLR method
        """
        Write7BitEncodedInt(self: BinaryWriter, value: int)
            Writes a 32-bit integer in a compressed format.
        
            value: The 32-bit integer to be written.
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
    def __new__(self, output, encoding=None, leaveOpen=None):
        """
        __new__(cls: type)
        __new__(cls: type, output: Stream)
        __new__(cls: type, output: Stream, encoding: Encoding)
        __new__(cls: type, output: Stream, encoding: Encoding, leaveOpen: bool)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BaseStream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the underlying stream of the System.IO.BinaryWriter.

Get: BaseStream(self: BinaryWriter) -> Stream

"""


    Null = None
    OutStream = None


class Stream(MarshalByRefObject, IDisposable):
    """ Provides a generic view of a sequence of bytes. """
    def BeginRead(self, buffer, offset, count, callback, state):
        """
        BeginRead(self: Stream, buffer: Array[Byte], offset: int, count: int, callback: AsyncCallback, state: object) -> IAsyncResult
        
            Begins an asynchronous read operation.
        
            buffer: The buffer to read the data into.
            offset: The byte offset in buffer at which to begin writing data read from the stream.
            count: The maximum number of bytes to read.
            callback: An optional asynchronous callback, to be called when the read is complete.
            state: A user-provided object that distinguishes this particular asynchronous read request from other 
             requests.
        
            Returns: An System.IAsyncResult that represents the asynchronous read, which could still be pending.
        """
        pass

    def BeginWrite(self, buffer, offset, count, callback, state):
        """
        BeginWrite(self: Stream, buffer: Array[Byte], offset: int, count: int, callback: AsyncCallback, state: object) -> IAsyncResult
        
            Begins an asynchronous write operation.
        
            buffer: The buffer to write data from.
            offset: The byte offset in buffer from which to begin writing.
            count: The maximum number of bytes to write.
            callback: An optional asynchronous callback, to be called when the write is complete.
            state: A user-provided object that distinguishes this particular asynchronous write request from other 
             requests.
        
            Returns: An IAsyncResult that represents the asynchronous write, which could still be pending.
        """
        pass

    def Close(self):
        """
        Close(self: Stream)
            Closes the current stream and releases any resources (such as sockets and file handles) 
             associated with the current stream.
        """
        pass

    def CopyTo(self, destination, bufferSize=None):
        """
        CopyTo(self: Stream, destination: Stream, bufferSize: int)
            Reads all the bytes from the current stream and writes them to a destination stream, using a 
             specified buffer size.
        
        
            destination: The stream that will contain the contents of the current stream.
            bufferSize: The size of the buffer. This value must be greater than zero. The default size is 4096.
        CopyTo(self: Stream, destination: Stream)
            Reads the bytes from the current stream and writes them to the destination stream.
        
            destination: The stream that will contain the contents of the current stream.
        """
        pass

    def CopyToAsync(self, destination, bufferSize=None, cancellationToken=None):
        """
        CopyToAsync(self: Stream, destination: Stream, bufferSize: int, cancellationToken: CancellationToken) -> Task
        CopyToAsync(self: Stream, destination: Stream, bufferSize: int) -> Task
        CopyToAsync(self: Stream, destination: Stream) -> Task
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
        Dispose(self: Stream)
            Releases all resources used by the System.IO.Stream.
        """
        pass

    def EndRead(self, asyncResult):
        """
        EndRead(self: Stream, asyncResult: IAsyncResult) -> int
        
            Waits for the pending asynchronous read to complete.
        
            asyncResult: The reference to the pending asynchronous request to finish.
            Returns: The number of bytes read from the stream, between zero (0) and the number of bytes you 
             requested. Streams return zero (0) only at the end of the stream, otherwise, they should block 
             until at least one byte is available.
        """
        pass

    def EndWrite(self, asyncResult):
        """
        EndWrite(self: Stream, asyncResult: IAsyncResult)
            Ends an asynchronous write operation.
        
            asyncResult: A reference to the outstanding asynchronous I/O request.
        """
        pass

    def Flush(self):
        """
        Flush(self: Stream)
            When overridden in a derived class, clears all buffers for this stream and causes any buffered 
             data to be written to the underlying device.
        """
        pass

    def FlushAsync(self, cancellationToken=None):
        """
        FlushAsync(self: Stream, cancellationToken: CancellationToken) -> Task
        FlushAsync(self: Stream) -> Task
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
        Read(self: Stream, offset: int, count: int) -> (int, Array[Byte])
        
            When overridden in a derived class, reads a sequence of bytes from the current stream and 
             advances the position within the stream by the number of bytes read.
        
        
            offset: The zero-based byte offset in buffer at which to begin storing the data read from the current 
             stream.
        
            count: The maximum number of bytes to be read from the current stream.
            Returns: The total number of bytes read into the buffer. This can be less than the number of bytes 
             requested if that many bytes are not currently available, or zero (0) if the end of the stream 
             has been reached.
        """
        pass

    def ReadAsync(self, buffer, offset, count, cancellationToken=None):
        """
        ReadAsync(self: Stream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task[int]
        ReadAsync(self: Stream, buffer: Array[Byte], offset: int, count: int) -> Task[int]
        """
        pass

    def ReadByte(self):
        """
        ReadByte(self: Stream) -> int
        
            Reads a byte from the stream and advances the position within the stream by one byte, or returns 
             -1 if at the end of the stream.
        
            Returns: The unsigned byte cast to an Int32, or -1 if at the end of the stream.
        """
        pass

    def Seek(self, offset, origin):
        """
        Seek(self: Stream, offset: Int64, origin: SeekOrigin) -> Int64
        
            When overridden in a derived class, sets the position within the current stream.
        
            offset: A byte offset relative to the origin parameter.
            origin: A value of type System.IO.SeekOrigin indicating the reference point used to obtain the new 
             position.
        
            Returns: The new position within the current stream.
        """
        pass

    def SetLength(self, value):
        """
        SetLength(self: Stream, value: Int64)
            When overridden in a derived class, sets the length of the current stream.
        
            value: The desired length of the current stream in bytes.
        """
        pass

    @staticmethod
    def Synchronized(stream):
        """
        Synchronized(stream: Stream) -> Stream
        
            Creates a thread-safe (synchronized) wrapper around the specified System.IO.Stream object.
        
            stream: The System.IO.Stream object to synchronize.
            Returns: A thread-safe System.IO.Stream object.
        """
        pass

    def Write(self, buffer, offset, count):
        """
        Write(self: Stream, buffer: Array[Byte], offset: int, count: int)
            When overridden in a derived class, writes a sequence of bytes to the current stream and 
             advances the current position within this stream by the number of bytes written.
        
        
            buffer: An array of bytes. This method copies count bytes from buffer to the current stream.
            offset: The zero-based byte offset in buffer at which to begin copying bytes to the current stream.
            count: The number of bytes to be written to the current stream.
        """
        pass

    def WriteAsync(self, buffer, offset, count, cancellationToken=None):
        """
        WriteAsync(self: Stream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task
        WriteAsync(self: Stream, buffer: Array[Byte], offset: int, count: int) -> Task
        """
        pass

    def WriteByte(self, value):
        """
        WriteByte(self: Stream, value: Byte)
            Writes a byte to the current position in the stream and advances the position within the stream 
             by one byte.
        
        
            value: The byte to write to the stream.
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

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets a value indicating whether the current stream supports reading.

Get: CanRead(self: Stream) -> bool

"""

    CanSeek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets a value indicating whether the current stream supports seeking.

Get: CanSeek(self: Stream) -> bool

"""

    CanTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that determines whether the current stream can time out.

Get: CanTimeout(self: Stream) -> bool

"""

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets a value indicating whether the current stream supports writing.

Get: CanWrite(self: Stream) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the length in bytes of the stream.

Get: Length(self: Stream) -> Int64

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets or sets the position within the current stream.

Get: Position(self: Stream) -> Int64

Set: Position(self: Stream) = value
"""

    ReadTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value, in miliseconds, that determines how long the stream will attempt to read before timing out.

Get: ReadTimeout(self: Stream) -> int

Set: ReadTimeout(self: Stream) = value
"""

    WriteTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value, in miliseconds, that determines how long the stream will attempt to write before timing out.

Get: WriteTimeout(self: Stream) -> int

Set: WriteTimeout(self: Stream) = value
"""


    Null = None


class BufferedStream(Stream, IDisposable):
    """
    Adds a buffering layer to read and write operations on another stream. This class cannot be inherited.
    
    BufferedStream(stream: Stream)
    BufferedStream(stream: Stream, bufferSize: int)
    """
    def BeginRead(self, buffer, offset, count, callback, state):
        """ BeginRead(self: BufferedStream, buffer: Array[Byte], offset: int, count: int, callback: AsyncCallback, state: object) -> IAsyncResult """
        pass

    def BeginWrite(self, buffer, offset, count, callback, state):
        """ BeginWrite(self: BufferedStream, buffer: Array[Byte], offset: int, count: int, callback: AsyncCallback, state: object) -> IAsyncResult """
        pass

    def CreateWaitHandle(self, *args): #cannot find CLR method
        """
        CreateWaitHandle(self: Stream) -> WaitHandle
        
            Allocates a System.Threading.WaitHandle object.
            Returns: A reference to the allocated WaitHandle.
        """
        pass

    def Dispose(self):
        """ Dispose(self: BufferedStream, disposing: bool) """
        pass

    def EndRead(self, asyncResult):
        """ EndRead(self: BufferedStream, asyncResult: IAsyncResult) -> int """
        pass

    def EndWrite(self, asyncResult):
        """ EndWrite(self: BufferedStream, asyncResult: IAsyncResult) """
        pass

    def Flush(self):
        """
        Flush(self: BufferedStream)
            Clears all buffers for this stream and causes any buffered data to be written to the underlying 
             device.
        """
        pass

    def FlushAsync(self, cancellationToken=None):
        """ FlushAsync(self: BufferedStream, cancellationToken: CancellationToken) -> Task """
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
        Read(self: BufferedStream, offset: int, count: int) -> (int, Array[Byte])
        
            Copies bytes from the current buffered stream to an array.
        
            offset: The byte offset in the buffer at which to begin reading bytes.
            count: The number of bytes to be read.
            Returns: The total number of bytes read into array. This can be less than the number of bytes requested 
             if that many bytes are not currently available, or 0 if the end of the stream has been reached 
             before any data can be read.
        """
        pass

    def ReadAsync(self, buffer, offset, count, cancellationToken=None):
        """ ReadAsync(self: BufferedStream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task[int] """
        pass

    def ReadByte(self):
        """
        ReadByte(self: BufferedStream) -> int
        
            Reads a byte from the underlying stream and returns the byte cast to an int, or returns -1 if 
             reading from the end of the stream.
        
            Returns: The byte cast to an int, or -1 if reading from the end of the stream.
        """
        pass

    def Seek(self, offset, origin):
        """
        Seek(self: BufferedStream, offset: Int64, origin: SeekOrigin) -> Int64
        
            Sets the position within the current buffered stream.
        
            offset: A byte offset relative to origin.
            origin: A value of type System.IO.SeekOrigin indicating the reference point from which to obtain the new 
             position.
        
            Returns: The new position within the current buffered stream.
        """
        pass

    def SetLength(self, value):
        """
        SetLength(self: BufferedStream, value: Int64)
            Sets the length of the buffered stream.
        
            value: An integer indicating the desired length of the current buffered stream in bytes.
        """
        pass

    def Write(self, array, offset, count):
        """
        Write(self: BufferedStream, array: Array[Byte], offset: int, count: int)
            Copies bytes to the buffered stream and advances the current position within the buffered stream 
             by the number of bytes written.
        
        
            array: The byte array from which to copy count bytes to the current buffered stream.
            offset: The offset in the buffer at which to begin copying bytes to the current buffered stream.
            count: The number of bytes to be written to the current buffered stream.
        """
        pass

    def WriteAsync(self, buffer, offset, count, cancellationToken=None):
        """ WriteAsync(self: BufferedStream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task """
        pass

    def WriteByte(self, value):
        """
        WriteByte(self: BufferedStream, value: Byte)
            Writes a byte to the current position in the buffered stream.
        
            value: A byte to write to the stream.
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
    def __new__(self, stream, bufferSize=None):
        """
        __new__(cls: type, stream: Stream)
        __new__(cls: type, stream: Stream, bufferSize: int)
        """
        pass

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the current stream supports reading.

Get: CanRead(self: BufferedStream) -> bool

"""

    CanSeek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the current stream supports seeking.

Get: CanSeek(self: BufferedStream) -> bool

"""

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the current stream supports writing.

Get: CanWrite(self: BufferedStream) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the stream length in bytes.

Get: Length(self: BufferedStream) -> Int64

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the position within the current stream.

Get: Position(self: BufferedStream) -> Int64

Set: Position(self: BufferedStream) = value
"""



class Directory(object):
    """ Exposes static methods for creating, moving, and enumerating through directories and subdirectories. This class cannot be inherited. """
    @staticmethod
    def CreateDirectory(path, directorySecurity=None):
        """
        CreateDirectory(path: str, directorySecurity: DirectorySecurity) -> DirectoryInfo
        
            Creates all the directories in the specified path, applying the specified Windows security.
        
            path: The directory to create.
            directorySecurity: The access control to apply to the directory.
            Returns: A System.IO.DirectoryInfo object representing the newly created directory.
        CreateDirectory(path: str) -> DirectoryInfo
        
            Creates all directories and subdirectories in the specified path.
        
            path: The directory path to create.
            Returns: A System.IO.DirectoryInfo as specified by path.
        """
        pass

    @staticmethod
    def Delete(path, recursive=None):
        """
        Delete(path: str, recursive: bool)
            Deletes the specified directory and, if indicated, any subdirectories and files in the directory.
        
            path: The name of the directory to remove.
            recursive: true to remove directories, subdirectories, and files in path; otherwise, false.
        Delete(path: str)
            Deletes an empty directory from a specified path.
        
            path: The name of the empty directory to remove. This directory must be writable or empty.
        """
        pass

    @staticmethod
    def EnumerateDirectories(path, searchPattern=None, searchOption=None):
        """
        EnumerateDirectories(path: str, searchPattern: str, searchOption: SearchOption) -> IEnumerable[str]
        
            Returns an enumerable collection of directory names that match a search pattern in a specified 
             path, and optionally searches subdirectories.
        
        
            path: The directory to search.
            searchPattern: The search string to match against the names of directories in path.
            searchOption: One of the values of the System.IO.SearchOption enumeration that specifies whether the search 
             operation should include only the current directory or should include all subdirectories.The 
             default value is System.IO.SearchOption.TopDirectoryOnly.
        
            Returns: An enumerable collection of directory names in the directory specified by path and that match 
             searchPattern and searchOption.
        
        EnumerateDirectories(path: str, searchPattern: str) -> IEnumerable[str]
        
            Returns an enumerable collection of directory names that match a search pattern in a specified 
             path.
        
        
            path: The directory to search.
            searchPattern: The search string to match against the names of directories in path.
            Returns: An enumerable collection of directory names in the directory specified by path and that match 
             searchPattern.
        
        EnumerateDirectories(path: str) -> IEnumerable[str]
        
            Returns an enumerable collection of directory names in a specified path.
        
            path: The directory to search.
            Returns: An enumerable collection of directory names in the directory specified by path.
        """
        pass

    @staticmethod
    def EnumerateFiles(path, searchPattern=None, searchOption=None):
        """
        EnumerateFiles(path: str, searchPattern: str, searchOption: SearchOption) -> IEnumerable[str]
        
            Returns an enumerable collection of file names that match a search pattern in a specified path, 
             and optionally searches subdirectories.
        
        
            path: The directory to search.
            searchPattern: The search string to match against the names of directories in path.
            searchOption: One of the values of the System.IO.SearchOption enumeration that specifies whether the search 
             operation should include only the current directory or should include all subdirectories.The 
             default value is System.IO.SearchOption.TopDirectoryOnly.
        
            Returns: An enumerable collection of file names in the directory specified by path and that match 
             searchPattern and searchOption.
        
        EnumerateFiles(path: str, searchPattern: str) -> IEnumerable[str]
        
            Returns an enumerable collection of file names that match a search pattern in a specified path.
        
            path: The directory to search.
            searchPattern: The search string to match against the names of directories in path.
            Returns: An enumerable collection of file names in the directory specified by path and that match 
             searchPattern.
        
        EnumerateFiles(path: str) -> IEnumerable[str]
        
            Returns an enumerable collection of file names in a specified path.
        
            path: The directory to search.
            Returns: An enumerable collection of file names in the directory specified by path.
        """
        pass

    @staticmethod
    def EnumerateFileSystemEntries(path, searchPattern=None, searchOption=None):
        """
        EnumerateFileSystemEntries(path: str, searchPattern: str, searchOption: SearchOption) -> IEnumerable[str]
        
            Returns an enumerable collection of file names and directory names that match a search pattern 
             in a specified path, and optionally searches subdirectories.
        
        
            path: The directory to search.
            searchPattern: The search string to match against the names of directories in path.
            searchOption: One of the values of the System.IO.SearchOption enumeration that specifies whether the search 
             operation should include only the current directory or should include all subdirectories.The 
             default value is System.IO.SearchOption.TopDirectoryOnly.
        
            Returns: An enumerable collection of file-system entries in the directory specified by path and that 
             match searchPattern and searchOption.
        
        EnumerateFileSystemEntries(path: str, searchPattern: str) -> IEnumerable[str]
        
            Returns an enumerable collection of file-system entries that match a search pattern in a 
             specified path.
        
        
            path: The directory to search.
            searchPattern: The search string to match against the names of directories in path.
            Returns: An enumerable collection of file-system entries in the directory specified by path and that 
             match searchPattern.
        
        EnumerateFileSystemEntries(path: str) -> IEnumerable[str]
        
            Returns an enumerable collection of file-system entries in a specified path.
        
            path: The directory to search.
            Returns: An enumerable collection of file-system entries in the directory specified by path.
        """
        pass

    @staticmethod
    def Exists(path):
        """
        Exists(path: str) -> bool
        
            Determines whether the given path refers to an existing directory on disk.
        
            path: The path to test.
            Returns: true if path refers to an existing directory; otherwise, false.
        """
        pass

    @staticmethod
    def GetAccessControl(path, includeSections=None):
        """
        GetAccessControl(path: str, includeSections: AccessControlSections) -> DirectorySecurity
        
            Gets a System.Security.AccessControl.DirectorySecurity object that encapsulates the specified 
             type of access control list (ACL) entries for a specified directory.
        
        
            path: The path to a directory containing a System.Security.AccessControl.DirectorySecurity object that 
             describes the file's access control list (ACL) information.
        
            includeSections: One of the System.Security.AccessControl.AccessControlSections values that specifies the type of 
             access control list (ACL) information to receive.
        
            Returns: A System.Security.AccessControl.DirectorySecurity object that encapsulates the access control 
             rules for the file described by the path parameter.
        
        GetAccessControl(path: str) -> DirectorySecurity
        
            Gets a System.Security.AccessControl.DirectorySecurity object that encapsulates the access 
             control list (ACL) entries for a specified directory.
        
        
            path: The path to a directory containing a System.Security.AccessControl.DirectorySecurity object that 
             describes the file's access control list (ACL) information.
        
            Returns: A System.Security.AccessControl.DirectorySecurity object that encapsulates the access control 
             rules for the file described by the path parameter.
        """
        pass

    @staticmethod
    def GetCreationTime(path):
        """
        GetCreationTime(path: str) -> DateTime
        
            Gets the creation date and time of a directory.
        
            path: The path of the directory.
            Returns: A System.DateTime structure set to the creation date and time for the specified directory. This 
             value is expressed in local time.
        """
        pass

    @staticmethod
    def GetCreationTimeUtc(path):
        """
        GetCreationTimeUtc(path: str) -> DateTime
        
            Gets the creation date and time, in Coordinated Universal Time (UTC) format, of a directory.
        
            path: The path of the directory.
            Returns: A System.DateTime structure set to the creation date and time for the specified directory. This 
             value is expressed in UTC time.
        """
        pass

    @staticmethod
    def GetCurrentDirectory():
        """
        GetCurrentDirectory() -> str
        
            Gets the current working directory of the application.
            Returns: A string that contains the path of the current working directory, and does not end with a 
             backslash (\).
        """
        pass

    @staticmethod
    def GetDirectories(path, searchPattern=None, searchOption=None):
        """
        GetDirectories(path: str, searchPattern: str, searchOption: SearchOption) -> Array[str]
        
            Gets the names of the directories (including their paths) that match the specified search 
             pattern in the current directory, and optionally searches subdirectories.
        
        
            path: The path to search.
            searchPattern: The search string to match against the names of files in path. The parameter cannot end in two 
             periods ("..") or contain two periods ("..") followed by System.IO.Path.DirectorySeparatorChar 
             or System.IO.Path.AltDirectorySeparatorChar, nor can it contain any of the characters in 
             System.IO.Path.InvalidPathChars.
        
            searchOption: One of the System.IO.SearchOption values that specifies whether the search operation should 
             include all subdirectories or only the current directory.
        
            Returns: A String array of directories that match the search pattern.
        GetDirectories(path: str, searchPattern: str) -> Array[str]
        
            Gets an array of directories (including their paths) that match the specified search pattern in 
             the current directory.
        
        
            path: The path to search.
            searchPattern: The search string to match against the names of files in path. The parameter cannot end in two 
             periods ("..") or contain two periods ("..") followed by System.IO.Path.DirectorySeparatorChar 
             or System.IO.Path.AltDirectorySeparatorChar, nor can it contain any of the characters in 
             System.IO.Path.InvalidPathChars.
        
            Returns: A String array of directories that match the search pattern.
        GetDirectories(path: str) -> Array[str]
        
            Gets the names of subdirectories (including their paths) in the specified directory.
        
            path: The path for which an array of subdirectory names is returned.
            Returns: An array of the names of subdirectories in path.
        """
        pass

    @staticmethod
    def GetDirectoryRoot(path):
        """
        GetDirectoryRoot(path: str) -> str
        
            Returns the volume information, root information, or both for the specified path.
        
            path: The path of a file or directory.
            Returns: A string containing the volume information, root information, or both for the specified path.
        """
        pass

    @staticmethod
    def GetFiles(path, searchPattern=None, searchOption=None):
        """
        GetFiles(path: str, searchPattern: str, searchOption: SearchOption) -> Array[str]
        
            Returns the names of files (including their paths) that match the specified search pattern in 
             the specified directory, using a value to determine whether to search subdirectories.
        
        
            path: The directory to search.
            searchPattern: The search string to match against the names of files in path. The parameter cannot end in two 
             periods ("..") or contain two periods ("..") followed by System.IO.Path.DirectorySeparatorChar 
             or System.IO.Path.AltDirectorySeparatorChar, nor can it contain any of the characters in 
             System.IO.Path.InvalidPathChars.
        
            searchOption: One of the System.IO.SearchOption values that specifies whether the search operation should 
             include all subdirectories or only the current directory.
        
            Returns: A String array containing the names of files in the specified directory that match the specified 
             search pattern. File names include the full path.
        
        GetFiles(path: str, searchPattern: str) -> Array[str]
        
            Returns the names of files (including their paths) that match the specified search pattern in 
             the specified directory.
        
        
            path: The directory to search.
            searchPattern: The search string to match against the names of files in path. The parameter cannot end in two 
             periods ("..") or contain two periods ("..") followed by System.IO.Path.DirectorySeparatorChar 
             or System.IO.Path.AltDirectorySeparatorChar, nor can it contain any of the characters in 
             System.IO.Path.InvalidPathChars.
        
            Returns: A String array containing the names of files in the specified directory that match the specified 
             search pattern. File names include the full path.
        
        GetFiles(path: str) -> Array[str]
        
            Returns the names of files (including their paths) in the specified directory.
        
            path: The directory from which to retrieve the files.
            Returns: A String array of file names in the specified directory.
        """
        pass

    @staticmethod
    def GetFileSystemEntries(path, searchPattern=None, searchOption=None):
        """
        GetFileSystemEntries(path: str, searchPattern: str, searchOption: SearchOption) -> Array[str]
        
            Gets an array of all the file names and directory names that match a search pattern in a 
             specified path, and optionally searches subdirectories.
        
        
            path: The directory to search.
            searchPattern: The string used to search for all files or directories that match its search pattern. The 
             default pattern is for all files and directories: "*"
        
            searchOption: The option that specifies whether the search operation should include only the current directory 
             or should include all subdirectories.The default value is 
             System.IO.SearchOption.TopDirectoryOnly.
        
            Returns: An array of file system entries that match the search criteria.
        GetFileSystemEntries(path: str, searchPattern: str) -> Array[str]
        
            Returns an array of file system entries that match the specified search criteria.
        
            path: The path to be searched.
            searchPattern: The search string to match against the names of files in path. The searchPattern parameter 
             cannot end in two periods ("..") or contain two periods ("..") followed by 
             System.IO.Path.DirectorySeparatorChar or System.IO.Path.AltDirectorySeparatorChar, nor can it 
             contain any of the characters in System.IO.Path.InvalidPathChars.
        
            Returns: An array of file system entries that match the search criteria.
        GetFileSystemEntries(path: str) -> Array[str]
        
            Returns the names of all files and subdirectories in the specified directory.
        
            path: The directory for which file and subdirectory names are returned.
            Returns: An array that contains the names of files and subdirectories in the specified directory.
        """
        pass

    @staticmethod
    def GetLastAccessTime(path):
        """
        GetLastAccessTime(path: str) -> DateTime
        
            Returns the date and time the specified file or directory was last accessed.
        
            path: The file or directory for which to obtain access date and time information.
            Returns: A System.DateTime structure set to the date and time the specified file or directory was last 
             accessed. This value is expressed in local time.
        """
        pass

    @staticmethod
    def GetLastAccessTimeUtc(path):
        """
        GetLastAccessTimeUtc(path: str) -> DateTime
        
            Returns the date and time, in Coordinated Universal Time (UTC) format, that the specified file 
             or directory was last accessed.
        
        
            path: The file or directory for which to obtain access date and time information.
            Returns: A System.DateTime structure set to the date and time the specified file or directory was last 
             accessed. This value is expressed in UTC time.
        """
        pass

    @staticmethod
    def GetLastWriteTime(path):
        """
        GetLastWriteTime(path: str) -> DateTime
        
            Returns the date and time the specified file or directory was last written to.
        
            path: The file or directory for which to obtain modification date and time information.
            Returns: A System.DateTime structure set to the date and time the specified file or directory was last 
             written to. This value is expressed in local time.
        """
        pass

    @staticmethod
    def GetLastWriteTimeUtc(path):
        """
        GetLastWriteTimeUtc(path: str) -> DateTime
        
            Returns the date and time, in Coordinated Universal Time (UTC) format, that the specified file 
             or directory was last written to.
        
        
            path: The file or directory for which to obtain modification date and time information.
            Returns: A System.DateTime structure set to the date and time the specified file or directory was last 
             written to. This value is expressed in UTC time.
        """
        pass

    @staticmethod
    def GetLogicalDrives():
        """
        GetLogicalDrives() -> Array[str]
        
            Retrieves the names of the logical drives on this computer in the form "<drive letter>:\".
            Returns: The logical drives on this computer.
        """
        pass

    @staticmethod
    def GetParent(path):
        """
        GetParent(path: str) -> DirectoryInfo
        
            Retrieves the parent directory of the specified path, including both absolute and relative paths.
        
            path: The path for which to retrieve the parent directory.
            Returns: The parent directory, or null if path is the root directory, including the root of a UNC server 
             or share name.
        """
        pass

    @staticmethod
    def Move(sourceDirName, destDirName):
        """
        Move(sourceDirName: str, destDirName: str)
            Moves a file or a directory and its contents to a new location.
        
            sourceDirName: The path of the file or directory to move.
            destDirName: The path to the new location for sourceDirName. If sourceDirName is a file, then destDirName 
             must also be a file name.
        """
        pass

    @staticmethod
    def SetAccessControl(path, directorySecurity):
        """
        SetAccessControl(path: str, directorySecurity: DirectorySecurity)
            Applies access control list (ACL) entries described by a 
             System.Security.AccessControl.DirectorySecurity object to the specified directory.
        
        
            path: A directory to add or remove access control list (ACL) entries from.
            directorySecurity: A System.Security.AccessControl.DirectorySecurity object that describes an ACL entry to apply to 
             the directory described by the path parameter.
        """
        pass

    @staticmethod
    def SetCreationTime(path, creationTime):
        """
        SetCreationTime(path: str, creationTime: DateTime)
            Sets the creation date and time for the specified file or directory.
        
            path: The file or directory for which to set the creation date and time information.
            creationTime: A System.DateTime containing the value to set for the creation date and time of path. This value 
             is expressed in local time.
        """
        pass

    @staticmethod
    def SetCreationTimeUtc(path, creationTimeUtc):
        """
        SetCreationTimeUtc(path: str, creationTimeUtc: DateTime)
            Sets the creation date and time, in Coordinated Universal Time (UTC) format, for the specified 
             file or directory.
        
        
            path: The file or directory for which to set the creation date and time information.
            creationTimeUtc: A System.DateTime containing the value to set for the creation date and time of path. This value 
             is expressed in UTC time.
        """
        pass

    @staticmethod
    def SetCurrentDirectory(path):
        """
        SetCurrentDirectory(path: str)
            Sets the application's current working directory to the specified directory.
        
            path: The path to which the current working directory is set.
        """
        pass

    @staticmethod
    def SetLastAccessTime(path, lastAccessTime):
        """
        SetLastAccessTime(path: str, lastAccessTime: DateTime)
            Sets the date and time the specified file or directory was last accessed.
        
            path: The file or directory for which to set the access date and time information.
            lastAccessTime: A System.DateTime containing the value to set for the access date and time of path. This value 
             is expressed in local time.
        """
        pass

    @staticmethod
    def SetLastAccessTimeUtc(path, lastAccessTimeUtc):
        """
        SetLastAccessTimeUtc(path: str, lastAccessTimeUtc: DateTime)
            Sets the date and time, in Coordinated Universal Time (UTC) format, that the specified file or 
             directory was last accessed.
        
        
            path: The file or directory for which to set the access date and time information.
            lastAccessTimeUtc: A System.DateTime containing the value to set for the access date and time of path. This value 
             is expressed in UTC time.
        """
        pass

    @staticmethod
    def SetLastWriteTime(path, lastWriteTime):
        """
        SetLastWriteTime(path: str, lastWriteTime: DateTime)
            Sets the date and time a directory was last written to.
        
            path: The path of the directory.
            lastWriteTime: The date and time the directory was last written to. This value is expressed in local time.
        """
        pass

    @staticmethod
    def SetLastWriteTimeUtc(path, lastWriteTimeUtc):
        """
        SetLastWriteTimeUtc(path: str, lastWriteTimeUtc: DateTime)
            Sets the date and time, in Coordinated Universal Time (UTC) format, that a directory was last 
             written to.
        
        
            path: The path of the directory.
            lastWriteTimeUtc: The date and time the directory was last written to. This value is expressed in UTC time.
        """
        pass

    __all__ = [
        'CreateDirectory',
        'Delete',
        'EnumerateDirectories',
        'EnumerateFiles',
        'EnumerateFileSystemEntries',
        'Exists',
        'GetAccessControl',
        'GetCreationTime',
        'GetCreationTimeUtc',
        'GetCurrentDirectory',
        'GetDirectories',
        'GetDirectoryRoot',
        'GetFiles',
        'GetFileSystemEntries',
        'GetLastAccessTime',
        'GetLastAccessTimeUtc',
        'GetLastWriteTime',
        'GetLastWriteTimeUtc',
        'GetLogicalDrives',
        'GetParent',
        'Move',
        'SetAccessControl',
        'SetCreationTime',
        'SetCreationTimeUtc',
        'SetCurrentDirectory',
        'SetLastAccessTime',
        'SetLastAccessTimeUtc',
        'SetLastWriteTime',
        'SetLastWriteTimeUtc',
    ]


class FileSystemInfo(MarshalByRefObject, ISerializable):
    """ Provides the base class for both System.IO.FileInfo and System.IO.DirectoryInfo objects. """
    def Delete(self):
        """
        Delete(self: FileSystemInfo)
            Deletes a file or directory.
        """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: FileSystemInfo, info: SerializationInfo, context: StreamingContext)
            Sets the System.Runtime.Serialization.SerializationInfo object with the file name and additional 
             exception information.
        
        
            info: The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about 
             the exception being thrown.
        
            context: The System.Runtime.Serialization.StreamingContext that contains contextual information about the 
             source or destination.
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

    def Refresh(self):
        """
        Refresh(self: FileSystemInfo)
            Refreshes the state of the object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the attributes for the current file or directory.

Get: Attributes(self: FileSystemInfo) -> FileAttributes

Set: Attributes(self: FileSystemInfo) = value
"""

    CreationTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the creation time of the current file or directory.

Get: CreationTime(self: FileSystemInfo) -> DateTime

Set: CreationTime(self: FileSystemInfo) = value
"""

    CreationTimeUtc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the creation time, in coordinated universal time (UTC), of the current file or directory.

Get: CreationTimeUtc(self: FileSystemInfo) -> DateTime

Set: CreationTimeUtc(self: FileSystemInfo) = value
"""

    Exists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the file or directory exists.

Get: Exists(self: FileSystemInfo) -> bool

"""

    Extension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the string representing the extension part of the file.

Get: Extension(self: FileSystemInfo) -> str

"""

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the full path of the directory or file.

Get: FullName(self: FileSystemInfo) -> str

"""

    LastAccessTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the time the current file or directory was last accessed.

Get: LastAccessTime(self: FileSystemInfo) -> DateTime

Set: LastAccessTime(self: FileSystemInfo) = value
"""

    LastAccessTimeUtc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the time, in coordinated universal time (UTC), that the current file or directory was last accessed.

Get: LastAccessTimeUtc(self: FileSystemInfo) -> DateTime

Set: LastAccessTimeUtc(self: FileSystemInfo) = value
"""

    LastWriteTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the time when the current file or directory was last written to.

Get: LastWriteTime(self: FileSystemInfo) -> DateTime

Set: LastWriteTime(self: FileSystemInfo) = value
"""

    LastWriteTimeUtc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the time, in coordinated universal time (UTC), when the current file or directory was last written to.

Get: LastWriteTimeUtc(self: FileSystemInfo) -> DateTime

Set: LastWriteTimeUtc(self: FileSystemInfo) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For files, gets the name of the file. For directories, gets the name of the last directory in the hierarchy if a hierarchy exists. Otherwise, the Name property gets the name of the directory.

Get: Name(self: FileSystemInfo) -> str

"""


    FullPath = None
    OriginalPath = None


class DirectoryInfo(FileSystemInfo, ISerializable):
    """
    Exposes instance methods for creating, moving, and enumerating through directories and subdirectories. This class cannot be inherited.
    
    DirectoryInfo(path: str)
    """
    def Create(self, directorySecurity=None):
        """
        Create(self: DirectoryInfo, directorySecurity: DirectorySecurity)
            Creates a directory using a System.Security.AccessControl.DirectorySecurity object.
        
            directorySecurity: The access control to apply to the directory.
        Create(self: DirectoryInfo)
            Creates a directory.
        """
        pass

    def CreateSubdirectory(self, path, directorySecurity=None):
        """
        CreateSubdirectory(self: DirectoryInfo, path: str, directorySecurity: DirectorySecurity) -> DirectoryInfo
        
            Creates a subdirectory or subdirectories on the specified path with the specified security. The 
             specified path can be relative to this instance of the System.IO.DirectoryInfo class.
        
        
            path: The specified path. This cannot be a different disk volume or Universal Naming Convention (UNC) 
             name.
        
            directorySecurity: The security to apply.
            Returns: The last directory specified in path.
        CreateSubdirectory(self: DirectoryInfo, path: str) -> DirectoryInfo
        
            Creates a subdirectory or subdirectories on the specified path. The specified path can be 
             relative to this instance of the System.IO.DirectoryInfo class.
        
        
            path: The specified path. This cannot be a different disk volume or Universal Naming Convention (UNC) 
             name.
        
            Returns: The last directory specified in path.
        """
        pass

    def Delete(self, recursive=None):
        """
        Delete(self: DirectoryInfo, recursive: bool)
            Deletes this instance of a System.IO.DirectoryInfo, specifying whether to delete subdirectories 
             and files.
        
        
            recursive: true to delete this directory, its subdirectories, and all files; otherwise, false.
        Delete(self: DirectoryInfo)
            Deletes this System.IO.DirectoryInfo if it is empty.
        """
        pass

    def EnumerateDirectories(self, searchPattern=None, searchOption=None):
        """
        EnumerateDirectories(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> IEnumerable[DirectoryInfo]
        
            Returns an enumerable collection of directory information that matches a specified search 
             pattern and search subdirectory option.
        
        
            searchPattern: The search string. The default pattern is "*", which returns all directories.
            searchOption: One of the enumeration values that specifies whether the search operation should include only 
             the current directory or all subdirectories. The default value is 
             System.IO.SearchOption.TopDirectoryOnly.
        
            Returns: An enumerable collection of directories that matches searchPattern and searchOption.
        EnumerateDirectories(self: DirectoryInfo, searchPattern: str) -> IEnumerable[DirectoryInfo]
        
            Returns an enumerable collection of directory information that matches a specified search 
             pattern.
        
        
            searchPattern: The search string. The default pattern is "*", which returns all directories.
            Returns: An enumerable collection of directories that matches searchPattern.
        EnumerateDirectories(self: DirectoryInfo) -> IEnumerable[DirectoryInfo]
        
            Returns an enumerable collection of directory information in the current directory.
            Returns: An enumerable collection of directories in the current directory.
        """
        pass

    def EnumerateFiles(self, searchPattern=None, searchOption=None):
        """
        EnumerateFiles(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> IEnumerable[FileInfo]
        
            Returns an enumerable collection of file information that matches a specified search pattern and 
             search subdirectory option.
        
        
            searchPattern: The search string. The default pattern is "*", which returns all files.
            searchOption: One of the enumeration values that specifies whether the search operation should include only 
             the current directory or all subdirectories. The default value is 
             System.IO.SearchOption.TopDirectoryOnly.
        
            Returns: An enumerable collection of files that matches searchPattern and searchOption.
        EnumerateFiles(self: DirectoryInfo, searchPattern: str) -> IEnumerable[FileInfo]
        
            Returns an enumerable collection of file information that matches a search pattern.
        
            searchPattern: The search string. The default pattern is "*", which returns all files.
            Returns: An enumerable collection of files that matches searchPattern.
        EnumerateFiles(self: DirectoryInfo) -> IEnumerable[FileInfo]
        
            Returns an enumerable collection of file information in the current directory.
            Returns: An enumerable collection of the files in the current directory.
        """
        pass

    def EnumerateFileSystemInfos(self, searchPattern=None, searchOption=None):
        """
        EnumerateFileSystemInfos(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> IEnumerable[FileSystemInfo]
        
            Returns an enumerable collection of file system information that matches a specified search 
             pattern and search subdirectory option.
        
        
            searchPattern: The search string. The default pattern is "*", which returns all files or directories.
            searchOption: One of the enumeration values that specifies whether the search operation should include only 
             the current directory or all subdirectories. The default value is 
             System.IO.SearchOption.TopDirectoryOnly.
        
            Returns: An enumerable collection of file system information objects that matches searchPattern and 
             searchOption.
        
        EnumerateFileSystemInfos(self: DirectoryInfo, searchPattern: str) -> IEnumerable[FileSystemInfo]
        
            Returns an enumerable collection of file system information that matches a specified search 
             pattern.
        
        
            searchPattern: The search string. The default pattern is "*", which returns all files and directories.
            Returns: An enumerable collection of file system information objects that matches searchPattern.
        EnumerateFileSystemInfos(self: DirectoryInfo) -> IEnumerable[FileSystemInfo]
        
            Returns an enumerable collection of file system information in the current directory.
            Returns: An enumerable collection of file system information in the current directory.
        """
        pass

    def GetAccessControl(self, includeSections=None):
        """
        GetAccessControl(self: DirectoryInfo, includeSections: AccessControlSections) -> DirectorySecurity
        
            Gets a System.Security.AccessControl.DirectorySecurity object that encapsulates the specified 
             type of access control list (ACL) entries for the directory described by the current 
             System.IO.DirectoryInfo object.
        
        
            includeSections: One of the System.Security.AccessControl.AccessControlSections values that specifies the type of 
             access control list (ACL) information to receive.
        
            Returns: A System.Security.AccessControl.DirectorySecurity object that encapsulates the access control 
             rules for the file described by the path parameter.ExceptionsException 
             typeConditionSystem.SystemExceptionThe directory could not be found or 
             modified.System.UnauthorizedAccessExceptionThe current process does not have access to open the 
             directory.System.IO.IOExceptionAn I/O error occurred while opening the 
             directory.System.PlatformNotSupportedExceptionThe current operating system is not Microsoft 
             Windows 2000 or later.System.UnauthorizedAccessExceptionThe directory is read-only.-or- This 
             operation is not supported on the current platform.-or- The caller does not have the required 
             permission.
        
        GetAccessControl(self: DirectoryInfo) -> DirectorySecurity
        
            Gets a System.Security.AccessControl.DirectorySecurity object that encapsulates the access 
             control list (ACL) entries for the directory described by the current System.IO.DirectoryInfo 
             object.
        
            Returns: A System.Security.AccessControl.DirectorySecurity object that encapsulates the access control 
             rules for the directory.
        """
        pass

    def GetDirectories(self, searchPattern=None, searchOption=None):
        """
        GetDirectories(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> Array[DirectoryInfo]
        
            Returns an array of directories in the current System.IO.DirectoryInfo matching the given search 
             criteria and using a value to determine whether to search subdirectories.
        
        
            searchPattern: The search string. For example, "System*" can be used to search for all directories that begin 
             with the word "System".
        
            searchOption: One of the enumeration values that specifies whether the search operation should include only 
             the current directory or all subdirectories.
        
            Returns: An array of type DirectoryInfo matching searchPattern.
        GetDirectories(self: DirectoryInfo, searchPattern: str) -> Array[DirectoryInfo]
        
            Returns an array of directories in the current System.IO.DirectoryInfo matching the given search 
             criteria.
        
        
            searchPattern: The search string. For example, "System*" can be used to search for all directories that begin 
             with the word "System".
        
            Returns: An array of type DirectoryInfo matching searchPattern.
        GetDirectories(self: DirectoryInfo) -> Array[DirectoryInfo]
        
            Returns the subdirectories of the current directory.
            Returns: An array of System.IO.DirectoryInfo objects.
        """
        pass

    def GetFiles(self, searchPattern=None, searchOption=None):
        """
        GetFiles(self: DirectoryInfo) -> Array[FileInfo]
        
            Returns a file list from the current directory.
            Returns: An array of type System.IO.FileInfo.
        GetFiles(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> Array[FileInfo]
        
            Returns a file list from the current directory matching the given search pattern and using a 
             value to determine whether to search subdirectories.
        
        
            searchPattern: The search string. For example, "System*" can be used to search for all directories that begin 
             with the word "System".
        
            searchOption: One of the enumeration values that specifies whether the search operation should include only 
             the current directory or all subdirectories.
        
            Returns: An array of type System.IO.FileInfo.
        GetFiles(self: DirectoryInfo, searchPattern: str) -> Array[FileInfo]
        
            Returns a file list from the current directory matching the given search pattern.
        
            searchPattern: The search string, such as "*.txt".
            Returns: An array of type System.IO.FileInfo.
        """
        pass

    def GetFileSystemInfos(self, searchPattern=None, searchOption=None):
        """
        GetFileSystemInfos(self: DirectoryInfo) -> Array[FileSystemInfo]
        
            Returns an array of strongly typed System.IO.FileSystemInfo entries representing all the files 
             and subdirectories in a directory.
        
            Returns: An array of strongly typed System.IO.FileSystemInfo entries.
        GetFileSystemInfos(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> Array[FileSystemInfo]
        
            Retrieves an array of System.IO.FileSystemInfo objects that represent the files and 
             subdirectories matching the specified search criteria.
        
        
            searchPattern: The search string. The default pattern is "*", which returns all files and directories.
            searchOption: One of the enumeration values that specifies whether the search operation should include only 
             the current directory or all subdirectories. The default value is 
             System.IO.SearchOption.TopDirectoryOnly.
        
            Returns: An array of file system entries that match the search criteria.
        GetFileSystemInfos(self: DirectoryInfo, searchPattern: str) -> Array[FileSystemInfo]
        
            Retrieves an array of strongly typed System.IO.FileSystemInfo objects representing the files and 
             subdirectories that match the specified search criteria.
        
        
            searchPattern: The search string. For example, "System*" can be used to search for all directories that begin 
             with the word "System".
        
            Returns: An array of strongly typed FileSystemInfo objects matching the search criteria.
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

    def MoveTo(self, destDirName):
        """
        MoveTo(self: DirectoryInfo, destDirName: str)
            Moves a System.IO.DirectoryInfo instance and its contents to a new path.
        
            destDirName: The name and path to which to move this directory. The destination cannot be another disk volume 
             or a directory with the identical name. It can be an existing directory to which you want to add 
             this directory as a subdirectory.
        """
        pass

    def SetAccessControl(self, directorySecurity):
        """
        SetAccessControl(self: DirectoryInfo, directorySecurity: DirectorySecurity)
            Applies access control list (ACL) entries described by a 
             System.Security.AccessControl.DirectorySecurity object to the directory described by the current 
             System.IO.DirectoryInfo object.
        
        
            directorySecurity: An object that describes an ACL entry to apply to the directory described by the path parameter.
        """
        pass

    def ToString(self):
        """
        ToString(self: DirectoryInfo) -> str
        
            Returns the original path that was passed by the user.
            Returns: Returns the original path that was passed by the user.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, path):
        """ __new__(cls: type, path: str) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Exists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the directory exists.

Get: Exists(self: DirectoryInfo) -> bool

"""

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullName(self: DirectoryInfo) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of this System.IO.DirectoryInfo instance.

Get: Name(self: DirectoryInfo) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent directory of a specified subdirectory.

Get: Parent(self: DirectoryInfo) -> DirectoryInfo

"""

    Root = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the root portion of a path.

Get: Root(self: DirectoryInfo) -> DirectoryInfo

"""


    FullPath = None
    OriginalPath = None


class IOException(SystemException, ISerializable, _Exception):
    """
    The exception that is thrown when an I/O error occurs.
    
    IOException()
    IOException(message: str)
    IOException(message: str, hresult: int)
    IOException(message: str, innerException: Exception)
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
    def __new__(self, message=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, hresult: int)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class DirectoryNotFoundException(IOException, ISerializable, _Exception):
    """
    The exception that is thrown when part of a file or directory cannot be found.
    
    DirectoryNotFoundException()
    DirectoryNotFoundException(message: str)
    DirectoryNotFoundException(message: str, innerException: Exception)
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
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class DriveInfo(object, ISerializable):
    """
    Provides access to information on a drive.
    
    DriveInfo(driveName: str)
    """
    @staticmethod
    def GetDrives():
        """
        GetDrives() -> Array[DriveInfo]
        
            Retrieves the drive names of all logical drives on a computer.
            Returns: An array of type System.IO.DriveInfo that represents the logical drives on a computer.
        """
        pass

    def ToString(self):
        """
        ToString(self: DriveInfo) -> str
        
            Returns a drive name as a string.
            Returns: The name of the drive.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, driveName):
        """ __new__(cls: type, driveName: str) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AvailableFreeSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates the amount of available free space on a drive.

Get: AvailableFreeSpace(self: DriveInfo) -> Int64

"""

    DriveFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the file system, such as NTFS or FAT32.

Get: DriveFormat(self: DriveInfo) -> str

"""

    DriveType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the drive type.

Get: DriveType(self: DriveInfo) -> DriveType

"""

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether a drive is ready.

Get: IsReady(self: DriveInfo) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of a drive.

Get: Name(self: DriveInfo) -> str

"""

    RootDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the root directory of a drive.

Get: RootDirectory(self: DriveInfo) -> DirectoryInfo

"""

    TotalFreeSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total amount of free space available on a drive.

Get: TotalFreeSpace(self: DriveInfo) -> Int64

"""

    TotalSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total size of storage space on a drive.

Get: TotalSize(self: DriveInfo) -> Int64

"""

    VolumeLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the volume label of a drive.

Get: VolumeLabel(self: DriveInfo) -> str

Set: VolumeLabel(self: DriveInfo) = value
"""



class DriveNotFoundException(IOException, ISerializable, _Exception):
    """
    The exception that is thrown when trying to access a drive or share that is not available.
    
    DriveNotFoundException()
    DriveNotFoundException(message: str)
    DriveNotFoundException(message: str, innerException: Exception)
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
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class DriveType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines constants for drive types, including CDRom, Fixed, Network, NoRootDirectory, Ram, Removable, and Unknown.
    
    enum DriveType, values: CDRom (5), Fixed (3), Network (4), NoRootDirectory (1), Ram (6), Removable (2), Unknown (0)
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

    CDRom = None
    Fixed = None
    Network = None
    NoRootDirectory = None
    Ram = None
    Removable = None
    Unknown = None
    value__ = None


class EndOfStreamException(IOException, ISerializable, _Exception):
    """
    The exception that is thrown when reading is attempted past the end of a stream.
    
    EndOfStreamException()
    EndOfStreamException(message: str)
    EndOfStreamException(message: str, innerException: Exception)
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
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class ErrorEventArgs(EventArgs):
    """
    Provides data for the System.IO.FileSystemWatcher.Error event.
    
    ErrorEventArgs(exception: Exception)
    """
    def GetException(self):
        """
        GetException(self: ErrorEventArgs) -> Exception
        
            Gets the System.Exception that represents the error that occurred.
            Returns: An System.Exception that represents the error that occurred.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, exception):
        """ __new__(cls: type, exception: Exception) """
        pass


class ErrorEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.IO.FileSystemWatcher.Error event of a System.IO.FileSystemWatcher object.
    
    ErrorEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ErrorEventHandler, sender: object, e: ErrorEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: ErrorEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ErrorEventHandler, sender: object, e: ErrorEventArgs) """
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


class File(object):
    """ Provides static methods for the creation, copying, deletion, moving, and opening of files, and aids in the creation of System.IO.FileStream objects. """
    @staticmethod
    def AppendAllLines(path, contents, encoding=None):
        """ AppendAllLines(path: str, contents: IEnumerable[str], encoding: Encoding)AppendAllLines(path: str, contents: IEnumerable[str]) """
        pass

    @staticmethod
    def AppendAllText(path, contents, encoding=None):
        """
        AppendAllText(path: str, contents: str, encoding: Encoding)
            Appends the specified string to the file, creating the file if it does not already exist.
        
            path: The file to append the specified string to.
            contents: The string to append to the file.
            encoding: The character encoding to use.
        AppendAllText(path: str, contents: str)
            Opens a file, appends the specified string to the file, and then closes the file. If the file 
             does not exist, this method creates a file, writes the specified string to the file, then closes 
             the file.
        
        
            path: The file to append the specified string to.
            contents: The string to append to the file.
        """
        pass

    @staticmethod
    def AppendText(path):
        """
        AppendText(path: str) -> StreamWriter
        
            Creates a System.IO.StreamWriter that appends UTF-8 encoded text to an existing file.
        
            path: The path to the file to append to.
            Returns: A StreamWriter that appends UTF-8 encoded text to an existing file.
        """
        pass

    @staticmethod
    def Copy(sourceFileName, destFileName, overwrite=None):
        """
        Copy(sourceFileName: str, destFileName: str, overwrite: bool)
            Copies an existing file to a new file. Overwriting a file of the same name is allowed.
        
            sourceFileName: The file to copy.
            destFileName: The name of the destination file. This cannot be a directory.
            overwrite: true if the destination file can be overwritten; otherwise, false.
        Copy(sourceFileName: str, destFileName: str)
            Copies an existing file to a new file. Overwriting a file of the same name is not allowed.
        
            sourceFileName: The file to copy.
            destFileName: The name of the destination file. This cannot be a directory or an existing file.
        """
        pass

    @staticmethod
    def Create(path, bufferSize=None, options=None, fileSecurity=None):
        """
        Create(path: str, bufferSize: int, options: FileOptions) -> FileStream
        
            Creates or overwrites the specified file, specifying a buffer size and a System.IO.FileOptions 
             value that describes how to create or overwrite the file.
        
        
            path: The name of the file.
            bufferSize: The number of bytes buffered for reads and writes to the file.
            options: One of the System.IO.FileOptions values that describes how to create or overwrite the file.
            Returns: A new file with the specified buffer size.
        Create(path: str, bufferSize: int, options: FileOptions, fileSecurity: FileSecurity) -> FileStream
        
            Creates or overwrites the specified file with the specified buffer size, file options, and file 
             security.
        
        
            path: The name of the file.
            bufferSize: The number of bytes buffered for reads and writes to the file.
            options: One of the System.IO.FileOptions values that describes how to create or overwrite the file.
            fileSecurity: One of the System.Security.AccessControl.FileSecurity values that determines the access control 
             and audit security for the file.
        
            Returns: A new file with the specified buffer size, file options, and file security.
        Create(path: str) -> FileStream
        
            Creates or overwrites a file in the specified path.
        
            path: The path and name of the file to create.
            Returns: A System.IO.FileStream that provides read/write access to the file specified in path.
        Create(path: str, bufferSize: int) -> FileStream
        
            Creates or overwrites the specified file.
        
            path: The name of the file.
            bufferSize: The number of bytes buffered for reads and writes to the file.
            Returns: A System.IO.FileStream with the specified buffer size that provides read/write access to the 
             file specified in path.
        """
        pass

    @staticmethod
    def CreateText(path):
        """
        CreateText(path: str) -> StreamWriter
        
            Creates or opens a file for writing UTF-8 encoded text.
        
            path: The file to be opened for writing.
            Returns: A System.IO.StreamWriter that writes to the specified file using UTF-8 encoding.
        """
        pass

    @staticmethod
    def Decrypt(path):
        """
        Decrypt(path: str)
            Decrypts a file that was encrypted by the current account using the 
             System.IO.File.Encrypt(System.String) method.
        
        
            path: A path that describes a file to decrypt.
        """
        pass

    @staticmethod
    def Delete(path):
        """
        Delete(path: str)
            Deletes the specified file.
        
            path: The name of the file to be deleted. Wildcard characters are not supported.
        """
        pass

    @staticmethod
    def Encrypt(path):
        """
        Encrypt(path: str)
            Encrypts a file so that only the account used to encrypt the file can decrypt it.
        
            path: A path that describes a file to encrypt.
        """
        pass

    @staticmethod
    def Exists(path):
        """
        Exists(path: str) -> bool
        
            Determines whether the specified file exists.
        
            path: The file to check.
            Returns: true if the caller has the required permissions and path contains the name of an existing file; 
             otherwise, false. This method also returns false if path is null, an invalid path, or a 
             zero-length string. If the caller does not have sufficient permissions to read the specified 
             file, no exception is thrown and the method returns false regardless of the existence of path.
        """
        pass

    @staticmethod
    def GetAccessControl(path, includeSections=None):
        """
        GetAccessControl(path: str, includeSections: AccessControlSections) -> FileSecurity
        
            Gets a System.Security.AccessControl.FileSecurity object that encapsulates the specified type of 
             access control list (ACL) entries for a particular file.
        
        
            path: The path to a file containing a System.Security.AccessControl.FileSecurity object that describes 
             the file's access control list (ACL) information.
        
            includeSections: One of the System.Security.AccessControl.AccessControlSections values that specifies the type of 
             access control list (ACL) information to receive.
        
            Returns: A System.Security.AccessControl.FileSecurity object that encapsulates the access control rules 
             for the file described by the path parameter.
        
        GetAccessControl(path: str) -> FileSecurity
        
            Gets a System.Security.AccessControl.FileSecurity object that encapsulates the access control 
             list (ACL) entries for a specified file.
        
        
            path: The path to a file containing a System.Security.AccessControl.FileSecurity object that describes 
             the file's access control list (ACL) information.
        
            Returns: A System.Security.AccessControl.FileSecurity object that encapsulates the access control rules 
             for the file described by the path parameter.
        """
        pass

    @staticmethod
    def GetAttributes(path):
        """
        GetAttributes(path: str) -> FileAttributes
        
            Gets the System.IO.FileAttributes of the file on the path.
        
            path: The path to the file.
            Returns: The System.IO.FileAttributes of the file on the path.
        """
        pass

    @staticmethod
    def GetCreationTime(path):
        """
        GetCreationTime(path: str) -> DateTime
        
            Returns the creation date and time of the specified file or directory.
        
            path: The file or directory for which to obtain creation date and time information.
            Returns: A System.DateTime structure set to the creation date and time for the specified file or 
             directory. This value is expressed in local time.
        """
        pass

    @staticmethod
    def GetCreationTimeUtc(path):
        """
        GetCreationTimeUtc(path: str) -> DateTime
        
            Returns the creation date and time, in coordinated universal time (UTC), of the specified file 
             or directory.
        
        
            path: The file or directory for which to obtain creation date and time information.
            Returns: A System.DateTime structure set to the creation date and time for the specified file or 
             directory. This value is expressed in UTC time.
        """
        pass

    @staticmethod
    def GetLastAccessTime(path):
        """
        GetLastAccessTime(path: str) -> DateTime
        
            Returns the date and time the specified file or directory was last accessed.
        
            path: The file or directory for which to obtain access date and time information.
            Returns: A System.DateTime structure set to the date and time that the specified file or directory was 
             last accessed. This value is expressed in local time.
        """
        pass

    @staticmethod
    def GetLastAccessTimeUtc(path):
        """
        GetLastAccessTimeUtc(path: str) -> DateTime
        
            Returns the date and time, in coordinated universal time (UTC), that the specified file or 
             directory was last accessed.
        
        
            path: The file or directory for which to obtain access date and time information.
            Returns: A System.DateTime structure set to the date and time that the specified file or directory was 
             last accessed. This value is expressed in UTC time.
        """
        pass

    @staticmethod
    def GetLastWriteTime(path):
        """
        GetLastWriteTime(path: str) -> DateTime
        
            Returns the date and time the specified file or directory was last written to.
        
            path: The file or directory for which to obtain write date and time information.
            Returns: A System.DateTime structure set to the date and time that the specified file or directory was 
             last written to. This value is expressed in local time.
        """
        pass

    @staticmethod
    def GetLastWriteTimeUtc(path):
        """
        GetLastWriteTimeUtc(path: str) -> DateTime
        
            Returns the date and time, in coordinated universal time (UTC), that the specified file or 
             directory was last written to.
        
        
            path: The file or directory for which to obtain write date and time information.
            Returns: A System.DateTime structure set to the date and time that the specified file or directory was 
             last written to. This value is expressed in UTC time.
        """
        pass

    @staticmethod
    def Move(sourceFileName, destFileName):
        """
        Move(sourceFileName: str, destFileName: str)
            Moves a specified file to a new location, providing the option to specify a new file name.
        
            sourceFileName: The name of the file to move.
            destFileName: The new path for the file.
        """
        pass

    @staticmethod
    def Open(path, mode, access=None, share=None):
        """
        Open(path: str, mode: FileMode, access: FileAccess, share: FileShare) -> FileStream
        
            Opens a System.IO.FileStream on the specified path, having the specified mode with read, write, 
             or read/write access and the specified sharing option.
        
        
            path: The file to open.
            mode: A System.IO.FileMode value that specifies whether a file is created if one does not exist, and 
             determines whether the contents of existing files are retained or overwritten.
        
            access: A System.IO.FileAccess value that specifies the operations that can be performed on the file.
            share: A System.IO.FileShare value specifying the type of access other threads have to the file.
            Returns: A System.IO.FileStream on the specified path, having the specified mode with read, write, or 
             read/write access and the specified sharing option.
        
        Open(path: str, mode: FileMode, access: FileAccess) -> FileStream
        
            Opens a System.IO.FileStream on the specified path, with the specified mode and access.
        
            path: The file to open.
            mode: A System.IO.FileMode value that specifies whether a file is created if one does not exist, and 
             determines whether the contents of existing files are retained or overwritten.
        
            access: A System.IO.FileAccess value that specifies the operations that can be performed on the file.
            Returns: An unshared System.IO.FileStream that provides access to the specified file, with the specified 
             mode and access.
        
        Open(path: str, mode: FileMode) -> FileStream
        
            Opens a System.IO.FileStream on the specified path with read/write access.
        
            path: The file to open.
            mode: A System.IO.FileMode value that specifies whether a file is created if one does not exist, and 
             determines whether the contents of existing files are retained or overwritten.
        
            Returns: A System.IO.FileStream opened in the specified mode and path, with read/write access and not 
             shared.
        """
        pass

    @staticmethod
    def OpenRead(path):
        """
        OpenRead(path: str) -> FileStream
        
            Opens an existing file for reading.
        
            path: The file to be opened for reading.
            Returns: A read-only System.IO.FileStream on the specified path.
        """
        pass

    @staticmethod
    def OpenText(path):
        """
        OpenText(path: str) -> StreamReader
        
            Opens an existing UTF-8 encoded text file for reading.
        
            path: The file to be opened for reading.
            Returns: A System.IO.StreamReader on the specified path.
        """
        pass

    @staticmethod
    def OpenWrite(path):
        """
        OpenWrite(path: str) -> FileStream
        
            Opens an existing file or creates a new file for writing.
        
            path: The file to be opened for writing.
            Returns: An unshared System.IO.FileStream object on the specified path with System.IO.FileAccess.Write 
             access.
        """
        pass

    @staticmethod
    def ReadAllBytes(path):
        """
        ReadAllBytes(path: str) -> Array[Byte]
        
            Opens a binary file, reads the contents of the file into a byte array, and then closes the file.
        
            path: The file to open for reading.
            Returns: A byte array containing the contents of the file.
        """
        pass

    @staticmethod
    def ReadAllLines(path, encoding=None):
        """
        ReadAllLines(path: str, encoding: Encoding) -> Array[str]
        
            Opens a file, reads all lines of the file with the specified encoding, and then closes the file.
        
            path: The file to open for reading.
            encoding: The encoding applied to the contents of the file.
            Returns: A string array containing all lines of the file.
        ReadAllLines(path: str) -> Array[str]
        
            Opens a text file, reads all lines of the file, and then closes the file.
        
            path: The file to open for reading.
            Returns: A string array containing all lines of the file.
        """
        pass

    @staticmethod
    def ReadAllText(path, encoding=None):
        """
        ReadAllText(path: str, encoding: Encoding) -> str
        
            Opens a file, reads all lines of the file with the specified encoding, and then closes the file.
        
            path: The file to open for reading.
            encoding: The encoding applied to the contents of the file.
            Returns: A string containing all lines of the file.
        ReadAllText(path: str) -> str
        
            Opens a text file, reads all lines of the file, and then closes the file.
        
            path: The file to open for reading.
            Returns: A string containing all lines of the file.
        """
        pass

    @staticmethod
    def ReadLines(path, encoding=None):
        """
        ReadLines(path: str, encoding: Encoding) -> IEnumerable[str]
        
            Read the lines of a file that has a specified encoding.
        
            path: The file to read.
            encoding: The encoding that is applied to the contents of the file.
            Returns: All the lines of the file, or the lines that are the result of a query.
        ReadLines(path: str) -> IEnumerable[str]
        
            Reads the lines of a file.
        
            path: The file to read.
            Returns: All the lines of the file, or the lines that are the result of a query.
        """
        pass

    @staticmethod
    def Replace(sourceFileName, destinationFileName, destinationBackupFileName, ignoreMetadataErrors=None):
        """
        Replace(sourceFileName: str, destinationFileName: str, destinationBackupFileName: str, ignoreMetadataErrors: bool)
            Replaces the contents of a specified file with the contents of another file, deleting the 
             original file, and creating a backup of the replaced file and optionally ignores merge errors.
        
        
            sourceFileName: The name of a file that replaces the file specified by destinationFileName.
            destinationFileName: The name of the file being replaced.
            destinationBackupFileName: The name of the backup file.
            ignoreMetadataErrors: true to ignore merge errors (such as attributes and access control lists (ACLs)) from the 
             replaced file to the replacement file; otherwise, false.
        
        Replace(sourceFileName: str, destinationFileName: str, destinationBackupFileName: str)
            Replaces the contents of a specified file with the contents of another file, deleting the 
             original file, and creating a backup of the replaced file.
        
        
            sourceFileName: The name of a file that replaces the file specified by destinationFileName.
            destinationFileName: The name of the file being replaced.
            destinationBackupFileName: The name of the backup file.
        """
        pass

    @staticmethod
    def SetAccessControl(path, fileSecurity):
        """
        SetAccessControl(path: str, fileSecurity: FileSecurity)
            Applies access control list (ACL) entries described by a 
             System.Security.AccessControl.FileSecurity object to the specified file.
        
        
            path: A file to add or remove access control list (ACL) entries from.
            fileSecurity: A System.Security.AccessControl.FileSecurity object that describes an ACL entry to apply to the 
             file described by the path parameter.
        """
        pass

    @staticmethod
    def SetAttributes(path, fileAttributes):
        """
        SetAttributes(path: str, fileAttributes: FileAttributes)
            Sets the specified System.IO.FileAttributes of the file on the specified path.
        
            path: The path to the file.
            fileAttributes: A bitwise combination of the enumeration values.
        """
        pass

    @staticmethod
    def SetCreationTime(path, creationTime):
        """
        SetCreationTime(path: str, creationTime: DateTime)
            Sets the date and time the file was created.
        
            path: The file for which to set the creation date and time information.
            creationTime: A System.DateTime containing the value to set for the creation date and time of path. This value 
             is expressed in local time.
        """
        pass

    @staticmethod
    def SetCreationTimeUtc(path, creationTimeUtc):
        """
        SetCreationTimeUtc(path: str, creationTimeUtc: DateTime)
            Sets the date and time, in coordinated universal time (UTC), that the file was created.
        
            path: The file for which to set the creation date and time information.
            creationTimeUtc: A System.DateTime containing the value to set for the creation date and time of path. This value 
             is expressed in UTC time.
        """
        pass

    @staticmethod
    def SetLastAccessTime(path, lastAccessTime):
        """
        SetLastAccessTime(path: str, lastAccessTime: DateTime)
            Sets the date and time the specified file was last accessed.
        
            path: The file for which to set the access date and time information.
            lastAccessTime: A System.DateTime containing the value to set for the last access date and time of path. This 
             value is expressed in local time.
        """
        pass

    @staticmethod
    def SetLastAccessTimeUtc(path, lastAccessTimeUtc):
        """
        SetLastAccessTimeUtc(path: str, lastAccessTimeUtc: DateTime)
            Sets the date and time, in coordinated universal time (UTC), that the specified file was last 
             accessed.
        
        
            path: The file for which to set the access date and time information.
            lastAccessTimeUtc: A System.DateTime containing the value to set for the last access date and time of path. This 
             value is expressed in UTC time.
        """
        pass

    @staticmethod
    def SetLastWriteTime(path, lastWriteTime):
        """
        SetLastWriteTime(path: str, lastWriteTime: DateTime)
            Sets the date and time that the specified file was last written to.
        
            path: The file for which to set the date and time information.
            lastWriteTime: A System.DateTime containing the value to set for the last write date and time of path. This 
             value is expressed in local time.
        """
        pass

    @staticmethod
    def SetLastWriteTimeUtc(path, lastWriteTimeUtc):
        """
        SetLastWriteTimeUtc(path: str, lastWriteTimeUtc: DateTime)
            Sets the date and time, in coordinated universal time (UTC), that the specified file was last 
             written to.
        
        
            path: The file for which to set the date and time information.
            lastWriteTimeUtc: A System.DateTime containing the value to set for the last write date and time of path. This 
             value is expressed in UTC time.
        """
        pass

    @staticmethod
    def WriteAllBytes(path, bytes):
        """
        WriteAllBytes(path: str, bytes: Array[Byte])
            Creates a new file, writes the specified byte array to the file, and then closes the file. If 
             the target file already exists, it is overwritten.
        
        
            path: The file to write to.
            bytes: The bytes to write to the file.
        """
        pass

    @staticmethod
    def WriteAllLines(path, contents, encoding=None):
        """
        WriteAllLines(path: str, contents: IEnumerable[str])WriteAllLines(path: str, contents: IEnumerable[str], encoding: Encoding)WriteAllLines(path: str, contents: Array[str])
            Creates a new file, write the specified string array to the file, and then closes the file.
        
            path: The file to write to.
            contents: The string array to write to the file.
        WriteAllLines(path: str, contents: Array[str], encoding: Encoding)
            Creates a new file, writes the specified string array to the file by using the specified 
             encoding, and then closes the file.
        
        
            path: The file to write to.
            contents: The string array to write to the file.
            encoding: An System.Text.Encoding object that represents the character encoding applied to the string 
             array.
        """
        pass

    @staticmethod
    def WriteAllText(path, contents, encoding=None):
        """
        WriteAllText(path: str, contents: str, encoding: Encoding)
            Creates a new file, writes the specified string to the file using the specified encoding, and 
             then closes the file. If the target file already exists, it is overwritten.
        
        
            path: The file to write to.
            contents: The string to write to the file.
            encoding: The encoding to apply to the string.
        WriteAllText(path: str, contents: str)
            Creates a new file, writes the specified string to the file, and then closes the file. If the 
             target file already exists, it is overwritten.
        
        
            path: The file to write to.
            contents: The string to write to the file.
        """
        pass

    __all__ = [
        'AppendAllLines',
        'AppendAllText',
        'AppendText',
        'Copy',
        'Create',
        'CreateText',
        'Decrypt',
        'Delete',
        'Encrypt',
        'Exists',
        'GetAccessControl',
        'GetAttributes',
        'GetCreationTime',
        'GetCreationTimeUtc',
        'GetLastAccessTime',
        'GetLastAccessTimeUtc',
        'GetLastWriteTime',
        'GetLastWriteTimeUtc',
        'Move',
        'Open',
        'OpenRead',
        'OpenText',
        'OpenWrite',
        'ReadAllBytes',
        'ReadAllLines',
        'ReadAllText',
        'ReadLines',
        'Replace',
        'SetAccessControl',
        'SetAttributes',
        'SetCreationTime',
        'SetCreationTimeUtc',
        'SetLastAccessTime',
        'SetLastAccessTimeUtc',
        'SetLastWriteTime',
        'SetLastWriteTimeUtc',
        'WriteAllBytes',
        'WriteAllLines',
        'WriteAllText',
    ]


class FileAccess(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines constants for read, write, or read/write access to a file.
    
    enum (flags) FileAccess, values: Read (1), ReadWrite (3), Write (2)
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

    Read = None
    ReadWrite = None
    value__ = None
    Write = None


class FileAttributes(Enum, IComparable, IFormattable, IConvertible):
    """
    Provides attributes for files and directories.
    
    enum (flags) FileAttributes, values: Archive (32), Compressed (2048), Device (64), Directory (16), Encrypted (16384), Hidden (2), IntegrityStream (32768), Normal (128), NoScrubData (131072), NotContentIndexed (8192), Offline (4096), ReadOnly (1), ReparsePoint (1024), SparseFile (512), System (4), Temporary (256)
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

    Archive = None
    Compressed = None
    Device = None
    Directory = None
    Encrypted = None
    Hidden = None
    IntegrityStream = None
    Normal = None
    NoScrubData = None
    NotContentIndexed = None
    Offline = None
    ReadOnly = None
    ReparsePoint = None
    SparseFile = None
    System = None
    Temporary = None
    value__ = None


class FileInfo(FileSystemInfo, ISerializable):
    """
    Provides properties and instance methods for the creation, copying, deletion, moving, and opening of files, and aids in the creation of System.IO.FileStream objects. This class cannot be inherited.
    
    FileInfo(fileName: str)
    """
    def AppendText(self):
        """
        AppendText(self: FileInfo) -> StreamWriter
        
            Creates a System.IO.StreamWriter that appends text to the file represented by this instance of 
             the System.IO.FileInfo.
        
            Returns: A new StreamWriter.
        """
        pass

    def CopyTo(self, destFileName, overwrite=None):
        """
        CopyTo(self: FileInfo, destFileName: str, overwrite: bool) -> FileInfo
        
            Copies an existing file to a new file, allowing the overwriting of an existing file.
        
            destFileName: The name of the new file to copy to.
            overwrite: true to allow an existing file to be overwritten; otherwise, false.
            Returns: A new file, or an overwrite of an existing file if overwrite is true. If the file exists and 
             overwrite is false, an System.IO.IOException is thrown.
        
        CopyTo(self: FileInfo, destFileName: str) -> FileInfo
        
            Copies an existing file to a new file, disallowing the overwriting of an existing file.
        
            destFileName: The name of the new file to copy to.
            Returns: A new file with a fully qualified path.
        """
        pass

    def Create(self):
        """
        Create(self: FileInfo) -> FileStream
        
            Creates a file.
            Returns: A new file.
        """
        pass

    def CreateText(self):
        """
        CreateText(self: FileInfo) -> StreamWriter
        
            Creates a System.IO.StreamWriter that writes a new text file.
            Returns: A new StreamWriter.
        """
        pass

    def Decrypt(self):
        """
        Decrypt(self: FileInfo)
            Decrypts a file that was encrypted by the current account using the System.IO.FileInfo.Encrypt 
             method.
        """
        pass

    def Delete(self):
        """
        Delete(self: FileInfo)
            Permanently deletes a file.
        """
        pass

    def Encrypt(self):
        """
        Encrypt(self: FileInfo)
            Encrypts a file so that only the account used to encrypt the file can decrypt it.
        """
        pass

    def GetAccessControl(self, includeSections=None):
        """
        GetAccessControl(self: FileInfo, includeSections: AccessControlSections) -> FileSecurity
        
            Gets a System.Security.AccessControl.FileSecurity object that encapsulates the specified type of 
             access control list (ACL) entries for the file described by the current System.IO.FileInfo 
             object.
        
        
            includeSections: One of the System.Security.AccessControl.AccessControlSections values that specifies which group 
             of access control entries to retrieve.
        
            Returns: A System.Security.AccessControl.FileSecurity object that encapsulates the access control rules 
             for the current file.
        
        GetAccessControl(self: FileInfo) -> FileSecurity
        
            Gets a System.Security.AccessControl.FileSecurity object that encapsulates the access control 
             list (ACL) entries for the file described by the current System.IO.FileInfo object.
        
            Returns: A System.Security.AccessControl.FileSecurity object that encapsulates the access control rules 
             for the current file.
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

    def MoveTo(self, destFileName):
        """
        MoveTo(self: FileInfo, destFileName: str)
            Moves a specified file to a new location, providing the option to specify a new file name.
        
            destFileName: The path to move the file to, which can specify a different file name.
        """
        pass

    def Open(self, mode, access=None, share=None):
        """
        Open(self: FileInfo, mode: FileMode, access: FileAccess, share: FileShare) -> FileStream
        
            Opens a file in the specified mode with read, write, or read/write access and the specified 
             sharing option.
        
        
            mode: A System.IO.FileMode constant specifying the mode (for example, Open or Append) in which to open 
             the file.
        
            access: A System.IO.FileAccess constant specifying whether to open the file with Read, Write, or 
             ReadWrite file access.
        
            share: A System.IO.FileShare constant specifying the type of access other FileStream objects have to 
             this file.
        
            Returns: A System.IO.FileStream object opened with the specified mode, access, and sharing options.
        Open(self: FileInfo, mode: FileMode, access: FileAccess) -> FileStream
        
            Opens a file in the specified mode with read, write, or read/write access.
        
            mode: A System.IO.FileMode constant specifying the mode (for example, Open or Append) in which to open 
             the file.
        
            access: A System.IO.FileAccess constant specifying whether to open the file with Read, Write, or 
             ReadWrite file access.
        
            Returns: A System.IO.FileStream object opened in the specified mode and access, and unshared.
        Open(self: FileInfo, mode: FileMode) -> FileStream
        
            Opens a file in the specified mode.
        
            mode: A System.IO.FileMode constant specifying the mode (for example, Open or Append) in which to open 
             the file.
        
            Returns: A file opened in the specified mode, with read/write access and unshared.
        """
        pass

    def OpenRead(self):
        """
        OpenRead(self: FileInfo) -> FileStream
        
            Creates a read-only System.IO.FileStream.
            Returns: A new read-only System.IO.FileStream object.
        """
        pass

    def OpenText(self):
        """
        OpenText(self: FileInfo) -> StreamReader
        
            Creates a System.IO.StreamReader with UTF8 encoding that reads from an existing text file.
            Returns: A new StreamReader with UTF8 encoding.
        """
        pass

    def OpenWrite(self):
        """
        OpenWrite(self: FileInfo) -> FileStream
        
            Creates a write-only System.IO.FileStream.
            Returns: A write-only unshared System.IO.FileStream object for a new or existing file.
        """
        pass

    def Replace(self, destinationFileName, destinationBackupFileName, ignoreMetadataErrors=None):
        """
        Replace(self: FileInfo, destinationFileName: str, destinationBackupFileName: str, ignoreMetadataErrors: bool) -> FileInfo
        
            Replaces the contents of a specified file with the file described by the current 
             System.IO.FileInfo object, deleting the original file, and creating a backup of the replaced 
             file.  Also specifies whether to ignore merge errors.
        
        
            destinationFileName: The name of a file to replace with the current file.
            destinationBackupFileName: The name of a file with which to create a backup of the file described by the destFileName 
             parameter.
        
            ignoreMetadataErrors: true to ignore merge errors (such as attributes and ACLs) from the replaced file to the 
             replacement file; otherwise false.
        
            Returns: A System.IO.FileInfo object that encapsulates information about the file described by the 
             destFileName parameter.
        
        Replace(self: FileInfo, destinationFileName: str, destinationBackupFileName: str) -> FileInfo
        
            Replaces the contents of a specified file with the file described by the current 
             System.IO.FileInfo object, deleting the original file, and creating a backup of the replaced 
             file.
        
        
            destinationFileName: The name of a file to replace with the current file.
            destinationBackupFileName: The name of a file with which to create a backup of the file described by the destFileName 
             parameter.
        
            Returns: A System.IO.FileInfo object that encapsulates information about the file described by the 
             destFileName parameter.
        """
        pass

    def SetAccessControl(self, fileSecurity):
        """
        SetAccessControl(self: FileInfo, fileSecurity: FileSecurity)
            Applies access control list (ACL) entries described by a 
             System.Security.AccessControl.FileSecurity object to the file described by the current 
             System.IO.FileInfo object.
        
        
            fileSecurity: A System.Security.AccessControl.FileSecurity object that describes an access control list (ACL) 
             entry to apply to the current file.
        """
        pass

    def ToString(self):
        """
        ToString(self: FileInfo) -> str
        
            Returns the path as a string.
            Returns: A string representing the path.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fileName):
        """ __new__(cls: type, fileName: str) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Directory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an instance of the parent directory.

Get: Directory(self: FileInfo) -> DirectoryInfo

"""

    DirectoryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a string representing the directory's full path.

Get: DirectoryName(self: FileInfo) -> str

"""

    Exists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether a file exists.

Get: Exists(self: FileInfo) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that determines if the current file is read only.

Get: IsReadOnly(self: FileInfo) -> bool

Set: IsReadOnly(self: FileInfo) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size, in bytes, of the current file.

Get: Length(self: FileInfo) -> Int64

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the file.

Get: Name(self: FileInfo) -> str

"""


    FullPath = None
    OriginalPath = None


class FileLoadException(IOException, ISerializable, _Exception):
    """
    The exception that is thrown when a managed assembly is found but cannot be loaded.
    
    FileLoadException()
    FileLoadException(message: str)
    FileLoadException(message: str, inner: Exception)
    FileLoadException(message: str, fileName: str)
    FileLoadException(message: str, fileName: str, inner: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: FileLoadException, info: SerializationInfo, context: StreamingContext)
            Sets the System.Runtime.Serialization.SerializationInfo with the file name and additional 
             exception information.
        
        
            info: The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about 
             the exception being thrown.
        
            context: The System.Runtime.Serialization.StreamingContext that contains contextual information about the 
             source or destination.
        """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def ToString(self):
        """
        ToString(self: FileLoadException) -> str
        
            Returns the fully qualified name of the current exception, and possibly the error message, the 
             name of the inner exception, and the stack trace.
        
            Returns: A string containing the fully qualified name of this exception, and possibly the error message, 
             the name of the inner exception, and the stack trace, depending on which 
             System.IO.FileLoadException constructor is used.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, message: str, fileName: str)
        __new__(cls: type, message: str, fileName: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the file that causes this exception.

Get: FileName(self: FileLoadException) -> str

"""

    FusionLog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the log file that describes why an assembly load failed.

Get: FusionLog(self: FileLoadException) -> str

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the error message and the name of the file that caused this exception.

Get: Message(self: FileLoadException) -> str

"""



class FileMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how the operating system should open a file.
    
    enum FileMode, values: Append (6), Create (2), CreateNew (1), Open (3), OpenOrCreate (4), Truncate (5)
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

    Append = None
    Create = None
    CreateNew = None
    Open = None
    OpenOrCreate = None
    Truncate = None
    value__ = None


class FileNotFoundException(IOException, ISerializable, _Exception):
    """
    The exception that is thrown when an attempt to access a file that does not exist on disk fails.
    
    FileNotFoundException()
    FileNotFoundException(message: str)
    FileNotFoundException(message: str, innerException: Exception)
    FileNotFoundException(message: str, fileName: str)
    FileNotFoundException(message: str, fileName: str, innerException: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: FileNotFoundException, info: SerializationInfo, context: StreamingContext)
            Sets the System.Runtime.Serialization.SerializationInfo object with the file name and additional 
             exception information.
        
        
            info: The object that holds the serialized object data about the exception being thrown.
            context: The object that contains contextual information about the source or destination.
        """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def ToString(self):
        """
        ToString(self: FileNotFoundException) -> str
        
            Returns the fully qualified name of this exception and possibly the error message, the name of 
             the inner exception, and the stack trace.
        
            Returns: The fully qualified name of this exception and possibly the error message, the name of the inner 
             exception, and the stack trace.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, message: str, fileName: str)
        __new__(cls: type, message: str, fileName: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the file that cannot be found.

Get: FileName(self: FileNotFoundException) -> str

"""

    FusionLog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the log file that describes why loading of an assembly failed.

Get: FusionLog(self: FileNotFoundException) -> str

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the error message that explains the reason for the exception.

Get: Message(self: FileNotFoundException) -> str

"""



class FileOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents additional options for creating a System.IO.FileStream object.
    
    enum (flags) FileOptions, values: Asynchronous (1073741824), DeleteOnClose (67108864), Encrypted (16384), None (0), RandomAccess (268435456), SequentialScan (134217728), WriteThrough (-2147483648)
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

    Asynchronous = None
    DeleteOnClose = None
    Encrypted = None
    None = None
    RandomAccess = None
    SequentialScan = None
    value__ = None
    WriteThrough = None


class FileShare(Enum, IComparable, IFormattable, IConvertible):
    """
    Contains constants for controlling the kind of access other System.IO.FileStream objects can have to the same file.
    
    enum (flags) FileShare, values: Delete (4), Inheritable (16), None (0), Read (1), ReadWrite (3), Write (2)
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

    Delete = None
    Inheritable = None
    None = None
    Read = None
    ReadWrite = None
    value__ = None
    Write = None


class FileStream(Stream, IDisposable):
    """
    Exposes a System.IO.Stream around a file, supporting both synchronous and asynchronous read and write operations.
    
    FileStream(path: str, mode: FileMode)
    FileStream(path: str, mode: FileMode, access: FileAccess)
    FileStream(path: str, mode: FileMode, access: FileAccess, share: FileShare)
    FileStream(path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int)
    FileStream(path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int, options: FileOptions)
    FileStream(path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int, useAsync: bool)
    FileStream(path: str, mode: FileMode, rights: FileSystemRights, share: FileShare, bufferSize: int, options: FileOptions, fileSecurity: FileSecurity)
    FileStream(path: str, mode: FileMode, rights: FileSystemRights, share: FileShare, bufferSize: int, options: FileOptions)
    FileStream(handle: IntPtr, access: FileAccess)
    FileStream(handle: IntPtr, access: FileAccess, ownsHandle: bool)
    FileStream(handle: IntPtr, access: FileAccess, ownsHandle: bool, bufferSize: int)
    FileStream(handle: IntPtr, access: FileAccess, ownsHandle: bool, bufferSize: int, isAsync: bool)
    FileStream(handle: SafeFileHandle, access: FileAccess)
    FileStream(handle: SafeFileHandle, access: FileAccess, bufferSize: int)
    FileStream(handle: SafeFileHandle, access: FileAccess, bufferSize: int, isAsync: bool)
    """
    def BeginRead(self, array, offset, numBytes, userCallback, stateObject):
        """
        BeginRead(self: FileStream, array: Array[Byte], offset: int, numBytes: int, userCallback: AsyncCallback, stateObject: object) -> IAsyncResult
        
            Begins an asynchronous read.
        
            array: The buffer to read data into.
            offset: The byte offset in array at which to begin reading.
            numBytes: The maximum number of bytes to read.
            userCallback: The method to be called when the asynchronous read operation is completed.
            stateObject: A user-provided object that distinguishes this particular asynchronous read request from other 
             requests.
        
            Returns: An object that references the asynchronous read.
        """
        pass

    def BeginWrite(self, array, offset, numBytes, userCallback, stateObject):
        """
        BeginWrite(self: FileStream, array: Array[Byte], offset: int, numBytes: int, userCallback: AsyncCallback, stateObject: object) -> IAsyncResult
        
            Begins an asynchronous write.
        
            array: The buffer containing data to write to the current stream.
            offset: The zero-based byte offset in array at which to begin copying bytes to the current stream.
            numBytes: The maximum number of bytes to write.
            userCallback: The method to be called when the asynchronous write operation is completed.
            stateObject: A user-provided object that distinguishes this particular asynchronous write request from other 
             requests.
        
            Returns: An object that references the asynchronous write.
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
        Dispose(self: FileStream, disposing: bool)
            Releases the unmanaged resources used by the System.IO.FileStream and optionally releases the 
             managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def EndRead(self, asyncResult):
        """
        EndRead(self: FileStream, asyncResult: IAsyncResult) -> int
        
            Waits for the pending asynchronous read to complete.
        
            asyncResult: The reference to the pending asynchronous request to wait for.
            Returns: The number of bytes read from the stream, between 0 and the number of bytes you requested. 
             Streams only return 0 at the end of the stream, otherwise, they should block until at least 1 
             byte is available.
        """
        pass

    def EndWrite(self, asyncResult):
        """
        EndWrite(self: FileStream, asyncResult: IAsyncResult)
            Ends an asynchronous write, blocking until the I/O operation has completed.
        
            asyncResult: The pending asynchronous I/O request.
        """
        pass

    def Flush(self, flushToDisk=None):
        """
        Flush(self: FileStream, flushToDisk: bool)
            Clears buffers for this stream and causes any buffered data to be written to the file, and also 
             clears all intermediate file buffers.
        
        
            flushToDisk: true to flush all intermediate file buffers; otherwise, false.
        Flush(self: FileStream)
            Clears buffers for this stream and causes any buffered data to be written to the file.
        """
        pass

    def FlushAsync(self, cancellationToken=None):
        """ FlushAsync(self: FileStream, cancellationToken: CancellationToken) -> Task """
        pass

    def GetAccessControl(self):
        """
        GetAccessControl(self: FileStream) -> FileSecurity
        
            Gets a System.Security.AccessControl.FileSecurity object that encapsulates the access control 
             list (ACL) entries for the file described by the current System.IO.FileStream object.
        
            Returns: An object that encapsulates the access control settings for the file described by the current 
             System.IO.FileStream object.
        """
        pass

    def Lock(self, position, length):
        """
        Lock(self: FileStream, position: Int64, length: Int64)
            Prevents other processes from reading from or writing to the System.IO.FileStream.
        
            position: The beginning of the range to lock. The value of this parameter must be equal to or greater than 
             zero (0).
        
            length: The range to be locked.
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
        Read(self: FileStream, offset: int, count: int) -> (int, Array[Byte])
        
            Reads a block of bytes from the stream and writes the data in a given buffer.
        
            offset: The byte offset in array at which the read bytes will be placed.
            count: The maximum number of bytes to read.
            Returns: The total number of bytes read into the buffer. This might be less than the number of bytes 
             requested if that number of bytes are not currently available, or zero if the end of the stream 
             is reached.
        """
        pass

    def ReadAsync(self, buffer, offset, count, cancellationToken=None):
        """ ReadAsync(self: FileStream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task[int] """
        pass

    def ReadByte(self):
        """
        ReadByte(self: FileStream) -> int
        
            Reads a byte from the file and advances the read position one byte.
            Returns: The byte, cast to an System.Int32, or -1 if the end of the stream has been reached.
        """
        pass

    def Seek(self, offset, origin):
        """
        Seek(self: FileStream, offset: Int64, origin: SeekOrigin) -> Int64
        
            Sets the current position of this stream to the given value.
        
            offset: The point relative to origin from which to begin seeking.
            origin: Specifies the beginning, the end, or the current position as a reference point for origin, using 
             a value of type System.IO.SeekOrigin.
        
            Returns: The new position in the stream.
        """
        pass

    def SetAccessControl(self, fileSecurity):
        """
        SetAccessControl(self: FileStream, fileSecurity: FileSecurity)
            Applies access control list (ACL) entries described by a 
             System.Security.AccessControl.FileSecurity object to the file described by the current 
             System.IO.FileStream object.
        
        
            fileSecurity: An object that describes an ACL entry to apply to the current file.
        """
        pass

    def SetLength(self, value):
        """
        SetLength(self: FileStream, value: Int64)
            Sets the length of this stream to the given value.
        
            value: The new length of the stream.
        """
        pass

    def Unlock(self, position, length):
        """
        Unlock(self: FileStream, position: Int64, length: Int64)
            Allows access by other processes to all or part of a file that was previously locked.
        
            position: The beginning of the range to unlock.
            length: The range to be unlocked.
        """
        pass

    def Write(self, array, offset, count):
        """
        Write(self: FileStream, array: Array[Byte], offset: int, count: int)
            Writes a block of bytes to this stream using data from a buffer.
        
            array: The buffer containing data to write to the stream.
            offset: The zero-based byte offset in array at which to begin copying bytes to the current stream.
            count: The number of bytes to be written to the current stream.
        """
        pass

    def WriteAsync(self, buffer, offset, count, cancellationToken=None):
        """ WriteAsync(self: FileStream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task """
        pass

    def WriteByte(self, value):
        """
        WriteByte(self: FileStream, value: Byte)
            Writes a byte to the current position in the file stream.
        
            value: A byte to write to the stream.
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
        __new__(cls: type, path: str, mode: FileMode)
        __new__(cls: type, path: str, mode: FileMode, access: FileAccess)
        __new__(cls: type, path: str, mode: FileMode, access: FileAccess, share: FileShare)
        __new__(cls: type, path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int)
        __new__(cls: type, path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int, options: FileOptions)
        __new__(cls: type, path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int, useAsync: bool)
        __new__(cls: type, path: str, mode: FileMode, rights: FileSystemRights, share: FileShare, bufferSize: int, options: FileOptions, fileSecurity: FileSecurity)
        __new__(cls: type, path: str, mode: FileMode, rights: FileSystemRights, share: FileShare, bufferSize: int, options: FileOptions)
        __new__(cls: type, handle: IntPtr, access: FileAccess)
        __new__(cls: type, handle: IntPtr, access: FileAccess, ownsHandle: bool)
        __new__(cls: type, handle: IntPtr, access: FileAccess, ownsHandle: bool, bufferSize: int)
        __new__(cls: type, handle: IntPtr, access: FileAccess, ownsHandle: bool, bufferSize: int, isAsync: bool)
        __new__(cls: type, handle: SafeFileHandle, access: FileAccess)
        __new__(cls: type, handle: SafeFileHandle, access: FileAccess, bufferSize: int)
        __new__(cls: type, handle: SafeFileHandle, access: FileAccess, bufferSize: int, isAsync: bool)
        """
        pass

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the current stream supports reading.

Get: CanRead(self: FileStream) -> bool

"""

    CanSeek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the current stream supports seeking.

Get: CanSeek(self: FileStream) -> bool

"""

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the current stream supports writing.

Get: CanWrite(self: FileStream) -> bool

"""

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the operating system file handle for the file that the current FileStream object encapsulates.

Get: Handle(self: FileStream) -> IntPtr

"""

    IsAsync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the FileStream was opened asynchronously or synchronously.

Get: IsAsync(self: FileStream) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length in bytes of the stream.

Get: Length(self: FileStream) -> Int64

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the FileStream that was passed to the constructor.

Get: Name(self: FileStream) -> str

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current position of this stream.

Get: Position(self: FileStream) -> Int64

Set: Position(self: FileStream) = value
"""

    SafeFileHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Microsoft.Win32.SafeHandles.SafeFileHandle object that represents the operating system file handle for the file that the current System.IO.FileStream object encapsulates.

Get: SafeFileHandle(self: FileStream) -> SafeFileHandle

"""



class FileSystemEventArgs(EventArgs):
    """
    Provides data for the directory events: System.IO.FileSystemWatcher.Changed, System.IO.FileSystemWatcher.Created, System.IO.FileSystemWatcher.Deleted.
    
    FileSystemEventArgs(changeType: WatcherChangeTypes, directory: str, name: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, changeType, directory, name):
        """ __new__(cls: type, changeType: WatcherChangeTypes, directory: str, name: str) """
        pass

    ChangeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of directory event that occurred.

Get: ChangeType(self: FileSystemEventArgs) -> WatcherChangeTypes

"""

    FullPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the fully qualifed path of the affected file or directory.

Get: FullPath(self: FileSystemEventArgs) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the affected file or directory.

Get: Name(self: FileSystemEventArgs) -> str

"""



class FileSystemEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.IO.FileSystemWatcher.Changed, System.IO.FileSystemWatcher.Created, or System.IO.FileSystemWatcher.Deleted event of a System.IO.FileSystemWatcher class.
    
    FileSystemEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: FileSystemEventHandler, sender: object, e: FileSystemEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: FileSystemEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: FileSystemEventHandler, sender: object, e: FileSystemEventArgs) """
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


class FileSystemWatcher(Component, IComponent, IDisposable, ISupportInitialize):
    """
    Listens to the file system change notifications and raises events when a directory, or file in a directory, changes.
    
    FileSystemWatcher()
    FileSystemWatcher(path: str)
    FileSystemWatcher(path: str, filter: str)
    """
    def BeginInit(self):
        """
        BeginInit(self: FileSystemWatcher)
            Begins the initialization of a System.IO.FileSystemWatcher used on a form or used by another 
             component. The initialization occurs at run time.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: FileSystemWatcher, disposing: bool)
            Releases the unmanaged resources used by the System.IO.FileSystemWatcher and optionally releases 
             the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def EndInit(self):
        """
        EndInit(self: FileSystemWatcher)
            Ends the initialization of a System.IO.FileSystemWatcher used on a form or used by another 
             component. The initialization occurs at run time.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Component, service: Type) -> object
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or 
             by its System.ComponentModel.Container.
        
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or 
             null if the System.ComponentModel.Component does not provide the specified service.
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

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: FileSystemWatcher, e: FileSystemEventArgs)
            Raises the System.IO.FileSystemWatcher.Changed event.
        
            e: A System.IO.FileSystemEventArgs that contains the event data.
        """
        pass

    def OnCreated(self, *args): #cannot find CLR method
        """
        OnCreated(self: FileSystemWatcher, e: FileSystemEventArgs)
            Raises the System.IO.FileSystemWatcher.Created event.
        
            e: A System.IO.FileSystemEventArgs that contains the event data.
        """
        pass

    def OnDeleted(self, *args): #cannot find CLR method
        """
        OnDeleted(self: FileSystemWatcher, e: FileSystemEventArgs)
            Raises the System.IO.FileSystemWatcher.Deleted event.
        
            e: A System.IO.FileSystemEventArgs that contains the event data.
        """
        pass

    def OnError(self, *args): #cannot find CLR method
        """
        OnError(self: FileSystemWatcher, e: ErrorEventArgs)
            Raises the System.IO.FileSystemWatcher.Error event.
        
            e: An System.IO.ErrorEventArgs that contains the event data.
        """
        pass

    def OnRenamed(self, *args): #cannot find CLR method
        """
        OnRenamed(self: FileSystemWatcher, e: RenamedEventArgs)
            Raises the System.IO.FileSystemWatcher.Renamed event.
        
            e: A System.IO.RenamedEventArgs that contains the event data.
        """
        pass

    def WaitForChanged(self, changeType, timeout=None):
        """
        WaitForChanged(self: FileSystemWatcher, changeType: WatcherChangeTypes, timeout: int) -> WaitForChangedResult
        
            A synchronous method that returns a structure that contains specific information on the change 
             that occurred, given the type of change you want to monitor and the time (in milliseconds) to 
             wait before timing out.
        
        
            changeType: The System.IO.WatcherChangeTypes to watch for.
            timeout: The time (in milliseconds) to wait before timing out.
            Returns: A System.IO.WaitForChangedResult that contains specific information on the change that occurred.
        WaitForChanged(self: FileSystemWatcher, changeType: WatcherChangeTypes) -> WaitForChangedResult
        
            A synchronous method that returns a structure that contains specific information on the change 
             that occurred, given the type of change you want to monitor.
        
        
            changeType: The System.IO.WatcherChangeTypes to watch for.
            Returns: A System.IO.WaitForChangedResult that contains specific information on the change that occurred.
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
    def __new__(self, path=None, filter=None):
        """
        __new__(cls: type)
        __new__(cls: type, path: str)
        __new__(cls: type, path: str, filter: str)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component can raise an event.

"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    EnableRaisingEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the component is enabled.

Get: EnableRaisingEvents(self: FileSystemWatcher) -> bool

Set: EnableRaisingEvents(self: FileSystemWatcher) = value
"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the filter string used to determine what files are monitored in a directory.

Get: Filter(self: FileSystemWatcher) -> str

Set: Filter(self: FileSystemWatcher) = value
"""

    IncludeSubdirectories = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether subdirectories within the specified path should be monitored.

Get: IncludeSubdirectories(self: FileSystemWatcher) -> bool

Set: IncludeSubdirectories(self: FileSystemWatcher) = value
"""

    InternalBufferSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the size (in bytes) of the internal buffer.

Get: InternalBufferSize(self: FileSystemWatcher) -> int

Set: InternalBufferSize(self: FileSystemWatcher) = value
"""

    NotifyFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of changes to watch for.

Get: NotifyFilter(self: FileSystemWatcher) -> NotifyFilters

Set: NotifyFilter(self: FileSystemWatcher) = value
"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the path of the directory to watch.

Get: Path(self: FileSystemWatcher) -> str

Set: Path(self: FileSystemWatcher) = value
"""

    Site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an System.ComponentModel.ISite for the System.IO.FileSystemWatcher.

Get: Site(self: FileSystemWatcher) -> ISite

Set: Site(self: FileSystemWatcher) = value
"""

    SynchronizingObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the object used to marshal the event handler calls issued as a result of a directory change.

Get: SynchronizingObject(self: FileSystemWatcher) -> ISynchronizeInvoke

Set: SynchronizingObject(self: FileSystemWatcher) = value
"""


    Changed = None
    Created = None
    Deleted = None
    Error = None
    Renamed = None


class InternalBufferOverflowException(SystemException, ISerializable, _Exception):
    """
    The exception thrown when the internal buffer overflows.
    
    InternalBufferOverflowException()
    InternalBufferOverflowException(message: str)
    InternalBufferOverflowException(message: str, inner: Exception)
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
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class InvalidDataException(SystemException, ISerializable, _Exception):
    """
    The exception that is thrown when a data stream is in an invalid format.
    
    InvalidDataException()
    InvalidDataException(message: str)
    InvalidDataException(message: str, innerException: Exception)
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
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class IODescriptionAttribute(DescriptionAttribute, _Attribute):
    """
    Sets the description visual designers can display when referencing an event, extender, or property.
    
    IODescriptionAttribute(description: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, description):
        """ __new__(cls: type, description: str) """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the description.

Get: Description(self: IODescriptionAttribute) -> str

"""

    DescriptionValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the string stored as the description.

"""



class MemoryStream(Stream, IDisposable):
    """
    Creates a stream whose backing store is memory.
    
    MemoryStream()
    MemoryStream(capacity: int)
    MemoryStream(buffer: Array[Byte])
    MemoryStream(buffer: Array[Byte], writable: bool)
    MemoryStream(buffer: Array[Byte], index: int, count: int)
    MemoryStream(buffer: Array[Byte], index: int, count: int, writable: bool)
    MemoryStream(buffer: Array[Byte], index: int, count: int, writable: bool, publiclyVisible: bool)
    """
    def CopyToAsync(self, destination, bufferSize=None, cancellationToken=None):
        """ CopyToAsync(self: MemoryStream, destination: Stream, bufferSize: int, cancellationToken: CancellationToken) -> Task """
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
        Dispose(self: MemoryStream, disposing: bool)
            Releases the unmanaged resources used by the System.IO.MemoryStream class and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def Flush(self):
        """
        Flush(self: MemoryStream)
            Overrides System.IO.Stream.Flush so that no action is performed.
        """
        pass

    def FlushAsync(self, cancellationToken=None):
        """ FlushAsync(self: MemoryStream, cancellationToken: CancellationToken) -> Task """
        pass

    def GetBuffer(self):
        """
        GetBuffer(self: MemoryStream) -> Array[Byte]
        
            Returns the array of unsigned bytes from which this stream was created.
            Returns: The byte array from which this stream was created, or the underlying array if a byte array was 
             not provided to the System.IO.MemoryStream constructor during construction of the current 
             instance.
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
        Read(self: MemoryStream, offset: int, count: int) -> (int, Array[Byte])
        
            Reads a block of bytes from the current stream and writes the data to a buffer.
        
            offset: The zero-based byte offset in buffer at which to begin storing data from the current stream.
            count: The maximum number of bytes to read.
            Returns: The total number of bytes written into the buffer. This can be less than the number of bytes 
             requested if that number of bytes are not currently available, or zero if the end of the stream 
             is reached before any bytes are read.
        """
        pass

    def ReadAsync(self, buffer, offset, count, cancellationToken=None):
        """ ReadAsync(self: MemoryStream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task[int] """
        pass

    def ReadByte(self):
        """
        ReadByte(self: MemoryStream) -> int
        
            Reads a byte from the current stream.
            Returns: The byte cast to a System.Int32, or -1 if the end of the stream has been reached.
        """
        pass

    def Seek(self, offset, loc):
        """
        Seek(self: MemoryStream, offset: Int64, loc: SeekOrigin) -> Int64
        
            Sets the position within the current stream to the specified value.
        
            offset: The new position within the stream. This is relative to the loc parameter, and can be positive 
             or negative.
        
            loc: A value of type System.IO.SeekOrigin, which acts as the seek reference point.
            Returns: The new position within the stream, calculated by combining the initial reference point and the 
             offset.
        """
        pass

    def SetLength(self, value):
        """
        SetLength(self: MemoryStream, value: Int64)
            Sets the length of the current stream to the specified value.
        
            value: The value at which to set the length.
        """
        pass

    def ToArray(self):
        """
        ToArray(self: MemoryStream) -> Array[Byte]
        
            Writes the stream contents to a byte array, regardless of the System.IO.MemoryStream.Position 
             property.
        
            Returns: A new byte array.
        """
        pass

    def TryGetBuffer(self, buffer):
        """ TryGetBuffer(self: MemoryStream) -> (bool, ArraySegment[Byte]) """
        pass

    def Write(self, buffer, offset, count):
        """
        Write(self: MemoryStream, buffer: Array[Byte], offset: int, count: int)
            Writes a block of bytes to the current stream using data read from a buffer.
        
            buffer: The buffer to write data from.
            offset: The zero-based byte offset in buffer at which to begin copying bytes to the current stream.
            count: The maximum number of bytes to write.
        """
        pass

    def WriteAsync(self, buffer, offset, count, cancellationToken=None):
        """ WriteAsync(self: MemoryStream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task """
        pass

    def WriteByte(self, value):
        """
        WriteByte(self: MemoryStream, value: Byte)
            Writes a byte to the current stream at the current position.
        
            value: The byte to write.
        """
        pass

    def WriteTo(self, stream):
        """
        WriteTo(self: MemoryStream, stream: Stream)
            Writes the entire contents of this memory stream to another stream.
        
            stream: The stream to write this memory stream to.
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
        __new__(cls: type, capacity: int)
        __new__(cls: type, buffer: Array[Byte])
        __new__(cls: type, buffer: Array[Byte], writable: bool)
        __new__(cls: type, buffer: Array[Byte], index: int, count: int)
        __new__(cls: type, buffer: Array[Byte], index: int, count: int, writable: bool)
        __new__(cls: type, buffer: Array[Byte], index: int, count: int, writable: bool, publiclyVisible: bool)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the current stream supports reading.

Get: CanRead(self: MemoryStream) -> bool

"""

    CanSeek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the current stream supports seeking.

Get: CanSeek(self: MemoryStream) -> bool

"""

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the current stream supports writing.

Get: CanWrite(self: MemoryStream) -> bool

"""

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of bytes allocated for this stream.

Get: Capacity(self: MemoryStream) -> int

Set: Capacity(self: MemoryStream) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length of the stream in bytes.

Get: Length(self: MemoryStream) -> Int64

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current position within the stream.

Get: Position(self: MemoryStream) -> Int64

Set: Position(self: MemoryStream) = value
"""



class NotifyFilters(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies changes to watch for in a file or folder.
    
    enum (flags) NotifyFilters, values: Attributes (4), CreationTime (64), DirectoryName (2), FileName (1), LastAccess (32), LastWrite (16), Security (256), Size (8)
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

    Attributes = None
    CreationTime = None
    DirectoryName = None
    FileName = None
    LastAccess = None
    LastWrite = None
    Security = None
    Size = None
    value__ = None


class Path(object):
    """ Performs operations on System.String instances that contain file or directory path information. These operations are performed in a cross-platform manner. """
    @staticmethod
    def ChangeExtension(path, extension):
        """
        ChangeExtension(path: str, extension: str) -> str
        
            Changes the extension of a path string.
        
            path: The path information to modify. The path cannot contain any of the characters defined in 
             System.IO.Path.GetInvalidPathChars.
        
            extension: The new extension (with or without a leading period). Specify null to remove an existing 
             extension from path.
        
            Returns: The modified path information.On Windows-based desktop platforms, if path is null or an empty 
             string (""), the path information is returned unmodified. If extension is null, the returned 
             string contains the specified path with its extension removed. If path has no extension, and 
             extension is not null, the returned path string contains extension appended to the end of path.
        """
        pass

    @staticmethod
    def Combine(*__args):
        """
        Combine(path1: str, path2: str, path3: str, path4: str) -> str
        
            Combines four strings into a path.
        
            path1: The first path to combine.
            path2: The second path to combine.
            path3: The third path to combine.
            path4: The fourth path to combine.
            Returns: The combined paths.
        Combine(*paths: Array[str]) -> str
        
            Combines an array of strings into a path.
        
            paths: An array of parts of the path.
            Returns: The combined paths.
        Combine(path1: str, path2: str) -> str
        
            Combines two strings into a path.
        
            path1: The first path to combine.
            path2: The second path to combine.
            Returns: The combined paths. If one of the specified paths is a zero-length string, this method returns 
             the other path. If path2 contains an absolute path, this method returns path2.
        
        Combine(path1: str, path2: str, path3: str) -> str
        
            Combines three strings into a path.
        
            path1: The first path to combine.
            path2: The second path to combine.
            path3: The third path to combine.
            Returns: The combined paths.
        """
        pass

    @staticmethod
    def GetDirectoryName(path):
        """
        GetDirectoryName(path: str) -> str
        
            Returns the directory information for the specified path string.
        
            path: The path of a file or directory.
            Returns: Directory information for path, or null if path denotes a root directory or is null. Returns 
             System.String.Empty if path does not contain directory information.
        """
        pass

    @staticmethod
    def GetExtension(path):
        """
        GetExtension(path: str) -> str
        
            Returns the extension of the specified path string.
        
            path: The path string from which to get the extension.
            Returns: The extension of the specified path (including the period "."), or null, or System.String.Empty. 
             If path is null, System.IO.Path.GetExtension(System.String) returns null. If path does not have 
             extension information, System.IO.Path.GetExtension(System.String) returns System.String.Empty.
        """
        pass

    @staticmethod
    def GetFileName(path):
        """
        GetFileName(path: str) -> str
        
            Returns the file name and extension of the specified path string.
        
            path: The path string from which to obtain the file name and extension.
            Returns: The characters after the last directory character in path. If the last character of path is a 
             directory or volume separator character, this method returns System.String.Empty. If path is 
             null, this method returns null.
        """
        pass

    @staticmethod
    def GetFileNameWithoutExtension(path):
        """
        GetFileNameWithoutExtension(path: str) -> str
        
            Returns the file name of the specified path string without the extension.
        
            path: The path of the file.
            Returns: The string returned by System.IO.Path.GetFileName(System.String), minus the last period (.) and 
             all characters following it.
        """
        pass

    @staticmethod
    def GetFullPath(path):
        """
        GetFullPath(path: str) -> str
        
            Returns the absolute path for the specified path string.
        
            path: The file or directory for which to obtain absolute path information.
            Returns: The fully qualified location of path, such as "C:\MyFile.txt".
        """
        pass

    @staticmethod
    def GetInvalidFileNameChars():
        """
        GetInvalidFileNameChars() -> Array[Char]
        
            Gets an array containing the characters that are not allowed in file names.
            Returns: An array containing the characters that are not allowed in file names.
        """
        pass

    @staticmethod
    def GetInvalidPathChars():
        """
        GetInvalidPathChars() -> Array[Char]
        
            Gets an array containing the characters that are not allowed in path names.
            Returns: An array containing the characters that are not allowed in path names.
        """
        pass

    @staticmethod
    def GetPathRoot(path):
        """
        GetPathRoot(path: str) -> str
        
            Gets the root directory information of the specified path.
        
            path: The path from which to obtain root directory information.
            Returns: The root directory of path, such as "C:\", or null if path is null, or an empty string if path 
             does not contain root directory information.
        """
        pass

    @staticmethod
    def GetRandomFileName():
        """
        GetRandomFileName() -> str
        
            Returns a random folder name or file name.
            Returns: A random folder name or file name.
        """
        pass

    @staticmethod
    def GetTempFileName():
        """
        GetTempFileName() -> str
        
            Creates a uniquely named, zero-byte temporary file on disk and returns the full path of that 
             file.
        
            Returns: The full path of the temporary file.
        """
        pass

    @staticmethod
    def GetTempPath():
        """
        GetTempPath() -> str
        
            Returns the path of the current user's temporary folder.
            Returns: The path to the temporary folder, ending with a backslash.
        """
        pass

    @staticmethod
    def HasExtension(path):
        """
        HasExtension(path: str) -> bool
        
            Determines whether a path includes a file name extension.
        
            path: The path to search for an extension.
            Returns: true if the characters that follow the last directory separator (\\ or /) or volume separator 
             (:) in the path include a period (.) followed by one or more characters; otherwise, false.
        """
        pass

    @staticmethod
    def IsPathRooted(path):
        """
        IsPathRooted(path: str) -> bool
        
            Gets a value indicating whether the specified path string contains a root.
        
            path: The path to test.
            Returns: true if path contains a root; otherwise, false.
        """
        pass

    AltDirectorySeparatorChar = None
    DirectorySeparatorChar = None
    InvalidPathChars = None
    PathSeparator = None
    VolumeSeparatorChar = None
    __all__ = [
        'AltDirectorySeparatorChar',
        'ChangeExtension',
        'Combine',
        'DirectorySeparatorChar',
        'GetDirectoryName',
        'GetExtension',
        'GetFileName',
        'GetFileNameWithoutExtension',
        'GetFullPath',
        'GetInvalidFileNameChars',
        'GetInvalidPathChars',
        'GetPathRoot',
        'GetRandomFileName',
        'GetTempFileName',
        'GetTempPath',
        'HasExtension',
        'InvalidPathChars',
        'IsPathRooted',
        'PathSeparator',
        'VolumeSeparatorChar',
    ]


class PathTooLongException(IOException, ISerializable, _Exception):
    """
    The exception that is thrown when a path or file name is longer than the system-defined maximum length.
    
    PathTooLongException()
    PathTooLongException(message: str)
    PathTooLongException(message: str, innerException: Exception)
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
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class RenamedEventArgs(FileSystemEventArgs):
    """
    Provides data for the System.IO.FileSystemWatcher.Renamed event.
    
    RenamedEventArgs(changeType: WatcherChangeTypes, directory: str, name: str, oldName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, changeType, directory, name, oldName):
        """ __new__(cls: type, changeType: WatcherChangeTypes, directory: str, name: str, oldName: str) """
        pass

    OldFullPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the previous fully qualified path of the affected file or directory.

Get: OldFullPath(self: RenamedEventArgs) -> str

"""

    OldName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the old name of the affected file or directory.

Get: OldName(self: RenamedEventArgs) -> str

"""



class RenamedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.IO.FileSystemWatcher.Renamed event of a System.IO.FileSystemWatcher class.
    
    RenamedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: RenamedEventHandler, sender: object, e: RenamedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: RenamedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: RenamedEventHandler, sender: object, e: RenamedEventArgs) """
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


class SearchOption(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies whether to search the current directory, or the current directory and all subdirectories.
    
    enum SearchOption, values: AllDirectories (1), TopDirectoryOnly (0)
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

    AllDirectories = None
    TopDirectoryOnly = None
    value__ = None


class SeekOrigin(Enum, IComparable, IFormattable, IConvertible):
    """
    Provides the fields that represent reference points in streams for seeking.
    
    enum SeekOrigin, values: Begin (0), Current (1), End (2)
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

    Begin = None
    Current = None
    End = None
    value__ = None


class TextReader(MarshalByRefObject, IDisposable):
    """ Represents a reader that can read a sequential series of characters. """
    def Close(self):
        """
        Close(self: TextReader)
            Closes the System.IO.TextReader and releases any system resources associated with the TextReader.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: TextReader)
            Releases all resources used by the System.IO.TextReader object.
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

    def Peek(self):
        """
        Peek(self: TextReader) -> int
        
            Reads the next character without changing the state of the reader or the character source. 
             Returns the next available character without actually reading it from the input stream.
        
            Returns: An integer representing the next character to be read, or -1 if no more characters are available 
             or the stream does not support seeking.
        """
        pass

    def Read(self, buffer=None, index=None, count=None):
        """
        Read(self: TextReader, index: int, count: int) -> (int, Array[Char])
        
            Reads a maximum of count characters from the current stream and writes the data to buffer, 
             beginning at index.
        
        
            index: The position in buffer at which to begin writing.
            count: The maximum number of characters to read. If the end of the stream is reached before count of 
             characters is read into buffer, the current method returns.
        
            Returns: The number of characters that have been read. The number will be less than or equal to count, 
             depending on whether the data is available within the stream. This method returns zero if called 
             when no more characters are left to read.
        
        Read(self: TextReader) -> int
        
            Reads the next character from the input stream and advances the character position by one 
             character.
        
            Returns: The next character from the input stream, or -1 if no more characters are available. The default 
             implementation returns -1.
        """
        pass

    def ReadAsync(self, buffer, index, count):
        """ ReadAsync(self: TextReader, buffer: Array[Char], index: int, count: int) -> Task[int] """
        pass

    def ReadBlock(self, buffer, index, count):
        """
        ReadBlock(self: TextReader, index: int, count: int) -> (int, Array[Char])
        
            Reads a maximum of count characters from the current stream, and writes the data to buffer, 
             beginning at index.
        
        
            index: The position in buffer at which to begin writing.
            count: The maximum number of characters to read.
            Returns: The position of the underlying stream is advanced by the number of characters that were read 
             into buffer.The number of characters that have been read. The number will be less than or equal 
             to count, depending on whether all input characters have been read.
        """
        pass

    def ReadBlockAsync(self, buffer, index, count):
        """ ReadBlockAsync(self: TextReader, buffer: Array[Char], index: int, count: int) -> Task[int] """
        pass

    def ReadLine(self):
        """
        ReadLine(self: TextReader) -> str
        
            Reads a line of characters from the current stream and returns the data as a string.
            Returns: The next line from the input stream, or null if all characters have been read.
        """
        pass

    def ReadLineAsync(self):
        """ ReadLineAsync(self: TextReader) -> Task[str] """
        pass

    def ReadToEnd(self):
        """
        ReadToEnd(self: TextReader) -> str
        
            Reads all characters from the current position to the end of the TextReader and returns them as 
             one string.
        
            Returns: A string containing all characters from the current position to the end of the TextReader.
        """
        pass

    def ReadToEndAsync(self):
        """ ReadToEndAsync(self: TextReader) -> Task[str] """
        pass

    @staticmethod
    def Synchronized(reader):
        """
        Synchronized(reader: TextReader) -> TextReader
        
            Creates a thread-safe wrapper around the specified TextReader.
        
            reader: The TextReader to synchronize.
            Returns: A thread-safe System.IO.TextReader.
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

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Null = None


class StreamReader(TextReader, IDisposable):
    """
    Implements a System.IO.TextReader that reads characters from a byte stream in a particular encoding.
    
    StreamReader(stream: Stream)
    StreamReader(stream: Stream, detectEncodingFromByteOrderMarks: bool)
    StreamReader(stream: Stream, encoding: Encoding)
    StreamReader(stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool)
    StreamReader(stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int)
    StreamReader(stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int, leaveOpen: bool)
    StreamReader(path: str)
    StreamReader(path: str, detectEncodingFromByteOrderMarks: bool)
    StreamReader(path: str, encoding: Encoding)
    StreamReader(path: str, encoding: Encoding, detectEncodingFromByteOrderMarks: bool)
    StreamReader(path: str, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int)
    """
    def Close(self):
        """
        Close(self: StreamReader)
            Closes the System.IO.StreamReader object and the underlying stream, and releases any system 
             resources associated with the reader.
        """
        pass

    def DiscardBufferedData(self):
        """
        DiscardBufferedData(self: StreamReader)
            Clears the internal buffer.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: StreamReader, disposing: bool)
            Closes the underlying stream, releases the unmanaged resources used by the 
             System.IO.StreamReader, and optionally releases the managed resources.
        
        
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

    def Peek(self):
        """
        Peek(self: StreamReader) -> int
        
            Returns the next available character but does not consume it.
            Returns: An integer representing the next character to be read, or -1 if there are no characters to be 
             read or if the stream does not support seeking.
        """
        pass

    def Read(self, buffer=None, index=None, count=None):
        """
        Read(self: StreamReader, index: int, count: int) -> (int, Array[Char])
        
            Reads a specified maximum of characters from the current stream into a buffer, beginning at the 
             specified index.
        
        
            index: The index of buffer at which to begin writing.
            count: The maximum number of characters to read.
            Returns: The number of characters that have been read, or 0 if at the end of the stream and no data was 
             read. The number will be less than or equal to the count parameter, depending on whether the 
             data is available within the stream.
        
        Read(self: StreamReader) -> int
        
            Reads the next character from the input stream and advances the character position by one 
             character.
        
            Returns: The next character from the input stream represented as an System.Int32 object, or -1 if no more 
             characters are available.
        """
        pass

    def ReadAsync(self, buffer, index, count):
        """ ReadAsync(self: StreamReader, buffer: Array[Char], index: int, count: int) -> Task[int] """
        pass

    def ReadBlock(self, buffer, index, count):
        """ ReadBlock(self: StreamReader, index: int, count: int) -> (int, Array[Char]) """
        pass

    def ReadBlockAsync(self, buffer, index, count):
        """ ReadBlockAsync(self: StreamReader, buffer: Array[Char], index: int, count: int) -> Task[int] """
        pass

    def ReadLine(self):
        """
        ReadLine(self: StreamReader) -> str
        
            Reads a line of characters from the current stream and returns the data as a string.
            Returns: The next line from the input stream, or null if the end of the input stream is reached.
        """
        pass

    def ReadLineAsync(self):
        """ ReadLineAsync(self: StreamReader) -> Task[str] """
        pass

    def ReadToEnd(self):
        """
        ReadToEnd(self: StreamReader) -> str
        
            Reads the stream from the current position to the end of the stream.
            Returns: The rest of the stream as a string, from the current position to the end. If the current 
             position is at the end of the stream, returns an empty string ("").
        """
        pass

    def ReadToEndAsync(self):
        """ ReadToEndAsync(self: StreamReader) -> Task[str] """
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
        __new__(cls: type, stream: Stream)
        __new__(cls: type, stream: Stream, detectEncodingFromByteOrderMarks: bool)
        __new__(cls: type, stream: Stream, encoding: Encoding)
        __new__(cls: type, stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool)
        __new__(cls: type, stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int)
        __new__(cls: type, stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int, leaveOpen: bool)
        __new__(cls: type, path: str)
        __new__(cls: type, path: str, detectEncodingFromByteOrderMarks: bool)
        __new__(cls: type, path: str, encoding: Encoding)
        __new__(cls: type, path: str, encoding: Encoding, detectEncodingFromByteOrderMarks: bool)
        __new__(cls: type, path: str, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    BaseStream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the underlying stream.

Get: BaseStream(self: StreamReader) -> Stream

"""

    CurrentEncoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current character encoding that the current System.IO.StreamReader object is using.

Get: CurrentEncoding(self: StreamReader) -> Encoding

"""

    EndOfStream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the current stream position is at the end of the stream.

Get: EndOfStream(self: StreamReader) -> bool

"""


    Null = None


class TextWriter(MarshalByRefObject, IDisposable):
    """ Represents a writer that can write a sequential series of characters. This class is abstract. """
    def Close(self):
        """
        Close(self: TextWriter)
            Closes the current writer and releases any system resources associated with the writer.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: TextWriter)
            Releases all resources used by the System.IO.TextWriter object.
        """
        pass

    def Flush(self):
        """
        Flush(self: TextWriter)
            Clears all buffers for the current writer and causes any buffered data to be written to the 
             underlying device.
        """
        pass

    def FlushAsync(self):
        """ FlushAsync(self: TextWriter) -> Task """
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

    @staticmethod
    def Synchronized(writer):
        """
        Synchronized(writer: TextWriter) -> TextWriter
        
            Creates a thread-safe wrapper around the specified TextWriter.
        
            writer: The TextWriter to synchronize.
            Returns: A thread-safe wrapper.
        """
        pass

    def Write(self, *__args):
        """
        Write(self: TextWriter, value: str)
            Writes a string to the text stream.
        
            value: The string to write.
        Write(self: TextWriter, value: object)
            Writes the text representation of an object to the text stream by calling ToString on that 
             object.
        
        
            value: The object to write.
        Write(self: TextWriter, value: float)
            Writes the text representation of an 8-byte floating-point value to the text stream.
        
            value: The 8-byte floating-point value to write.
        Write(self: TextWriter, value: Decimal)
            Writes the text representation of a decimal value to the text stream.
        
            value: The decimal value to write.
        Write(self: TextWriter, format: str, arg0: object, arg1: object, arg2: object)
            Writes out a formatted string, using the same semantics as 
             System.String.Format(System.String,System.Object).
        
        
            format: The formatting string.
            arg0: An object to write into the formatted string.
            arg1: An object to write into the formatted string.
            arg2: An object to write into the formatted string.
        Write(self: TextWriter, format: str, *arg: Array[object])
            Writes out a formatted string, using the same semantics as 
             System.String.Format(System.String,System.Object).
        
        
            format: The formatting string.
            arg: The object array to write into the formatted string.
        Write(self: TextWriter, format: str, arg0: object)
            Writes out a formatted string, using the same semantics as 
             System.String.Format(System.String,System.Object).
        
        
            format: The formatting string.
            arg0: An object to write into the formatted string.
        Write(self: TextWriter, format: str, arg0: object, arg1: object)
            Writes out a formatted string, using the same semantics as 
             System.String.Format(System.String,System.Object).
        
        
            format: The formatting string.
            arg0: An object to write into the formatted string.
            arg1: An object to write into the formatted string.
        Write(self: TextWriter, value: Single)
            Writes the text representation of a 4-byte floating-point value to the text stream.
        
            value: The 4-byte floating-point value to write.
        Write(self: TextWriter, buffer: Array[Char], index: int, count: int)
            Writes a subarray of characters to the text stream.
        
            buffer: The character array to write data from.
            index: Starting index in the buffer.
            count: The number of characters to write.
        Write(self: TextWriter, value: bool)
            Writes the text representation of a Boolean value to the text stream.
        
            value: The Boolean to write.
        Write(self: TextWriter, value: Char)
            Writes a character to the text stream.
        
            value: The character to write to the text stream.
        Write(self: TextWriter, buffer: Array[Char])
            Writes a character array to the text stream.
        
            buffer: The character array to write to the text stream.
        Write(self: TextWriter, value: Int64)
            Writes the text representation of an 8-byte signed integer to the text stream.
        
            value: The 8-byte signed integer to write.
        Write(self: TextWriter, value: UInt64)
            Writes the text representation of an 8-byte unsigned integer to the text stream.
        
            value: The 8-byte unsigned integer to write.
        Write(self: TextWriter, value: int)
            Writes the text representation of a 4-byte signed integer to the text stream.
        
            value: The 4-byte signed integer to write.
        Write(self: TextWriter, value: UInt32)
            Writes the text representation of a 4-byte unsigned integer to the text stream.
        
            value: The 4-byte unsigned integer to write.
        """
        pass

    def WriteAsync(self, *__args):
        """
        WriteAsync(self: TextWriter, buffer: Array[Char]) -> Task
        WriteAsync(self: TextWriter, buffer: Array[Char], index: int, count: int) -> Task
        WriteAsync(self: TextWriter, value: Char) -> Task
        WriteAsync(self: TextWriter, value: str) -> Task
        """
        pass

    def WriteLine(self, *__args):
        """
        WriteLine(self: TextWriter, value: Decimal)
            Writes the text representation of a decimal value followed by a line terminator to the text 
             stream.
        
        
            value: The decimal value to write.
        WriteLine(self: TextWriter, value: str)
            Writes a string followed by a line terminator to the text stream.
        
            value: The string to write. If value is null, only the line termination characters are written.
        WriteLine(self: TextWriter, value: Single)
            Writes the text representation of a 4-byte floating-point value followed by a line terminator to 
             the text stream.
        
        
            value: The 4-byte floating-point value to write.
        WriteLine(self: TextWriter, value: float)
            Writes the text representation of a 8-byte floating-point value followed by a line terminator to 
             the text stream.
        
        
            value: The 8-byte floating-point value to write.
        WriteLine(self: TextWriter, value: object)
            Writes the text representation of an object by calling ToString on this object, followed by a 
             line terminator to the text stream.
        
        
            value: The object to write. If value is null, only the line termination characters are written.
        WriteLine(self: TextWriter, format: str, arg0: object, arg1: object, arg2: object)
            Writes out a formatted string and a new line, using the same semantics as 
             System.String.Format(System.String,System.Object).
        
        
            format: The formatting string.
            arg0: The object to write into the format string.
            arg1: The object to write into the format string.
            arg2: The object to write into the format string.
        WriteLine(self: TextWriter, format: str, *arg: Array[object])
            Writes out a formatted string and a new line, using the same semantics as 
             System.String.Format(System.String,System.Object).
        
        
            format: The formatting string.
            arg: The object array to write into format string.
        WriteLine(self: TextWriter, format: str, arg0: object)
            Writes out a formatted string and a new line, using the same semantics as 
             System.String.Format(System.String,System.Object).
        
        
            format: The formatted string.
            arg0: The object to write into the formatted string.
        WriteLine(self: TextWriter, format: str, arg0: object, arg1: object)
            Writes out a formatted string and a new line, using the same semantics as 
             System.String.Format(System.String,System.Object).
        
        
            format: The formatting string.
            arg0: The object to write into the format string.
            arg1: The object to write into the format string.
        WriteLine(self: TextWriter, buffer: Array[Char])
            Writes an array of characters followed by a line terminator to the text stream.
        
            buffer: The character array from which data is read.
        WriteLine(self: TextWriter, buffer: Array[Char], index: int, count: int)
            Writes a subarray of characters followed by a line terminator to the text stream.
        
            buffer: The character array from which data is read.
            index: The index into buffer at which to begin reading.
            count: The maximum number of characters to write.
        WriteLine(self: TextWriter)
            Writes a line terminator to the text stream.
        WriteLine(self: TextWriter, value: Char)
            Writes a character followed by a line terminator to the text stream.
        
            value: The character to write to the text stream.
        WriteLine(self: TextWriter, value: bool)
            Writes the text representation of a Boolean followed by a line terminator to the text stream.
        
            value: The Boolean to write.
        WriteLine(self: TextWriter, value: Int64)
            Writes the text representation of an 8-byte signed integer followed by a line terminator to the 
             text stream.
        
        
            value: The 8-byte signed integer to write.
        WriteLine(self: TextWriter, value: UInt64)
            Writes the text representation of an 8-byte unsigned integer followed by a line terminator to 
             the text stream.
        
        
            value: The 8-byte unsigned integer to write.
        WriteLine(self: TextWriter, value: int)
            Writes the text representation of a 4-byte signed integer followed by a line terminator to the 
             text stream.
        
        
            value: The 4-byte signed integer to write.
        WriteLine(self: TextWriter, value: UInt32)
            Writes the text representation of a 4-byte unsigned integer followed by a line terminator to the 
             text stream.
        
        
            value: The 4-byte unsigned integer to write.
        """
        pass

    def WriteLineAsync(self, *__args):
        """
        WriteLineAsync(self: TextWriter, buffer: Array[Char], index: int, count: int) -> Task
        WriteLineAsync(self: TextWriter) -> Task
        WriteLineAsync(self: TextWriter, buffer: Array[Char]) -> Task
        WriteLineAsync(self: TextWriter, value: Char) -> Task
        WriteLineAsync(self: TextWriter, value: str) -> Task
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
        """
        __new__(cls: type)
        __new__(cls: type, formatProvider: IFormatProvider)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, returns the System.Text.Encoding in which the output is written.

Get: Encoding(self: TextWriter) -> Encoding

"""

    FormatProvider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that controls formatting.

Get: FormatProvider(self: TextWriter) -> IFormatProvider

"""

    NewLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the line terminator string used by the current TextWriter.

Get: NewLine(self: TextWriter) -> str

Set: NewLine(self: TextWriter) = value
"""


    CoreNewLine = None
    Null = None


class StreamWriter(TextWriter, IDisposable):
    """
    Implements a System.IO.TextWriter for writing characters to a stream in a particular encoding.
    
    StreamWriter(stream: Stream)
    StreamWriter(stream: Stream, encoding: Encoding)
    StreamWriter(stream: Stream, encoding: Encoding, bufferSize: int)
    StreamWriter(stream: Stream, encoding: Encoding, bufferSize: int, leaveOpen: bool)
    StreamWriter(path: str)
    StreamWriter(path: str, append: bool)
    StreamWriter(path: str, append: bool, encoding: Encoding)
    StreamWriter(path: str, append: bool, encoding: Encoding, bufferSize: int)
    """
    def Close(self):
        """
        Close(self: StreamWriter)
            Closes the current StreamWriter object and the underlying stream.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: StreamWriter, disposing: bool)
            Releases the unmanaged resources used by the System.IO.StreamWriter and optionally releases the 
             managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def Flush(self):
        """
        Flush(self: StreamWriter)
            Clears all buffers for the current writer and causes any buffered data to be written to the 
             underlying stream.
        """
        pass

    def FlushAsync(self):
        """ FlushAsync(self: StreamWriter) -> Task """
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

    def Write(self, *__args):
        """
        Write(self: StreamWriter, buffer: Array[Char], index: int, count: int)
            Writes a subarray of characters to the stream.
        
            buffer: A character array containing the data to write.
            index: The index into buffer at which to begin writing.
            count: The number of characters to read from buffer.
        Write(self: StreamWriter, value: str)
            Writes a string to the stream.
        
            value: The string to write to the stream. If value is null, nothing is written.
        Write(self: StreamWriter, value: Char)
            Writes a character to the stream.
        
            value: The character to write to the text stream.
        Write(self: StreamWriter, buffer: Array[Char])
            Writes a character array to the stream.
        
            buffer: A character array containing the data to write. If buffer is null, nothing is written.
        """
        pass

    def WriteAsync(self, *__args):
        """
        WriteAsync(self: StreamWriter, buffer: Array[Char], index: int, count: int) -> Task
        WriteAsync(self: StreamWriter, value: str) -> Task
        WriteAsync(self: StreamWriter, value: Char) -> Task
        """
        pass

    def WriteLineAsync(self, *__args):
        """
        WriteLineAsync(self: StreamWriter, value: str) -> Task
        WriteLineAsync(self: StreamWriter, buffer: Array[Char], index: int, count: int) -> Task
        WriteLineAsync(self: StreamWriter) -> Task
        WriteLineAsync(self: StreamWriter, value: Char) -> Task
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
        __new__(cls: type, stream: Stream)
        __new__(cls: type, stream: Stream, encoding: Encoding)
        __new__(cls: type, stream: Stream, encoding: Encoding, bufferSize: int)
        __new__(cls: type, stream: Stream, encoding: Encoding, bufferSize: int, leaveOpen: bool)
        __new__(cls: type, path: str)
        __new__(cls: type, path: str, append: bool)
        __new__(cls: type, path: str, append: bool, encoding: Encoding)
        __new__(cls: type, path: str, append: bool, encoding: Encoding, bufferSize: int)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    AutoFlush = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the System.IO.StreamWriter will flush its buffer to the underlying stream after every call to System.IO.StreamWriter.Write(System.Char).

Get: AutoFlush(self: StreamWriter) -> bool

Set: AutoFlush(self: StreamWriter) = value
"""

    BaseStream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the underlying stream that interfaces with a backing store.

Get: BaseStream(self: StreamWriter) -> Stream

"""

    Encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Text.Encoding in which the output is written.

Get: Encoding(self: StreamWriter) -> Encoding

"""


    CoreNewLine = None
    Null = None


class StringReader(TextReader, IDisposable):
    """
    Implements a System.IO.TextReader that reads from a string.
    
    StringReader(s: str)
    """
    def Close(self):
        """
        Close(self: StringReader)
            Closes the System.IO.StringReader.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: StringReader, disposing: bool)
            Releases the unmanaged resources used by the System.IO.StringReader and optionally releases the 
             managed resources.
        
        
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

    def Peek(self):
        """
        Peek(self: StringReader) -> int
        
            Returns the next available character but does not consume it.
            Returns: An integer representing the next character to be read, or -1 if no more characters are available 
             or the stream does not support seeking.
        """
        pass

    def Read(self, buffer=None, index=None, count=None):
        """
        Read(self: StringReader, index: int, count: int) -> (int, Array[Char])
        
            Reads a block of characters from the input string and advances the character position by count.
        
            index: The starting index in the buffer.
            count: The number of characters to read.
            Returns: The total number of characters read into the buffer. This can be less than the number of 
             characters requested if that many characters are not currently available, or zero if the end of 
             the underlying string has been reached.
        
        Read(self: StringReader) -> int
        
            Reads the next character from the input string and advances the character position by one 
             character.
        
            Returns: The next character from the underlying string, or -1 if no more characters are available.
        """
        pass

    def ReadAsync(self, buffer, index, count):
        """ ReadAsync(self: StringReader, buffer: Array[Char], index: int, count: int) -> Task[int] """
        pass

    def ReadBlockAsync(self, buffer, index, count):
        """ ReadBlockAsync(self: StringReader, buffer: Array[Char], index: int, count: int) -> Task[int] """
        pass

    def ReadLine(self):
        """
        ReadLine(self: StringReader) -> str
        
            Reads a line from the underlying string.
            Returns: The next line from the underlying string, or null if the end of the underlying string is reached.
        """
        pass

    def ReadLineAsync(self):
        """ ReadLineAsync(self: StringReader) -> Task[str] """
        pass

    def ReadToEnd(self):
        """
        ReadToEnd(self: StringReader) -> str
        
            Reads the stream as a string, either in its entirety or from the current position to the end of 
             the stream.
        
            Returns: The content from the current position to the end of the underlying string.
        """
        pass

    def ReadToEndAsync(self):
        """ ReadToEndAsync(self: StringReader) -> Task[str] """
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
    def __new__(self, s):
        """ __new__(cls: type, s: str) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class StringWriter(TextWriter, IDisposable):
    """
    Implements a System.IO.TextWriter for writing information to a string. The information is stored in an underlying System.Text.StringBuilder.
    
    StringWriter()
    StringWriter(formatProvider: IFormatProvider)
    StringWriter(sb: StringBuilder)
    StringWriter(sb: StringBuilder, formatProvider: IFormatProvider)
    """
    def Close(self):
        """
        Close(self: StringWriter)
            Closes the current System.IO.StringWriter and the underlying stream.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: StringWriter, disposing: bool)
            Releases the unmanaged resources used by the System.IO.StringWriter and optionally releases the 
             managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def FlushAsync(self):
        """ FlushAsync(self: StringWriter) -> Task """
        pass

    def GetStringBuilder(self):
        """
        GetStringBuilder(self: StringWriter) -> StringBuilder
        
            Returns the underlying System.Text.StringBuilder.
            Returns: The underlying StringBuilder.
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

    def ToString(self):
        """
        ToString(self: StringWriter) -> str
        
            Returns a string containing the characters written to the current StringWriter so far.
            Returns: The string containing the characters written to the current StringWriter.
        """
        pass

    def Write(self, *__args):
        """
        Write(self: StringWriter, value: str)
            Writes a string to this instance of the StringWriter.
        
            value: The string to write.
        Write(self: StringWriter, buffer: Array[Char], index: int, count: int)
            Writes the specified region of a character array to this instance of the StringWriter.
        
            buffer: The character array to read data from.
            index: The index at which to begin reading from buffer.
            count: The maximum number of characters to write.
        Write(self: StringWriter, value: Char)
            Writes a character to this instance of the StringWriter.
        
            value: The character to write.
        """
        pass

    def WriteAsync(self, *__args):
        """
        WriteAsync(self: StringWriter, buffer: Array[Char], index: int, count: int) -> Task
        WriteAsync(self: StringWriter, value: str) -> Task
        WriteAsync(self: StringWriter, value: Char) -> Task
        """
        pass

    def WriteLineAsync(self, *__args):
        """
        WriteLineAsync(self: StringWriter, buffer: Array[Char], index: int, count: int) -> Task
        WriteLineAsync(self: StringWriter, value: str) -> Task
        WriteLineAsync(self: StringWriter, value: Char) -> Task
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
        __new__(cls: type, formatProvider: IFormatProvider)
        __new__(cls: type, sb: StringBuilder)
        __new__(cls: type, sb: StringBuilder, formatProvider: IFormatProvider)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Text.Encoding in which the output is written.

Get: Encoding(self: StringWriter) -> Encoding

"""


    CoreNewLine = None


class UnmanagedMemoryAccessor(object, IDisposable):
    """
    Provides random access to unmanaged blocks of memory from managed code.
    
    UnmanagedMemoryAccessor(buffer: SafeBuffer, offset: Int64, capacity: Int64)
    UnmanagedMemoryAccessor(buffer: SafeBuffer, offset: Int64, capacity: Int64, access: FileAccess)
    """
    def Dispose(self):
        """
        Dispose(self: UnmanagedMemoryAccessor)
            Releases all resources used by the System.IO.UnmanagedMemoryAccessor.
        """
        pass

    def Initialize(self, *args): #cannot find CLR method
        """
        Initialize(self: UnmanagedMemoryAccessor, buffer: SafeBuffer, offset: Int64, capacity: Int64, access: FileAccess)
            Sets the initial values for the accessor.
        
            buffer: The buffer to contain the accessor.
            offset: The byte at which to start the accessor.
            capacity: The size, in bytes, of memory to allocate.
            access: The type of access allowed to the memory. The default is 
             System.IO.MemoryMappedFiles.MemoryMappedFileAccess.ReadWrite.
        """
        pass

    def Read(self, position, structure):
        """ Read[T](self: UnmanagedMemoryAccessor, position: Int64) -> T """
        pass

    def ReadArray(self, position, array, offset, count):
        """ ReadArray[T](self: UnmanagedMemoryAccessor, position: Int64, array: Array[T], offset: int, count: int) -> int """
        pass

    def ReadBoolean(self, position):
        """
        ReadBoolean(self: UnmanagedMemoryAccessor, position: Int64) -> bool
        
            Reads a Boolean value from the accessor.
        
            position: The number of bytes into the accessor at which to begin reading.
            Returns: true or false.
        """
        pass

    def ReadByte(self, position):
        """
        ReadByte(self: UnmanagedMemoryAccessor, position: Int64) -> Byte
        
            Reads a byte value from the accessor.
        
            position: The number of bytes into the accessor at which to begin reading.
            Returns: The value that was read.
        """
        pass

    def ReadChar(self, position):
        """
        ReadChar(self: UnmanagedMemoryAccessor, position: Int64) -> Char
        
            Reads a character from the accessor.
        
            position: The number of bytes into the accessor at which to begin reading.
            Returns: The value that was read.
        """
        pass

    def ReadDecimal(self, position):
        """
        ReadDecimal(self: UnmanagedMemoryAccessor, position: Int64) -> Decimal
        
            Reads a decimal value from the accessor.
        
            position: The number of bytes into the accessor at which to begin reading.
            Returns: The value that was read.
        """
        pass

    def ReadDouble(self, position):
        """
        ReadDouble(self: UnmanagedMemoryAccessor, position: Int64) -> float
        
            Reads a double-precision floating-point value from the accessor.
        
            position: The number of bytes into the accessor at which to begin reading.
            Returns: The value that was read.
        """
        pass

    def ReadInt16(self, position):
        """
        ReadInt16(self: UnmanagedMemoryAccessor, position: Int64) -> Int16
        
            Reads a 16-bit integer from the accessor.
        
            position: The number of bytes into the accessor at which to begin reading.
            Returns: The value that was read.
        """
        pass

    def ReadInt32(self, position):
        """
        ReadInt32(self: UnmanagedMemoryAccessor, position: Int64) -> int
        
            Reads a 32-bit integer from the accessor.
        
            position: The number of bytes into the accessor at which to begin reading.
            Returns: The value that was read.
        """
        pass

    def ReadInt64(self, position):
        """
        ReadInt64(self: UnmanagedMemoryAccessor, position: Int64) -> Int64
        
            Reads a 64-bit integer from the accessor.
        
            position: The number of bytes into the accessor at which to begin reading.
            Returns: The value that was read.
        """
        pass

    def ReadSByte(self, position):
        """
        ReadSByte(self: UnmanagedMemoryAccessor, position: Int64) -> SByte
        
            Reads an 8-bit signed integer from the accessor.
        
            position: The number of bytes into the accessor at which to begin reading.
            Returns: The value that was read.
        """
        pass

    def ReadSingle(self, position):
        """
        ReadSingle(self: UnmanagedMemoryAccessor, position: Int64) -> Single
        
            Reads a single-precision floating-point value from the accessor.
        
            position: The number of bytes into the accessor at which to begin reading.
            Returns: The value that was read.
        """
        pass

    def ReadUInt16(self, position):
        """
        ReadUInt16(self: UnmanagedMemoryAccessor, position: Int64) -> UInt16
        
            Reads an unsigned 16-bit integer from the accessor.
        
            position: The number of bytes into the accessor at which to begin reading.
            Returns: The value that was read.
        """
        pass

    def ReadUInt32(self, position):
        """
        ReadUInt32(self: UnmanagedMemoryAccessor, position: Int64) -> UInt32
        
            Reads an unsigned 32-bit integer from the accessor.
        
            position: The number of bytes into the accessor at which to begin reading.
            Returns: The value that was read.
        """
        pass

    def ReadUInt64(self, position):
        """
        ReadUInt64(self: UnmanagedMemoryAccessor, position: Int64) -> UInt64
        
            Reads an unsigned 64-bit integer from the accessor.
        
            position: The number of bytes into the accessor at which to begin reading.
            Returns: The value that was read.
        """
        pass

    def Write(self, position, *__args):
        """
        Write(self: UnmanagedMemoryAccessor, position: Int64, value: SByte)
            Writes an 8-bit integer into the accessor.
        
            position: The number of bytes into the accessor at which to begin writing.
            value: The value to write.
        Write(self: UnmanagedMemoryAccessor, position: Int64, value: float)
            Writes a Double value into the accessor.
        
            position: The number of bytes into the accessor at which to begin writing.
            value: The value to write.
        Write(self: UnmanagedMemoryAccessor, position: Int64, value: Single)
            Writes a Single into the accessor.
        
            position: The number of bytes into the accessor at which to begin writing.
            value: The value to write.
        Write(self: UnmanagedMemoryAccessor, position: Int64, value: UInt16)
            Writes an unsigned 16-bit integer into the accessor.
        
            position: The number of bytes into the accessor at which to begin writing.
            value: The value to write.
        Write[T](self: UnmanagedMemoryAccessor, position: Int64, structure: T) -> T
        Write(self: UnmanagedMemoryAccessor, position: Int64, value: UInt64)
            Writes an unsigned 64-bit integer into the accessor.
        
            position: The number of bytes into the accessor at which to begin writing.
            value: The value to write.
        Write(self: UnmanagedMemoryAccessor, position: Int64, value: UInt32)
            Writes an unsigned 32-bit integer into the accessor.
        
            position: The number of bytes into the accessor at which to begin writing.
            value: The value to write.
        Write(self: UnmanagedMemoryAccessor, position: Int64, value: Char)
            Writes a character into the accessor.
        
            position: The number of bytes into the accessor at which to begin writing.
            value: The value to write.
        Write(self: UnmanagedMemoryAccessor, position: Int64, value: Byte)
            Writes a byte value into the accessor.
        
            position: The number of bytes into the accessor at which to begin writing.
            value: The value to write.
        Write(self: UnmanagedMemoryAccessor, position: Int64, value: bool)
            Writes a Boolean value into the accessor.
        
            position: The number of bytes into the accessor at which to begin writing.
            value: The value to write.
        Write(self: UnmanagedMemoryAccessor, position: Int64, value: Int16)
            Writes a 16-bit integer into the accessor.
        
            position: The number of bytes into the accessor at which to begin writing.
            value: The value to write.
        Write(self: UnmanagedMemoryAccessor, position: Int64, value: Decimal)
            Writes a decimal value into the accessor.
        
            position: The number of bytes into the accessor at which to begin writing.
            value: The value to write.
        Write(self: UnmanagedMemoryAccessor, position: Int64, value: Int64)
            Writes a 64-bit integer into the accessor.
        
            position: The number of bytes into the accessor at which to begin writing.
            value: The value to write.
        Write(self: UnmanagedMemoryAccessor, position: Int64, value: int)
            Writes a 32-bit integer into the accessor.
        
            position: The number of bytes into the accessor at which to begin writing.
            value: The value to write.
        """
        pass

    def WriteArray(self, position, array, offset, count):
        """ WriteArray[T](self: UnmanagedMemoryAccessor, position: Int64, array: Array[T], offset: int, count: int) """
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
    def __new__(self, buffer, offset, capacity, access=None):
        """
        __new__(cls: type)
        __new__(cls: type, buffer: SafeBuffer, offset: Int64, capacity: Int64)
        __new__(cls: type, buffer: SafeBuffer, offset: Int64, capacity: Int64, access: FileAccess)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines whether the accessor is readable.

Get: CanRead(self: UnmanagedMemoryAccessor) -> bool

"""

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines whether the accessory is writable.

Get: CanWrite(self: UnmanagedMemoryAccessor) -> bool

"""

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the capacity of the accessor.

Get: Capacity(self: UnmanagedMemoryAccessor) -> Int64

"""

    IsOpen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines whether the accessor is currently open by a process.

"""



class UnmanagedMemoryStream(Stream, IDisposable):
    """
    Provides access to unmanaged blocks of memory from managed code.
    
    UnmanagedMemoryStream(buffer: SafeBuffer, offset: Int64, length: Int64)
    UnmanagedMemoryStream(buffer: SafeBuffer, offset: Int64, length: Int64, access: FileAccess)
    UnmanagedMemoryStream(pointer: Byte*, length: Int64)
    UnmanagedMemoryStream(pointer: Byte*, length: Int64, capacity: Int64, access: FileAccess)
    """
    def CreateWaitHandle(self, *args): #cannot find CLR method
        """
        CreateWaitHandle(self: Stream) -> WaitHandle
        
            Allocates a System.Threading.WaitHandle object.
            Returns: A reference to the allocated WaitHandle.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: UnmanagedMemoryStream, disposing: bool)
            Releases the unmanaged resources used by the System.IO.UnmanagedMemoryStream and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def Flush(self):
        """
        Flush(self: UnmanagedMemoryStream)
            Overrides the System.IO.Stream.Flush method so that no action is performed.
        """
        pass

    def FlushAsync(self, cancellationToken=None):
        """ FlushAsync(self: UnmanagedMemoryStream, cancellationToken: CancellationToken) -> Task """
        pass

    def Initialize(self, *args): #cannot find CLR method
        """
        Initialize(self: UnmanagedMemoryStream, buffer: SafeBuffer, offset: Int64, length: Int64, access: FileAccess)
            Initializes a new instance of the System.IO.UnmanagedMemoryStream class in a safe buffer with a 
             specified offset, length, and file access.
        
        
            buffer: The buffer to contain the unmanaged memory stream.
            offset: The byte position in the buffer at which to start the unmanaged memory stream.
            length: The length of the unmanaged memory stream.
            access: The mode of file access to the unmanaged memory stream.
        Initialize(self: UnmanagedMemoryStream, pointer: Byte*, length: Int64, capacity: Int64, access: FileAccess)
            Initializes a new instance of the System.IO.UnmanagedMemoryStream class by using a pointer to an 
             unmanaged memory location.
        
        
            pointer: A pointer to an unmanaged memory location.
            length: The length of the memory to use.
            capacity: The total amount of memory assigned to the stream.
            access: One of the System.IO.FileAccess values.
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
        Read(self: UnmanagedMemoryStream, offset: int, count: int) -> (int, Array[Byte])
        
            Reads the specified number of bytes into the specified array.
        
            offset: The zero-based byte offset in buffer at which to begin storing the data read from the current 
             stream.
        
            count: The maximum number of bytes to read from the current stream.
            Returns: The total number of bytes read into the buffer. This can be less than the number of bytes 
             requested if that many bytes are not currently available, or zero (0) if the end of the stream 
             has been reached.
        """
        pass

    def ReadAsync(self, buffer, offset, count, cancellationToken=None):
        """ ReadAsync(self: UnmanagedMemoryStream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task[int] """
        pass

    def ReadByte(self):
        """
        ReadByte(self: UnmanagedMemoryStream) -> int
        
            Reads a byte from a stream and advances the position within the stream by one byte, or returns 
             -1 if at the end of the stream.
        
            Returns: The unsigned byte cast to an System.Int32 object, or -1 if at the end of the stream.
        """
        pass

    def Seek(self, offset, loc):
        """
        Seek(self: UnmanagedMemoryStream, offset: Int64, loc: SeekOrigin) -> Int64
        
            Sets the current position of the current stream to the given value.
        
            offset: The point relative to origin to begin seeking from.
            loc: Specifies the beginning, the end, or the current position as a reference point for origin, using 
             a value of type System.IO.SeekOrigin.
        
            Returns: The new position in the stream.
        """
        pass

    def SetLength(self, value):
        """
        SetLength(self: UnmanagedMemoryStream, value: Int64)
            Sets the length of a stream to a specified value.
        
            value: The length of the stream.
        """
        pass

    def Write(self, buffer, offset, count):
        """
        Write(self: UnmanagedMemoryStream, buffer: Array[Byte], offset: int, count: int)
            Writes a block of bytes to the current stream using data from a buffer.
        
            buffer: The byte array from which to copy bytes to the current stream.
            offset: The offset in the buffer at which to begin copying bytes to the current stream.
            count: The number of bytes to write to the current stream.
        """
        pass

    def WriteAsync(self, buffer, offset, count, cancellationToken=None):
        """ WriteAsync(self: UnmanagedMemoryStream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task """
        pass

    def WriteByte(self, value):
        """
        WriteByte(self: UnmanagedMemoryStream, value: Byte)
            Writes a byte to the current position in the file stream.
        
            value: A byte value written to the stream.
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
        __new__(cls: type, buffer: SafeBuffer, offset: Int64, length: Int64)
        __new__(cls: type, buffer: SafeBuffer, offset: Int64, length: Int64, access: FileAccess)
        __new__(cls: type, pointer: Byte*, length: Int64)
        __new__(cls: type, pointer: Byte*, length: Int64, capacity: Int64, access: FileAccess)
        """
        pass

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether a stream supports reading.

Get: CanRead(self: UnmanagedMemoryStream) -> bool

"""

    CanSeek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether a stream supports seeking.

Get: CanSeek(self: UnmanagedMemoryStream) -> bool

"""

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether a stream supports writing.

Get: CanWrite(self: UnmanagedMemoryStream) -> bool

"""

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the stream length (size) or the total amount of memory assigned to a stream (capacity).

Get: Capacity(self: UnmanagedMemoryStream) -> Int64

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length of the data in a stream.

Get: Length(self: UnmanagedMemoryStream) -> Int64

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current position in a stream.

Get: Position(self: UnmanagedMemoryStream) -> Int64

Set: Position(self: UnmanagedMemoryStream) = value
"""

    PositionPointer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a byte pointer to a stream based on the current position in the stream.

Get: PositionPointer(self: UnmanagedMemoryStream) -> Byte*

Set: PositionPointer(self: UnmanagedMemoryStream) = value
"""



class WaitForChangedResult(object):
    """ Contains information on the change that occurred. """
    ChangeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of change that occurred.

Get: ChangeType(self: WaitForChangedResult) -> WatcherChangeTypes

Set: ChangeType(self: WaitForChangedResult) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the file or directory that changed.

Get: Name(self: WaitForChangedResult) -> str

Set: Name(self: WaitForChangedResult) = value
"""

    OldName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the original name of the file or directory that was renamed.

Get: OldName(self: WaitForChangedResult) -> str

Set: OldName(self: WaitForChangedResult) = value
"""

    TimedOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the wait operation timed out.

Get: TimedOut(self: WaitForChangedResult) -> bool

Set: TimedOut(self: WaitForChangedResult) = value
"""



class WatcherChangeTypes(Enum, IComparable, IFormattable, IConvertible):
    """
    Changes that might occur to a file or directory.
    
    enum (flags) WatcherChangeTypes, values: All (15), Changed (4), Created (1), Deleted (2), Renamed (8)
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

    All = None
    Changed = None
    Created = None
    Deleted = None
    Renamed = None
    value__ = None


# variables with complex values

