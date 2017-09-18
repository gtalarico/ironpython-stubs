class MemoryStream(Stream,IDisposable):
 """
 Creates a stream whose backing store is memory.

 

 MemoryStream()

 MemoryStream(capacity: int)

 MemoryStream(buffer: Array[Byte])

 MemoryStream(buffer: Array[Byte],writable: bool)

 MemoryStream(buffer: Array[Byte],index: int,count: int)

 MemoryStream(buffer: Array[Byte],index: int,count: int,writable: bool)

 MemoryStream(buffer: Array[Byte],index: int,count: int,writable: bool,publiclyVisible: bool)
 """
 def CopyToAsync(self,destination,bufferSize=None,cancellationToken=None):
  """ CopyToAsync(self: MemoryStream,destination: Stream,bufferSize: int,cancellationToken: CancellationToken) -> Task """
  pass
 def CreateWaitHandle(self,*args):
  """
  CreateWaitHandle(self: Stream) -> WaitHandle

  

   Allocates a System.Threading.WaitHandle object.

   Returns: A reference to the allocated WaitHandle.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: MemoryStream,disposing: bool)

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
 def FlushAsync(self,cancellationToken=None):
  """ FlushAsync(self: MemoryStream,cancellationToken: CancellationToken) -> Task """
  pass
 def GetBuffer(self):
  """
  GetBuffer(self: MemoryStream) -> Array[Byte]

  

   Returns the array of unsigned bytes from which this stream was created.

   Returns: The byte array from which this stream was created,or the underlying array if a byte array was 

    not provided to the System.IO.MemoryStream constructor during construction of the current 

    instance.
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
  Read(self: MemoryStream,offset: int,count: int) -> (int,Array[Byte])

  

   Reads a block of bytes from the current stream and writes the data to a buffer.

  

   offset: The zero-based byte offset in buffer at which to begin storing data from the current stream.

   count: The maximum number of bytes to read.

   Returns: The total number of bytes written into the buffer. This can be less than the number of bytes 

    requested if that number of bytes are not currently available,or zero if the end of the stream 

    is reached before any bytes are read.
  """
  pass
 def ReadAsync(self,buffer,offset,count,cancellationToken=None):
  """ ReadAsync(self: MemoryStream,buffer: Array[Byte],offset: int,count: int,cancellationToken: CancellationToken) -> Task[int] """
  pass
 def ReadByte(self):
  """
  ReadByte(self: MemoryStream) -> int

  

   Reads a byte from the current stream.

   Returns: The byte cast to a System.Int32,or -1 if the end of the stream has been reached.
  """
  pass
 def Seek(self,offset,loc):
  """
  Seek(self: MemoryStream,offset: Int64,loc: SeekOrigin) -> Int64

  

   Sets the position within the current stream to the specified value.

  

   offset: The new position within the stream. This is relative to the loc parameter,and can be positive 

    or negative.

  

   loc: A value of type System.IO.SeekOrigin,which acts as the seek reference point.

   Returns: The new position within the stream,calculated by combining the initial reference point and the 

    offset.
  """
  pass
 def SetLength(self,value):
  """
  SetLength(self: MemoryStream,value: Int64)

   Sets the length of the current stream to the specified value.

  

   value: The value at which to set the length.
  """
  pass
 def ToArray(self):
  """
  ToArray(self: MemoryStream) -> Array[Byte]

  

   Writes the stream contents to a byte array,regardless of the System.IO.MemoryStream.Position 

    property.

  

   Returns: A new byte array.
  """
  pass
 def TryGetBuffer(self,buffer):
  """ TryGetBuffer(self: MemoryStream) -> (bool,ArraySegment[Byte]) """
  pass
 def Write(self,buffer,offset,count):
  """
  Write(self: MemoryStream,buffer: Array[Byte],offset: int,count: int)

   Writes a block of bytes to the current stream using data read from a buffer.

  

   buffer: The buffer to write data from.

   offset: The zero-based byte offset in buffer at which to begin copying bytes to the current stream.

   count: The maximum number of bytes to write.
  """
  pass
 def WriteAsync(self,buffer,offset,count,cancellationToken=None):
  """ WriteAsync(self: MemoryStream,buffer: Array[Byte],offset: int,count: int,cancellationToken: CancellationToken) -> Task """
  pass
 def WriteByte(self,value):
  """
  WriteByte(self: MemoryStream,value: Byte)

   Writes a byte to the current stream at the current position.

  

   value: The byte to write.
  """
  pass
 def WriteTo(self,stream):
  """
  WriteTo(self: MemoryStream,stream: Stream)

   Writes the entire contents of this memory stream to another stream.

  

   stream: The stream to write this memory stream to.
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

  __new__(cls: type,capacity: int)

  __new__(cls: type,buffer: Array[Byte])

  __new__(cls: type,buffer: Array[Byte],writable: bool)

  __new__(cls: type,buffer: Array[Byte],index: int,count: int)

  __new__(cls: type,buffer: Array[Byte],index: int,count: int,writable: bool)

  __new__(cls: type,buffer: Array[Byte],index: int,count: int,writable: bool,publiclyVisible: bool)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 CanRead=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current stream supports reading.



Get: CanRead(self: MemoryStream) -> bool



"""

 CanSeek=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current stream supports seeking.



Get: CanSeek(self: MemoryStream) -> bool



"""

 CanWrite=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current stream supports writing.



Get: CanWrite(self: MemoryStream) -> bool



"""

 Capacity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of bytes allocated for this stream.



Get: Capacity(self: MemoryStream) -> int



Set: Capacity(self: MemoryStream)=value

"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length of the stream in bytes.



Get: Length(self: MemoryStream) -> Int64



"""

 Position=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current position within the stream.



Get: Position(self: MemoryStream) -> Int64



Set: Position(self: MemoryStream)=value

"""


