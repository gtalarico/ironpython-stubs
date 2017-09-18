class BinaryReader(object,IDisposable):
 """
 Reads primitive data types as binary values in a specific encoding.

 

 BinaryReader(input: Stream)

 BinaryReader(input: Stream,encoding: Encoding)

 BinaryReader(input: Stream,encoding: Encoding,leaveOpen: bool)
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
 def FillBuffer(self,*args):
  """
  FillBuffer(self: BinaryReader,numBytes: int)

   Fills the internal buffer with the specified number of bytes read from the stream.

  

   numBytes: The number of bytes to be read.
  """
  pass
 def PeekChar(self):
  """
  PeekChar(self: BinaryReader) -> int

  

   Returns the next available character and does not advance the byte or character position.

   Returns: The next available character,or -1 if no more characters are available or the stream does not 

    support seeking.
  """
  pass
 def Read(self,buffer=None,index=None,count=None):
  """
  Read(self: BinaryReader,buffer: Array[Byte],index: int,count: int) -> int

  

   Reads the specified number of bytes from the stream,starting from a specified point in the byte 

    array.

  

  

   buffer: The buffer to read data into.

   index: The starting point in the buffer at which to begin reading into the buffer.

   count: The number of bytes to read.

   Returns: The number of bytes read into buffer. This might be less than the number of bytes requested if 

    that many bytes are not available,or it might be zero if the end of the stream is reached.

  

  Read(self: BinaryReader,buffer: Array[Char],index: int,count: int) -> int

  

   Reads the specified number of characters from the stream,starting from a specified point in the 

    character array.

  

  

   buffer: The buffer to read data into.

   index: The starting point in the buffer at which to begin reading into the buffer.

   count: The number of characters to read.

   Returns: The total number of characters read into the buffer. This might be less than the number of 

    characters requested if that many characters are not currently available,or it might be zero if 

    the end of the stream is reached.

  

  Read(self: BinaryReader) -> int

  

   Reads characters from the underlying stream and advances the current position of the stream in 

    accordance with the Encoding used and the specific character being read from the stream.

  

   Returns: The next character from the input stream,or -1 if no characters are currently available.
  """
  pass
 def Read7BitEncodedInt(self,*args):
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

  

   Returns: true if the byte is nonzero; otherwise,false.
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
 def ReadBytes(self,count):
  """
  ReadBytes(self: BinaryReader,count: int) -> Array[Byte]

  

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
 def ReadChars(self,count):
  """
  ReadChars(self: BinaryReader,count: int) -> Array[Char]

  

   Reads the specified number of characters from the current stream,returns the data in a 

    character array,and advances the current position in accordance with the Encoding used and the 

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

  

   Reads a string from the current stream. The string is prefixed with the length,encoded as an 

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
 def __new__(self,input,encoding=None,leaveOpen=None):
  """
  __new__(cls: type,input: Stream)

  __new__(cls: type,input: Stream,encoding: Encoding)

  __new__(cls: type,input: Stream,encoding: Encoding,leaveOpen: bool)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 BaseStream=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Exposes access to the underlying stream of the System.IO.BinaryReader.



Get: BaseStream(self: BinaryReader) -> Stream



"""


