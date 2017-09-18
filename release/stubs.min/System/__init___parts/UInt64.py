class UInt64(object,IComparable,IFormattable,IConvertible,IComparable[UInt64],IEquatable[UInt64]):
 """ Represents a 64-bit unsigned integer. """
 def bit_length(self,*args):
  """ bit_length(value: UInt64) -> int """
  pass
 def CompareTo(self,value):
  """
  CompareTo(self: UInt64,value: UInt64) -> int

  

   Compares this instance to a specified 64-bit unsigned integer and returns an indication of their 

    relative values.

  

  

   value: An unsigned integer to compare.

   Returns: A signed number indicating the relative values of this instance and value.Return Value 

    Description Less than zero This instance is less than value. Zero This instance is equal to 

    value. Greater than zero This instance is greater than value.

  

  CompareTo(self: UInt64,value: object) -> int

  

   Compares this instance to a specified object and returns an indication of their relative values.

  

   value: An object to compare,or null.

   Returns: A signed number indicating the relative values of this instance and value.Return Value 

    Description Less than zero This instance is less than value. Zero This instance is equal to 

    value. Greater than zero This instance is greater than value.-or- value is null.
  """
  pass
 def conjugate(self,*args):
  """ conjugate(x: UInt64) -> UInt64 """
  pass
 def Equals(self,obj):
  """
  Equals(self: UInt64,obj: UInt64) -> bool

  

   Returns a value indicating whether this instance is equal to a specified System.UInt64 value.

  

   obj: A System.UInt64 value to compare to this instance.

   Returns: true if obj has the same value as this instance; otherwise,false.

  Equals(self: UInt64,obj: object) -> bool

  

   Returns a value indicating whether this instance is equal to a specified object.

  

   obj: An object to compare to this instance.

   Returns: true if obj is an instance of System.UInt64 and equals the value of this instance; otherwise,

    false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: UInt64) -> int

  

   Returns the hash code for this instance.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def GetTypeCode(self):
  """
  GetTypeCode(self: UInt64) -> TypeCode

  

   Returns the System.TypeCode for value type System.UInt64.

   Returns: The enumerated constant,System.TypeCode.UInt64.
  """
  pass
 @staticmethod
 def Parse(s,*__args):
  """
  Parse(s: str,provider: IFormatProvider) -> UInt64

  

   Converts the string representation of a number in a specified culture-specific format to its 

    64-bit unsigned integer equivalent.

  

  

   s: A string that represents the number to convert.

   provider: An object that supplies culture-specific formatting information about s.

   Returns: A 64-bit unsigned integer equivalent to the number specified in s.

  Parse(s: str,style: NumberStyles,provider: IFormatProvider) -> UInt64

  

   Converts the string representation of a number in a specified style and culture-specific format 

    to its 64-bit unsigned integer equivalent.

  

  

   s: A string that represents the number to convert. The string is interpreted by using the style 

    specified by the style parameter.

  

   style: A bitwise combination of enumeration values that indicates the style elements that can be 

    present in s. A typical value to specify is System.Globalization.NumberStyles.Integer.

  

   provider: An object that supplies culture-specific formatting information about s.

   Returns: A 64-bit unsigned integer equivalent to the number specified in s.

  Parse(s: str) -> UInt64

  

   Converts the string representation of a number to its 64-bit unsigned integer equivalent.

  

   s: A string that represents the number to convert.

   Returns: A 64-bit unsigned integer equivalent to the number contained in s.

  Parse(s: str,style: NumberStyles) -> UInt64

  

   Converts the string representation of a number in a specified style to its 64-bit unsigned 

    integer equivalent.

  

  

   s: A string that represents the number to convert. The string is interpreted by using the style 

    specified by the style parameter.

  

   style: A bitwise combination of the enumeration values that specifies the permitted format of s. A 

    typical value to specify is System.Globalization.NumberStyles.Integer.

  

   Returns: A 64-bit unsigned integer equivalent to the number specified in s.
  """
  pass
 def ToString(self,*__args):
  """
  ToString(self: UInt64,format: str) -> str

  

   Converts the numeric value of this instance to its equivalent string representation using the 

    specified format.

  

  

   format: A numeric format string.

   Returns: The string representation of the value of this instance as specified by format.

  ToString(self: UInt64,format: str,provider: IFormatProvider) -> str

  

   Converts the numeric value of this instance to its equivalent string representation using the 

    specified format and culture-specific format information.

  

  

   format: A numeric format string.

   provider: An object that supplies culture-specific formatting information about this instance.

   Returns: The string representation of the value of this instance as specified by format and provider.

  ToString(self: UInt64) -> str

  

   Converts the numeric value of this instance to its equivalent string representation.

   Returns: The string representation of the value of this instance,consisting of a sequence of digits 

    ranging from 0 to 9,without a sign or leading zeroes.

  

  ToString(self: UInt64,provider: IFormatProvider) -> str

  

   Converts the numeric value of this instance to its equivalent string representation using the 

    specified culture-specific format information.

  

  

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of the value of this instance as specified by provider.
  """
  pass
 @staticmethod
 def TryParse(s,*__args):
  """
  TryParse(s: str,style: NumberStyles,provider: IFormatProvider) -> (bool,UInt64)

  

   Tries to convert the string representation of a number in a specified style and culture-specific 

    format to its 64-bit unsigned integer equivalent. A return value indicates whether the 

    conversion succeeded or failed.

  

  

   s: A string that represents the number to convert. The string is interpreted by using the style 

    specified by the style parameter.

  

   style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical 

    value to specify is System.Globalization.NumberStyles.Integer.

  

   provider: An object that supplies culture-specific formatting information about s.

   Returns: true if s was converted successfully; otherwise,false.

  TryParse(s: str) -> (bool,UInt64)

  

   Tries to convert the string representation of a number to its 64-bit unsigned integer 

    equivalent. A return value indicates whether the conversion succeeded or failed.

  

  

   s: A string that represents the number to convert.

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
  __and__(x: UInt64,y: Int64) -> long

  __and__(x: UInt64,y: UInt64) -> UInt64
  """
  pass
 def __cmp__(self,*args):
  """ x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y) """
  pass
 def __div__(self,*args):
  """ x.__div__(y) <==> x/yx.__div__(y) <==> x/y """
  pass
 def __float__(self,*args):
  """ __float__(x: UInt64) -> float """
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
  """ __hex__(value: UInt64) -> str """
  pass
 def __index__(self,*args):
  """ __index__(x: UInt64) -> long """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __int__(self,*args):
  """ __int__(x: UInt64) -> int """
  pass
 def __invert__(self,*args):
  """ __invert__(x: UInt64) -> object """
  pass
 def __lshift__(self,*args):
  """ x.__rshift__(y) <==> x<<y """
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
  """ __nonzero__(x: UInt64) -> bool """
  pass
 def __or__(self,*args):
  """
  __or__(x: UInt64,y: Int64) -> long

  __or__(x: UInt64,y: UInt64) -> UInt64
  """
  pass
 def __pos__(self,*args):
  """ __pos__(x: UInt64) -> UInt64 """
  pass
 def __pow__(self,*args):
  """ x.__pow__(y[,z]) <==> pow(x,y[,z])x.__pow__(y[,z]) <==> pow(x,y[,z]) """
  pass
 def __radd__(self,*args):
  """
  __radd__(x: Int64,y: UInt64) -> object

  __radd__(x: UInt64,y: UInt64) -> object
  """
  pass
 def __rand__(self,*args):
  """
  __rand__(x: Int64,y: UInt64) -> long

  __rand__(x: UInt64,y: UInt64) -> UInt64
  """
  pass
 def __rdiv__(self,*args):
  """
  __rdiv__(x: Int64,y: UInt64) -> object

  __rdiv__(x: UInt64,y: UInt64) -> object
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(x: UInt64) -> str """
  pass
 def __rfloordiv__(self,*args):
  """
  __rfloordiv__(x: Int64,y: UInt64) -> object

  __rfloordiv__(x: UInt64,y: UInt64) -> UInt64
  """
  pass
 def __rmod__(self,*args):
  """
  __rmod__(x: Int64,y: UInt64) -> long

  __rmod__(x: UInt64,y: UInt64) -> UInt64
  """
  pass
 def __rmul__(self,*args):
  """
  __rmul__(x: Int64,y: UInt64) -> object

  __rmul__(x: UInt64,y: UInt64) -> object
  """
  pass
 def __ror__(self,*args):
  """
  __ror__(x: Int64,y: UInt64) -> long

  __ror__(x: UInt64,y: UInt64) -> UInt64
  """
  pass
 def __rpow__(self,*args):
  """
  __rpow__(x: Int64,y: UInt64) -> object

  __rpow__(x: UInt64,y: UInt64) -> object
  """
  pass
 def __rshift__(self,*args):
  """ x.__rshift__(y) <==> x>>y """
  pass
 def __rsub__(self,*args):
  """
  __rsub__(x: Int64,y: UInt64) -> object

  __rsub__(x: UInt64,y: UInt64) -> object
  """
  pass
 def __rtruediv__(self,*args):
  """
  __rtruediv__(x: Int64,y: UInt64) -> float

  __rtruediv__(x: UInt64,y: UInt64) -> float
  """
  pass
 def __rxor__(self,*args):
  """
  __rxor__(x: Int64,y: UInt64) -> long

  __rxor__(x: UInt64,y: UInt64) -> UInt64
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
  """ __trunc__(x: UInt64) -> UInt64 """
  pass
 def __xor__(self,*args):
  """
  __xor__(x: UInt64,y: Int64) -> long

  __xor__(x: UInt64,y: UInt64) -> UInt64
  """
  pass
 denominator=None
 imag=None
 MaxValue=None
 MinValue=None
 numerator=None
 real=None

