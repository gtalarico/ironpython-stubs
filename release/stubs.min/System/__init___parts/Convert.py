class Convert(object):
 """ Converts a base data type to another base data type. """
 @staticmethod
 def ChangeType(value,*__args):
  """
  ChangeType(value: object,conversionType: Type) -> object

  

   Returns an object of the specified type and whose value is equivalent to the specified object.

  

   value: An object that implements the System.IConvertible interface.

   conversionType: The type of object to return.

   Returns: An object whose type is conversionType and whose value is equivalent to value.-or-A null 

    reference (Nothing in Visual Basic),if value is null and conversionType is not a value type.

  

  ChangeType(value: object,conversionType: Type,provider: IFormatProvider) -> object

  

   Returns an object of the specified type whose value is equivalent to the specified object. A 

    parameter supplies culture-specific formatting information.

  

  

   value: An object that implements the System.IConvertible interface.

   conversionType: The type of object to return.

   provider: An object that supplies culture-specific formatting information.

   Returns: An object whose type is conversionType and whose value is equivalent to value.-or- value,if the 

    System.Type of value and conversionType are equal.-or- A null reference (Nothing in Visual 

    Basic),if value is null and conversionType is not a value type.

  

  ChangeType(value: object,typeCode: TypeCode) -> object

  

   Returns an object of the specified type whose value is equivalent to the specified object.

  

   value: An object that implements the System.IConvertible interface.

   typeCode: The type of object to return.

   Returns: An object whose underlying type is typeCode and whose value is equivalent to value.-or-A null 

    reference (Nothing in Visual Basic),if value is null and typeCode is System.TypeCode.Empty,

    System.TypeCode.String,or System.TypeCode.Object.

  

  ChangeType(value: object,typeCode: TypeCode,provider: IFormatProvider) -> object

  

   Returns an object of the specified type whose value is equivalent to the specified object. A 

    parameter supplies culture-specific formatting information.

  

  

   value: An object that implements the System.IConvertible interface.

   typeCode: The type of object to return.

   provider: An object that supplies culture-specific formatting information.

   Returns: An object whose underlying type is typeCode and whose value is equivalent to value.-or- A null 

    reference (Nothing in Visual Basic),if value is null and typeCode is System.TypeCode.Empty,

    System.TypeCode.String,or System.TypeCode.Object.
  """
  pass
 @staticmethod
 def FromBase64CharArray(inArray,offset,length):
  """
  FromBase64CharArray(inArray: Array[Char],offset: int,length: int) -> Array[Byte]

  

   Converts a subset of a Unicode character array,which encodes binary data as base-64 digits,to 

    an equivalent 8-bit unsigned integer array. Parameters specify the subset in the input array and 

    the number of elements to convert.

  

  

   inArray: A Unicode character array.

   offset: A position within inArray.

   length: The number of elements in inArray to convert.

   Returns: An array of 8-bit unsigned integers equivalent to length elements at position offset in inArray.
  """
  pass
 @staticmethod
 def FromBase64String(s):
  """
  FromBase64String(s: str) -> Array[Byte]

  

   Converts the specified string,which encodes binary data as base-64 digits,to an equivalent 

    8-bit unsigned integer array.

  

  

   s: The string to convert.

   Returns: An array of 8-bit unsigned integers that is equivalent to s.
  """
  pass
 @staticmethod
 def GetTypeCode(value):
  """
  GetTypeCode(value: object) -> TypeCode

  

   Returns the System.TypeCode for the specified object.

  

   value: An object that implements the System.IConvertible interface.

   Returns: The System.TypeCode for value,or System.TypeCode.Empty if value is null.
  """
  pass
 @staticmethod
 def IsDBNull(value):
  """
  IsDBNull(value: object) -> bool

  

   Returns an indication whether the specified object is of type System.DBNull.

  

   value: An object.

   Returns: true if value is of type System.DBNull; otherwise,false.
  """
  pass
 @staticmethod
 def ToBase64CharArray(inArray,offsetIn,length,outArray,offsetOut,options=None):
  """
  ToBase64CharArray(inArray: Array[Byte],offsetIn: int,length: int,outArray: Array[Char],offsetOut: int,options: Base64FormattingOptions) -> int

  

   Converts a subset of an 8-bit unsigned integer array to an equivalent subset of a Unicode 

    character array encoded with base-64 digits. Parameters specify the subsets as offsets in the 

    input and output arrays,the number of elements in the input array to convert,and whether line 

    breaks are inserted in the output array.

  

  

   inArray: An input array of 8-bit unsigned integers.

   offsetIn: A position within inArray.

   length: The number of elements of inArray to convert.

   outArray: An output array of Unicode characters.

   offsetOut: A position within outArray.

   options: System.Base64FormattingOptions.InsertLineBreaks to insert a line break every 76 characters,or 

    System.Base64FormattingOptions.None to not insert line breaks.

  

   Returns: A 32-bit signed integer containing the number of bytes in outArray.

  ToBase64CharArray(inArray: Array[Byte],offsetIn: int,length: int,outArray: Array[Char],offsetOut: int) -> int

  

   Converts a subset of an 8-bit unsigned integer array to an equivalent subset of a Unicode 

    character array encoded with base-64 digits. Parameters specify the subsets as offsets in the 

    input and output arrays,and the number of elements in the input array to convert.

  

  

   inArray: An input array of 8-bit unsigned integers.

   offsetIn: A position within inArray.

   length: The number of elements of inArray to convert.

   outArray: An output array of Unicode characters.

   offsetOut: A position within outArray.

   Returns: A 32-bit signed integer containing the number of bytes in outArray.
  """
  pass
 @staticmethod
 def ToBase64String(inArray,*__args):
  """
  ToBase64String(inArray: Array[Byte],offset: int,length: int) -> str

  

   Converts a subset of an array of 8-bit unsigned integers to its equivalent string representation 

    that is encoded with base-64 digits. Parameters specify the subset as an offset in the input 

    array,and the number of elements in the array to convert.

  

  

   inArray: An array of 8-bit unsigned integers.

   offset: An offset in inArray.

   length: The number of elements of inArray to convert.

   Returns: The string representation in base 64 of length elements of inArray,starting at position offset.

  ToBase64String(inArray: Array[Byte],offset: int,length: int,options: Base64FormattingOptions) -> str

  

   Converts a subset of an array of 8-bit unsigned integers to its equivalent string representation 

    that is encoded with base-64 digits. Parameters specify the subset as an offset in the input 

    array,the number of elements in the array to convert,and whether to insert line breaks in the 

    return value.

  

  

   inArray: An array of 8-bit unsigned integers.

   offset: An offset in inArray.

   length: The number of elements of inArray to convert.

   options: System.Base64FormattingOptions.InsertLineBreaks to insert a line break every 76 characters,or 

    System.Base64FormattingOptions.None to not insert line breaks.

  

   Returns: The string representation in base 64 of length elements of inArray,starting at position offset.

  ToBase64String(inArray: Array[Byte]) -> str

  

   Converts an array of 8-bit unsigned integers to its equivalent string representation that is 

    encoded with base-64 digits.

  

  

   inArray: An array of 8-bit unsigned integers.

   Returns: The string representation,in base 64,of the contents of inArray.

  ToBase64String(inArray: Array[Byte],options: Base64FormattingOptions) -> str

  

   Converts an array of 8-bit unsigned integers to its equivalent string representation that is 

    encoded with base-64 digits. A parameter specifies whether to insert line breaks in the return 

    value.

  

  

   inArray: An array of 8-bit unsigned integers.

   options: System.Base64FormattingOptions.InsertLineBreaks to insert a line break every 76 characters,or 

    System.Base64FormattingOptions.None to not insert line breaks.

  

   Returns: The string representation in base 64 of the elements in inArray.
  """
  pass
 @staticmethod
 def ToBoolean(value,provider=None):
  """
  ToBoolean(value: UInt64) -> bool

  

   Converts the value of the specified 64-bit unsigned integer to an equivalent Boolean value.

  

   value: The 64-bit unsigned integer to convert.

   Returns: true if value is not zero; otherwise,false.

  ToBoolean(value: str) -> bool

  

   Converts the specified string representation of a logical value to its Boolean equivalent.

  

   value: A string that contains the value of either System.Boolean.TrueString or 

    System.Boolean.FalseString.

  

   Returns: true if value equals System.Boolean.TrueString,or false if value equals 

    System.Boolean.FalseString or null.

  

  ToBoolean(value: UInt32) -> bool

  

   Converts the value of the specified 32-bit unsigned integer to an equivalent Boolean value.

  

   value: The 32-bit unsigned integer to convert.

   Returns: true if value is not zero; otherwise,false.

  ToBoolean(value: Int64) -> bool

  

   Converts the value of the specified 64-bit signed integer to an equivalent Boolean value.

  

   value: The 64-bit signed integer to convert.

   Returns: true if value is not zero; otherwise,false.

  ToBoolean(value: str,provider: IFormatProvider) -> bool

  

   Converts the specified string representation of a logical value to its Boolean equivalent,using 

    the specified culture-specific formatting information.

  

  

   value: A string that contains the value of either System.Boolean.TrueString or 

    System.Boolean.FalseString.

  

   provider: An object that supplies culture-specific formatting information. This parameter is ignored.

   Returns: true if value equals System.Boolean.TrueString,or false if value equals 

    System.Boolean.FalseString or null.

  

  ToBoolean(value: Decimal) -> bool

  

   Converts the value of the specified decimal number to an equivalent Boolean value.

  

   value: The number to convert.

   Returns: true if value is not zero; otherwise,false.

  ToBoolean(value: DateTime) -> bool

  

   Calling this method always throws System.InvalidCastException.

  

   value: The date and time value to convert.

   Returns: This conversion is not supported. No value is returned.

  ToBoolean(value: Single) -> bool

  

   Converts the value of the specified single-precision floating-point number to an equivalent 

    Boolean value.

  

  

   value: The single-precision floating-point number to convert.

   Returns: true if value is not zero; otherwise,false.

  ToBoolean(value: float) -> bool

  

   Converts the value of the specified double-precision floating-point number to an equivalent 

    Boolean value.

  

  

   value: The double-precision floating-point number to convert.

   Returns: true if value is not zero; otherwise,false.

  ToBoolean(value: bool) -> bool

  

   Returns the specified Boolean value; no actual conversion is performed.

  

   value: The Boolean value to return.

   Returns: value is returned unchanged.

  ToBoolean(value: SByte) -> bool

  

   Converts the value of the specified 8-bit signed integer to an equivalent Boolean value.

  

   value: The 8-bit signed integer to convert.

   Returns: true if value is not zero; otherwise,false.

  ToBoolean(value: object) -> bool

  

   Converts the value of a specified object to an equivalent Boolean value.

  

   value: An object that implements the System.IConvertible interface,or null.

   Returns: true or false,which reflects the value returned by invoking the 

    System.IConvertible.ToBoolean(System.IFormatProvider) method for the underlying type of value. 

    If value is null,the method returns false.

  

  ToBoolean(value: object,provider: IFormatProvider) -> bool

  

   Converts the value of the specified object to an equivalent Boolean value,using the specified 

    culture-specific formatting information.

  

  

   value: An object that implements the System.IConvertible interface,or null.

   provider: An object that supplies culture-specific formatting information.

   Returns: true or false,which reflects the value returned by invoking the 

    System.IConvertible.ToBoolean(System.IFormatProvider) method for the underlying type of value. 

    If value is null,the method returns false.

  

  ToBoolean(value: Char) -> bool

  

   Calling this method always throws System.InvalidCastException.

  

   value: The Unicode character to convert.

   Returns: This conversion is not supported. No value is returned.

  ToBoolean(value: UInt16) -> bool

  

   Converts the value of the specified 16-bit unsigned integer to an equivalent Boolean value.

  

   value: The 16-bit unsigned integer to convert.

   Returns: true if value is not zero; otherwise,false.

  ToBoolean(value: int) -> bool

  

   Converts the value of the specified 32-bit signed integer to an equivalent Boolean value.

  

   value: The 32-bit signed integer to convert.

   Returns: true if value is not zero; otherwise,false.

  ToBoolean(value: Byte) -> bool

  

   Converts the value of the specified 8-bit unsigned integer to an equivalent Boolean value.

  

   value: The 8-bit unsigned integer to convert.

   Returns: true if value is not zero; otherwise,false.

  ToBoolean(value: Int16) -> bool

  

   Converts the value of the specified 16-bit signed integer to an equivalent Boolean value.

  

   value: The 16-bit signed integer to convert.

   Returns: true if value is not zero; otherwise,false.
  """
  pass
 @staticmethod
 def ToByte(value,*__args):
  """
  ToByte(value: Single) -> Byte

  

   Converts the value of the specified single-precision floating-point number to an equivalent 

    8-bit unsigned integer.

  

  

   value: A single-precision floating-point number.

   Returns: value,rounded to the nearest 8-bit unsigned integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToByte(value: float) -> Byte

  

   Converts the value of the specified double-precision floating-point number to an equivalent 

    8-bit unsigned integer.

  

  

   value: The double-precision floating-point number to convert.

   Returns: value,rounded to the nearest 8-bit unsigned integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToByte(value: Int64) -> Byte

  

   Converts the value of the specified 64-bit signed integer to an equivalent 8-bit unsigned 

    integer.

  

  

   value: The 64-bit signed integer to convert.

   Returns: An 8-bit unsigned integer that is equivalent to value.

  ToByte(value: UInt64) -> Byte

  

   Converts the value of the specified 64-bit unsigned integer to an equivalent 8-bit unsigned 

    integer.

  

  

   value: The 64-bit unsigned integer to convert.

   Returns: An 8-bit unsigned integer that is equivalent to value.

  ToByte(value: Decimal) -> Byte

  

   Converts the value of the specified decimal number to an equivalent 8-bit unsigned integer.

  

   value: The number to convert.

   Returns: value,rounded to the nearest 8-bit unsigned integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToByte(value: DateTime) -> Byte

  

   Calling this method always throws System.InvalidCastException.

  

   value: The date and time value to convert.

   Returns: This conversion is not supported. No value is returned.

  ToByte(value: str,fromBase: int) -> Byte

  

   Converts the string representation of a number in a specified base to an equivalent 8-bit 

    unsigned integer.

  

  

   value: A string that contains the number to convert.

   fromBase: The base of the number in value,which must be 2,8,10,or 16.

   Returns: An 8-bit unsigned integer that is equivalent to the number in value,or 0 (zero) if value is 

    null.

  

  ToByte(value: str) -> Byte

  

   Converts the specified string representation of a number to an equivalent 8-bit unsigned integer.

  

   value: A string that contains the number to convert.

   Returns: An 8-bit unsigned integer that is equivalent to value,or zero if value is null.

  ToByte(value: str,provider: IFormatProvider) -> Byte

  

   Converts the specified string representation of a number to an equivalent 8-bit unsigned 

    integer,using specified culture-specific formatting information.

  

  

   value: A string that contains the number to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: An 8-bit unsigned integer that is equivalent to value,or zero if value is null.

  ToByte(value: UInt32) -> Byte

  

   Converts the value of the specified 32-bit unsigned integer to an equivalent 8-bit unsigned 

    integer.

  

  

   value: The 32-bit unsigned integer to convert.

   Returns: An 8-bit unsigned integer that is equivalent to value.

  ToByte(value: bool) -> Byte

  

   Converts the specified Boolean value to the equivalent 8-bit unsigned integer.

  

   value: The Boolean value to convert.

   Returns: The number 1 if value is true; otherwise,0.

  ToByte(value: Byte) -> Byte

  

   Returns the specified 8-bit unsigned integer; no actual conversion is performed.

  

   value: The 8-bit unsigned integer to return.

   Returns: value is returned unchanged.

  ToByte(value: object) -> Byte

  

   Converts the value of the specified object to an 8-bit unsigned integer.

  

   value: An object that implements the System.IConvertible interface,or null.

   Returns: An 8-bit unsigned integer that is equivalent to value,or zero if value is null.

  ToByte(value: object,provider: IFormatProvider) -> Byte

  

   Converts the value of the specified object to an 8-bit unsigned integer,using the specified 

    culture-specific formatting information.

  

  

   value: An object that implements the System.IConvertible interface.

   provider: An object that supplies culture-specific formatting information.

   Returns: An 8-bit unsigned integer that is equivalent to value,or zero if value is null.

  ToByte(value: Char) -> Byte

  

   Converts the value of the specified Unicode character to the equivalent 8-bit unsigned integer.

  

   value: The Unicode character to convert.

   Returns: An 8-bit unsigned integer that is equivalent to value.

  ToByte(value: UInt16) -> Byte

  

   Converts the value of the specified 16-bit unsigned integer to an equivalent 8-bit unsigned 

    integer.

  

  

   value: The 16-bit unsigned integer to convert.

   Returns: An 8-bit unsigned integer that is equivalent to value.

  ToByte(value: int) -> Byte

  

   Converts the value of the specified 32-bit signed integer to an equivalent 8-bit unsigned 

    integer.

  

  

   value: The 32-bit signed integer to convert.

   Returns: An 8-bit unsigned integer that is equivalent to value.

  ToByte(value: SByte) -> Byte

  

   Converts the value of the specified 8-bit signed integer to an equivalent 8-bit unsigned integer.

  

   value: The 8-bit signed integer to be converted.

   Returns: An 8-bit unsigned integer that is equivalent to value.

  ToByte(value: Int16) -> Byte

  

   Converts the value of the specified 16-bit signed integer to an equivalent 8-bit unsigned 

    integer.

  

  

   value: The 16-bit signed integer to convert.

   Returns: An 8-bit unsigned integer that is equivalent to value.
  """
  pass
 @staticmethod
 def ToChar(value,provider=None):
  """
  ToChar(value: UInt64) -> Char

  

   Converts the value of the specified 64-bit unsigned integer to its equivalent Unicode character.

  

   value: The 64-bit unsigned integer to convert.

   Returns: A Unicode character that is equivalent to value.

  ToChar(value: str) -> Char

  

   Converts the first character of a specified string to a Unicode character.

  

   value: A string of length 1.

   Returns: A Unicode character that is equivalent to the first and only character in value.

  ToChar(value: UInt32) -> Char

  

   Converts the value of the specified 32-bit unsigned integer to its equivalent Unicode character.

  

   value: The 32-bit unsigned integer to convert.

   Returns: A Unicode character that is equivalent to value.

  ToChar(value: Int64) -> Char

  

   Converts the value of the specified 64-bit signed integer to its equivalent Unicode character.

  

   value: The 64-bit signed integer to convert.

   Returns: A Unicode character that is equivalent to value.

  ToChar(value: str,provider: IFormatProvider) -> Char

  

   Converts the first character of a specified string to a Unicode character,using specified 

    culture-specific formatting information.

  

  

   value: A string of length 1 or null.

   provider: An object that supplies culture-specific formatting information. This parameter is ignored.

   Returns: A Unicode character that is equivalent to the first and only character in value.

  ToChar(value: Decimal) -> Char

  

   Calling this method always throws System.InvalidCastException.

  

   value: The decimal number to convert.

   Returns: This conversion is not supported. No value is returned.

  ToChar(value: DateTime) -> Char

  

   Calling this method always throws System.InvalidCastException.

  

   value: The date and time value to convert.

   Returns: This conversion is not supported. No value is returned.

  ToChar(value: Single) -> Char

  

   Calling this method always throws System.InvalidCastException.

  

   value: The single-precision floating-point number to convert.

   Returns: This conversion is not supported. No value is returned.

  ToChar(value: float) -> Char

  

   Calling this method always throws System.InvalidCastException.

  

   value: The double-precision floating-point number to convert.

   Returns: This conversion is not supported. No value is returned.

  ToChar(value: bool) -> Char

  

   Calling this method always throws System.InvalidCastException.

  

   value: The Boolean value to convert.

   Returns: This conversion is not supported. No value is returned.

  ToChar(value: Char) -> Char

  

   Returns the specified Unicode character value; no actual conversion is performed.

  

   value: The Unicode character to return.

   Returns: value is returned unchanged.

  ToChar(value: object) -> Char

  

   Converts the value of the specified object to a Unicode character.

  

   value: An object that implements the System.IConvertible interface.

   Returns: A Unicode character that is equivalent to value,or System.Char.MinValue if value is null.

  ToChar(value: object,provider: IFormatProvider) -> Char

  

   Converts the value of the specified object to its equivalent Unicode character,using the 

    specified culture-specific formatting information.

  

  

   value: An object that implements the System.IConvertible interface.

   provider: An object that supplies culture-specific formatting information.

   Returns: A Unicode character that is equivalent to value,or System.Char.MinValue if value is null.

  ToChar(value: SByte) -> Char

  

   Converts the value of the specified 8-bit signed integer to its equivalent Unicode character.

  

   value: The 8-bit signed integer to convert.

   Returns: A Unicode character that is equivalent to value.

  ToChar(value: UInt16) -> Char

  

   Converts the value of the specified 16-bit unsigned integer to its equivalent Unicode character.

  

   value: The 16-bit unsigned integer to convert.

   Returns: A Unicode character that is equivalent to value.

  ToChar(value: int) -> Char

  

   Converts the value of the specified 32-bit signed integer to its equivalent Unicode character.

  

   value: The 32-bit signed integer to convert.

   Returns: A Unicode character that is equivalent to value.

  ToChar(value: Byte) -> Char

  

   Converts the value of the specified 8-bit unsigned integer to its equivalent Unicode character.

  

   value: The 8-bit unsigned integer to convert.

   Returns: A Unicode character that is equivalent to value.

  ToChar(value: Int16) -> Char

  

   Converts the value of the specified 16-bit signed integer to its equivalent Unicode character.

  

   value: The 16-bit signed integer to convert.

   Returns: A Unicode character that is equivalent to value.
  """
  pass
 @staticmethod
 def ToDateTime(value,provider=None):
  """
  ToDateTime(value: Int64) -> DateTime

  

   Calling this method always throws System.InvalidCastException.

  

   value: The 64-bit signed integer to convert.

   Returns: This conversion is not supported. No value is returned.

  ToDateTime(value: UInt64) -> DateTime

  

   Calling this method always throws System.InvalidCastException.

  

   value: The 64-bit unsigned integer to convert.

   Returns: This conversion is not supported. No value is returned.

  ToDateTime(value: int) -> DateTime

  

   Calling this method always throws System.InvalidCastException.

  

   value: The 32-bit signed integer to convert.

   Returns: This conversion is not supported. No value is returned.

  ToDateTime(value: UInt32) -> DateTime

  

   Calling this method always throws System.InvalidCastException.

  

   value: The 32-bit unsigned integer to convert.

   Returns: This conversion is not supported. No value is returned.

  ToDateTime(value: bool) -> DateTime

  

   Calling this method always throws System.InvalidCastException.

  

   value: The Boolean value to convert.

   Returns: This conversion is not supported. No value is returned.

  ToDateTime(value: float) -> DateTime

  

   Calling this method always throws System.InvalidCastException.

  

   value: The double-precision floating-point value to convert.

   Returns: This conversion is not supported. No value is returned.

  ToDateTime(value: Decimal) -> DateTime

  

   Calling this method always throws System.InvalidCastException.

  

   value: The number to convert.

   Returns: This conversion is not supported. No value is returned.

  ToDateTime(value: Char) -> DateTime

  

   Calling this method always throws System.InvalidCastException.

  

   value: The Unicode character to convert.

   Returns: This conversion is not supported. No value is returned.

  ToDateTime(value: Single) -> DateTime

  

   Calling this method always throws System.InvalidCastException.

  

   value: The single-precision floating-point value to convert.

   Returns: This conversion is not supported. No value is returned.

  ToDateTime(value: object,provider: IFormatProvider) -> DateTime

  

   Converts the value of the specified object to a System.DateTime object,using the specified 

    culture-specific formatting information.

  

  

   value: An object that implements the System.IConvertible interface.

   provider: An object that supplies culture-specific formatting information.

   Returns: The date and time equivalent of the value of value,or the date and time equivalent of 

    System.DateTime.MinValue if value is null.

  

  ToDateTime(value: str) -> DateTime

  

   Converts the specified string representation of a date and time to an equivalent date and time 

    value.

  

  

   value: The string representation of a date and time.

   Returns: The date and time equivalent of the value of value,or the date and time equivalent of 

    System.DateTime.MinValue if value is null.

  

  ToDateTime(value: DateTime) -> DateTime

  

   Returns the specified System.DateTime object; no actual conversion is performed.

  

   value: A date and time value.

   Returns: value is returned unchanged.

  ToDateTime(value: object) -> DateTime

  

   Converts the value of the specified object to a System.DateTime object.

  

   value: An object that implements the System.IConvertible interface,or null.

   Returns: The date and time equivalent of the value of value,or a date and time equivalent of 

    System.DateTime.MinValue if value is null.

  

  ToDateTime(value: str,provider: IFormatProvider) -> DateTime

  

   Converts the specified string representation of a number to an equivalent date and time,using 

    the specified culture-specific formatting information.

  

  

   value: A string that contains a date and time to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: The date and time equivalent of the value of value,or the date and time equivalent of 

    System.DateTime.MinValue if value is null.

  

  ToDateTime(value: Int16) -> DateTime

  

   Calling this method always throws System.InvalidCastException.

  

   value: The 16-bit signed integer to convert.

   Returns: This conversion is not supported. No value is returned.

  ToDateTime(value: UInt16) -> DateTime

  

   Calling this method always throws System.InvalidCastException.

  

   value: The 16-bit unsigned integer to convert.

   Returns: This conversion is not supported. No value is returned.

  ToDateTime(value: SByte) -> DateTime

  

   Calling this method always throws System.InvalidCastException.

  

   value: The 8-bit signed integer to convert.

   Returns: This conversion is not supported. No value is returned.

  ToDateTime(value: Byte) -> DateTime

  

   Calling this method always throws System.InvalidCastException.

  

   value: The 8-bit unsigned integer to convert.

   Returns: This conversion is not supported. No value is returned.
  """
  pass
 @staticmethod
 def ToDecimal(value,provider=None):
  """
  ToDecimal(value: Single) -> Decimal

  

   Converts the value of the specified single-precision floating-point number to the equivalent 

    decimal number.

  

  

   value: The single-precision floating-point number to convert.

   Returns: A decimal number that is equivalent to value.

  ToDecimal(value: float) -> Decimal

  

   Converts the value of the specified double-precision floating-point number to an equivalent 

    decimal number.

  

  

   value: The double-precision floating-point number to convert.

   Returns: A decimal number that is equivalent to value.

  ToDecimal(value: Int64) -> Decimal

  

   Converts the value of the specified 64-bit signed integer to an equivalent decimal number.

  

   value: The 64-bit signed integer to convert.

   Returns: A decimal number that is equivalent to value.

  ToDecimal(value: UInt64) -> Decimal

  

   Converts the value of the specified 64-bit unsigned integer to an equivalent decimal number.

  

   value: The 64-bit unsigned integer to convert.

   Returns: A decimal number that is equivalent to value.

  ToDecimal(value: str) -> Decimal

  

   Converts the specified string representation of a number to an equivalent decimal number.

  

   value: A string that contains a number to convert.

   Returns: A decimal number that is equivalent to the number in value,or 0 (zero) if value is null.

  ToDecimal(value: bool) -> Decimal

  

   Converts the specified Boolean value to the equivalent decimal number.

  

   value: The Boolean value to convert.

   Returns: The number 1 if value is true; otherwise,0.

  ToDecimal(value: DateTime) -> Decimal

  

   Calling this method always throws System.InvalidCastException.

  

   value: The date and time value to convert.

   Returns: This conversion is not supported. No value is returned.

  ToDecimal(value: str,provider: IFormatProvider) -> Decimal

  

   Converts the specified string representation of a number to an equivalent decimal number,using 

    the specified culture-specific formatting information.

  

  

   value: A string that contains a number to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: A decimal number that is equivalent to the number in value,or 0 (zero) if value is null.

  ToDecimal(value: Decimal) -> Decimal

  

   Returns the specified decimal number; no actual conversion is performed.

  

   value: A decimal number.

   Returns: value is returned unchanged.

  ToDecimal(value: SByte) -> Decimal

  

   Converts the value of the specified 8-bit signed integer to the equivalent decimal number.

  

   value: The 8-bit signed integer to convert.

   Returns: A decimal number that is equivalent to value.

  ToDecimal(value: Byte) -> Decimal

  

   Converts the value of the specified 8-bit unsigned integer to the equivalent decimal number.

  

   value: The 8-bit unsigned integer to convert.

   Returns: The decimal number that is equivalent to value.

  ToDecimal(value: object) -> Decimal

  

   Converts the value of the specified object to an equivalent decimal number.

  

   value: An object that implements the System.IConvertible interface,or null.

   Returns: A decimal number that is equivalent to value,or 0 (zero) if value is null.

  ToDecimal(value: object,provider: IFormatProvider) -> Decimal

  

   Converts the value of the specified object to an equivalent decimal number,using the specified 

    culture-specific formatting information.

  

  

   value: An object that implements the System.IConvertible interface.

   provider: An object that supplies culture-specific formatting information.

   Returns: A decimal number that is equivalent to value,or 0 (zero) if value is null.

  ToDecimal(value: Char) -> Decimal

  

   Calling this method always throws System.InvalidCastException.

  

   value: The Unicode character to convert.

   Returns: This conversion is not supported. No value is returned.

  ToDecimal(value: int) -> Decimal

  

   Converts the value of the specified 32-bit signed integer to an equivalent decimal number.

  

   value: The 32-bit signed integer to convert.

   Returns: A decimal number that is equivalent to value.

  ToDecimal(value: UInt32) -> Decimal

  

   Converts the value of the specified 32-bit unsigned integer to an equivalent decimal number.

  

   value: The 32-bit unsigned integer to convert.

   Returns: A decimal number that is equivalent to value.

  ToDecimal(value: Int16) -> Decimal

  

   Converts the value of the specified 16-bit signed integer to an equivalent decimal number.

  

   value: The 16-bit signed integer to convert.

   Returns: A decimal number that is equivalent to value.

  ToDecimal(value: UInt16) -> Decimal

  

   Converts the value of the specified 16-bit unsigned integer to an equivalent decimal number.

  

   value: The 16-bit unsigned integer to convert.

   Returns: The decimal number that is equivalent to value.
  """
  pass
 @staticmethod
 def ToDouble(value,provider=None):
  """
  ToDouble(value: Single) -> float

  

   Converts the value of the specified single-precision floating-point number to an equivalent 

    double-precision floating-point number.

  

  

   value: The single-precision floating-point number.

   Returns: A double-precision floating-point number that is equivalent to value.

  ToDouble(value: float) -> float

  

   Returns the specified double-precision floating-point number; no actual conversion is performed.

  

   value: The double-precision floating-point number to return.

   Returns: value is returned unchanged.

  ToDouble(value: Int64) -> float

  

   Converts the value of the specified 64-bit signed integer to an equivalent double-precision 

    floating-point number.

  

  

   value: The 64-bit signed integer to convert.

   Returns: A double-precision floating-point number that is equivalent to value.

  ToDouble(value: UInt64) -> float

  

   Converts the value of the specified 64-bit unsigned integer to an equivalent double-precision 

    floating-point number.

  

  

   value: The 64-bit unsigned integer to convert.

   Returns: A double-precision floating-point number that is equivalent to value.

  ToDouble(value: Decimal) -> float

  

   Converts the value of the specified decimal number to an equivalent double-precision 

    floating-point number.

  

  

   value: The decimal number to convert.

   Returns: A double-precision floating-point number that is equivalent to value.

  ToDouble(value: bool) -> float

  

   Converts the specified Boolean value to the equivalent double-precision floating-point number.

  

   value: The Boolean value to convert.

   Returns: The number 1 if value is true; otherwise,0.

  ToDouble(value: DateTime) -> float

  

   Calling this method always throws System.InvalidCastException.

  

   value: The date and time value to convert.

   Returns: This conversion is not supported. No value is returned.

  ToDouble(value: str) -> float

  

   Converts the specified string representation of a number to an equivalent double-precision 

    floating-point number.

  

  

   value: A string that contains the number to convert.

   Returns: A double-precision floating-point number that is equivalent to the number in value,or 0 (zero) 

    if value is null.

  

  ToDouble(value: str,provider: IFormatProvider) -> float

  

   Converts the specified string representation of a number to an equivalent double-precision 

    floating-point number,using the specified culture-specific formatting information.

  

  

   value: A string that contains the number to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: A double-precision floating-point number that is equivalent to the number in value,or 0 (zero) 

    if value is null.

  

  ToDouble(value: SByte) -> float

  

   Converts the value of the specified 8-bit signed integer to the equivalent double-precision 

    floating-point number.

  

  

   value: The 8-bit signed integer to convert.

   Returns: The 8-bit signed integer that is equivalent to value.

  ToDouble(value: Byte) -> float

  

   Converts the value of the specified 8-bit unsigned integer to the equivalent double-precision 

    floating-point number.

  

  

   value: The 8-bit unsigned integer to convert.

   Returns: The double-precision floating-point number that is equivalent to value.

  ToDouble(value: object) -> float

  

   Converts the value of the specified object to a double-precision floating-point number.

  

   value: An object that implements the System.IConvertible interface,or null.

   Returns: A double-precision floating-point number that is equivalent to value,or zero if value is null.

  ToDouble(value: object,provider: IFormatProvider) -> float

  

   Converts the value of the specified object to an double-precision floating-point number,using 

    the specified culture-specific formatting information.

  

  

   value: An object that implements the System.IConvertible interface.

   provider: An object that supplies culture-specific formatting information.

   Returns: A double-precision floating-point number that is equivalent to value,or zero if value is null.

  ToDouble(value: Int16) -> float

  

   Converts the value of the specified 16-bit signed integer to an equivalent double-precision 

    floating-point number.

  

  

   value: The 16-bit signed integer to convert.

   Returns: A double-precision floating-point number equivalent to value.

  ToDouble(value: int) -> float

  

   Converts the value of the specified 32-bit signed integer to an equivalent double-precision 

    floating-point number.

  

  

   value: The 32-bit signed integer to convert.

   Returns: A double-precision floating-point number that is equivalent to value.

  ToDouble(value: UInt32) -> float

  

   Converts the value of the specified 32-bit unsigned integer to an equivalent double-precision 

    floating-point number.

  

  

   value: The 32-bit unsigned integer to convert.

   Returns: A double-precision floating-point number that is equivalent to value.

  ToDouble(value: Char) -> float

  

   Calling this method always throws System.InvalidCastException.

  

   value: The Unicode character to convert.

   Returns: This conversion is not supported. No value is returned.

  ToDouble(value: UInt16) -> float

  

   Converts the value of the specified 16-bit unsigned integer to the equivalent double-precision 

    floating-point number.

  

  

   value: The 16-bit unsigned integer to convert.

   Returns: A double-precision floating-point number that is equivalent to value.
  """
  pass
 @staticmethod
 def ToInt16(value,*__args):
  """
  ToInt16(value: Single) -> Int16

  

   Converts the value of the specified single-precision floating-point number to an equivalent 

    16-bit signed integer.

  

  

   value: The single-precision floating-point number to convert.

   Returns: value,rounded to the nearest 16-bit signed integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToInt16(value: float) -> Int16

  

   Converts the value of the specified double-precision floating-point number to an equivalent 

    16-bit signed integer.

  

  

   value: The double-precision floating-point number to convert.

   Returns: value,rounded to the nearest 16-bit signed integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToInt16(value: Int64) -> Int16

  

   Converts the value of the specified 64-bit signed integer to an equivalent 16-bit signed integer.

  

   value: The 64-bit signed integer to convert.

   Returns: A 16-bit signed integer that is equivalent to value.

  ToInt16(value: UInt64) -> Int16

  

   Converts the value of the specified 64-bit unsigned integer to an equivalent 16-bit signed 

    integer.

  

  

   value: The 64-bit unsigned integer to convert.

   Returns: A 16-bit signed integer that is equivalent to value.

  ToInt16(value: Decimal) -> Int16

  

   Converts the value of the specified decimal number to an equivalent 16-bit signed integer.

  

   value: The decimal number to convert.

   Returns: value,rounded to the nearest 16-bit signed integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToInt16(value: DateTime) -> Int16

  

   Calling this method always throws System.InvalidCastException.

  

   value: The date and time value to convert.

   Returns: This conversion is not supported. No value is returned.

  ToInt16(value: str,fromBase: int) -> Int16

  

   Converts the string representation of a number in a specified base to an equivalent 16-bit 

    signed integer.

  

  

   value: A string that contains the number to convert.

   fromBase: The base of the number in value,which must be 2,8,10,or 16.

   Returns: A 16-bit signed integer that is equivalent to the number in value,or 0 (zero) if value is null.

  ToInt16(value: str) -> Int16

  

   Converts the specified string representation of a number to an equivalent 16-bit signed integer.

  

   value: A string that contains the number to convert.

   Returns: A 16-bit signed integer that is equivalent to the number in value,or 0 (zero) if value is null.

  ToInt16(value: str,provider: IFormatProvider) -> Int16

  

   Converts the specified string representation of a number to an equivalent 16-bit signed integer,

    using the specified culture-specific formatting information.

  

  

   value: A string that contains the number to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: A 16-bit signed integer that is equivalent to the number in value,or 0 (zero) if value is null.

  ToInt16(value: Int16) -> Int16

  

   Returns the specified 16-bit signed integer; no actual conversion is performed.

  

   value: The 16-bit signed integer to return.

   Returns: value is returned unchanged.

  ToInt16(value: bool) -> Int16

  

   Converts the specified Boolean value to the equivalent 16-bit signed integer.

  

   value: The Boolean value to convert.

   Returns: The number 1 if value is true; otherwise,0.

  ToInt16(value: Char) -> Int16

  

   Converts the value of the specified Unicode character to the equivalent 16-bit signed integer.

  

   value: The Unicode character to convert.

   Returns: A 16-bit signed integer that is equivalent to value.

  ToInt16(value: object) -> Int16

  

   Converts the value of the specified object to a 16-bit signed integer.

  

   value: An object that implements the System.IConvertible interface,or null.

   Returns: A 16-bit signed integer that is equivalent to value,or zero if value is null.

  ToInt16(value: object,provider: IFormatProvider) -> Int16

  

   Converts the value of the specified object to a 16-bit signed integer,using the specified 

    culture-specific formatting information.

  

  

   value: An object that implements the System.IConvertible interface.

   provider: An object that supplies culture-specific formatting information.

   Returns: A 16-bit signed integer that is equivalent to value,or zero if value is null.

  ToInt16(value: SByte) -> Int16

  

   Converts the value of the specified 8-bit signed integer to the equivalent 16-bit signed integer.

  

   value: The 8-bit signed integer to convert.

   Returns: A 8-bit signed integer that is equivalent to value.

  ToInt16(value: int) -> Int16

  

   Converts the value of the specified 32-bit signed integer to an equivalent 16-bit signed integer.

  

   value: The 32-bit signed integer to convert.

   Returns: The 16-bit signed integer equivalent of value.

  ToInt16(value: UInt32) -> Int16

  

   Converts the value of the specified 32-bit unsigned integer to an equivalent 16-bit signed 

    integer.

  

  

   value: The 32-bit unsigned integer to convert.

   Returns: A 16-bit signed integer that is equivalent to value.

  ToInt16(value: Byte) -> Int16

  

   Converts the value of the specified 8-bit unsigned integer to the equivalent 16-bit signed 

    integer.

  

  

   value: The 8-bit unsigned integer to convert.

   Returns: A 16-bit signed integer that is equivalent to value.

  ToInt16(value: UInt16) -> Int16

  

   Converts the value of the specified 16-bit unsigned integer to the equivalent 16-bit signed 

    integer.

  

  

   value: The 16-bit unsigned integer to convert.

   Returns: A 16-bit signed integer that is equivalent to value.
  """
  pass
 @staticmethod
 def ToInt32(value,*__args):
  """
  ToInt32(value: Single) -> int

  

   Converts the value of the specified single-precision floating-point number to an equivalent 

    32-bit signed integer.

  

  

   value: The single-precision floating-point number to convert.

   Returns: value,rounded to the nearest 32-bit signed integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToInt32(value: float) -> int

  

   Converts the value of the specified double-precision floating-point number to an equivalent 

    32-bit signed integer.

  

  

   value: The double-precision floating-point number to convert.

   Returns: value,rounded to the nearest 32-bit signed integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToInt32(value: Int64) -> int

  

   Converts the value of the specified 64-bit signed integer to an equivalent 32-bit signed integer.

  

   value: The 64-bit signed integer to convert.

   Returns: A 32-bit signed integer that is equivalent to value.

  ToInt32(value: UInt64) -> int

  

   Converts the value of the specified 64-bit unsigned integer to an equivalent 32-bit signed 

    integer.

  

  

   value: The 64-bit unsigned integer to convert.

   Returns: A 32-bit signed integer that is equivalent to value.

  ToInt32(value: Decimal) -> int

  

   Converts the value of the specified decimal number to an equivalent 32-bit signed integer.

  

   value: The decimal number to convert.

   Returns: value,rounded to the nearest 32-bit signed integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToInt32(value: DateTime) -> int

  

   Calling this method always throws System.InvalidCastException.

  

   value: The date and time value to convert.

   Returns: This conversion is not supported. No value is returned.

  ToInt32(value: str,fromBase: int) -> int

  

   Converts the string representation of a number in a specified base to an equivalent 32-bit 

    signed integer.

  

  

   value: A string that contains the number to convert.

   fromBase: The base of the number in value,which must be 2,8,10,or 16.

   Returns: A 32-bit signed integer that is equivalent to the number in value,or 0 (zero) if value is null.

  ToInt32(value: str) -> int

  

   Converts the specified string representation of a number to an equivalent 32-bit signed integer.

  

   value: A string that contains the number to convert.

   Returns: A 32-bit signed integer that is equivalent to the number in value,or 0 (zero) if value is null.

  ToInt32(value: str,provider: IFormatProvider) -> int

  

   Converts the specified string representation of a number to an equivalent 32-bit signed integer,

    using the specified culture-specific formatting information.

  

  

   value: A string that contains the number to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: A 32-bit signed integer that is equivalent to the number in value,or 0 (zero) if value is null.

  ToInt32(value: int) -> int

  

   Returns the specified 32-bit signed integer; no actual conversion is performed.

  

   value: The 32-bit signed integer to return.

   Returns: value is returned unchanged.

  ToInt32(value: bool) -> int

  

   Converts the specified Boolean value to the equivalent 32-bit signed integer.

  

   value: The Boolean value to convert.

   Returns: The number 1 if value is true; otherwise,0.

  ToInt32(value: Char) -> int

  

   Converts the value of the specified Unicode character to the equivalent 32-bit signed integer.

  

   value: The Unicode character to convert.

   Returns: A 32-bit signed integer that is equivalent to value.

  ToInt32(value: object) -> int

  

   Converts the value of the specified object to a 32-bit signed integer.

  

   value: An object that implements the System.IConvertible interface,or null.

   Returns: A 32-bit signed integer equivalent to value,or zero if value is null.

  ToInt32(value: object,provider: IFormatProvider) -> int

  

   Converts the value of the specified object to a 32-bit signed integer,using the specified 

    culture-specific formatting information.

  

  

   value: An object that implements the System.IConvertible interface.

   provider: An object that supplies culture-specific formatting information.

   Returns: A 32-bit signed integer that is equivalent to value,or zero if value is null.

  ToInt32(value: SByte) -> int

  

   Converts the value of the specified 8-bit signed integer to the equivalent 32-bit signed integer.

  

   value: The 8-bit signed integer to convert.

   Returns: A 8-bit signed integer that is equivalent to value.

  ToInt32(value: UInt16) -> int

  

   Converts the value of the specified 16-bit unsigned integer to the equivalent 32-bit signed 

    integer.

  

  

   value: The 16-bit unsigned integer to convert.

   Returns: A 32-bit signed integer that is equivalent to value.

  ToInt32(value: UInt32) -> int

  

   Converts the value of the specified 32-bit unsigned integer to an equivalent 32-bit signed 

    integer.

  

  

   value: The 32-bit unsigned integer to convert.

   Returns: A 32-bit signed integer that is equivalent to value.

  ToInt32(value: Byte) -> int

  

   Converts the value of the specified 8-bit unsigned integer to the equivalent 32-bit signed 

    integer.

  

  

   value: The 8-bit unsigned integer to convert.

   Returns: A 32-bit signed integer that is equivalent to value.

  ToInt32(value: Int16) -> int

  

   Converts the value of the specified 16-bit signed integer to an equivalent 32-bit signed integer.

  

   value: The 16-bit signed integer to convert.

   Returns: A 32-bit signed integer that is equivalent to value.
  """
  pass
 @staticmethod
 def ToInt64(value,*__args):
  """
  ToInt64(value: Single) -> Int64

  

   Converts the value of the specified single-precision floating-point number to an equivalent 

    64-bit signed integer.

  

  

   value: The single-precision floating-point number to convert.

   Returns: value,rounded to the nearest 64-bit signed integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToInt64(value: float) -> Int64

  

   Converts the value of the specified double-precision floating-point number to an equivalent 

    64-bit signed integer.

  

  

   value: The double-precision floating-point number to convert.

   Returns: value,rounded to the nearest 64-bit signed integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToInt64(value: UInt64) -> Int64

  

   Converts the value of the specified 64-bit unsigned integer to an equivalent 64-bit signed 

    integer.

  

  

   value: The 64-bit unsigned integer to convert.

   Returns: A 64-bit signed integer that is equivalent to value.

  ToInt64(value: Int64) -> Int64

  

   Returns the specified 64-bit signed integer; no actual conversion is performed.

  

   value: A 64-bit signed integer.

   Returns: value is returned unchanged.

  ToInt64(value: Decimal) -> Int64

  

   Converts the value of the specified decimal number to an equivalent 64-bit signed integer.

  

   value: The decimal number to convert.

   Returns: value,rounded to the nearest 64-bit signed integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToInt64(value: DateTime) -> Int64

  

   Calling this method always throws System.InvalidCastException.

  

   value: The date and time value to convert.

   Returns: This conversion is not supported. No value is returned.

  ToInt64(value: str,fromBase: int) -> Int64

  

   Converts the string representation of a number in a specified base to an equivalent 64-bit 

    signed integer.

  

  

   value: A string that contains the number to convert.

   fromBase: The base of the number in value,which must be 2,8,10,or 16.

   Returns: A 64-bit signed integer that is equivalent to the number in value,or 0 (zero) if value is null.

  ToInt64(value: str) -> Int64

  

   Converts the specified string representation of a number to an equivalent 64-bit signed integer.

  

   value: A string that contains a number to convert.

   Returns: A 64-bit signed integer that is equivalent to the number in value,or 0 (zero) if value is null.

  ToInt64(value: str,provider: IFormatProvider) -> Int64

  

   Converts the specified string representation of a number to an equivalent 64-bit signed integer,

    using the specified culture-specific formatting information.

  

  

   value: A string that contains the number to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: A 64-bit signed integer that is equivalent to the number in value,or 0 (zero) if value is null.

  ToInt64(value: UInt32) -> Int64

  

   Converts the value of the specified 32-bit unsigned integer to an equivalent 64-bit signed 

    integer.

  

  

   value: The 32-bit unsigned integer to convert.

   Returns: A 64-bit signed integer that is equivalent to value.

  ToInt64(value: bool) -> Int64

  

   Converts the specified Boolean value to the equivalent 64-bit signed integer.

  

   value: The Boolean value to convert.

   Returns: The number 1 if value is true; otherwise,0.

  ToInt64(value: Char) -> Int64

  

   Converts the value of the specified Unicode character to the equivalent 64-bit signed integer.

  

   value: The Unicode character to convert.

   Returns: A 64-bit signed integer that is equivalent to value.

  ToInt64(value: object) -> Int64

  

   Converts the value of the specified object to a 64-bit signed integer.

  

   value: An object that implements the System.IConvertible interface,or null.

   Returns: A 64-bit signed integer that is equivalent to value,or zero if value is null.

  ToInt64(value: object,provider: IFormatProvider) -> Int64

  

   Converts the value of the specified object to a 64-bit signed integer,using the specified 

    culture-specific formatting information.

  

  

   value: An object that implements the System.IConvertible interface.

   provider: An object that supplies culture-specific formatting information.

   Returns: A 64-bit signed integer that is equivalent to value,or zero if value is null.

  ToInt64(value: SByte) -> Int64

  

   Converts the value of the specified 8-bit signed integer to the equivalent 64-bit signed integer.

  

   value: The 8-bit signed integer to convert.

   Returns: A 64-bit signed integer that is equivalent to value.

  ToInt64(value: UInt16) -> Int64

  

   Converts the value of the specified 16-bit unsigned integer to the equivalent 64-bit signed 

    integer.

  

  

   value: The 16-bit unsigned integer to convert.

   Returns: A 64-bit signed integer that is equivalent to value.

  ToInt64(value: int) -> Int64

  

   Converts the value of the specified 32-bit signed integer to an equivalent 64-bit signed integer.

  

   value: The 32-bit signed integer to convert.

   Returns: A 64-bit signed integer that is equivalent to value.

  ToInt64(value: Byte) -> Int64

  

   Converts the value of the specified 8-bit unsigned integer to the equivalent 64-bit signed 

    integer.

  

  

   value: The 8-bit unsigned integer to convert.

   Returns: A 64-bit signed integer that is equivalent to value.

  ToInt64(value: Int16) -> Int64

  

   Converts the value of the specified 16-bit signed integer to an equivalent 64-bit signed integer.

  

   value: The 16-bit signed integer to convert.

   Returns: A 64-bit signed integer that is equivalent to value.
  """
  pass
 @staticmethod
 def ToSByte(value,*__args):
  """
  ToSByte(value: Single) -> SByte

  

   Converts the value of the specified single-precision floating-point number to an equivalent 

    8-bit signed integer.

  

  

   value: The single-precision floating-point number to convert.

   Returns: value,rounded to the nearest 8-bit signed integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToSByte(value: float) -> SByte

  

   Converts the value of the specified double-precision floating-point number to an equivalent 

    8-bit signed integer.

  

  

   value: The double-precision floating-point number to convert.

   Returns: value,rounded to the nearest 8-bit signed integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToSByte(value: Int64) -> SByte

  

   Converts the value of the specified 64-bit signed integer to an equivalent 8-bit signed integer.

  

   value: The 64-bit signed integer to convert.

   Returns: An 8-bit signed integer that is equivalent to value.

  ToSByte(value: UInt64) -> SByte

  

   Converts the value of the specified 64-bit unsigned integer to an equivalent 8-bit signed 

    integer.

  

  

   value: The 64-bit unsigned integer to convert.

   Returns: An 8-bit signed integer that is equivalent to value.

  ToSByte(value: Decimal) -> SByte

  

   Converts the value of the specified decimal number to an equivalent 8-bit signed integer.

  

   value: The decimal number to convert.

   Returns: value,rounded to the nearest 8-bit signed integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToSByte(value: DateTime) -> SByte

  

   Calling this method always throws System.InvalidCastException.

  

   value: The date and time value to convert.

   Returns: This conversion is not supported. No value is returned.

  ToSByte(value: str,fromBase: int) -> SByte

  

   Converts the string representation of a number in a specified base to an equivalent 8-bit signed 

    integer.

  

  

   value: A string that contains the number to convert.

   fromBase: The base of the number in value,which must be 2,8,10,or 16.

   Returns: An 8-bit signed integer that is equivalent to the number in value,or 0 (zero) if value is null.

  ToSByte(value: str) -> SByte

  

   Converts the specified string representation of a number to an equivalent 8-bit signed integer.

  

   value: A string that contains the number to convert.

   Returns: An 8-bit signed integer that is equivalent to the number in value,or 0 (zero) if value is null.

  ToSByte(value: str,provider: IFormatProvider) -> SByte

  

   Converts the specified string representation of a number to an equivalent 8-bit signed integer,

    using the specified culture-specific formatting information.

  

  

   value: A string that contains the number to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: An 8-bit signed integer that is equivalent to value.

  ToSByte(value: UInt32) -> SByte

  

   Converts the value of the specified 32-bit unsigned integer to an equivalent 8-bit signed 

    integer.

  

  

   value: The 32-bit unsigned integer to convert.

   Returns: An 8-bit signed integer that is equivalent to value.

  ToSByte(value: bool) -> SByte

  

   Converts the specified Boolean value to the equivalent 8-bit signed integer.

  

   value: The Boolean value to convert.

   Returns: The number 1 if value is true; otherwise,0.

  ToSByte(value: SByte) -> SByte

  

   Returns the specified 8-bit signed integer; no actual conversion is performed.

  

   value: The 8-bit signed integer to return.

   Returns: value is returned unchanged.

  ToSByte(value: object) -> SByte

  

   Converts the value of the specified object to an 8-bit signed integer.

  

   value: An object that implements the System.IConvertible interface,or null.

   Returns: An 8-bit signed integer that is equivalent to value,or zero if value is null.

  ToSByte(value: object,provider: IFormatProvider) -> SByte

  

   Converts the value of the specified object to an 8-bit signed integer,using the specified 

    culture-specific formatting information.

  

  

   value: An object that implements the System.IConvertible interface.

   provider: An object that supplies culture-specific formatting information.

   Returns: An 8-bit signed integer that is equivalent to value,or zero if value is null.

  ToSByte(value: Char) -> SByte

  

   Converts the value of the specified Unicode character to the equivalent 8-bit signed integer.

  

   value: The Unicode character to convert.

   Returns: An 8-bit signed integer that is equivalent to value.

  ToSByte(value: UInt16) -> SByte

  

   Converts the value of the specified 16-bit unsigned integer to the equivalent 8-bit signed 

    integer.

  

  

   value: The 16-bit unsigned integer to convert.

   Returns: An 8-bit signed integer that is equivalent to value.

  ToSByte(value: int) -> SByte

  

   Converts the value of the specified 32-bit signed integer to an equivalent 8-bit signed integer.

  

   value: The 32-bit signed integer to convert.

   Returns: An 8-bit signed integer that is equivalent to value.

  ToSByte(value: Byte) -> SByte

  

   Converts the value of the specified 8-bit unsigned integer to the equivalent 8-bit signed 

    integer.

  

  

   value: The 8-bit unsigned integer to convert.

   Returns: An 8-bit signed integer that is equivalent to value.

  ToSByte(value: Int16) -> SByte

  

   Converts the value of the specified 16-bit signed integer to the equivalent 8-bit signed integer.

  

   value: The 16-bit signed integer to convert.

   Returns: An 8-bit signed integer that is equivalent to value.
  """
  pass
 @staticmethod
 def ToSingle(value,provider=None):
  """
  ToSingle(value: Single) -> Single

  

   Returns the specified single-precision floating-point number; no actual conversion is performed.

  

   value: The single-precision floating-point number to return.

   Returns: value is returned unchanged.

  ToSingle(value: float) -> Single

  

   Converts the value of the specified double-precision floating-point number to an equivalent 

    single-precision floating-point number.

  

  

   value: The double-precision floating-point number to convert.

   Returns: A single-precision floating-point number that is equivalent to value.value is rounded using 

    rounding to nearest. For example,when rounded to two decimals,the value 2.345 becomes 2.34 and 

    the value 2.355 becomes 2.36.

  

  ToSingle(value: Int64) -> Single

  

   Converts the value of the specified 64-bit signed integer to an equivalent single-precision 

    floating-point number.

  

  

   value: The 64-bit signed integer to convert.

   Returns: A single-precision floating-point number that is equivalent to value.

  ToSingle(value: UInt64) -> Single

  

   Converts the value of the specified 64-bit unsigned integer to an equivalent single-precision 

    floating-point number.

  

  

   value: The 64-bit unsigned integer to convert.

   Returns: A single-precision floating-point number that is equivalent to value.

  ToSingle(value: Decimal) -> Single

  

   Converts the value of the specified decimal number to an equivalent single-precision 

    floating-point number.

  

  

   value: The decimal number to convert.

   Returns: A single-precision floating-point number that is equivalent to value.value is rounded using 

    rounding to nearest. For example,when rounded to two decimals,the value 2.345 becomes 2.34 and 

    the value 2.355 becomes 2.36.

  

  ToSingle(value: bool) -> Single

  

   Converts the specified Boolean value to the equivalent single-precision floating-point number.

  

   value: The Boolean value to convert.

   Returns: The number 1 if value is true; otherwise,0.

  ToSingle(value: DateTime) -> Single

  

   Calling this method always throws System.InvalidCastException.

  

   value: The date and time value to convert.

   Returns: This conversion is not supported. No value is returned.

  ToSingle(value: str) -> Single

  

   Converts the specified string representation of a number to an equivalent single-precision 

    floating-point number.

  

  

   value: A string that contains the number to convert.

   Returns: A single-precision floating-point number that is equivalent to the number in value,or 0 (zero) 

    if value is null.

  

  ToSingle(value: str,provider: IFormatProvider) -> Single

  

   Converts the specified string representation of a number to an equivalent single-precision 

    floating-point number,using the specified culture-specific formatting information.

  

  

   value: A string that contains the number to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: A single-precision floating-point number that is equivalent to the number in value,or 0 (zero) 

    if value is null.

  

  ToSingle(value: SByte) -> Single

  

   Converts the value of the specified 8-bit signed integer to the equivalent single-precision 

    floating-point number.

  

  

   value: The 8-bit signed integer to convert.

   Returns: An 8-bit signed integer that is equivalent to value.

  ToSingle(value: Byte) -> Single

  

   Converts the value of the specified 8-bit unsigned integer to the equivalent single-precision 

    floating-point number.

  

  

   value: The 8-bit unsigned integer to convert.

   Returns: A single-precision floating-point number that is equivalent to value.

  ToSingle(value: object) -> Single

  

   Converts the value of the specified object to a single-precision floating-point number.

  

   value: An object that implements the System.IConvertible interface,or null.

   Returns: A single-precision floating-point number that is equivalent to value,or zero if value is null.

  ToSingle(value: object,provider: IFormatProvider) -> Single

  

   Converts the value of the specified object to an single-precision floating-point number,using 

    the specified culture-specific formatting information.

  

  

   value: An object that implements the System.IConvertible interface.

   provider: An object that supplies culture-specific formatting information.

   Returns: A single-precision floating-point number that is equivalent to value,or zero if value is null.

  ToSingle(value: Char) -> Single

  

   Calling this method always throws System.InvalidCastException.

  

   value: The Unicode character to convert.

   Returns: This conversion is not supported. No value is returned.

  ToSingle(value: int) -> Single

  

   Converts the value of the specified 32-bit signed integer to an equivalent single-precision 

    floating-point number.

  

  

   value: The 32-bit signed integer to convert.

   Returns: A single-precision floating-point number that is equivalent to value.

  ToSingle(value: UInt32) -> Single

  

   Converts the value of the specified 32-bit unsigned integer to an equivalent single-precision 

    floating-point number.

  

  

   value: The 32-bit unsigned integer to convert.

   Returns: A single-precision floating-point number that is equivalent to value.

  ToSingle(value: Int16) -> Single

  

   Converts the value of the specified 16-bit signed integer to an equivalent single-precision 

    floating-point number.

  

  

   value: The 16-bit signed integer to convert.

   Returns: A single-precision floating-point number that is equivalent to value.

  ToSingle(value: UInt16) -> Single

  

   Converts the value of the specified 16-bit unsigned integer to the equivalent single-precision 

    floating-point number.

  

  

   value: The 16-bit unsigned integer to convert.

   Returns: A single-precision floating-point number that is equivalent to value.
  """
  pass
 @staticmethod
 def ToString(value=None,*__args):
  """
  ToString(value: float) -> str

  

   Converts the value of the specified double-precision floating-point number to its equivalent 

    string representation.

  

  

   value: The double-precision floating-point number to convert.

   Returns: The string representation of value.

  ToString(value: Single,provider: IFormatProvider) -> str

  

   Converts the value of the specified single-precision floating-point number to its equivalent 

    string representation,using the specified culture-specific formatting information.

  

  

   value: The single-precision floating-point number to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of value.

  ToString(value: Decimal) -> str

  

   Converts the value of the specified decimal number to its equivalent string representation.

  

   value: The decimal number to convert.

   Returns: The string representation of value.

  ToString(value: float,provider: IFormatProvider) -> str

  

   Converts the value of the specified double-precision floating-point number to its equivalent 

    string representation.

  

  

   value: The double-precision floating-point number to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of value.

  ToString(value: Single) -> str

  

   Converts the value of the specified single-precision floating-point number to its equivalent 

    string representation.

  

  

   value: The single-precision floating-point number to convert.

   Returns: The string representation of value.

  ToString(value: Int64,provider: IFormatProvider) -> str

  

   Converts the value of the specified 64-bit signed integer to its equivalent string 

    representation,using the specified culture-specific formatting information.

  

  

   value: The 64-bit signed integer to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of value.

  ToString(value: Int64) -> str

  

   Converts the value of the specified 64-bit signed integer to its equivalent string 

    representation.

  

  

   value: The 64-bit signed integer to convert.

   Returns: The string representation of value.

  ToString(value: UInt64,provider: IFormatProvider) -> str

  

   Converts the value of the specified 64-bit unsigned integer to its equivalent string 

    representation,using the specified culture-specific formatting information.

  

  

   value: The 64-bit unsigned integer to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of value.

  ToString(value: UInt64) -> str

  

   Converts the value of the specified 64-bit unsigned integer to its equivalent string 

    representation.

  

  

   value: The 64-bit unsigned integer to convert.

   Returns: The string representation of value.

  ToString(value: Int16,toBase: int) -> str

  

   Converts the value of a 16-bit signed integer to its equivalent string representation in a 

    specified base.

  

  

   value: The 16-bit signed integer to convert.

   toBase: The base of the return value,which must be 2,8,10,or 16.

   Returns: The string representation of value in base toBase.

  ToString(value: Byte,toBase: int) -> str

  

   Converts the value of an 8-bit unsigned integer to its equivalent string representation in a 

    specified base.

  

  

   value: The 8-bit unsigned integer to convert.

   toBase: The base of the return value,which must be 2,8,10,or 16.

   Returns: The string representation of value in base toBase.

  ToString(value: Int64,toBase: int) -> str

  

   Converts the value of a 64-bit signed integer to its equivalent string representation in a 

    specified base.

  

  

   value: The 64-bit signed integer to convert.

   toBase: The base of the return value,which must be 2,8,10,or 16.

   Returns: The string representation of value in base toBase.

  ToString(value: int,toBase: int) -> str

  

   Converts the value of a 32-bit signed integer to its equivalent string representation in a 

    specified base.

  

  

   value: The 32-bit signed integer to convert.

   toBase: The base of the return value,which must be 2,8,10,or 16.

   Returns: The string representation of value in base toBase.

  ToString(value: str,provider: IFormatProvider) -> str

  

   Returns the specified string instance; no actual conversion is performed.

  

   value: The string to return.

   provider: An object that supplies culture-specific formatting information. This parameter is ignored.

   Returns: value is returned unchanged.

  ToString(value: DateTime) -> str

  

   Converts the value of the specified System.DateTime to its equivalent string representation.

  

   value: The date and time value to convert.

   Returns: The string representation of value.

  ToString(value: Decimal,provider: IFormatProvider) -> str

  

   Converts the value of the specified decimal number to its equivalent string representation,

    using the specified culture-specific formatting information.

  

  

   value: The decimal number to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of value.

  ToString(value: str) -> str

  

   Returns the specified string instance; no actual conversion is performed.

  

   value: The string to return.

   Returns: value is returned unchanged.

  ToString(value: DateTime,provider: IFormatProvider) -> str

  

   Converts the value of the specified System.DateTime to its equivalent string representation,

    using the specified culture-specific formatting information.

  

  

   value: The date and time value to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of value.

  ToString(value: SByte) -> str

  

   Converts the value of the specified 8-bit signed integer to its equivalent string representation.

  

   value: The 8-bit signed integer to convert.

   Returns: The string representation of value.

  ToString(value: Char,provider: IFormatProvider) -> str

  

   Converts the value of the specified Unicode character to its equivalent string representation,

    using the specified culture-specific formatting information.

  

  

   value: The Unicode character to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of value.

  ToString(value: Byte) -> str

  

   Converts the value of the specified 8-bit unsigned integer to its equivalent string 

    representation.

  

  

   value: The 8-bit unsigned integer to convert.

   Returns: The string representation of value.

  ToString(value: SByte,provider: IFormatProvider) -> str

  

   Converts the value of the specified 8-bit signed integer to its equivalent string 

    representation,using the specified culture-specific formatting information.

  

  

   value: The 8-bit signed integer to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of value.

  ToString(value: Char) -> str

  

   Converts the value of the specified Unicode character to its equivalent string representation.

  

   value: The Unicode character to convert.

   Returns: The string representation of value.

  ToString(value: object,provider: IFormatProvider) -> str

  

   Converts the value of the specified object to its equivalent string representation using the 

    specified culture-specific formatting information.

  

  

   value: An object that supplies the value to convert,or null.

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of value,or System.String.Empty if value is null.

  ToString(value: object) -> str

  

   Converts the value of the specified object to its equivalent string representation.

  

   value: An object that supplies the value to convert,or null.

   Returns: The string representation of value,or System.String.Empty if value is null.

  ToString(value: bool,provider: IFormatProvider) -> str

  

   Converts the specified Boolean value to its equivalent string representation.

  

   value: The Boolean value to convert.

   provider: An instance of an object. This parameter is ignored.

   Returns: The string representation of value.

  ToString(value: bool) -> str

  

   Converts the specified Boolean value to its equivalent string representation.

  

   value: The Boolean value to convert.

   Returns: The string representation of value.

  ToString(value: int,provider: IFormatProvider) -> str

  

   Converts the value of the specified 32-bit signed integer to its equivalent string 

    representation,using the specified culture-specific formatting information.

  

  

   value: The 32-bit signed integer to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of value.

  ToString(value: int) -> str

  

   Converts the value of the specified 32-bit signed integer to its equivalent string 

    representation.

  

  

   value: The 32-bit signed integer to convert.

   Returns: The string representation of value.

  ToString(value: UInt32,provider: IFormatProvider) -> str

  

   Converts the value of the specified 32-bit unsigned integer to its equivalent string 

    representation,using the specified culture-specific formatting information.

  

  

   value: The 32-bit unsigned integer to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of value.

  ToString(value: UInt32) -> str

  

   Converts the value of the specified 32-bit unsigned integer to its equivalent string 

    representation.

  

  

   value: The 32-bit unsigned integer to convert.

   Returns: The string representation of value.

  ToString(value: UInt16,provider: IFormatProvider) -> str

  

   Converts the value of the specified 16-bit unsigned integer to its equivalent string 

    representation,using the specified culture-specific formatting information.

  

  

   value: The 16-bit unsigned integer to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of value.

  ToString(value: Int16) -> str

  

   Converts the value of the specified 16-bit signed integer to its equivalent string 

    representation.

  

  

   value: The 16-bit signed integer to convert.

   Returns: The string representation of value.

  ToString(value: Byte,provider: IFormatProvider) -> str

  

   Converts the value of the specified 8-bit unsigned integer to its equivalent string 

    representation,using the specified culture-specific formatting information.

  

  

   value: The 8-bit unsigned integer to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of value.

  ToString(value: UInt16) -> str

  

   Converts the value of the specified 16-bit unsigned integer to its equivalent string 

    representation.

  

  

   value: The 16-bit unsigned integer to convert.

   Returns: The string representation of value.

  ToString(value: Int16,provider: IFormatProvider) -> str

  

   Converts the value of the specified 16-bit signed integer to its equivalent string 

    representation,using the specified culture-specific formatting information.

  

  

   value: The 16-bit signed integer to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of value.
  """
  pass
 @staticmethod
 def ToUInt16(value,*__args):
  """
  ToUInt16(value: Single) -> UInt16

  

   Converts the value of the specified single-precision floating-point number to an equivalent 

    16-bit unsigned integer.

  

  

   value: The single-precision floating-point number to convert.

   Returns: value,rounded to the nearest 16-bit unsigned integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToUInt16(value: float) -> UInt16

  

   Converts the value of the specified double-precision floating-point number to an equivalent 

    16-bit unsigned integer.

  

  

   value: The double-precision floating-point number to convert.

   Returns: value,rounded to the nearest 16-bit unsigned integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToUInt16(value: Int64) -> UInt16

  

   Converts the value of the specified 64-bit signed integer to an equivalent 16-bit unsigned 

    integer.

  

  

   value: The 64-bit signed integer to convert.

   Returns: A 16-bit unsigned integer that is equivalent to value.

  ToUInt16(value: UInt64) -> UInt16

  

   Converts the value of the specified 64-bit unsigned integer to an equivalent 16-bit unsigned 

    integer.

  

  

   value: The 64-bit unsigned integer to convert.

   Returns: A 16-bit unsigned integer that is equivalent to value.

  ToUInt16(value: Decimal) -> UInt16

  

   Converts the value of the specified decimal number to an equivalent 16-bit unsigned integer.

  

   value: The decimal number to convert.

   Returns: value,rounded to the nearest 16-bit unsigned integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToUInt16(value: DateTime) -> UInt16

  

   Calling this method always throws System.InvalidCastException.

  

   value: The date and time value to convert.

   Returns: This conversion is not supported. No value is returned.

  ToUInt16(value: str,fromBase: int) -> UInt16

  

   Converts the string representation of a number in a specified base to an equivalent 16-bit 

    unsigned integer.

  

  

   value: A string that contains the number to convert.

   fromBase: The base of the number in value,which must be 2,8,10,or 16.

   Returns: A 16-bit unsigned integer that is equivalent to the number in value,or 0 (zero) if value is 

    null.

  

  ToUInt16(value: str) -> UInt16

  

   Converts the specified string representation of a number to an equivalent 16-bit unsigned 

    integer.

  

  

   value: A string that contains the number to convert.

   Returns: A 16-bit unsigned integer that is equivalent to the number in value,or 0 (zero) if value is 

    null.

  

  ToUInt16(value: str,provider: IFormatProvider) -> UInt16

  

   Converts the specified string representation of a number to an equivalent 16-bit unsigned 

    integer,using the specified culture-specific formatting information.

  

  

   value: A string that contains the number to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: A 16-bit unsigned integer that is equivalent to the number in value,or 0 (zero) if value is 

    null.

  

  ToUInt16(value: UInt32) -> UInt16

  

   Converts the value of the specified 32-bit unsigned integer to an equivalent 16-bit unsigned 

    integer.

  

  

   value: The 32-bit unsigned integer to convert.

   Returns: A 16-bit unsigned integer that is equivalent to value.

  ToUInt16(value: bool) -> UInt16

  

   Converts the specified Boolean value to the equivalent 16-bit unsigned integer.

  

   value: The Boolean value to convert.

   Returns: The number 1 if value is true; otherwise,0.

  ToUInt16(value: Char) -> UInt16

  

   Converts the value of the specified Unicode character to the equivalent 16-bit unsigned integer.

  

   value: The Unicode character to convert.

   Returns: The 16-bit unsigned integer equivalent to value.

  ToUInt16(value: object) -> UInt16

  

   Converts the value of the specified object to a 16-bit unsigned integer.

  

   value: An object that implements the System.IConvertible interface,or null.

   Returns: A 16-bit unsigned integer that is equivalent to value,or zero if value is null.

  ToUInt16(value: object,provider: IFormatProvider) -> UInt16

  

   Converts the value of the specified object to a 16-bit unsigned integer,using the specified 

    culture-specific formatting information.

  

  

   value: An object that implements the System.IConvertible interface.

   provider: An object that supplies culture-specific formatting information.

   Returns: A 16-bit unsigned integer that is equivalent to value,or zero if value is null.

  ToUInt16(value: SByte) -> UInt16

  

   Converts the value of the specified 8-bit signed integer to the equivalent 16-bit unsigned 

    integer.

  

  

   value: The 8-bit signed integer to convert.

   Returns: A 16-bit unsigned integer that is equivalent to value.

  ToUInt16(value: int) -> UInt16

  

   Converts the value of the specified 32-bit signed integer to an equivalent 16-bit unsigned 

    integer.

  

  

   value: The 32-bit signed integer to convert.

   Returns: A 16-bit unsigned integer that is equivalent to value.

  ToUInt16(value: UInt16) -> UInt16

  

   Returns the specified 16-bit unsigned integer; no actual conversion is performed.

  

   value: The 16-bit unsigned integer to return.

   Returns: value is returned unchanged.

  ToUInt16(value: Byte) -> UInt16

  

   Converts the value of the specified 8-bit unsigned integer to the equivalent 16-bit unsigned 

    integer.

  

  

   value: The 8-bit unsigned integer to convert.

   Returns: A 16-bit unsigned integer that is equivalent to value.

  ToUInt16(value: Int16) -> UInt16

  

   Converts the value of the specified 16-bit signed integer to the equivalent 16-bit unsigned 

    integer.

  

  

   value: The 16-bit signed integer to convert.

   Returns: A 16-bit unsigned integer that is equivalent to value.
  """
  pass
 @staticmethod
 def ToUInt32(value,*__args):
  """
  ToUInt32(value: Single) -> UInt32

  

   Converts the value of the specified single-precision floating-point number to an equivalent 

    32-bit unsigned integer.

  

  

   value: The single-precision floating-point number to convert.

   Returns: value,rounded to the nearest 32-bit unsigned integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToUInt32(value: float) -> UInt32

  

   Converts the value of the specified double-precision floating-point number to an equivalent 

    32-bit unsigned integer.

  

  

   value: The double-precision floating-point number to convert.

   Returns: value,rounded to the nearest 32-bit unsigned integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToUInt32(value: Int64) -> UInt32

  

   Converts the value of the specified 64-bit signed integer to an equivalent 32-bit unsigned 

    integer.

  

  

   value: The 64-bit signed integer to convert.

   Returns: A 32-bit unsigned integer that is equivalent to value.

  ToUInt32(value: UInt64) -> UInt32

  

   Converts the value of the specified 64-bit unsigned integer to an equivalent 32-bit unsigned 

    integer.

  

  

   value: The 64-bit unsigned integer to convert.

   Returns: A 32-bit unsigned integer that is equivalent to value.

  ToUInt32(value: Decimal) -> UInt32

  

   Converts the value of the specified decimal number to an equivalent 32-bit unsigned integer.

  

   value: The decimal number to convert.

   Returns: value,rounded to the nearest 32-bit unsigned integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToUInt32(value: DateTime) -> UInt32

  

   Calling this method always throws System.InvalidCastException.

  

   value: The date and time value to convert.

   Returns: This conversion is not supported. No value is returned.

  ToUInt32(value: str,fromBase: int) -> UInt32

  

   Converts the string representation of a number in a specified base to an equivalent 32-bit 

    unsigned integer.

  

  

   value: A string that contains the number to convert.

   fromBase: The base of the number in value,which must be 2,8,10,or 16.

   Returns: A 32-bit unsigned integer that is equivalent to the number in value,or 0 (zero) if value is 

    null.

  

  ToUInt32(value: str) -> UInt32

  

   Converts the specified string representation of a number to an equivalent 32-bit unsigned 

    integer.

  

  

   value: A string that contains the number to convert.

   Returns: A 32-bit unsigned integer that is equivalent to the number in value,or 0 (zero) if value is 

    null.

  

  ToUInt32(value: str,provider: IFormatProvider) -> UInt32

  

   Converts the specified string representation of a number to an equivalent 32-bit unsigned 

    integer,using the specified culture-specific formatting information.

  

  

   value: A string that contains the number to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: A 32-bit unsigned integer that is equivalent to the number in value,or 0 (zero) if value is 

    null.

  

  ToUInt32(value: UInt32) -> UInt32

  

   Returns the specified 32-bit unsigned integer; no actual conversion is performed.

  

   value: The 32-bit unsigned integer to return.

   Returns: value is returned unchanged.

  ToUInt32(value: bool) -> UInt32

  

   Converts the specified Boolean value to the equivalent 32-bit unsigned integer.

  

   value: The Boolean value to convert.

   Returns: The number 1 if value is true; otherwise,0.

  ToUInt32(value: Char) -> UInt32

  

   Converts the value of the specified Unicode character to the equivalent 32-bit unsigned integer.

  

   value: The Unicode character to convert.

   Returns: A 32-bit unsigned integer that is equivalent to value.

  ToUInt32(value: object) -> UInt32

  

   Converts the value of the specified object to a 32-bit unsigned integer.

  

   value: An object that implements the System.IConvertible interface,or null.

   Returns: A 32-bit unsigned integer that is equivalent to value,or 0 (zero) if value is null.

  ToUInt32(value: object,provider: IFormatProvider) -> UInt32

  

   Converts the value of the specified object to a 32-bit unsigned integer,using the specified 

    culture-specific formatting information.

  

  

   value: An object that implements the System.IConvertible interface.

   provider: An object that supplies culture-specific formatting information.

   Returns: A 32-bit unsigned integer that is equivalent to value,or zero if value is null.

  ToUInt32(value: SByte) -> UInt32

  

   Converts the value of the specified 8-bit signed integer to the equivalent 32-bit unsigned 

    integer.

  

  

   value: The 8-bit signed integer to convert.

   Returns: A 32-bit unsigned integer that is equivalent to value.

  ToUInt32(value: UInt16) -> UInt32

  

   Converts the value of the specified 16-bit unsigned integer to the equivalent 32-bit unsigned 

    integer.

  

  

   value: The 16-bit unsigned integer to convert.

   Returns: A 32-bit unsigned integer that is equivalent to value.

  ToUInt32(value: int) -> UInt32

  

   Converts the value of the specified 32-bit signed integer to an equivalent 32-bit unsigned 

    integer.

  

  

   value: The 32-bit signed integer to convert.

   Returns: A 32-bit unsigned integer that is equivalent to value.

  ToUInt32(value: Byte) -> UInt32

  

   Converts the value of the specified 8-bit unsigned integer to the equivalent 32-bit unsigned 

    integer.

  

  

   value: The 8-bit unsigned integer to convert.

   Returns: A 32-bit unsigned integer that is equivalent to value.

  ToUInt32(value: Int16) -> UInt32

  

   Converts the value of the specified 16-bit signed integer to the equivalent 32-bit unsigned 

    integer.

  

  

   value: The 16-bit signed integer to convert.

   Returns: A 32-bit unsigned integer that is equivalent to value.
  """
  pass
 @staticmethod
 def ToUInt64(value,*__args):
  """
  ToUInt64(value: Single) -> UInt64

  

   Converts the value of the specified single-precision floating-point number to an equivalent 

    64-bit unsigned integer.

  

  

   value: The single-precision floating-point number to convert.

   Returns: value,rounded to the nearest 64-bit unsigned integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToUInt64(value: float) -> UInt64

  

   Converts the value of the specified double-precision floating-point number to an equivalent 

    64-bit unsigned integer.

  

  

   value: The double-precision floating-point number to convert.

   Returns: value,rounded to the nearest 64-bit unsigned integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToUInt64(value: Int64) -> UInt64

  

   Converts the value of the specified 64-bit signed integer to an equivalent 64-bit unsigned 

    integer.

  

  

   value: The 64-bit signed integer to convert.

   Returns: A 64-bit unsigned integer that is equivalent to value.

  ToUInt64(value: UInt64) -> UInt64

  

   Returns the specified 64-bit unsigned integer; no actual conversion is performed.

  

   value: The 64-bit unsigned integer to return.

   Returns: value is returned unchanged.

  ToUInt64(value: Decimal) -> UInt64

  

   Converts the value of the specified decimal number to an equivalent 64-bit unsigned integer.

  

   value: The decimal number to convert.

   Returns: value,rounded to the nearest 64-bit unsigned integer. If value is halfway between two whole 

    numbers,the even number is returned; that is,4.5 is converted to 4,and 5.5 is converted to 6.

  

  ToUInt64(value: DateTime) -> UInt64

  

   Calling this method always throws System.InvalidCastException.

  

   value: The date and time value to convert.

   Returns: This conversion is not supported. No value is returned.

  ToUInt64(value: str,fromBase: int) -> UInt64

  

   Converts the string representation of a number in a specified base to an equivalent 64-bit 

    unsigned integer.

  

  

   value: A string that contains the number to convert.

   fromBase: The base of the number in value,which must be 2,8,10,or 16.

   Returns: A 64-bit unsigned integer that is equivalent to the number in value,or 0 (zero) if value is 

    null.

  

  ToUInt64(value: str) -> UInt64

  

   Converts the specified string representation of a number to an equivalent 64-bit unsigned 

    integer.

  

  

   value: A string that contains the number to convert.

   Returns: A 64-bit signed integer that is equivalent to the number in value,or 0 (zero) if value is null.

  ToUInt64(value: str,provider: IFormatProvider) -> UInt64

  

   Converts the specified string representation of a number to an equivalent 64-bit unsigned 

    integer,using the specified culture-specific formatting information.

  

  

   value: A string that contains the number to convert.

   provider: An object that supplies culture-specific formatting information.

   Returns: A 64-bit unsigned integer that is equivalent to the number in value,or 0 (zero) if value is 

    null.

  

  ToUInt64(value: UInt32) -> UInt64

  

   Converts the value of the specified 32-bit unsigned integer to an equivalent 64-bit unsigned 

    integer.

  

  

   value: The 32-bit unsigned integer to convert.

   Returns: A 64-bit unsigned integer that is equivalent to value.

  ToUInt64(value: bool) -> UInt64

  

   Converts the specified Boolean value to the equivalent 64-bit unsigned integer.

  

   value: The Boolean value to convert.

   Returns: The number 1 if value is true; otherwise,0.

  ToUInt64(value: Char) -> UInt64

  

   Converts the value of the specified Unicode character to the equivalent 64-bit unsigned integer.

  

   value: The Unicode character to convert.

   Returns: A 64-bit unsigned integer that is equivalent to value.

  ToUInt64(value: object) -> UInt64

  

   Converts the value of the specified object to a 64-bit unsigned integer.

  

   value: An object that implements the System.IConvertible interface,or null.

   Returns: A 64-bit unsigned integer that is equivalent to value,or zero if value is null.

  ToUInt64(value: object,provider: IFormatProvider) -> UInt64

  

   Converts the value of the specified object to a 64-bit unsigned integer,using the specified 

    culture-specific formatting information.

  

  

   value: An object that implements the System.IConvertible interface.

   provider: An object that supplies culture-specific formatting information.

   Returns: A 64-bit unsigned integer that is equivalent to value,or zero if value is null.

  ToUInt64(value: SByte) -> UInt64

  

   Converts the value of the specified 8-bit signed integer to the equivalent 64-bit unsigned 

    integer.

  

  

   value: The 8-bit signed integer to convert.

   Returns: A 64-bit unsigned integer that is equivalent to value.

  ToUInt64(value: UInt16) -> UInt64

  

   Converts the value of the specified 16-bit unsigned integer to the equivalent 64-bit unsigned 

    integer.

  

  

   value: The 16-bit unsigned integer to convert.

   Returns: A 64-bit unsigned integer that is equivalent to value.

  ToUInt64(value: int) -> UInt64

  

   Converts the value of the specified 32-bit signed integer to an equivalent 64-bit unsigned 

    integer.

  

  

   value: The 32-bit signed integer to convert.

   Returns: A 64-bit unsigned integer that is equivalent to value.

  ToUInt64(value: Byte) -> UInt64

  

   Converts the value of the specified 8-bit unsigned integer to the equivalent 64-bit unsigned 

    integer.

  

  

   value: The 8-bit unsigned integer to convert.

   Returns: A 64-bit signed integer that is equivalent to value.

  ToUInt64(value: Int16) -> UInt64

  

   Converts the value of the specified 16-bit signed integer to the equivalent 64-bit unsigned 

    integer.

  

  

   value: The 16-bit signed integer to convert.

   Returns: A 64-bit unsigned integer that is equivalent to value.
  """
  pass
 DBNull=None
 __all__=[
  'ChangeType',
  'DBNull',
  'FromBase64CharArray',
  'FromBase64String',
  'GetTypeCode',
  'IsDBNull',
  'ToBase64CharArray',
  'ToBase64String',
  'ToBoolean',
  'ToByte',
  'ToChar',
  'ToDateTime',
  'ToDecimal',
  'ToDouble',
  'ToInt16',
  'ToInt32',
  'ToInt64',
  'ToSByte',
  'ToSingle',
  'ToString',
  'ToUInt16',
  'ToUInt32',
  'ToUInt64',
 ]

