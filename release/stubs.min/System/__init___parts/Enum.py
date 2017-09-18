class Enum(object,IComparable,IFormattable,IConvertible):
 """ Provides the base class for enumerations. """
 def CompareTo(self,target):
  """
  CompareTo(self: Enum,target: object) -> int

  

   Compares this instance to a specified object and returns an indication of their relative values.

  

   target: An object to compare,or null.

   Returns: A signed number that indicates the relative values of this instance and target.Value Meaning 

    Less than zero The value of this instance is less than the value of target. Zero The value of 

    this instance is equal to the value of target. Greater than zero The value of this instance is 

    greater than the value of target.-or- target is null.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: Enum,obj: object) -> bool

  

   Returns a value indicating whether this instance is equal to a specified object.

  

   obj: An object to compare with this instance,or null.

   Returns: true if obj is an System.Enum with the same underlying type and value as this instance; 

    otherwise,false.
  """
  pass
 @staticmethod
 def Format(enumType,value,format):
  """
  Format(enumType: Type,value: object,format: str) -> str

  

   Converts the specified value of a specified enumerated type to its equivalent string 

    representation according to the specified format.

  

  

   enumType: The enumeration type of the value to convert.

   value: The value to convert.

   format: The output format to use.

   Returns: A string representation of value.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Enum) -> int

  

   Returns the hash code for the value of this instance.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 @staticmethod
 def GetName(enumType,value):
  """
  GetName(enumType: Type,value: object) -> str

  

   Retrieves the name of the constant in the specified enumeration that has the specified value.

  

   enumType: An enumeration type.

   value: The value of a particular enumerated constant in terms of its underlying type.

   Returns: A string containing the name of the enumerated constant in enumType whose value is value; or 

    null if no such constant is found.
  """
  pass
 @staticmethod
 def GetNames(enumType):
  """
  GetNames(enumType: Type) -> Array[str]

  

   Retrieves an array of the names of the constants in a specified enumeration.

  

   enumType: An enumeration type.

   Returns: A string array of the names of the constants in enumType.
  """
  pass
 def GetTypeCode(self):
  """
  GetTypeCode(self: Enum) -> TypeCode

  

   Returns the underlying System.TypeCode for this instance.

   Returns: The type for this instance.
  """
  pass
 @staticmethod
 def GetUnderlyingType(enumType):
  """
  GetUnderlyingType(enumType: Type) -> Type

  

   Returns the underlying type of the specified enumeration.

  

   enumType: The enumeration whose underlying type will be retrieved.

   Returns: The underlying type of enumType.
  """
  pass
 @staticmethod
 def GetValues(enumType):
  """
  GetValues(enumType: Type) -> Array

  

   Retrieves an array of the values of the constants in a specified enumeration.

  

   enumType: The enumeration type to retrieve values from.

   Returns: An array that contains the values of the constants in enumType.
  """
  pass
 def HasFlag(self,flag):
  """
  HasFlag(self: Enum,flag: Enum) -> bool

  

   Determines whether one or more bit fields are set in the current instance.

  

   flag: An enumeration value.

   Returns: true if the bit field or bit fields that are set in flag are also set in the current instance; 

    otherwise,false.
  """
  pass
 @staticmethod
 def IsDefined(enumType,value):
  """
  IsDefined(enumType: Type,value: object) -> bool

  

   Indicates whether a constant with a specified value exists in a specified enumeration.

  

   enumType: The enumeration type to check.

   value: The value or name of a constant in enumType.

   Returns: true if a constant in enumType has a value equal to value; otherwise,false.
  """
  pass
 @staticmethod
 def Parse(enumType,value,ignoreCase=None):
  """
  Parse(enumType: Type,value: str,ignoreCase: bool) -> object

  

   Converts the string representation of the name or numeric value of one or more enumerated 

    constants to an equivalent enumerated object. A parameter specifies whether the operation is 

    case-insensitive.

  

  

   enumType: An enumeration type.

   value: A string containing the name or value to convert.

   ignoreCase: true to ignore case; false to regard case.

   Returns: An object of type enumType whose value is represented by value.

  Parse(enumType: Type,value: str) -> object

  

   Converts the string representation of the name or numeric value of one or more enumerated 

    constants to an equivalent enumerated object.

  

  

   enumType: An enumeration type.

   value: A string containing the name or value to convert.

   Returns: An object of type enumType whose value is represented by value.
  """
  pass
 @staticmethod
 def ToObject(enumType,value):
  """
  ToObject(enumType: Type,value: UInt32) -> object

  

   Converts the specified 32-bit unsigned integer value to an enumeration member.

  

   enumType: The enumeration type to return.

   value: The value to convert to an enumeration member.

   Returns: An instance of the enumeration set to value.

  ToObject(enumType: Type,value: UInt16) -> object

  

   Converts the specified 16-bit unsigned integer value to an enumeration member.

  

   enumType: The enumeration type to return.

   value: The value to convert to an enumeration member.

   Returns: An instance of the enumeration set to value.

  ToObject(enumType: Type,value: UInt64) -> object

  

   Converts the specified 64-bit unsigned integer value to an enumeration member.

  

   enumType: The enumeration type to return.

   value: The value to convert to an enumeration member.

   Returns: An instance of the enumeration set to value.

  ToObject(enumType: Type,value: Int64) -> object

  

   Converts the specified 64-bit signed integer to an enumeration member.

  

   enumType: The enumeration type to return.

   value: The value to convert to an enumeration member.

   Returns: An instance of the enumeration set to value.

  ToObject(enumType: Type,value: Byte) -> object

  

   Converts the specified 8-bit unsigned integer to an enumeration member.

  

   enumType: The enumeration type to return.

   value: The value to convert to an enumeration member.

   Returns: An instance of the enumeration set to value.

  ToObject(enumType: Type,value: SByte) -> object

  

   Converts the specified 8-bit signed integer value to an enumeration member.

  

   enumType: The enumeration type to return.

   value: The value to convert to an enumeration member.

   Returns: An instance of the enumeration set to value.

  ToObject(enumType: Type,value: object) -> object

  

   Converts the specified object with an integer value to an enumeration member.

  

   enumType: The enumeration type to return.

   value: The value convert to an enumeration member.

   Returns: An enumeration object whose value is value.

  ToObject(enumType: Type,value: int) -> object

  

   Converts the specified 32-bit signed integer to an enumeration member.

  

   enumType: The enumeration type to return.

   value: The value to convert to an enumeration member.

   Returns: An instance of the enumeration set to value.

  ToObject(enumType: Type,value: Int16) -> object

  

   Converts the specified 16-bit signed integer to an enumeration member.

  

   enumType: The enumeration type to return.

   value: The value to convert to an enumeration member.

   Returns: An instance of the enumeration set to value.
  """
  pass
 def ToString(self,*__args):
  """
  ToString(self: Enum,format: str) -> str

  

   Converts the value of this instance to its equivalent string representation using the specified 

    format.

  

  

   format: A format string.

   Returns: The string representation of the value of this instance as specified by format.

  ToString(self: Enum,provider: IFormatProvider) -> str

  

   This method overload is obsolete; use System.Enum.ToString.

  

   provider: (obsolete)

   Returns: The string representation of the value of this instance.

  ToString(self: Enum) -> str

  

   Converts the value of this instance to its equivalent string representation.

   Returns: The string representation of the value of this instance.

  ToString(self: Enum,format: str,provider: IFormatProvider) -> str

  

   This method overload is obsolete; use System.Enum.ToString(System.String).

  

   format: A format specification.

   provider: (Obsolete.)

   Returns: The string representation of the value of this instance as specified by format.
  """
  pass
 @staticmethod
 def TryParse(value,*__args):
  """
  TryParse[TEnum](value: str,ignoreCase: bool) -> (bool,TEnum)

  TryParse[TEnum](value: str) -> (bool,TEnum)
  """
  pass
 def __and__(self,*args):
  """ __and__(self: object,other: object) -> object """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __invert__(self,*args):
  """ __invert__(self: object) -> object """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __nonzero__(self,*args):
  """ __nonzero__(self: object) -> bool """
  pass
 def __or__(self,*args):
  """ __or__(self: object,other: object) -> object """
  pass
 def __rand__(self,*args):
  """ __rand__(self: object,other: object) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __ror__(self,*args):
  """ __ror__(self: object,other: object) -> object """
  pass
 def __rxor__(self,*args):
  """ __rxor__(self: object,other: object) -> object """
  pass
 def __str__(self,*args):
  pass
 def __xor__(self,*args):
  """ __xor__(self: object,other: object) -> object """
  pass
