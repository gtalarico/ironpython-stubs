class StreamReader(TextReader,IDisposable):
 """
 Implements a System.IO.TextReader that reads characters from a byte stream in a particular encoding.

 

 StreamReader(stream: Stream)

 StreamReader(stream: Stream,detectEncodingFromByteOrderMarks: bool)

 StreamReader(stream: Stream,encoding: Encoding)

 StreamReader(stream: Stream,encoding: Encoding,detectEncodingFromByteOrderMarks: bool)

 StreamReader(stream: Stream,encoding: Encoding,detectEncodingFromByteOrderMarks: bool,bufferSize: int)

 StreamReader(stream: Stream,encoding: Encoding,detectEncodingFromByteOrderMarks: bool,bufferSize: int,leaveOpen: bool)

 StreamReader(path: str)

 StreamReader(path: str,detectEncodingFromByteOrderMarks: bool)

 StreamReader(path: str,encoding: Encoding)

 StreamReader(path: str,encoding: Encoding,detectEncodingFromByteOrderMarks: bool)

 StreamReader(path: str,encoding: Encoding,detectEncodingFromByteOrderMarks: bool,bufferSize: int)
 """
 def Close(self):
  """
  Close(self: StreamReader)

   Closes the System.IO.StreamReader object and the underlying stream,and releases any system 

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
  Dispose(self: StreamReader,disposing: bool)

   Closes the underlying stream,releases the unmanaged resources used by the 

    System.IO.StreamReader,and optionally releases the managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
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
 def Peek(self):
  """
  Peek(self: StreamReader) -> int

  

   Returns the next available character but does not consume it.

   Returns: An integer representing the next character to be read,or -1 if there are no characters to be 

    read or if the stream does not support seeking.
  """
  pass
 def Read(self,buffer=None,index=None,count=None):
  """
  Read(self: StreamReader,index: int,count: int) -> (int,Array[Char])

  

   Reads a specified maximum of characters from the current stream into a buffer,beginning at the 

    specified index.

  

  

   index: The index of buffer at which to begin writing.

   count: The maximum number of characters to read.

   Returns: The number of characters that have been read,or 0 if at the end of the stream and no data was 

    read. The number will be less than or equal to the count parameter,depending on whether the 

    data is available within the stream.

  

  Read(self: StreamReader) -> int

  

   Reads the next character from the input stream and advances the character position by one 

    character.

  

   Returns: The next character from the input stream represented as an System.Int32 object,or -1 if no more 

    characters are available.
  """
  pass
 def ReadAsync(self,buffer,index,count):
  """ ReadAsync(self: StreamReader,buffer: Array[Char],index: int,count: int) -> Task[int] """
  pass
 def ReadBlock(self,buffer,index,count):
  """ ReadBlock(self: StreamReader,index: int,count: int) -> (int,Array[Char]) """
  pass
 def ReadBlockAsync(self,buffer,index,count):
  """ ReadBlockAsync(self: StreamReader,buffer: Array[Char],index: int,count: int) -> Task[int] """
  pass
 def ReadLine(self):
  """
  ReadLine(self: StreamReader) -> str

  

   Reads a line of characters from the current stream and returns the data as a string.

   Returns: The next line from the input stream,or null if the end of the input stream is reached.
  """
  pass
 def ReadLineAsync(self):
  """ ReadLineAsync(self: StreamReader) -> Task[str] """
  pass
 def ReadToEnd(self):
  """
  ReadToEnd(self: StreamReader) -> str

  

   Reads the stream from the current position to the end of the stream.

   Returns: The rest of the stream as a string,from the current position to the end. If the current 

    position is at the end of the stream,returns an empty string ("").
  """
  pass
 def ReadToEndAsync(self):
  """ ReadToEndAsync(self: StreamReader) -> Task[str] """
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

  __new__(cls: type,stream: Stream,detectEncodingFromByteOrderMarks: bool)

  __new__(cls: type,stream: Stream,encoding: Encoding)

  __new__(cls: type,stream: Stream,encoding: Encoding,detectEncodingFromByteOrderMarks: bool)

  __new__(cls: type,stream: Stream,encoding: Encoding,detectEncodingFromByteOrderMarks: bool,bufferSize: int)

  __new__(cls: type,stream: Stream,encoding: Encoding,detectEncodingFromByteOrderMarks: bool,bufferSize: int,leaveOpen: bool)

  __new__(cls: type,path: str)

  __new__(cls: type,path: str,detectEncodingFromByteOrderMarks: bool)

  __new__(cls: type,path: str,encoding: Encoding)

  __new__(cls: type,path: str,encoding: Encoding,detectEncodingFromByteOrderMarks: bool)

  __new__(cls: type,path: str,encoding: Encoding,detectEncodingFromByteOrderMarks: bool,bufferSize: int)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 BaseStream=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the underlying stream.



Get: BaseStream(self: StreamReader) -> Stream



"""

 CurrentEncoding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current character encoding that the current System.IO.StreamReader object is using.



Get: CurrentEncoding(self: StreamReader) -> Encoding



"""

 EndOfStream=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the current stream position is at the end of the stream.



Get: EndOfStream(self: StreamReader) -> bool



"""


 Null=None

