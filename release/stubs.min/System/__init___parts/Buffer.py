class Buffer(object):
 """ Manipulates arrays of primitive types. """
 @staticmethod
 def BlockCopy(src,srcOffset,dst,dstOffset,count):
  """
  BlockCopy(src: Array,srcOffset: int,dst: Array,dstOffset: int,count: int)

   Copies a specified number of bytes from a source array starting at a particular offset to a 

    destination array starting at a particular offset.

  

  

   src: The source buffer.

   srcOffset: The zero-based byte offset into src.

   dst: The destination buffer.

   dstOffset: The zero-based byte offset into dst.

   count: The number of bytes to copy.
  """
  pass
 @staticmethod
 def ByteLength(array):
  """
  ByteLength(array: Array) -> int

  

   Returns the number of bytes in the specified array.

  

   array: An array.

   Returns: The number of bytes in the array.
  """
  pass
 @staticmethod
 def GetByte(array,index):
  """
  GetByte(array: Array,index: int) -> Byte

  

   Retrieves the byte at a specified location in a specified array.

  

   array: An array.

   index: A location in the array.

   Returns: Returns the index byte in the array.
  """
  pass
 @staticmethod
 def MemoryCopy(source,destination,destinationSizeInBytes,sourceBytesToCopy):
  """ MemoryCopy(source: Void*,destination: Void*,destinationSizeInBytes: UInt64,sourceBytesToCopy: UInt64)MemoryCopy(source: Void*,destination: Void*,destinationSizeInBytes: Int64,sourceBytesToCopy: Int64) """
  pass
 @staticmethod
 def SetByte(array,index,value):
  """
  SetByte(array: Array,index: int,value: Byte)

   Assigns a specified value to a byte at a particular location in a specified array.

  

   array: An array.

   index: A location in the array.

   value: A value to assign.
  """
  pass
 __all__=[
  'BlockCopy',
  'ByteLength',
  'GetByte',
  'MemoryCopy',
  'SetByte',
 ]

