class Int16(object,IComparable,IFormattable,IConvertible,IComparable[Int16],IEquatable[Int16]):
 """ Represents a 16-bit signed integer. """
 def bit_length(self,*args):
  """ bit_length(value: Int16) -> int """
  pass
 def CompareTo(self,value):
  """
  CompareTo(self: Int16,value: Int16) -> int

  

   Compares this instance to a specified 16-bit signed integer and returns an integer that 

    indicates whether the value of this instance is less than,equal to,or greater than the value 

    of the specified 16-bit signed integer.

  

  

   value: An integer to compare.

   Returns: A signed number indicating the relative values of this instance and value.Return Value 

    Description Less than zero This instance is less than value. Zero This instance is equal to 

    value. Greater than zero This instance is greater than value.

  

  CompareTo(self: Int16,value: object) -> int

  

   Compares this instance to a specified object and returns an integer that indicates whether the 

    value of this instance is less than,equal to,or greater than the value of the object.

  

  

   value: An object to compare,or null.

   Returns: A signed number indicating the relative values of this instance and value.Return Value 

    Description Less than zero This instance is less than value. Zero This instance is equal to 

    value. Greater than zero This instance is greater than value.-or- value is null.
  """
  pass
 def conjugate(self,*args):
  """ conjugate(x: Int16) -> Int16 """
  pass
 def Equals(self,obj):
  """
  Equals(self: Int16,obj: Int16) -> bool

  

   Returns a value indicating whether this instance is equal to a specified System.Int16 value.

  

   obj: An System.Int16 value to compare to this instance.

   Returns: true if obj has the same value as this instance; otherwise,false.

  Equals(self: Int16,obj: object) -> bool

  

   Returns a value indicating whether this instance is equal to a specified object.

  

   obj: An object to compare to this instance.

   Returns: true if obj is an instance of System.Int16 and equals the value of this instance; otherwise,

    false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Int16) -> int

  

   Returns the hash code for this instance.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def GetTypeCode(self):
  """
  GetTypeCode(self: Int16) -> TypeCode

  

   Returns the System.TypeCode for value type System.Int16.

   Returns: The enumerated constant,System.TypeCode.Int16.
  """
  pass
 @staticmethod
 def Parse(s,*__args):
  """
  Parse(s: str,provider: IFormatProvider) -> Int16

  

   Converts the string representation of a number in a specified culture-specific format to its 

    16-bit signed integer equivalent.

  

  

   s: A string containing a number to convert.

   provider: An System.IFormatProvider that supplies culture-specific formatting information about s.

   Returns: A 16-bit signed integer equivalent to the number specified in s.

  Parse(s: str,style: NumberStyles,provider: IFormatProvider) -> Int16

  

   Converts the string representation of a number in a specified style and culture-specific format 

    to its 16-bit signed integer equivalent.

  

  

   s: A string containing a number to convert.

   style: A bitwise combination of enumeration values that indicates the style elements that can be 

    present in s. A typical value to specify is System.Globalization.NumberStyles.Integer.

  

   provider: An System.IFormatProvider that supplies culture-specific formatting information about s.

   Returns: A 16-bit signed integer equivalent to the number specified in s.

  Parse(s: str) -> Int16

  

   Converts the string representation of a number to its 16-bit signed integer equivalent.

  

   s: A string containing a number to convert.

   Returns: A 16-bit signed integer equivalent to the number contained in s.

  Parse(s: str,style: NumberStyles) -> Int16

  

   Converts the string representation of a number in a specified style to its 16-bit signed integer 

    equivalent.

  

  

   s: A string containing a number to convert.

   style: A bitwise combination of the enumeration values that indicates the style elements that can be 

    present in s. A typical value to specify is System.Globalization.NumberStyles.Integer.

  

   Returns: A 16-bit signed integer equivalent to the number specified in s.
  """
  pass
 def ToString(self,*__args):
  """
  ToString(self: Int16,format: str) -> str

  

   Converts the numeric value of this instance to its equivalent string representation,using the 

    specified format.

  

  

   format: A numeric format string.

   Returns: The string representation of the value of this instance as specified by format.

  ToString(self: Int16,format: str,provider: IFormatProvider) -> str

  

   Converts the numeric value of this instance to its equivalent string representation using the 

    specified format and culture-specific formatting information.

  

  

   format: A numeric format string.

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of the value of this instance as specified by format and provider.

  ToString(self: Int16) -> str

  

   Converts the numeric value of this instance to its equivalent string representation.

   Returns: The string representation of the value of this instance,consisting of a minus sign if the value 

    is negative,and a sequence of digits ranging from 0 to 9 with no leading zeroes.

  

  ToString(self: Int16,provider: IFormatProvider) -> str

  

   Converts the numeric value of this instance to its equivalent string representation using the 

    specified culture-specific format information.

  

  

   provider: An System.IFormatProvider that supplies culture-specific formatting information.

   Returns: The string representation of the value of this instance as specified by provider.
  """
  pass
 @staticmethod
 def TryParse(s,*__args):
  """
  TryParse(s: str,style: NumberStyles,provider: IFormatProvider) -> (bool,Int16)

  

   Converts the string representation of a number in a specified style and culture-specific format 

    to its 16-bit signed integer equivalent. A return value indicates whether the conversion 

    succeeded or failed.

  

  

   s: A string containing a number to convert. The string is interpreted using the style specified by 

    style.

  

   style: A bitwise combination of enumeration values that indicates the style elements that can be 

    present in s. A typical value to specify is System.Globalization.NumberStyles.Integer.

  

   provider: An object that supplies culture-specific formatting information about s.

   Returns: true if s was converted successfully; otherwise,false.

  TryParse(s: str) -> (bool,Int16)

  

   Converts the string representation of a number to its 16-bit signed integer equivalent. A return 

    value indicates whether the conversion succeeded or failed.

  

  

   s: A string containing a number to convert.

   Returns: true if s was converted successfully; otherwise,false.
  """
  pass
 def __abs__(self,*args):
  """ x.__abs__() <==> abs(x) """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __and__(self,*args):
  """ __and__(x: Int16,y: Int16) -> Int16 """
  pass
 def __cmp__(self,*args):
  """ x.__cmp__(y) <==> cmp(x,y) """
  pass
 def __div__(self,*args):
  """ x.__div__(y) <==> x/y """
  pass
 def __float__(self,*args):
  """ __float__(x: Int16) -> float """
  pass
 def __floordiv__(self,*args):
  """ x.__floordiv__(y) <==> x//y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __hash__(self,*args):
  """ x.__hash__() <==> hash(x) """
  pass
 def __hex__(self,*args):
  """ __hex__(value: Int16) -> str """
  pass
 def __index__(self,*args):
  """ __index__(x: Int16) -> int """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __int__(self,*args):
  """ __int__(x: Int16) -> int """
  pass
 def __invert__(self,*args):
  """ __invert__(x: Int16) -> Int16 """
  pass
 def __lshift__(self,*args):
  """ x.__rshift__(y) <==> x<<yx.__rshift__(y) <==> x<<y """
  pass
 def __mod__(self,*args):
  """ x.__mod__(y) <==> x%y """
  pass
 def __mul__(self,*args):
  """ x.__mul__(y) <==> x*y """
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
  """ __nonzero__(x: Int16) -> bool """
  pass
 def __or__(self,*args):
  """ __or__(x: Int16,y: Int16) -> Int16 """
  pass
 def __pos__(self,*args):
  """ __pos__(x: Int16) -> Int16 """
  pass
 def __pow__(self,*args):
  """ x.__pow__(y[,z]) <==> pow(x,y[,z]) """
  pass
 def __radd__(self,*args):
  """ __radd__(x: Int16,y: Int16) -> object """
  pass
 def __rand__(self,*args):
  """ __rand__(x: Int16,y: Int16) -> Int16 """
  pass
 def __rdiv__(self,*args):
  """ __rdiv__(x: Int16,y: Int16) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(x: Int16) -> str """
  pass
 def __rfloordiv__(self,*args):
  """ __rfloordiv__(x: Int16,y: Int16) -> object """
  pass
 def __rmod__(self,*args):
  """ __rmod__(x: Int16,y: Int16) -> Int16 """
  pass
 def __rmul__(self,*args):
  """ __rmul__(x: Int16,y: Int16) -> object """
  pass
 def __ror__(self,*args):
  """ __ror__(x: Int16,y: Int16) -> Int16 """
  pass
 def __rpow__(self,*args):
  """ __rpow__(x: Int16,y: Int16) -> object """
  pass
 def __rshift__(self,*args):
  """ x.__rshift__(y) <==> x>>yx.__rshift__(y) <==> x>>y """
  pass
 def __rsub__(self,*args):
  """ __rsub__(x: Int16,y: Int16) -> object """
  pass
 def __rtruediv__(self,*args):
  """ __rtruediv__(x: Int16,y: Int16) -> float """
  pass
 def __rxor__(self,*args):
  """ __rxor__(x: Int16,y: Int16) -> Int16 """
  pass
 def __str__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-y """
  pass
 def __truediv__(self,*args):
  """ x.__truediv__(y) <==> x/y """
  pass
 def __trunc__(self,*args):
  """ __trunc__(x: Int16) -> Int16 """
  pass
 def __xor__(self,*args):
  """ __xor__(x: Int16,y: Int16) -> Int16 """
  pass
 denominator=None
 imag=None
 MaxValue=None
 MinValue=None
 numerator=None
 real=None

