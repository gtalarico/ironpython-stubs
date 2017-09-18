class SByte(object,IComparable,IFormattable,IConvertible,IComparable[SByte],IEquatable[SByte]):
 """ Represents an 8-bit signed integer. """
 def bit_length(self,*args):
  """ bit_length(value: SByte) -> int """
  pass
 def CompareTo(self,*__args):
  """
  CompareTo(self: SByte,value: SByte) -> int

  

   Compares this instance to a specified 8-bit signed integer and returns an indication of their 

    relative values.

  

  

   value: An 8-bit signed integer to compare.

   Returns: A signed integer that indicates the relative order of this instance and value.Return Value 

    Description Less than zero This instance is less than value. Zero This instance is equal to 

    value. Greater than zero This instance is greater than value.

  

  CompareTo(self: SByte,obj: object) -> int

  

   Compares this instance to a specified object and returns an indication of their relative values.

  

   obj: An object to compare,or null.

   Returns: A signed number indicating the relative values of this instance and obj.Return Value Description 

    Less than zero This instance is less than obj. Zero This instance is equal to obj. Greater than 

    zero This instance is greater than obj.-or- obj is null.
  """
  pass
 def conjugate(self,*args):
  """ conjugate(x: SByte) -> SByte """
  pass
 def Equals(self,obj):
  """
  Equals(self: SByte,obj: SByte) -> bool

  

   Returns a value indicating whether this instance is equal to a specified System.SByte value.

  

   obj: An System.SByte value to compare to this instance.

   Returns: true if obj has the same value as this instance; otherwise,false.

  Equals(self: SByte,obj: object) -> bool

  

   Returns a value indicating whether this instance is equal to a specified object.

  

   obj: An object to compare with this instance.

   Returns: true if obj is an instance of System.SByte and equals the value of this instance; otherwise,

    false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: SByte) -> int

  

   Returns the hash code for this instance.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def GetTypeCode(self):
  """
  GetTypeCode(self: SByte) -> TypeCode

  

   Returns the System.TypeCode for value type System.SByte.

   Returns: The enumerated constant,System.TypeCode.SByte.
  """
  pass
 @staticmethod
 def Parse(s,*__args):
  """
  Parse(s: str,provider: IFormatProvider) -> SByte

  

   Converts the string representation of a number in a specified culture-specific format to its 

    8-bit signed integer equivalent.

  

  

   s: A string that represents a number to convert. The string is interpreted using the 

    System.Globalization.NumberStyles.Integer style.

  

   provider: An object that supplies culture-specific formatting information about s. If provider is null,

    the thread current culture is used.

  

   Returns: An 8-bit signed integer that is equivalent to the number specified in s.

  Parse(s: str,style: NumberStyles,provider: IFormatProvider) -> SByte

  

   Converts the string representation of a number that is in a specified style and culture-specific 

    format to its 8-bit signed equivalent.

  

  

   s: A string that contains the number to convert. The string is interpreted by using the style 

    specified by style.

  

   style: A bitwise combination of the enumeration values that indicates the style elements that can be 

    present in s. A typical value to specify is System.Globalization.NumberStyles.Integer.

  

   provider: An object that supplies culture-specific formatting information about s. If provider is null,

    the thread current culture is used.

  

   Returns: An 8-bit signed byte value that is equivalent to the number specified in the s parameter.

  Parse(s: str) -> SByte

  

   Converts the string representation of a number to its 8-bit signed integer equivalent.

  

   s: A string that represents a number to convert. The string is interpreted using the 

    System.Globalization.NumberStyles.Integer style.

  

   Returns: An 8-bit signed integer that is equivalent to the number contained in the s parameter.

  Parse(s: str,style: NumberStyles) -> SByte

  

   Converts the string representation of a number in a specified style to its 8-bit signed integer 

    equivalent.

  

  

   s: A string that contains a number to convert. The string is interpreted using the style specified 

    by style.

  

   style: A bitwise combination of the enumeration values that indicates the style elements that can be 

    present in s. A typical value to specify is System.Globalization.NumberStyles.Integer.

  

   Returns: An 8-bit signed integer that is equivalent to the number specified in s.
  """
  pass
 def ToString(self,*__args):
  """
  ToString(self: SByte,format: str) -> str

  

   Converts the numeric value of this instance to its equivalent string representation,using the 

    specified format.

  

  

   format: A standard or custom numeric format string.

   Returns: The string representation of the value of this instance as specified by format.

  ToString(self: SByte,format: str,provider: IFormatProvider) -> str

  

   Converts the numeric value of this instance to its equivalent string representation using the 

    specified format and culture-specific format information.

  

  

   format: A standard or custom numeric format string.

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of the value of this instance as specified by format and provider.

  ToString(self: SByte) -> str

  

   Converts the numeric value of this instance to its equivalent string representation.

   Returns: The string representation of the value of this instance,consisting of a negative sign if the 

    value is negative,and a sequence of digits ranging from 0 to 9 with no leading zeroes.

  

  ToString(self: SByte,provider: IFormatProvider) -> str

  

   Converts the numeric value of this instance to its equivalent string representation using the 

    specified culture-specific format information.

  

  

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of the value of this instance,as specified by provider.
  """
  pass
 @staticmethod
 def TryParse(s,*__args):
  """
  TryParse(s: str,style: NumberStyles,provider: IFormatProvider) -> (bool,SByte)

  

   Tries to convert the string representation of a number in a specified style and culture-specific 

    format to its System.SByte equivalent,and returns a value that indicates whether the conversion 

    succeeded.

  

  

   s: A string representing a number to convert.

   style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical 

    value to specify is System.Globalization.NumberStyles.Integer.

  

   provider: An object that supplies culture-specific formatting information about s.

   Returns: true if s was converted successfully; otherwise,false.

  TryParse(s: str) -> (bool,SByte)

  

   Tries to convert the string representation of a number to its System.SByte equivalent,and 

    returns a value that indicates whether the conversion succeeded.

  

  

   s: A string that contains a number to convert.

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
  """ __and__(x: SByte,y: SByte) -> SByte """
  pass
 def __cmp__(self,*args):
  """ x.__cmp__(y) <==> cmp(x,y) """
  pass
 def __div__(self,*args):
  """ x.__div__(y) <==> x/y """
  pass
 def __float__(self,*args):
  """ __float__(x: SByte) -> float """
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
  """ __hex__(value: SByte) -> str """
  pass
 def __index__(self,*args):
  """ __index__(x: SByte) -> int """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __int__(self,*args):
  """ __int__(x: SByte) -> int """
  pass
 def __invert__(self,*args):
  """ __invert__(x: SByte) -> SByte """
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
  """ __nonzero__(x: SByte) -> bool """
  pass
 def __or__(self,*args):
  """ __or__(x: SByte,y: SByte) -> SByte """
  pass
 def __pos__(self,*args):
  """ __pos__(x: SByte) -> SByte """
  pass
 def __pow__(self,*args):
  """ x.__pow__(y[,z]) <==> pow(x,y[,z]) """
  pass
 def __radd__(self,*args):
  """ __radd__(x: SByte,y: SByte) -> object """
  pass
 def __rand__(self,*args):
  """ __rand__(x: SByte,y: SByte) -> SByte """
  pass
 def __rdiv__(self,*args):
  """ __rdiv__(x: SByte,y: SByte) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(x: SByte) -> str """
  pass
 def __rfloordiv__(self,*args):
  """ __rfloordiv__(x: SByte,y: SByte) -> object """
  pass
 def __rmod__(self,*args):
  """ __rmod__(x: SByte,y: SByte) -> SByte """
  pass
 def __rmul__(self,*args):
  """ __rmul__(x: SByte,y: SByte) -> object """
  pass
 def __ror__(self,*args):
  """ __ror__(x: SByte,y: SByte) -> SByte """
  pass
 def __rpow__(self,*args):
  """ __rpow__(x: SByte,y: SByte) -> object """
  pass
 def __rshift__(self,*args):
  """ x.__rshift__(y) <==> x>>yx.__rshift__(y) <==> x>>y """
  pass
 def __rsub__(self,*args):
  """ __rsub__(x: SByte,y: SByte) -> object """
  pass
 def __rtruediv__(self,*args):
  """ __rtruediv__(x: SByte,y: SByte) -> float """
  pass
 def __rxor__(self,*args):
  """ __rxor__(x: SByte,y: SByte) -> SByte """
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
  """ __trunc__(x: SByte) -> SByte """
  pass
 def __xor__(self,*args):
  """ __xor__(x: SByte,y: SByte) -> SByte """
  pass
 denominator=None
 imag=None
 MaxValue=None
 MinValue=None
 numerator=None
 real=None

