class TextWriter(MarshalByRefObject,IDisposable):
 """ Represents a writer that can write a sequential series of characters. This class is abstract. """
 def Close(self):
  """
  Close(self: TextWriter)

   Closes the current writer and releases any system resources associated with the writer.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: TextWriter)

   Releases all resources used by the System.IO.TextWriter object.
  """
  pass
 def Flush(self):
  """
  Flush(self: TextWriter)

   Clears all buffers for the current writer and causes any buffered data to be written to the 

    underlying device.
  """
  pass
 def FlushAsync(self):
  """ FlushAsync(self: TextWriter) -> Task """
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
 @staticmethod
 def Synchronized(writer):
  """
  Synchronized(writer: TextWriter) -> TextWriter

  

   Creates a thread-safe wrapper around the specified TextWriter.

  

   writer: The TextWriter to synchronize.

   Returns: A thread-safe wrapper.
  """
  pass
 def Write(self,*__args):
  """
  Write(self: TextWriter,value: str)

   Writes a string to the text stream.

  

   value: The string to write.

  Write(self: TextWriter,value: object)

   Writes the text representation of an object to the text stream by calling ToString on that 

    object.

  

  

   value: The object to write.

  Write(self: TextWriter,value: float)

   Writes the text representation of an 8-byte floating-point value to the text stream.

  

   value: The 8-byte floating-point value to write.

  Write(self: TextWriter,value: Decimal)

   Writes the text representation of a decimal value to the text stream.

  

   value: The decimal value to write.

  Write(self: TextWriter,format: str,arg0: object,arg1: object,arg2: object)

   Writes out a formatted string,using the same semantics as 

    System.String.Format(System.String,System.Object).

  

  

   format: The formatting string.

   arg0: An object to write into the formatted string.

   arg1: An object to write into the formatted string.

   arg2: An object to write into the formatted string.

  Write(self: TextWriter,format: str,*arg: Array[object])

   Writes out a formatted string,using the same semantics as 

    System.String.Format(System.String,System.Object).

  

  

   format: The formatting string.

   arg: The object array to write into the formatted string.

  Write(self: TextWriter,format: str,arg0: object)

   Writes out a formatted string,using the same semantics as 

    System.String.Format(System.String,System.Object).

  

  

   format: The formatting string.

   arg0: An object to write into the formatted string.

  Write(self: TextWriter,format: str,arg0: object,arg1: object)

   Writes out a formatted string,using the same semantics as 

    System.String.Format(System.String,System.Object).

  

  

   format: The formatting string.

   arg0: An object to write into the formatted string.

   arg1: An object to write into the formatted string.

  Write(self: TextWriter,value: Single)

   Writes the text representation of a 4-byte floating-point value to the text stream.

  

   value: The 4-byte floating-point value to write.

  Write(self: TextWriter,buffer: Array[Char],index: int,count: int)

   Writes a subarray of characters to the text stream.

  

   buffer: The character array to write data from.

   index: Starting index in the buffer.

   count: The number of characters to write.

  Write(self: TextWriter,value: bool)

   Writes the text representation of a Boolean value to the text stream.

  

   value: The Boolean to write.

  Write(self: TextWriter,value: Char)

   Writes a character to the text stream.

  

   value: The character to write to the text stream.

  Write(self: TextWriter,buffer: Array[Char])

   Writes a character array to the text stream.

  

   buffer: The character array to write to the text stream.

  Write(self: TextWriter,value: Int64)

   Writes the text representation of an 8-byte signed integer to the text stream.

  

   value: The 8-byte signed integer to write.

  Write(self: TextWriter,value: UInt64)

   Writes the text representation of an 8-byte unsigned integer to the text stream.

  

   value: The 8-byte unsigned integer to write.

  Write(self: TextWriter,value: int)

   Writes the text representation of a 4-byte signed integer to the text stream.

  

   value: The 4-byte signed integer to write.

  Write(self: TextWriter,value: UInt32)

   Writes the text representation of a 4-byte unsigned integer to the text stream.

  

   value: The 4-byte unsigned integer to write.
  """
  pass
 def WriteAsync(self,*__args):
  """
  WriteAsync(self: TextWriter,buffer: Array[Char]) -> Task

  WriteAsync(self: TextWriter,buffer: Array[Char],index: int,count: int) -> Task

  WriteAsync(self: TextWriter,value: Char) -> Task

  WriteAsync(self: TextWriter,value: str) -> Task
  """
  pass
 def WriteLine(self,*__args):
  """
  WriteLine(self: TextWriter,value: Decimal)

   Writes the text representation of a decimal value followed by a line terminator to the text 

    stream.

  

  

   value: The decimal value to write.

  WriteLine(self: TextWriter,value: str)

   Writes a string followed by a line terminator to the text stream.

  

   value: The string to write. If value is null,only the line termination characters are written.

  WriteLine(self: TextWriter,value: Single)

   Writes the text representation of a 4-byte floating-point value followed by a line terminator to 

    the text stream.

  

  

   value: The 4-byte floating-point value to write.

  WriteLine(self: TextWriter,value: float)

   Writes the text representation of a 8-byte floating-point value followed by a line terminator to 

    the text stream.

  

  

   value: The 8-byte floating-point value to write.

  WriteLine(self: TextWriter,value: object)

   Writes the text representation of an object by calling ToString on this object,followed by a 

    line terminator to the text stream.

  

  

   value: The object to write. If value is null,only the line termination characters are written.

  WriteLine(self: TextWriter,format: str,arg0: object,arg1: object,arg2: object)

   Writes out a formatted string and a new line,using the same semantics as 

    System.String.Format(System.String,System.Object).

  

  

   format: The formatting string.

   arg0: The object to write into the format string.

   arg1: The object to write into the format string.

   arg2: The object to write into the format string.

  WriteLine(self: TextWriter,format: str,*arg: Array[object])

   Writes out a formatted string and a new line,using the same semantics as 

    System.String.Format(System.String,System.Object).

  

  

   format: The formatting string.

   arg: The object array to write into format string.

  WriteLine(self: TextWriter,format: str,arg0: object)

   Writes out a formatted string and a new line,using the same semantics as 

    System.String.Format(System.String,System.Object).

  

  

   format: The formatted string.

   arg0: The object to write into the formatted string.

  WriteLine(self: TextWriter,format: str,arg0: object,arg1: object)

   Writes out a formatted string and a new line,using the same semantics as 

    System.String.Format(System.String,System.Object).

  

  

   format: The formatting string.

   arg0: The object to write into the format string.

   arg1: The object to write into the format string.

  WriteLine(self: TextWriter,buffer: Array[Char])

   Writes an array of characters followed by a line terminator to the text stream.

  

   buffer: The character array from which data is read.

  WriteLine(self: TextWriter,buffer: Array[Char],index: int,count: int)

   Writes a subarray of characters followed by a line terminator to the text stream.

  

   buffer: The character array from which data is read.

   index: The index into buffer at which to begin reading.

   count: The maximum number of characters to write.

  WriteLine(self: TextWriter)

   Writes a line terminator to the text stream.

  WriteLine(self: TextWriter,value: Char)

   Writes a character followed by a line terminator to the text stream.

  

   value: The character to write to the text stream.

  WriteLine(self: TextWriter,value: bool)

   Writes the text representation of a Boolean followed by a line terminator to the text stream.

  

   value: The Boolean to write.

  WriteLine(self: TextWriter,value: Int64)

   Writes the text representation of an 8-byte signed integer followed by a line terminator to the 

    text stream.

  

  

   value: The 8-byte signed integer to write.

  WriteLine(self: TextWriter,value: UInt64)

   Writes the text representation of an 8-byte unsigned integer followed by a line terminator to 

    the text stream.

  

  

   value: The 8-byte unsigned integer to write.

  WriteLine(self: TextWriter,value: int)

   Writes the text representation of a 4-byte signed integer followed by a line terminator to the 

    text stream.

  

  

   value: The 4-byte signed integer to write.

  WriteLine(self: TextWriter,value: UInt32)

   Writes the text representation of a 4-byte unsigned integer followed by a line terminator to the 

    text stream.

  

  

   value: The 4-byte unsigned integer to write.
  """
  pass
 def WriteLineAsync(self,*__args):
  """
  WriteLineAsync(self: TextWriter,buffer: Array[Char],index: int,count: int) -> Task

  WriteLineAsync(self: TextWriter) -> Task

  WriteLineAsync(self: TextWriter,buffer: Array[Char]) -> Task

  WriteLineAsync(self: TextWriter,value: Char) -> Task

  WriteLineAsync(self: TextWriter,value: str) -> Task
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
 def __new__(self,*args): #cannot find CLR constructor
  """
  __new__(cls: type)

  __new__(cls: type,formatProvider: IFormatProvider)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 Encoding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,returns the System.Text.Encoding in which the output is written.



Get: Encoding(self: TextWriter) -> Encoding



"""

 FormatProvider=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an object that controls formatting.



Get: FormatProvider(self: TextWriter) -> IFormatProvider



"""

 NewLine=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the line terminator string used by the current TextWriter.



Get: NewLine(self: TextWriter) -> str



Set: NewLine(self: TextWriter)=value

"""


 CoreNewLine=None
 Null=None

