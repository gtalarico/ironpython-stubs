class UnmanagedMemoryStream(Stream,IDisposable):
 """
 Provides access to unmanaged blocks of memory from managed code.

 

 UnmanagedMemoryStream(buffer: SafeBuffer,offset: Int64,length: Int64)

 UnmanagedMemoryStream(buffer: SafeBuffer,offset: Int64,length: Int64,access: FileAccess)

 UnmanagedMemoryStream(pointer: Byte*,length: Int64)

 UnmanagedMemoryStream(pointer: Byte*,length: Int64,capacity: Int64,access: FileAccess)
 """
 def CreateWaitHandle(self,*args):
  """
  CreateWaitHandle(self: Stream) -> WaitHandle

  

   Allocates a System.Threading.WaitHandle object.

   Returns: A reference to the allocated WaitHandle.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: UnmanagedMemoryStream,disposing: bool)

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
 def FlushAsync(self,cancellationToken=None):
  """ FlushAsync(self: UnmanagedMemoryStream,cancellationToken: CancellationToken) -> Task """
  pass
 def Initialize(self,*args):
  """
  Initialize(self: UnmanagedMemoryStream,buffer: SafeBuffer,offset: Int64,length: Int64,access: FileAccess)

   Initializes a new instance of the System.IO.UnmanagedMemoryStream class in a safe buffer with a 

    specified offset,length,and file access.

  

  

   buffer: The buffer to contain the unmanaged memory stream.

   offset: The byte position in the buffer at which to start the unmanaged memory stream.

   length: The length of the unmanaged memory stream.

   access: The mode of file access to the unmanaged memory stream.

  Initialize(self: UnmanagedMemoryStream,pointer: Byte*,length: Int64,capacity: Int64,access: FileAccess)

   Initializes a new instance of the System.IO.UnmanagedMemoryStream class by using a pointer to an 

    unmanaged memory location.

  

  

   pointer: A pointer to an unmanaged memory location.

   length: The length of the memory to use.

   capacity: The total amount of memory assigned to the stream.

   access: One of the System.IO.FileAccess values.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject

  

   Creates a shallow copy of the current System.MarshalByRefObject object.

  

   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the 

    object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 

    false is usually appropriate. true to copy the current System.MarshalByRefObject object's 

    identity to its clone,which will cause remoting client calls to be routed to the remote server 

    object.

  

   Returns: A shallow copy of the current System.MarshalByRefObject object.

  MemberwiseClone(self: object) -> object

  

   Creates a shallow copy of the current System.Object.

   Returns: A shallow copy of the current System.Object.
  """
  pass
 def ObjectInvariant(self,*args):
  """
  ObjectInvariant(self: Stream)

   Provides support for a System.Diagnostics.Contracts.Contract.
  """
  pass
 def Read(self,buffer,offset,count):
  """
  Read(self: UnmanagedMemoryStream,offset: int,count: int) -> (int,Array[Byte])

  

   Reads the specified number of bytes into the specified array.

  

   offset: The zero-based byte offset in buffer at which to begin storing the data read from the current 

    stream.

  

   count: The maximum number of bytes to read from the current stream.

   Returns: The total number of bytes read into the buffer. This can be less than the number of bytes 

    requested if that many bytes are not currently available,or zero (0) if the end of the stream 

    has been reached.
  """
  pass
 def ReadAsync(self,buffer,offset,count,cancellationToken=None):
  """ ReadAsync(self: UnmanagedMemoryStream,buffer: Array[Byte],offset: int,count: int,cancellationToken: CancellationToken) -> Task[int] """
  pass
 def ReadByte(self):
  """
  ReadByte(self: UnmanagedMemoryStream) -> int

  

   Reads a byte from a stream and advances the position within the stream by one byte,or returns 

    -1 if at the end of the stream.

  

   Returns: The unsigned byte cast to an System.Int32 object,or -1 if at the end of the stream.
  """
  pass
 def Seek(self,offset,loc):
  """
  Seek(self: UnmanagedMemoryStream,offset: Int64,loc: SeekOrigin) -> Int64

  

   Sets the current position of the current stream to the given value.

  

   offset: The point relative to origin to begin seeking from.

   loc: Specifies the beginning,the end,or the current position as a reference point for origin,using 

    a value of type System.IO.SeekOrigin.

  

   Returns: The new position in the stream.
  """
  pass
 def SetLength(self,value):
  """
  SetLength(self: UnmanagedMemoryStream,value: Int64)

   Sets the length of a stream to a specified value.

  

   value: The length of the stream.
  """
  pass
 def Write(self,buffer,offset,count):
  """
  Write(self: UnmanagedMemoryStream,buffer: Array[Byte],offset: int,count: int)

   Writes a block of bytes to the current stream using data from a buffer.

  

   buffer: The byte array from which to copy bytes to the current stream.

   offset: The offset in the buffer at which to begin copying bytes to the current stream.

   count: The number of bytes to write to the current stream.
  """
  pass
 def WriteAsync(self,buffer,offset,count,cancellationToken=None):
  """ WriteAsync(self: UnmanagedMemoryStream,buffer: Array[Byte],offset: int,count: int,cancellationToken: CancellationToken) -> Task """
  pass
 def WriteByte(self,value):
  """
  WriteByte(self: UnmanagedMemoryStream,value: Byte)

   Writes a byte to the current position in the file stream.

  

   value: A byte value written to the stream.
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
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,buffer: SafeBuffer,offset: Int64,length: Int64)

  __new__(cls: type,buffer: SafeBuffer,offset: Int64,length: Int64,access: FileAccess)

  __new__(cls: type,pointer: Byte*,length: Int64)

  __new__(cls: type,pointer: Byte*,length: Int64,capacity: Int64,access: FileAccess)
  """
  pass
 CanRead=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether a stream supports reading.



Get: CanRead(self: UnmanagedMemoryStream) -> bool



"""

 CanSeek=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether a stream supports seeking.



Get: CanSeek(self: UnmanagedMemoryStream) -> bool



"""

 CanWrite=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether a stream supports writing.



Get: CanWrite(self: UnmanagedMemoryStream) -> bool



"""

 Capacity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the stream length (size) or the total amount of memory assigned to a stream (capacity).



Get: Capacity(self: UnmanagedMemoryStream) -> Int64



"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length of the data in a stream.



Get: Length(self: UnmanagedMemoryStream) -> Int64



"""

 Position=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current position in a stream.



Get: Position(self: UnmanagedMemoryStream) -> Int64



Set: Position(self: UnmanagedMemoryStream)=value

"""

 PositionPointer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a byte pointer to a stream based on the current position in the stream.



Get: PositionPointer(self: UnmanagedMemoryStream) -> Byte*



Set: PositionPointer(self: UnmanagedMemoryStream)=value

"""


