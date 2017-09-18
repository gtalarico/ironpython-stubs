class Byte(object,IComparable,IFormattable,IConvertible,IComparable[Byte],IEquatable[Byte]):
 """ Represents an 8-bit unsigned integer. """
 def bit_length(self,*args):
  """ bit_length(value: Byte) -> int """
  pass
 def CompareTo(self,value):
  """
  CompareTo(self: Byte,value: Byte) -> int

  

   Compares this instance to a specified 8-bit unsigned integer and returns an indication of their 

    relative values.

  

  

   value: An 8-bit unsigned integer to compare.

   Returns: A signed integer that indicates the relative order of this instance and value.Return Value 

    Description Less than zero This instance is less than value. Zero This instance is equal to 

    value. Greater than zero This instance is greater than value.

  

  CompareTo(self: Byte,value: object) -> int

  

   Compares this instance to a specified object and returns an indication of their relative values.

  

   value: An object to compare,or null.

   Returns: A signed integer that indicates the relative order of this instance and value.Return Value 

    Description Less than zero This instance is less than value. Zero This instance is equal to 

    value. Greater than zero This instance is greater than value.-or- value is null.
  """
  pass
 def conjugate(self,*args):
  """ conjugate(x: Byte) -> Byte """
  pass
 def Equals(self,obj):
  """
  Equals(self: Byte,obj: Byte) -> bool

  

   Returns a value indicating whether this instance and a specified System.Byte object represent 

    the same value.

  

  

   obj: An object to compare to this instance.

   Returns: true if obj is equal to this instance; otherwise,false.

  Equals(self: Byte,obj: object) -> bool

  

   Returns a value indicating whether this instance is equal to a specified object.

  

   obj: An object to compare with this instance,or null.

   Returns: true if obj is an instance of System.Byte and equals the value of this instance; otherwise,

    false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Byte) -> int

  

   Returns the hash code for this instance.

   Returns: A hash code for the current System.Byte.
  """
  pass
 def GetTypeCode(self):
  """
  GetTypeCode(self: Byte) -> TypeCode

  

   Returns the System.TypeCode for value type System.Byte.

   Returns: The enumerated constant,System.TypeCode.Byte.
  """
  pass
 @staticmethod
 def Parse(s,*__args):
  """
  Parse(s: str,provider: IFormatProvider) -> Byte

  

   Converts the string representation of a number in a specified culture-specific format to its 

    System.Byte equivalent.

  

  

   s: A string that contains a number to convert. The string is interpreted using the 

    System.Globalization.NumberStyles.Integer style.

  

   provider: An object that supplies culture-specific parsing information about s. If provider is null,the 

    thread current culture is used.

  

   Returns: A byte value that is equivalent to the number contained in s.

  Parse(s: str,style: NumberStyles,provider: IFormatProvider) -> Byte

  

   Converts the string representation of a number in a specified style and culture-specific format 

    to its System.Byte equivalent.

  

  

   s: A string that contains a number to convert. The string is interpreted using the style specified 

    by style.

  

   style: A bitwise combination of enumeration values that indicates the style elements that can be 

    present in s. A typical value to specify is System.Globalization.NumberStyles.Integer.

  

   provider: An object that supplies culture-specific information about the format of s. If provider is null,

    the thread current culture is used.

  

   Returns: A byte value that is equivalent to the number contained in s.

  Parse(s: str) -> Byte

  

   Converts the string representation of a number to its System.Byte equivalent.

  

   s: A string that contains a number to convert. The string is interpreted using the 

    System.Globalization.NumberStyles.Integer style.

  

   Returns: A byte value that is equivalent to the number contained in s.

  Parse(s: str,style: NumberStyles) -> Byte

  

   Converts the string representation of a number in a specified style to its System.Byte 

    equivalent.

  

  

   s: A string that contains a number to convert. The string is interpreted using the style specified 

    by style.

  

   style: A bitwise combination of enumeration values that indicates the style elements that can be 

    present in s. A typical value to specify is System.Globalization.NumberStyles.Integer.

  

   Returns: A byte value that is equivalent to the number contained in s.
  """
  pass
 def ToString(self,*__args):
  """
  ToString(self: Byte,provider: IFormatProvider) -> str

  

   Converts the numeric value of the current System.Byte object to its equivalent string 

    representation using the specified culture-specific formatting information.

  

  

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of the value of this object in the format specified by the provider 

    parameter.

  

  ToString(self: Byte,format: str,provider: IFormatProvider) -> str

  

   Converts the value of the current System.Byte object to its equivalent string representation 

    using the specified format and culture-specific formatting information.

  

  

   format: A standard or custom numeric format string.

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of the current System.Byte object,formatted as specified by the 

    format and provider parameters.

  

  ToString(self: Byte) -> str

  

   Converts the value of the current System.Byte object to its equivalent string representation.

   Returns: The string representation of the value of this object,which consists of a sequence of digits 

    that range from 0 to 9 with no leading zeroes.

  

  ToString(self: Byte,format: str) -> str

  

   Converts the value of the current System.Byte object to its equivalent string representation 

    using the specified format.

  

  

   format: A numeric format string.

   Returns: The string representation of the current System.Byte object,formatted as specified by the 

    format parameter.
  """
  pass
 @staticmethod
 def TryParse(s,*__args):
  """
  TryParse(s: str,style: NumberStyles,provider: IFormatProvider) -> (bool,Byte)

  

   Converts the string representation of a number in a specified style and culture-specific format 

    to its System.Byte equivalent. A return value indicates whether the conversion succeeded or 

    failed.

  

  

   s: A string containing a number to convert. The string is interpreted using the style specified by 

    style.

  

   style: A bitwise combination of enumeration values that indicates the style elements that can be 

    present in s. A typical value to specify is System.Globalization.NumberStyles.Integer.

  

   provider: An object that supplies culture-specific formatting information about s. If provider is null,

    the thread current culture is used.

  

   Returns: true if s was converted successfully; otherwise,false.

  TryParse(s: str) -> (bool,Byte)

  

   Tries to convert the string representation of a number to its System.Byte equivalent,and 

    returns a value that indicates whether the conversion succeeded.

  

  

   s: A string that contains a number to convert. The string is interpreted using the 

    System.Globalization.NumberStyles.Integer style.

  

   Returns: true if s was converted successfully; otherwise,false.
  """
  pass
 def __abs__(self,*args):
  """ x.__abs__() <==> abs(x) """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
  pass
 def __and__(self,*args):
  """
  __and__(x: Byte,y: SByte) -> Int16

  __and__(x: Byte,y: Byte) -> Byte
  """
  pass
 def __cmp__(self,*args):
  """ x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y) """
  pass
 def __div__(self,*args):
  """ x.__div__(y) <==> x/yx.__div__(y) <==> x/y """
  pass
 def __float__(self,*args):
  """ __float__(x: Byte) -> float """
  pass
 def __floordiv__(self,*args):
  """ x.__floordiv__(y) <==> x//yx.__floordiv__(y) <==> x//y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __hash__(self,*args):
  """ x.__hash__() <==> hash(x) """
  pass
 def __hex__(self,*args):
  """ __hex__(value: Byte) -> str """
  pass
 def __index__(self,*args):
  """ __index__(x: Byte) -> int """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __int__(self,*args):
  """ __int__(x: Byte) -> int """
  pass
 def __invert__(self,*args):
  """ __invert__(x: Byte) -> object """
  pass
 def __lshift__(self,*args):
  """ x.__rshift__(y) <==> x<<yx.__rshift__(y) <==> x<<y """
  pass
 def __mod__(self,*args):
  """ x.__mod__(y) <==> x%yx.__mod__(y) <==> x%y """
  pass
 def __mul__(self,*args):
  """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
  pass
 def __neg__(self,*args):
  """ x.__neg__() <==> -x """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """
  __new__(cls: type,value: object) -> object

  __new__(cls: type) -> object
  """
  pass
 def __nonzero__(self,*args):
  """ __nonzero__(x: Byte) -> bool """
  pass
 def __or__(self,*args):
  """
  __or__(x: Byte,y: SByte) -> Int16

  __or__(x: Byte,y: Byte) -> Byte
  """
  pass
 def __pos__(self,*args):
  """ __pos__(x: Byte) -> Byte """
  pass
 def __pow__(self,*args):
  """ x.__pow__(y[,z]) <==> pow(x,y[,z])x.__pow__(y[,z]) <==> pow(x,y[,z]) """
  pass
 def __radd__(self,*args):
  """
  __radd__(x: SByte,y: Byte) -> object

  __radd__(x: Byte,y: Byte) -> object
  """
  pass
 def __rand__(self,*args):
  """
  __rand__(x: SByte,y: Byte) -> Int16

  __rand__(x: Byte,y: Byte) -> Byte
  """
  pass
 def __rdiv__(self,*args):
  """
  __rdiv__(x: SByte,y: Byte) -> object

  __rdiv__(x: Byte,y: Byte) -> object
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(x: Byte) -> str """
  pass
 def __rfloordiv__(self,*args):
  """
  __rfloordiv__(x: SByte,y: Byte) -> object

  __rfloordiv__(x: Byte,y: Byte) -> Byte
  """
  pass
 def __rmod__(self,*args):
  """
  __rmod__(x: SByte,y: Byte) -> Int16

  __rmod__(x: Byte,y: Byte) -> Byte
  """
  pass
 def __rmul__(self,*args):
  """
  __rmul__(x: SByte,y: Byte) -> object

  __rmul__(x: Byte,y: Byte) -> object
  """
  pass
 def __ror__(self,*args):
  """
  __ror__(x: SByte,y: Byte) -> Int16

  __ror__(x: Byte,y: Byte) -> Byte
  """
  pass
 def __rpow__(self,*args):
  """
  __rpow__(x: SByte,y: Byte) -> object

  __rpow__(x: Byte,y: Byte) -> object
  """
  pass
 def __rshift__(self,*args):
  """ x.__rshift__(y) <==> x>>yx.__rshift__(y) <==> x>>y """
  pass
 def __rsub__(self,*args):
  """
  __rsub__(x: SByte,y: Byte) -> object

  __rsub__(x: Byte,y: Byte) -> object
  """
  pass
 def __rtruediv__(self,*args):
  """
  __rtruediv__(x: SByte,y: Byte) -> float

  __rtruediv__(x: Byte,y: Byte) -> float
  """
  pass
 def __rxor__(self,*args):
  """
  __rxor__(x: SByte,y: Byte) -> Int16

  __rxor__(x: Byte,y: Byte) -> Byte
  """
  pass
 def __str__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
  pass
 def __truediv__(self,*args):
  """ x.__truediv__(y) <==> x/yx.__truediv__(y) <==> x/y """
  pass
 def __trunc__(self,*args):
  """ __trunc__(x: Byte) -> Byte """
  pass
 def __xor__(self,*args):
  """
  __xor__(x: Byte,y: SByte) -> Int16

  __xor__(x: Byte,y: Byte) -> Byte
  """
  pass
 denominator=None
 imag=None
 MaxValue=None
 MinValue=None
 numerator=None
 real=None

