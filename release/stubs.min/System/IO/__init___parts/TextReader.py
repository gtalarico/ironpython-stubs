class TextReader(MarshalByRefObject,IDisposable):
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
  Peek(self: TextReader) -> int

  

   Reads the next character without changing the state of the reader or the character source. 

    Returns the next available character without actually reading it from the input stream.

  

   Returns: An integer representing the next character to be read,or -1 if no more characters are available 

    or the stream does not support seeking.
  """
  pass
 def Read(self,buffer=None,index=None,count=None):
  """
  Read(self: TextReader,index: int,count: int) -> (int,Array[Char])

  

   Reads a maximum of count characters from the current stream and writes the data to buffer,

    beginning at index.

  

  

   index: The position in buffer at which to begin writing.

   count: The maximum number of characters to read. If the end of the stream is reached before count of 

    characters is read into buffer,the current method returns.

  

   Returns: The number of characters that have been read. The number will be less than or equal to count,

    depending on whether the data is available within the stream. This method returns zero if called 

    when no more characters are left to read.

  

  Read(self: TextReader) -> int

  

   Reads the next character from the input stream and advances the character position by one 

    character.

  

   Returns: The next character from the input stream,or -1 if no more characters are available. The default 

    implementation returns -1.
  """
  pass
 def ReadAsync(self,buffer,index,count):
  """ ReadAsync(self: TextReader,buffer: Array[Char],index: int,count: int) -> Task[int] """
  pass
 def ReadBlock(self,buffer,index,count):
  """
  ReadBlock(self: TextReader,index: int,count: int) -> (int,Array[Char])

  

   Reads a maximum of count characters from the current stream,and writes the data to buffer,

    beginning at index.

  

  

   index: The position in buffer at which to begin writing.

   count: The maximum number of characters to read.

   Returns: The position of the underlying stream is advanced by the number of characters that were read 

    into buffer.The number of characters that have been read. The number will be less than or equal 

    to count,depending on whether all input characters have been read.
  """
  pass
 def ReadBlockAsync(self,buffer,index,count):
  """ ReadBlockAsync(self: TextReader,buffer: Array[Char],index: int,count: int) -> Task[int] """
  pass
 def ReadLine(self):
  """
  ReadLine(self: TextReader) -> str

  

   Reads a line of characters from the current stream and returns the data as a string.

   Returns: The next line from the input stream,or null if all characters have been read.
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
 Null=None

