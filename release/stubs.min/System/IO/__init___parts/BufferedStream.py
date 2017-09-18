class BufferedStream(Stream,IDisposable):
 """
 Adds a buffering layer to read and write operations on another stream. This class cannot be inherited.

 

 BufferedStream(stream: Stream)

 BufferedStream(stream: Stream,bufferSize: int)
 """
 def BeginRead(self,buffer,offset,count,callback,state):
  """ BeginRead(self: BufferedStream,buffer: Array[Byte],offset: int,count: int,callback: AsyncCallback,state: object) -> IAsyncResult """
  pass
 def BeginWrite(self,buffer,offset,count,callback,state):
  """ BeginWrite(self: BufferedStream,buffer: Array[Byte],offset: int,count: int,callback: AsyncCallback,state: object) -> IAsyncResult """
  pass
 def CreateWaitHandle(self,*args):
  """
  CreateWaitHandle(self: Stream) -> WaitHandle

  

   Allocates a System.Threading.WaitHandle object.

   Returns: A reference to the allocated WaitHandle.
  """
  pass
 def Dispose(self):
  """ Dispose(self: BufferedStream,disposing: bool) """
  pass
 def EndRead(self,asyncResult):
  """ EndRead(self: BufferedStream,asyncResult: IAsyncResult) -> int """
  pass
 def EndWrite(self,asyncResult):
  """ EndWrite(self: BufferedStream,asyncResult: IAsyncResult) """
  pass
 def Flush(self):
  """
  Flush(self: BufferedStream)

   Clears all buffers for this stream and causes any buffered data to be written to the underlying 

    device.
  """
  pass
 def FlushAsync(self,cancellationToken=None):
  """ FlushAsync(self: BufferedStream,cancellationToken: CancellationToken) -> Task """
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
 def Read(self,array,offset,count):
  """
  Read(self: BufferedStream,offset: int,count: int) -> (int,Array[Byte])

  

   Copies bytes from the current buffered stream to an array.

  

   offset: The byte offset in the buffer at which to begin reading bytes.

   count: The number of bytes to be read.

   Returns: The total number of bytes read into array. This can be less than the number of bytes requested 

    if that many bytes are not currently available,or 0 if the end of the stream has been reached 

    before any data can be read.
  """
  pass
 def ReadAsync(self,buffer,offset,count,cancellationToken=None):
  """ ReadAsync(self: BufferedStream,buffer: Array[Byte],offset: int,count: int,cancellationToken: CancellationToken) -> Task[int] """
  pass
 def ReadByte(self):
  """
  ReadByte(self: BufferedStream) -> int

  

   Reads a byte from the underlying stream and returns the byte cast to an int,or returns -1 if 

    reading from the end of the stream.

  

   Returns: The byte cast to an int,or -1 if reading from the end of the stream.
  """
  pass
 def Seek(self,offset,origin):
  """
  Seek(self: BufferedStream,offset: Int64,origin: SeekOrigin) -> Int64

  

   Sets the position within the current buffered stream.

  

   offset: A byte offset relative to origin.

   origin: A value of type System.IO.SeekOrigin indicating the reference point from which to obtain the new 

    position.

  

   Returns: The new position within the current buffered stream.
  """
  pass
 def SetLength(self,value):
  """
  SetLength(self: BufferedStream,value: Int64)

   Sets the length of the buffered stream.

  

   value: An integer indicating the desired length of the current buffered stream in bytes.
  """
  pass
 def Write(self,array,offset,count):
  """
  Write(self: BufferedStream,array: Array[Byte],offset: int,count: int)

   Copies bytes to the buffered stream and advances the current position within the buffered stream 

    by the number of bytes written.

  

  

   array: The byte array from which to copy count bytes to the current buffered stream.

   offset: The offset in the buffer at which to begin copying bytes to the current buffered stream.

   count: The number of bytes to be written to the current buffered stream.
  """
  pass
 def WriteAsync(self,buffer,offset,count,cancellationToken=None):
  """ WriteAsync(self: BufferedStream,buffer: Array[Byte],offset: int,count: int,cancellationToken: CancellationToken) -> Task """
  pass
 def WriteByte(self,value):
  """
  WriteByte(self: BufferedStream,value: Byte)

   Writes a byte to the current position in the buffered stream.

  

   value: A byte to write to the stream.
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
 def __new__(self,stream,bufferSize=None):
  """
  __new__(cls: type,stream: Stream)

  __new__(cls: type,stream: Stream,bufferSize: int)
  """
  pass
 CanRead=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current stream supports reading.



Get: CanRead(self: BufferedStream) -> bool



"""

 CanSeek=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current stream supports seeking.



Get: CanSeek(self: BufferedStream) -> bool



"""

 CanWrite=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current stream supports writing.



Get: CanWrite(self: BufferedStream) -> bool



"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the stream length in bytes.



Get: Length(self: BufferedStream) -> Int64



"""

 Position=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the position within the current stream.



Get: Position(self: BufferedStream) -> Int64



Set: Position(self: BufferedStream)=value

"""


