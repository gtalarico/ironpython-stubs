class StreamWriter(TextWriter,IDisposable):
 """
 Implements a System.IO.TextWriter for writing characters to a stream in a particular encoding.

 

 StreamWriter(stream: Stream)

 StreamWriter(stream: Stream,encoding: Encoding)

 StreamWriter(stream: Stream,encoding: Encoding,bufferSize: int)

 StreamWriter(stream: Stream,encoding: Encoding,bufferSize: int,leaveOpen: bool)

 StreamWriter(path: str)

 StreamWriter(path: str,append: bool)

 StreamWriter(path: str,append: bool,encoding: Encoding)

 StreamWriter(path: str,append: bool,encoding: Encoding,bufferSize: int)
 """
 def Close(self):
  """
  Close(self: StreamWriter)

   Closes the current StreamWriter object and the underlying stream.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: StreamWriter,disposing: bool)

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
 def Write(self,*__args):
  """
  Write(self: StreamWriter,buffer: Array[Char],index: int,count: int)

   Writes a subarray of characters to the stream.

  

   buffer: A character array containing the data to write.

   index: The index into buffer at which to begin writing.

   count: The number of characters to read from buffer.

  Write(self: StreamWriter,value: str)

   Writes a string to the stream.

  

   value: The string to write to the stream. If value is null,nothing is written.

  Write(self: StreamWriter,value: Char)

   Writes a character to the stream.

  

   value: The character to write to the text stream.

  Write(self: StreamWriter,buffer: Array[Char])

   Writes a character array to the stream.

  

   buffer: A character array containing the data to write. If buffer is null,nothing is written.
  """
  pass
 def WriteAsync(self,*__args):
  """
  WriteAsync(self: StreamWriter,buffer: Array[Char],index: int,count: int) -> Task

  WriteAsync(self: StreamWriter,value: str) -> Task

  WriteAsync(self: StreamWriter,value: Char) -> Task
  """
  pass
 def WriteLineAsync(self,*__args):
  """
  WriteLineAsync(self: StreamWriter,value: str) -> Task

  WriteLineAsync(self: StreamWriter,buffer: Array[Char],index: int,count: int) -> Task

  WriteLineAsync(self: StreamWriter) -> Task

  WriteLineAsync(self: StreamWriter,value: Char) -> Task
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
  __new__(cls: type,stream: Stream)

  __new__(cls: type,stream: Stream,encoding: Encoding)

  __new__(cls: type,stream: Stream,encoding: Encoding,bufferSize: int)

  __new__(cls: type,stream: Stream,encoding: Encoding,bufferSize: int,leaveOpen: bool)

  __new__(cls: type,path: str)

  __new__(cls: type,path: str,append: bool)

  __new__(cls: type,path: str,append: bool,encoding: Encoding)

  __new__(cls: type,path: str,append: bool,encoding: Encoding,bufferSize: int)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 AutoFlush=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.IO.StreamWriter will flush its buffer to the underlying stream after every call to System.IO.StreamWriter.Write(System.Char).



Get: AutoFlush(self: StreamWriter) -> bool



Set: AutoFlush(self: StreamWriter)=value

"""

 BaseStream=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the underlying stream that interfaces with a backing store.



Get: BaseStream(self: StreamWriter) -> Stream



"""

 Encoding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Text.Encoding in which the output is written.



Get: Encoding(self: StreamWriter) -> Encoding



"""


 CoreNewLine=None
 Null=None

