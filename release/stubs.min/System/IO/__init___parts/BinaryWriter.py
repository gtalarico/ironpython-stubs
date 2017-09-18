class BinaryWriter(object,IDisposable):
 """
 Writes primitive types in binary to a stream and supports writing strings in a specific encoding.

 

 BinaryWriter(output: Stream)

 BinaryWriter(output: Stream,encoding: Encoding)

 BinaryWriter(output: Stream,encoding: Encoding,leaveOpen: bool)
 """
 def Close(self):
  """
  Close(self: BinaryWriter)

   Closes the current System.IO.BinaryWriter and the underlying stream.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: BinaryWriter)

   Releases all resources used by the current instance of the System.IO.BinaryWriter class.
  """
  pass
 def Flush(self):
  """
  Flush(self: BinaryWriter)

   Clears all buffers for the current writer and causes any buffered data to be written to the 

    underlying device.
  """
  pass
 def Seek(self,offset,origin):
  """
  Seek(self: BinaryWriter,offset: int,origin: SeekOrigin) -> Int64

  

   Sets the position within the current stream.

  

   offset: A byte offset relative to origin.

   origin: A field of System.IO.SeekOrigin indicating the reference point from which the new position is to 

    be obtained.

  

   Returns: The position with the current stream.
  """
  pass
 def Write(self,*__args):
  """
  Write(self: BinaryWriter,value: UInt16)

   Writes a two-byte unsigned integer to the current stream and advances the stream position by two 

    bytes.

  

  

   value: The two-byte unsigned integer to write.

  Write(self: BinaryWriter,value: int)

   Writes a four-byte signed integer to the current stream and advances the stream position by four 

    bytes.

  

  

   value: The four-byte signed integer to write.

  Write(self: BinaryWriter,value: Decimal)

   Writes a decimal value to the current stream and advances the stream position by sixteen bytes.

  

   value: The decimal value to write.

  Write(self: BinaryWriter,value: Int16)

   Writes a two-byte signed integer to the current stream and advances the stream position by two 

    bytes.

  

  

   value: The two-byte signed integer to write.

  Write(self: BinaryWriter,value: UInt32)

   Writes a four-byte unsigned integer to the current stream and advances the stream position by 

    four bytes.

  

  

   value: The four-byte unsigned integer to write.

  Write(self: BinaryWriter,value: Single)

   Writes a four-byte floating-point value to the current stream and advances the stream position 

    by four bytes.

  

  

   value: The four-byte floating-point value to write.

  Write(self: BinaryWriter,value: str)

   Writes a length-prefixed string to this stream in the current encoding of the 

    System.IO.BinaryWriter,and advances the current position of the stream in accordance with the 

    encoding used and the specific characters being written to the stream.

  

  

   value: The value to write.

  Write(self: BinaryWriter,value: Int64)

   Writes an eight-byte signed integer to the current stream and advances the stream position by 

    eight bytes.

  

  

   value: The eight-byte signed integer to write.

  Write(self: BinaryWriter,value: UInt64)

   Writes an eight-byte unsigned integer to the current stream and advances the stream position by 

    eight bytes.

  

  

   value: The eight-byte unsigned integer to write.

  Write(self: BinaryWriter,value: SByte)

   Writes a signed byte to the current stream and advances the stream position by one byte.

  

   value: The signed byte to write.

  Write(self: BinaryWriter,buffer: Array[Byte])

   Writes a byte array to the underlying stream.

  

   buffer: A byte array containing the data to write.

  Write(self: BinaryWriter,value: bool)

   Writes a one-byte Boolean value to the current stream,with 0 representing false and 1 

    representing true.

  

  

   value: The Boolean value to write (0 or 1).

  Write(self: BinaryWriter,value: Byte)

   Writes an unsigned byte to the current stream and advances the stream position by one byte.

  

   value: The unsigned byte to write.

  Write(self: BinaryWriter,buffer: Array[Byte],index: int,count: int)

   Writes a region of a byte array to the current stream.

  

   buffer: A byte array containing the data to write.

   index: The starting point in buffer at which to begin writing.

   count: The number of bytes to write.

  Write(self: BinaryWriter,chars: Array[Char],index: int,count: int)

   Writes a section of a character array to the current stream,and advances the current position 

    of the stream in accordance with the Encoding used and perhaps the specific characters being 

    written to the stream.

  

  

   chars: A character array containing the data to write.

   index: The starting point in chars from which to begin writing.

   count: The number of characters to write.

  Write(self: BinaryWriter,value: float)

   Writes an eight-byte floating-point value to the current stream and advances the stream position 

    by eight bytes.

  

  

   value: The eight-byte floating-point value to write.

  Write(self: BinaryWriter,ch: Char)

   Writes a Unicode character to the current stream and advances the current position of the stream 

    in accordance with the Encoding used and the specific characters being written to the stream.

  

  

   ch: The non-surrogate,Unicode character to write.

  Write(self: BinaryWriter,chars: Array[Char])

   Writes a character array to the current stream and advances the current position of the stream 

    in accordance with the Encoding used and the specific characters being written to the stream.

  

  

   chars: A character array containing the data to write.
  """
  pass
 def Write7BitEncodedInt(self,*args):
  """
  Write7BitEncodedInt(self: BinaryWriter,value: int)

   Writes a 32-bit integer in a compressed format.

  

   value: The 32-bit integer to be written.
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
 def __new__(self,output,encoding=None,leaveOpen=None):
  """
  __new__(cls: type)

  __new__(cls: type,output: Stream)

  __new__(cls: type,output: Stream,encoding: Encoding)

  __new__(cls: type,output: Stream,encoding: Encoding,leaveOpen: bool)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 BaseStream=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the underlying stream of the System.IO.BinaryWriter.



Get: BaseStream(self: BinaryWriter) -> Stream



"""


 Null=None
 OutStream=None

