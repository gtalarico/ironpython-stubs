class StringReader(TextReader,IDisposable):
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
  Dispose(self: StringReader,disposing: bool)

   Releases the unmanaged resources used by the System.IO.StringReader and optionally releases the 

    managed resources.

  

  

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
  Peek(self: StringReader) -> int

  

   Returns the next available character but does not consume it.

   Returns: An integer representing the next character to be read,or -1 if no more characters are available 

    or the stream does not support seeking.
  """
  pass
 def Read(self,buffer=None,index=None,count=None):
  """
  Read(self: StringReader,index: int,count: int) -> (int,Array[Char])

  

   Reads a block of characters from the input string and advances the character position by count.

  

   index: The starting index in the buffer.

   count: The number of characters to read.

   Returns: The total number of characters read into the buffer. This can be less than the number of 

    characters requested if that many characters are not currently available,or zero if the end of 

    the underlying string has been reached.

  

  Read(self: StringReader) -> int

  

   Reads the next character from the input string and advances the character position by one 

    character.

  

   Returns: The next character from the underlying string,or -1 if no more characters are available.
  """
  pass
 def ReadAsync(self,buffer,index,count):
  """ ReadAsync(self: StringReader,buffer: Array[Char],index: int,count: int) -> Task[int] """
  pass
 def ReadBlockAsync(self,buffer,index,count):
  """ ReadBlockAsync(self: StringReader,buffer: Array[Char],index: int,count: int) -> Task[int] """
  pass
 def ReadLine(self):
  """
  ReadLine(self: StringReader) -> str

  

   Reads a line from the underlying string.

   Returns: The next line from the underlying string,or null if the end of the underlying string is reached.
  """
  pass
 def ReadLineAsync(self):
  """ ReadLineAsync(self: StringReader) -> Task[str] """
  pass
 def ReadToEnd(self):
  """
  ReadToEnd(self: StringReader) -> str

  

   Reads the stream as a string,either in its entirety or from the current position to the end of 

    the stream.

  

   Returns: The content from the current position to the end of the underlying string.
  """
  pass
 def ReadToEndAsync(self):
  """ ReadToEndAsync(self: StringReader) -> Task[str] """
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
 def __new__(self,s):
  """ __new__(cls: type,s: str) """
  pass
 def __reduce_ex__(self,*args):
  pass
