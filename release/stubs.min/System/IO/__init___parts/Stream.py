class Stream(MarshalByRefObject,IDisposable):
 """ Provides a generic view of a sequence of bytes. """
 def BeginRead(self,buffer,offset,count,callback,state):
  """
  BeginRead(self: Stream,buffer: Array[Byte],offset: int,count: int,callback: AsyncCallback,state: object) -> IAsyncResult

  

   Begins an asynchronous read operation.

  

   buffer: The buffer to read the data into.

   offset: The byte offset in buffer at which to begin writing data read from the stream.

   count: The maximum number of bytes to read.

   callback: An optional asynchronous callback,to be called when the read is complete.

   state: A user-provided object that distinguishes this particular asynchronous read request from other 

    requests.

  

   Returns: An System.IAsyncResult that represents the asynchronous read,which could still be pending.
  """
  pass
 def BeginWrite(self,buffer,offset,count,callback,state):
  """
  BeginWrite(self: Stream,buffer: Array[Byte],offset: int,count: int,callback: AsyncCallback,state: object) -> IAsyncResult

  

   Begins an asynchronous write operation.

  

   buffer: The buffer to write data from.

   offset: The byte offset in buffer from which to begin writing.

   count: The maximum number of bytes to write.

   callback: An optional asynchronous callback,to be called when the write is complete.

   state: A user-provided object that distinguishes this particular asynchronous write request from other 

    requests.

  

   Returns: An IAsyncResult that represents the asynchronous write,which could still be pending.
  """
  pass
 def Close(self):
  """
  Close(self: Stream)

   Closes the current stream and releases any resources (such as sockets and file handles) 

    associated with the current stream.
  """
  pass
 def CopyTo(self,destination,bufferSize=None):
  """
  CopyTo(self: Stream,destination: Stream,bufferSize: int)

   Reads all the bytes from the current stream and writes them to a destination stream,using a 

    specified buffer size.

  

  

   destination: The stream that will contain the contents of the current stream.

   bufferSize: The size of the buffer. This value must be greater than zero. The default size is 4096.

  CopyTo(self: Stream,destination: Stream)

   Reads the bytes from the current stream and writes them to the destination stream.

  

   destination: The stream that will contain the contents of the current stream.
  """
  pass
 def CopyToAsync(self,destination,bufferSize=None,cancellationToken=None):
  """
  CopyToAsync(self: Stream,destination: Stream,bufferSize: int,cancellationToken: CancellationToken) -> Task

  CopyToAsync(self: Stream,destination: Stream,bufferSize: int) -> Task

  CopyToAsync(self: Stream,destination: Stream) -> Task
  """
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
  Dispose(self: Stream)

   Releases all resources used by the System.IO.Stream.
  """
  pass
 def EndRead(self,asyncResult):
  """
  EndRead(self: Stream,asyncResult: IAsyncResult) -> int

  

   Waits for the pending asynchronous read to complete.

  

   asyncResult: The reference to the pending asynchronous request to finish.

   Returns: The number of bytes read from the stream,between zero (0) and the number of bytes you 

    requested. Streams return zero (0) only at the end of the stream,otherwise,they should block 

    until at least one byte is available.
  """
  pass
 def EndWrite(self,asyncResult):
  """
  EndWrite(self: Stream,asyncResult: IAsyncResult)

   Ends an asynchronous write operation.

  

   asyncResult: A reference to the outstanding asynchronous I/O request.
  """
  pass
 def Flush(self):
  """
  Flush(self: Stream)

   When overridden in a derived class,clears all buffers for this stream and causes any buffered 

    data to be written to the underlying device.
  """
  pass
 def FlushAsync(self,cancellationToken=None):
  """
  FlushAsync(self: Stream,cancellationToken: CancellationToken) -> Task

  FlushAsync(self: Stream) -> Task
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
  Read(self: Stream,offset: int,count: int) -> (int,Array[Byte])

  

   When overridden in a derived class,reads a sequence of bytes from the current stream and 

    advances the position within the stream by the number of bytes read.

  

  

   offset: The zero-based byte offset in buffer at which to begin storing the data read from the current 

    stream.

  

   count: The maximum number of bytes to be read from the current stream.

   Returns: The total number of bytes read into the buffer. This can be less than the number of bytes 

    requested if that many bytes are not currently available,or zero (0) if the end of the stream 

    has been reached.
  """
  pass
 def ReadAsync(self,buffer,offset,count,cancellationToken=None):
  """
  ReadAsync(self: Stream,buffer: Array[Byte],offset: int,count: int,cancellationToken: CancellationToken) -> Task[int]

  ReadAsync(self: Stream,buffer: Array[Byte],offset: int,count: int) -> Task[int]
  """
  pass
 def ReadByte(self):
  """
  ReadByte(self: Stream) -> int

  

   Reads a byte from the stream and advances the position within the stream by one byte,or returns 

    -1 if at the end of the stream.

  

   Returns: The unsigned byte cast to an Int32,or -1 if at the end of the stream.
  """
  pass
 def Seek(self,offset,origin):
  """
  Seek(self: Stream,offset: Int64,origin: SeekOrigin) -> Int64

  

   When overridden in a derived class,sets the position within the current stream.

  

   offset: A byte offset relative to the origin parameter.

   origin: A value of type System.IO.SeekOrigin indicating the reference point used to obtain the new 

    position.

  

   Returns: The new position within the current stream.
  """
  pass
 def SetLength(self,value):
  """
  SetLength(self: Stream,value: Int64)

   When overridden in a derived class,sets the length of the current stream.

  

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
 def Write(self,buffer,offset,count):
  """
  Write(self: Stream,buffer: Array[Byte],offset: int,count: int)

   When overridden in a derived class,writes a sequence of bytes to the current stream and 

    advances the current position within this stream by the number of bytes written.

  

  

   buffer: An array of bytes. This method copies count bytes from buffer to the current stream.

   offset: The zero-based byte offset in buffer at which to begin copying bytes to the current stream.

   count: The number of bytes to be written to the current stream.
  """
  pass
 def WriteAsync(self,buffer,offset,count,cancellationToken=None):
  """
  WriteAsync(self: Stream,buffer: Array[Byte],offset: int,count: int,cancellationToken: CancellationToken) -> Task

  WriteAsync(self: Stream,buffer: Array[Byte],offset: int,count: int) -> Task
  """
  pass
 def WriteByte(self,value):
  """
  WriteByte(self: Stream,value: Byte)

   Writes a byte to the current position in the stream and advances the position within the stream 

    by one byte.

  

  

   value: The byte to write to the stream.
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
 def __reduce_ex__(self,*args):
  pass
 CanRead=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets a value indicating whether the current stream supports reading.



Get: CanRead(self: Stream) -> bool



"""

 CanSeek=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets a value indicating whether the current stream supports seeking.



Get: CanSeek(self: Stream) -> bool



"""

 CanTimeout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines whether the current stream can time out.



Get: CanTimeout(self: Stream) -> bool



"""

 CanWrite=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets a value indicating whether the current stream supports writing.



Get: CanWrite(self: Stream) -> bool



"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets the length in bytes of the stream.



Get: Length(self: Stream) -> Int64



"""

 Position=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets or sets the position within the current stream.



Get: Position(self: Stream) -> Int64



Set: Position(self: Stream)=value

"""

 ReadTimeout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value,in miliseconds,that determines how long the stream will attempt to read before timing out.



Get: ReadTimeout(self: Stream) -> int



Set: ReadTimeout(self: Stream)=value

"""

 WriteTimeout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value,in miliseconds,that determines how long the stream will attempt to write before timing out.



Get: WriteTimeout(self: Stream) -> int



Set: WriteTimeout(self: Stream)=value

"""


 Null=None

