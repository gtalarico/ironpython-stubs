class BitConverter(object):
 """ Converts base data types to an array of bytes,and an array of bytes to base data types. """
 @staticmethod
 def DoubleToInt64Bits(value):
  """
  DoubleToInt64Bits(value: float) -> Int64

  

   Converts the specified double-precision floating point number to a 64-bit signed integer.

  

   value: The number to convert.

   Returns: A 64-bit signed integer whose value is equivalent to value.
  """
  pass
 @staticmethod
 def GetBytes(value):
  """
  GetBytes(value: UInt32) -> Array[Byte]

  

   Returns the specified 32-bit unsigned integer value as an array of bytes.

  

   value: The number to convert.

   Returns: An array of bytes with length 4.

  GetBytes(value: UInt16) -> Array[Byte]

  

   Returns the specified 16-bit unsigned integer value as an array of bytes.

  

   value: The number to convert.

   Returns: An array of bytes with length 2.

  GetBytes(value: UInt64) -> Array[Byte]

  

   Returns the specified 64-bit unsigned integer value as an array of bytes.

  

   value: The number to convert.

   Returns: An array of bytes with length 8.

  GetBytes(value: float) -> Array[Byte]

  

   Returns the specified double-precision floating point value as an array of bytes.

  

   value: The number to convert.

   Returns: An array of bytes with length 8.

  GetBytes(value: Single) -> Array[Byte]

  

   Returns the specified single-precision floating point value as an array of bytes.

  

   value: The number to convert.

   Returns: An array of bytes with length 4.

  GetBytes(value: Char) -> Array[Byte]

  

   Returns the specified Unicode character value as an array of bytes.

  

   value: A character to convert.

   Returns: An array of bytes with length 2.

  GetBytes(value: bool) -> Array[Byte]

  

   Returns the specified Boolean value as an array of bytes.

  

   value: A Boolean value.

   Returns: An array of bytes with length 1.

  GetBytes(value: Int16) -> Array[Byte]

  

   Returns the specified 16-bit signed integer value as an array of bytes.

  

   value: The number to convert.

   Returns: An array of bytes with length 2.

  GetBytes(value: Int64) -> Array[Byte]

  

   Returns the specified 64-bit signed integer value as an array of bytes.

  

   value: The number to convert.

   Returns: An array of bytes with length 8.

  GetBytes(value: int) -> Array[Byte]

  

   Returns the specified 32-bit signed integer value as an array of bytes.

  

   value: The number to convert.

   Returns: An array of bytes with length 4.
  """
  pass
 @staticmethod
 def Int64BitsToDouble(value):
  """
  Int64BitsToDouble(value: Int64) -> float

  

   Converts the specified 64-bit signed integer to a double-precision floating point number.

  

   value: The number to convert.

   Returns: A double-precision floating point number whose value is equivalent to value.
  """
  pass
 @staticmethod
 def ToBoolean(value,startIndex):
  """
  ToBoolean(value: Array[Byte],startIndex: int) -> bool

  

   Returns a Boolean value converted from one byte at a specified position in a byte array.

  

   value: An array of bytes.

   startIndex: The starting position within value.

   Returns: true if the byte at startIndex in value is nonzero; otherwise,false.
  """
  pass
 @staticmethod
 def ToChar(value,startIndex):
  """
  ToChar(value: Array[Byte],startIndex: int) -> Char

  

   Returns a Unicode character converted from two bytes at a specified position in a byte array.

  

   value: An array.

   startIndex: The starting position within value.

   Returns: A character formed by two bytes beginning at startIndex.
  """
  pass
 @staticmethod
 def ToDouble(value,startIndex):
  """
  ToDouble(value: Array[Byte],startIndex: int) -> float

  

   Returns a double-precision floating point number converted from eight bytes at a specified 

    position in a byte array.

  

  

   value: An array of bytes.

   startIndex: The starting position within value.

   Returns: A double precision floating point number formed by eight bytes beginning at startIndex.
  """
  pass
 @staticmethod
 def ToInt16(value,startIndex):
  """
  ToInt16(value: Array[Byte],startIndex: int) -> Int16

  

   Returns a 16-bit signed integer converted from two bytes at a specified position in a byte array.

  

   value: An array of bytes.

   startIndex: The starting position within value.

   Returns: A 16-bit signed integer formed by two bytes beginning at startIndex.
  """
  pass
 @staticmethod
 def ToInt32(value,startIndex):
  """
  ToInt32(value: Array[Byte],startIndex: int) -> int

  

   Returns a 32-bit signed integer converted from four bytes at a specified position in a byte 

    array.

  

  

   value: An array of bytes.

   startIndex: The starting position within value.

   Returns: A 32-bit signed integer formed by four bytes beginning at startIndex.
  """
  pass
 @staticmethod
 def ToInt64(value,startIndex):
  """
  ToInt64(value: Array[Byte],startIndex: int) -> Int64

  

   Returns a 64-bit signed integer converted from eight bytes at a specified position in a byte 

    array.

  

  

   value: An array of bytes.

   startIndex: The starting position within value.

   Returns: A 64-bit signed integer formed by eight bytes beginning at startIndex.
  """
  pass
 @staticmethod
 def ToSingle(value,startIndex):
  """
  ToSingle(value: Array[Byte],startIndex: int) -> Single

  

   Returns a single-precision floating point number converted from four bytes at a specified 

    position in a byte array.

  

  

   value: An array of bytes.

   startIndex: The starting position within value.

   Returns: A single-precision floating point number formed by four bytes beginning at startIndex.
  """
  pass
 @staticmethod
 def ToString(value=None,startIndex=None,length=None):
  """
  ToString(value: Array[Byte],startIndex: int) -> str

  

   Converts the numeric value of each element of a specified subarray of bytes to its equivalent 

    hexadecimal string representation.

  

  

   value: An array of bytes.

   startIndex: The starting position within value.

   Returns: A string of hexadecimal pairs separated by hyphens,where each pair represents the corresponding 

    element in a subarray of value; for example,"7F-2C-4A-00".

  

  ToString(value: Array[Byte]) -> str

  

   Converts the numeric value of each element of a specified array of bytes to its equivalent 

    hexadecimal string representation.

  

  

   value: An array of bytes.

   Returns: A string of hexadecimal pairs separated by hyphens,where each pair represents the corresponding 

    element in value; for example,"7F-2C-4A-00".

  

  ToString(value: Array[Byte],startIndex: int,length: int) -> str

  

   Converts the numeric value of each element of a specified subarray of bytes to its equivalent 

    hexadecimal string representation.

  

  

   value: An array of bytes.

   startIndex: The starting position within value.

   length: The number of array elements in value to convert.

   Returns: A string of hexadecimal pairs separated by hyphens,where each pair represents the corresponding 

    element in a subarray of value; for example,"7F-2C-4A-00".
  """
  pass
 @staticmethod
 def ToUInt16(value,startIndex):
  """
  ToUInt16(value: Array[Byte],startIndex: int) -> UInt16

  

   Returns a 16-bit unsigned integer converted from two bytes at a specified position in a byte 

    array.

  

  

   value: The array of bytes.

   startIndex: The starting position within value.

   Returns: A 16-bit unsigned integer formed by two bytes beginning at startIndex.
  """
  pass
 @staticmethod
 def ToUInt32(value,startIndex):
  """
  ToUInt32(value: Array[Byte],startIndex: int) -> UInt32

  

   Returns a 32-bit unsigned integer converted from four bytes at a specified position in a byte 

    array.

  

  

   value: An array of bytes.

   startIndex: The starting position within value.

   Returns: A 32-bit unsigned integer formed by four bytes beginning at startIndex.
  """
  pass
 @staticmethod
 def ToUInt64(value,startIndex):
  """
  ToUInt64(value: Array[Byte],startIndex: int) -> UInt64

  

   Returns a 64-bit unsigned integer converted from eight bytes at a specified position in a byte 

    array.

  

  

   value: An array of bytes.

   startIndex: The starting position within value.

   Returns: A 64-bit unsigned integer formed by the eight bytes beginning at startIndex.
  """
  pass
 IsLittleEndian=True
 __all__=[
  'DoubleToInt64Bits',
  'GetBytes',
  'Int64BitsToDouble',
  'IsLittleEndian',
  'ToBoolean',
  'ToChar',
  'ToDouble',
  'ToInt16',
  'ToInt32',
  'ToInt64',
  'ToSingle',
  'ToString',
  'ToUInt16',
  'ToUInt32',
  'ToUInt64',
 ]

