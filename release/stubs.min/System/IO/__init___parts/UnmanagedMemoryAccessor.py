class UnmanagedMemoryAccessor(object,IDisposable):
 """
 Provides random access to unmanaged blocks of memory from managed code.

 

 UnmanagedMemoryAccessor(buffer: SafeBuffer,offset: Int64,capacity: Int64)

 UnmanagedMemoryAccessor(buffer: SafeBuffer,offset: Int64,capacity: Int64,access: FileAccess)
 """
 def Dispose(self):
  """
  Dispose(self: UnmanagedMemoryAccessor)

   Releases all resources used by the System.IO.UnmanagedMemoryAccessor.
  """
  pass
 def Initialize(self,*args):
  """
  Initialize(self: UnmanagedMemoryAccessor,buffer: SafeBuffer,offset: Int64,capacity: Int64,access: FileAccess)

   Sets the initial values for the accessor.

  

   buffer: The buffer to contain the accessor.

   offset: The byte at which to start the accessor.

   capacity: The size,in bytes,of memory to allocate.

   access: The type of access allowed to the memory. The default is 

    System.IO.MemoryMappedFiles.MemoryMappedFileAccess.ReadWrite.
  """
  pass
 def Read(self,position,structure):
  """ Read[T](self: UnmanagedMemoryAccessor,position: Int64) -> T """
  pass
 def ReadArray(self,position,array,offset,count):
  """ ReadArray[T](self: UnmanagedMemoryAccessor,position: Int64,array: Array[T],offset: int,count: int) -> int """
  pass
 def ReadBoolean(self,position):
  """
  ReadBoolean(self: UnmanagedMemoryAccessor,position: Int64) -> bool

  

   Reads a Boolean value from the accessor.

  

   position: The number of bytes into the accessor at which to begin reading.

   Returns: true or false.
  """
  pass
 def ReadByte(self,position):
  """
  ReadByte(self: UnmanagedMemoryAccessor,position: Int64) -> Byte

  

   Reads a byte value from the accessor.

  

   position: The number of bytes into the accessor at which to begin reading.

   Returns: The value that was read.
  """
  pass
 def ReadChar(self,position):
  """
  ReadChar(self: UnmanagedMemoryAccessor,position: Int64) -> Char

  

   Reads a character from the accessor.

  

   position: The number of bytes into the accessor at which to begin reading.

   Returns: The value that was read.
  """
  pass
 def ReadDecimal(self,position):
  """
  ReadDecimal(self: UnmanagedMemoryAccessor,position: Int64) -> Decimal

  

   Reads a decimal value from the accessor.

  

   position: The number of bytes into the accessor at which to begin reading.

   Returns: The value that was read.
  """
  pass
 def ReadDouble(self,position):
  """
  ReadDouble(self: UnmanagedMemoryAccessor,position: Int64) -> float

  

   Reads a double-precision floating-point value from the accessor.

  

   position: The number of bytes into the accessor at which to begin reading.

   Returns: The value that was read.
  """
  pass
 def ReadInt16(self,position):
  """
  ReadInt16(self: UnmanagedMemoryAccessor,position: Int64) -> Int16

  

   Reads a 16-bit integer from the accessor.

  

   position: The number of bytes into the accessor at which to begin reading.

   Returns: The value that was read.
  """
  pass
 def ReadInt32(self,position):
  """
  ReadInt32(self: UnmanagedMemoryAccessor,position: Int64) -> int

  

   Reads a 32-bit integer from the accessor.

  

   position: The number of bytes into the accessor at which to begin reading.

   Returns: The value that was read.
  """
  pass
 def ReadInt64(self,position):
  """
  ReadInt64(self: UnmanagedMemoryAccessor,position: Int64) -> Int64

  

   Reads a 64-bit integer from the accessor.

  

   position: The number of bytes into the accessor at which to begin reading.

   Returns: The value that was read.
  """
  pass
 def ReadSByte(self,position):
  """
  ReadSByte(self: UnmanagedMemoryAccessor,position: Int64) -> SByte

  

   Reads an 8-bit signed integer from the accessor.

  

   position: The number of bytes into the accessor at which to begin reading.

   Returns: The value that was read.
  """
  pass
 def ReadSingle(self,position):
  """
  ReadSingle(self: UnmanagedMemoryAccessor,position: Int64) -> Single

  

   Reads a single-precision floating-point value from the accessor.

  

   position: The number of bytes into the accessor at which to begin reading.

   Returns: The value that was read.
  """
  pass
 def ReadUInt16(self,position):
  """
  ReadUInt16(self: UnmanagedMemoryAccessor,position: Int64) -> UInt16

  

   Reads an unsigned 16-bit integer from the accessor.

  

   position: The number of bytes into the accessor at which to begin reading.

   Returns: The value that was read.
  """
  pass
 def ReadUInt32(self,position):
  """
  ReadUInt32(self: UnmanagedMemoryAccessor,position: Int64) -> UInt32

  

   Reads an unsigned 32-bit integer from the accessor.

  

   position: The number of bytes into the accessor at which to begin reading.

   Returns: The value that was read.
  """
  pass
 def ReadUInt64(self,position):
  """
  ReadUInt64(self: UnmanagedMemoryAccessor,position: Int64) -> UInt64

  

   Reads an unsigned 64-bit integer from the accessor.

  

   position: The number of bytes into the accessor at which to begin reading.

   Returns: The value that was read.
  """
  pass
 def Write(self,position,*__args):
  """
  Write(self: UnmanagedMemoryAccessor,position: Int64,value: SByte)

   Writes an 8-bit integer into the accessor.

  

   position: The number of bytes into the accessor at which to begin writing.

   value: The value to write.

  Write(self: UnmanagedMemoryAccessor,position: Int64,value: float)

   Writes a Double value into the accessor.

  

   position: The number of bytes into the accessor at which to begin writing.

   value: The value to write.

  Write(self: UnmanagedMemoryAccessor,position: Int64,value: Single)

   Writes a Single into the accessor.

  

   position: The number of bytes into the accessor at which to begin writing.

   value: The value to write.

  Write(self: UnmanagedMemoryAccessor,position: Int64,value: UInt16)

   Writes an unsigned 16-bit integer into the accessor.

  

   position: The number of bytes into the accessor at which to begin writing.

   value: The value to write.

  Write[T](self: UnmanagedMemoryAccessor,position: Int64,structure: T) -> T

  Write(self: UnmanagedMemoryAccessor,position: Int64,value: UInt64)

   Writes an unsigned 64-bit integer into the accessor.

  

   position: The number of bytes into the accessor at which to begin writing.

   value: The value to write.

  Write(self: UnmanagedMemoryAccessor,position: Int64,value: UInt32)

   Writes an unsigned 32-bit integer into the accessor.

  

   position: The number of bytes into the accessor at which to begin writing.

   value: The value to write.

  Write(self: UnmanagedMemoryAccessor,position: Int64,value: Char)

   Writes a character into the accessor.

  

   position: The number of bytes into the accessor at which to begin writing.

   value: The value to write.

  Write(self: UnmanagedMemoryAccessor,position: Int64,value: Byte)

   Writes a byte value into the accessor.

  

   position: The number of bytes into the accessor at which to begin writing.

   value: The value to write.

  Write(self: UnmanagedMemoryAccessor,position: Int64,value: bool)

   Writes a Boolean value into the accessor.

  

   position: The number of bytes into the accessor at which to begin writing.

   value: The value to write.

  Write(self: UnmanagedMemoryAccessor,position: Int64,value: Int16)

   Writes a 16-bit integer into the accessor.

  

   position: The number of bytes into the accessor at which to begin writing.

   value: The value to write.

  Write(self: UnmanagedMemoryAccessor,position: Int64,value: Decimal)

   Writes a decimal value into the accessor.

  

   position: The number of bytes into the accessor at which to begin writing.

   value: The value to write.

  Write(self: UnmanagedMemoryAccessor,position: Int64,value: Int64)

   Writes a 64-bit integer into the accessor.

  

   position: The number of bytes into the accessor at which to begin writing.

   value: The value to write.

  Write(self: UnmanagedMemoryAccessor,position: Int64,value: int)

   Writes a 32-bit integer into the accessor.

  

   position: The number of bytes into the accessor at which to begin writing.

   value: The value to write.
  """
  pass
 def WriteArray(self,position,array,offset,count):
  """ WriteArray[T](self: UnmanagedMemoryAccessor,position: Int64,array: Array[T],offset: int,count: int) """
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
 def __new__(self,buffer,offset,capacity,access=None):
  """
  __new__(cls: type)

  __new__(cls: type,buffer: SafeBuffer,offset: Int64,capacity: Int64)

  __new__(cls: type,buffer: SafeBuffer,offset: Int64,capacity: Int64,access: FileAccess)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 CanRead=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines whether the accessor is readable.



Get: CanRead(self: UnmanagedMemoryAccessor) -> bool



"""

 CanWrite=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines whether the accessory is writable.



Get: CanWrite(self: UnmanagedMemoryAccessor) -> bool



"""

 Capacity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the capacity of the accessor.



Get: Capacity(self: UnmanagedMemoryAccessor) -> Int64



"""

 IsOpen=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines whether the accessor is currently open by a process.



"""


