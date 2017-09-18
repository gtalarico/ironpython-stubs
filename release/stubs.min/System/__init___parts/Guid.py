class Guid(object,IFormattable,IComparable,IComparable[Guid],IEquatable[Guid]):
 """
 Represents a globally unique identifier (GUID).

 

 Guid(b: Array[Byte])

 Guid(a: UInt32,b: UInt16,c: UInt16,d: Byte,e: Byte,f: Byte,g: Byte,h: Byte,i: Byte,j: Byte,k: Byte)

 Guid(a: int,b: Int16,c: Int16,d: Array[Byte])

 Guid(a: int,b: Int16,c: Int16,d: Byte,e: Byte,f: Byte,g: Byte,h: Byte,i: Byte,j: Byte,k: Byte)

 Guid(g: str)
 """
 def CompareTo(self,value):
  """
  CompareTo(self: Guid,value: Guid) -> int

  

   Compares this instance to a specified System.Guid object and returns an indication of their 

    relative values.

  

  

   value: An object to compare to this instance.

   Returns: A signed number indicating the relative values of this instance and value.Return value 

    Description A negative integer This instance is less than value. Zero This instance is equal to 

    value. A positive integer This instance is greater than value.

  

  CompareTo(self: Guid,value: object) -> int

  

   Compares this instance to a specified object and returns an indication of their relative values.

  

   value: An object to compare,or null.

   Returns: A signed number indicating the relative values of this instance and value.Return value 

    Description A negative integer This instance is less than value. Zero This instance is equal to 

    value. A positive integer This instance is greater than value,or value is null.
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Guid,g: Guid) -> bool

  

   Returns a value indicating whether this instance and a specified System.Guid object represent 

    the same value.

  

  

   g: An object to compare to this instance.

   Returns: true if g is equal to this instance; otherwise,false.

  Equals(self: Guid,o: object) -> bool

  

   Returns a value that indicates whether this instance is equal to a specified object.

  

   o: The object to compare with this instance.

   Returns: true if o is a System.Guid that has the same value as this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Guid) -> int

  

   Returns the hash code for this instance.

   Returns: The hash code for this instance.
  """
  pass
 @staticmethod
 def NewGuid():
  """
  NewGuid() -> Guid

  

   Initializes a new instance of the System.Guid structure.

   Returns: A new GUID object.
  """
  pass
 @staticmethod
 def Parse(input):
  """
  Parse(input: str) -> Guid

  

   Converts the string representation of a GUID to the equivalent System.Guid structure.

  

   input: The GUID to convert.

   Returns: A structure that contains the value that was parsed.
  """
  pass
 @staticmethod
 def ParseExact(input,format):
  """
  ParseExact(input: str,format: str) -> Guid

  

   Converts the string representation of a GUID to the equivalent System.Guid structure,provided 

    that the string is in the specified format.

  

  

   input: The GUID to convert.

   format: One of the following specifiers that indicates the exact format to use when interpreting input: 

    "N","D","B","P",or "X".

  

   Returns: A structure that contains the value that was parsed.
  """
  pass
 def ToByteArray(self):
  """
  ToByteArray(self: Guid) -> Array[Byte]

  

   Returns a 16-element byte array that contains the value of this instance.

   Returns: A 16-element byte array.
  """
  pass
 def ToString(self,format=None,provider=None):
  """
  ToString(self: Guid,format: str,provider: IFormatProvider) -> str

  

   Returns a string representation of the value of this instance of the System.Guid structure,

    according to the provided format specifier and culture-specific format information.

  

  

   format: A single format specifier that indicates how to format the value of this System.Guid. The format 

    parameter can be "N","D","B","P",or "X". If format is null or an empty string (""),"D" is 

    used.

  

   provider: (Reserved) An object that supplies culture-specific formatting services.

   Returns: The value of this System.Guid,represented as a series of lowercase hexadecimal digits in the 

    specified format.

  

  ToString(self: Guid,format: str) -> str

  

   Returns a string representation of the value of this System.Guid instance,according to the 

    provided format specifier.

  

  

   format: A single format specifier that indicates how to format the value of this System.Guid. The format 

    parameter can be "N","D","B","P",or "X". If format is null or an empty string (""),"D" is 

    used.

  

   Returns: The value of this System.Guid,represented as a series of lowercase hexadecimal digits in the 

    specified format.

  

  ToString(self: Guid) -> str

  

   Returns a string representation of the value of this instance in registry format.

   Returns: The value of this System.Guid,formatted using the "D" format specifier as follows: 

    xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx where the value of the GUID is represented as a series of 

    lowercase hexadecimal digits in groups of 8,4,4,4,and 12 digits and separated by hyphens. An 

    example of a return value is "382c74c3-721d-4f34-80e5-57657b6cbc27".
  """
  pass
 @staticmethod
 def TryParse(input,result):
  """
  TryParse(input: str) -> (bool,Guid)

  

   Converts the string representation of a GUID to the equivalent System.Guid structure.

  

   input: The GUID to convert.

   Returns: true if the parse operation was successful; otherwise,false.
  """
  pass
 @staticmethod
 def TryParseExact(input,format,result):
  """
  TryParseExact(input: str,format: str) -> (bool,Guid)

  

   Converts the string representation of a GUID to the equivalent System.Guid structure,provided 

    that the string is in the specified format.

  

  

   input: The GUID to convert.

   format: One of the following specifiers that indicates the exact format to use when interpreting input: 

    "N","D","B","P",or "X".

  

   Returns: true if the parse operation was successful; otherwise,false.
  """
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
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,b: Array[Byte])

  __new__(cls: type,a: UInt32,b: UInt16,c: UInt16,d: Byte,e: Byte,f: Byte,g: Byte,h: Byte,i: Byte,j: Byte,k: Byte)

  __new__(cls: type,a: int,b: Int16,c: Int16,d: Array[Byte])

  __new__(cls: type,a: int,b: Int16,c: Int16,d: Byte,e: Byte,f: Byte,g: Byte,h: Byte,i: Byte,j: Byte,k: Byte)

  __new__(cls: type,g: str)

  __new__[Guid]() -> Guid
  """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 Empty=None

