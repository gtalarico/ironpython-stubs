class FileStream(Stream,IDisposable):
 """
 Exposes a System.IO.Stream around a file,supporting both synchronous and asynchronous read and write operations.

 

 FileStream(path: str,mode: FileMode)

 FileStream(path: str,mode: FileMode,access: FileAccess)

 FileStream(path: str,mode: FileMode,access: FileAccess,share: FileShare)

 FileStream(path: str,mode: FileMode,access: FileAccess,share: FileShare,bufferSize: int)

 FileStream(path: str,mode: FileMode,access: FileAccess,share: FileShare,bufferSize: int,options: FileOptions)

 FileStream(path: str,mode: FileMode,access: FileAccess,share: FileShare,bufferSize: int,useAsync: bool)

 FileStream(path: str,mode: FileMode,rights: FileSystemRights,share: FileShare,bufferSize: int,options: FileOptions,fileSecurity: FileSecurity)

 FileStream(path: str,mode: FileMode,rights: FileSystemRights,share: FileShare,bufferSize: int,options: FileOptions)

 FileStream(handle: IntPtr,access: FileAccess)

 FileStream(handle: IntPtr,access: FileAccess,ownsHandle: bool)

 FileStream(handle: IntPtr,access: FileAccess,ownsHandle: bool,bufferSize: int)

 FileStream(handle: IntPtr,access: FileAccess,ownsHandle: bool,bufferSize: int,isAsync: bool)

 FileStream(handle: SafeFileHandle,access: FileAccess)

 FileStream(handle: SafeFileHandle,access: FileAccess,bufferSize: int)

 FileStream(handle: SafeFileHandle,access: FileAccess,bufferSize: int,isAsync: bool)
 """
 def BeginRead(self,array,offset,numBytes,userCallback,stateObject):
  """
  BeginRead(self: FileStream,array: Array[Byte],offset: int,numBytes: int,userCallback: AsyncCallback,stateObject: object) -> IAsyncResult

  

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
 def BeginWrite(self,array,offset,numBytes,userCallback,stateObject):
  """
  BeginWrite(self: FileStream,array: Array[Byte],offset: int,numBytes: int,userCallback: AsyncCallback,stateObject: object) -> IAsyncResult

  

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
 def CreateWaitHandle(self,*args):
  """
  CreateWaitHandle(self: Stream) -> WaitHandle

  

   Allocates a System.Threading.WaitHandle object.

   Returns: A reference to the allocated WaitHandle.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: FileStream,disposing: bool)

   Releases the unmanaged resources used by the System.IO.FileStream and optionally releases the 

    managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def EndRead(self,asyncResult):
  """
  EndRead(self: FileStream,asyncResult: IAsyncResult) -> int

  

   Waits for the pending asynchronous read to complete.

  

   asyncResult: The reference to the pending asynchronous request to wait for.

   Returns: The number of bytes read from the stream,between 0 and the number of bytes you requested. 

    Streams only return 0 at the end of the stream,otherwise,they should block until at least 1 

    byte is available.
  """
  pass
 def EndWrite(self,asyncResult):
  """
  EndWrite(self: FileStream,asyncResult: IAsyncResult)

   Ends an asynchronous write,blocking until the I/O operation has completed.

  

   asyncResult: The pending asynchronous I/O request.
  """
  pass
 def Flush(self,flushToDisk=None):
  """
  Flush(self: FileStream,flushToDisk: bool)

   Clears buffers for this stream and causes any buffered data to be written to the file,and also 

    clears all intermediate file buffers.

  

  

   flushToDisk: true to flush all intermediate file buffers; otherwise,false.

  Flush(self: FileStream)

   Clears buffers for this stream and causes any buffered data to be written to the file.
  """
  pass
 def FlushAsync(self,cancellationToken=None):
  """ FlushAsync(self: FileStream,cancellationToken: CancellationToken) -> Task """
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
 def Lock(self,position,length):
  """
  Lock(self: FileStream,position: Int64,length: Int64)

   Prevents other processes from reading from or writing to the System.IO.FileStream.

  

   position: The beginning of the range to lock. The value of this parameter must be equal to or greater than 

    zero (0).

  

   length: The range to be locked.
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
 def Read(self,array,offset,count):
  """
  Read(self: FileStream,offset: int,count: int) -> (int,Array[Byte])

  

   Reads a block of bytes from the stream and writes the data in a given buffer.

  

   offset: The byte offset in array at which the read bytes will be placed.

   count: The maximum number of bytes to read.

   Returns: The total number of bytes read into the buffer. This might be less than the number of bytes 

    requested if that number of bytes are not currently available,or zero if the end of the stream 

    is reached.
  """
  pass
 def ReadAsync(self,buffer,offset,count,cancellationToken=None):
  """ ReadAsync(self: FileStream,buffer: Array[Byte],offset: int,count: int,cancellationToken: CancellationToken) -> Task[int] """
  pass
 def ReadByte(self):
  """
  ReadByte(self: FileStream) -> int

  

   Reads a byte from the file and advances the read position one byte.

   Returns: The byte,cast to an System.Int32,or -1 if the end of the stream has been reached.
  """
  pass
 def Seek(self,offset,origin):
  """
  Seek(self: FileStream,offset: Int64,origin: SeekOrigin) -> Int64

  

   Sets the current position of this stream to the given value.

  

   offset: The point relative to origin from which to begin seeking.

   origin: Specifies the beginning,the end,or the current position as a reference point for origin,using 

    a value of type System.IO.SeekOrigin.

  

   Returns: The new position in the stream.
  """
  pass
 def SetAccessControl(self,fileSecurity):
  """
  SetAccessControl(self: FileStream,fileSecurity: FileSecurity)

   Applies access control list (ACL) entries described by a 

    System.Security.AccessControl.FileSecurity object to the file described by the current 

    System.IO.FileStream object.

  

  

   fileSecurity: An object that describes an ACL entry to apply to the current file.
  """
  pass
 def SetLength(self,value):
  """
  SetLength(self: FileStream,value: Int64)

   Sets the length of this stream to the given value.

  

   value: The new length of the stream.
  """
  pass
 def Unlock(self,position,length):
  """
  Unlock(self: FileStream,position: Int64,length: Int64)

   Allows access by other processes to all or part of a file that was previously locked.

  

   position: The beginning of the range to unlock.

   length: The range to be unlocked.
  """
  pass
 def Write(self,array,offset,count):
  """
  Write(self: FileStream,array: Array[Byte],offset: int,count: int)

   Writes a block of bytes to this stream using data from a buffer.

  

   array: The buffer containing data to write to the stream.

   offset: The zero-based byte offset in array at which to begin copying bytes to the current stream.

   count: The number of bytes to be written to the current stream.
  """
  pass
 def WriteAsync(self,buffer,offset,count,cancellationToken=None):
  """ WriteAsync(self: FileStream,buffer: Array[Byte],offset: int,count: int,cancellationToken: CancellationToken) -> Task """
  pass
 def WriteByte(self,value):
  """
  WriteByte(self: FileStream,value: Byte)

   Writes a byte to the current position in the file stream.

  

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
 def __new__(self,*__args):
  """
  __new__(cls: type,path: str,mode: FileMode)

  __new__(cls: type,path: str,mode: FileMode,access: FileAccess)

  __new__(cls: type,path: str,mode: FileMode,access: FileAccess,share: FileShare)

  __new__(cls: type,path: str,mode: FileMode,access: FileAccess,share: FileShare,bufferSize: int)

  __new__(cls: type,path: str,mode: FileMode,access: FileAccess,share: FileShare,bufferSize: int,options: FileOptions)

  __new__(cls: type,path: str,mode: FileMode,access: FileAccess,share: FileShare,bufferSize: int,useAsync: bool)

  __new__(cls: type,path: str,mode: FileMode,rights: FileSystemRights,share: FileShare,bufferSize: int,options: FileOptions,fileSecurity: FileSecurity)

  __new__(cls: type,path: str,mode: FileMode,rights: FileSystemRights,share: FileShare,bufferSize: int,options: FileOptions)

  __new__(cls: type,handle: IntPtr,access: FileAccess)

  __new__(cls: type,handle: IntPtr,access: FileAccess,ownsHandle: bool)

  __new__(cls: type,handle: IntPtr,access: FileAccess,ownsHandle: bool,bufferSize: int)

  __new__(cls: type,handle: IntPtr,access: FileAccess,ownsHandle: bool,bufferSize: int,isAsync: bool)

  __new__(cls: type,handle: SafeFileHandle,access: FileAccess)

  __new__(cls: type,handle: SafeFileHandle,access: FileAccess,bufferSize: int)

  __new__(cls: type,handle: SafeFileHandle,access: FileAccess,bufferSize: int,isAsync: bool)
  """
  pass
 CanRead=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current stream supports reading.



Get: CanRead(self: FileStream) -> bool



"""

 CanSeek=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current stream supports seeking.



Get: CanSeek(self: FileStream) -> bool



"""

 CanWrite=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current stream supports writing.



Get: CanWrite(self: FileStream) -> bool



"""

 Handle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the operating system file handle for the file that the current FileStream object encapsulates.



Get: Handle(self: FileStream) -> IntPtr



"""

 IsAsync=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the FileStream was opened asynchronously or synchronously.



Get: IsAsync(self: FileStream) -> bool



"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length in bytes of the stream.



Get: Length(self: FileStream) -> Int64



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the FileStream that was passed to the constructor.



Get: Name(self: FileStream) -> str



"""

 Position=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current position of this stream.



Get: Position(self: FileStream) -> Int64



Set: Position(self: FileStream)=value

"""

 SafeFileHandle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a Microsoft.Win32.SafeHandles.SafeFileHandle object that represents the operating system file handle for the file that the current System.IO.FileStream object encapsulates.



Get: SafeFileHandle(self: FileStream) -> SafeFileHandle



"""


