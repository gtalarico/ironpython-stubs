class Single(object,IComparable,IFormattable,IConvertible,IComparable[Single],IEquatable[Single]):
 """ Represents a single-precision floating-point number. """
 def CompareTo(self,value):
  """
  CompareTo(self: Single,value: Single) -> int

  

   Compares this instance to a specified single-precision floating-point number and returns an 

    integer that indicates whether the value of this instance is less than,equal to,or greater 

    than the value of the specified single-precision floating-point number.

  

  

   value: A single-precision floating-point number to compare.

   Returns: A signed number indicating the relative values of this instance and value.Return Value 

    Description Less than zero This instance is less than value.-or- This instance is not a number 

    (System.Single.NaN) and value is a number. Zero This instance is equal to value.-or- Both this 

    instance and value are not a number (System.Single.NaN),System.Single.PositiveInfinity,or 

    System.Single.NegativeInfinity. Greater than zero This instance is greater than value.-or- This 

    instance is a number and value is not a number (System.Single.NaN).

  

  CompareTo(self: Single,value: object) -> int

  

   Compares this instance to a specified object and returns an integer that indicates whether the 

    value of this instance is less than,equal to,or greater than the value of the specified 

    object.

  

  

   value: An object to compare,or null.

   Returns: A signed number indicating the relative values of this instance and value.Return Value 

    Description Less than zero This instance is less than value.-or- This instance is not a number 

    (System.Single.NaN) and value is a number. Zero This instance is equal to value.-or- This 

    instance and value are both not a number (System.Single.NaN),System.Single.PositiveInfinity,or 

    System.Single.NegativeInfinity. Greater than zero This instance is greater than value.-or- This 

    instance is a number and value is not a number (System.Single.NaN).-or- value is null.
  """
  pass
 def conjugate(self,*args):
  """ conjugate(x: Single) -> Single """
  pass
 def Equals(self,obj):
  """
  Equals(self: Single,obj: Single) -> bool

  

   Returns a value indicating whether this instance and a specified System.Single object represent 

    the same value.

  

  

   obj: An object to compare with this instance.

   Returns: true if obj is equal to this instance; otherwise,false.

  Equals(self: Single,obj: object) -> bool

  

   Returns a value indicating whether this instance is equal to a specified object.

  

   obj: An object to compare with this instance.

   Returns: true if obj is an instance of System.Single and equals the value of this instance; otherwise,

    false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Single) -> int

  

   Returns the hash code for this instance.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def GetTypeCode(self):
  """
  GetTypeCode(self: Single) -> TypeCode

  

   Returns the System.TypeCode for value type System.Single.

   Returns: The enumerated constant,System.TypeCode.Single.
  """
  pass
 @staticmethod
 def IsInfinity(f):
  """
  IsInfinity(f: Single) -> bool

  

   Returns a value indicating whether the specified number evaluates to negative or positive 

    infinity.

  

  

   f: A single-precision floating-point number.

   Returns: true if f evaluates to System.Single.PositiveInfinity or System.Single.NegativeInfinity; 

    otherwise,false.
  """
  pass
 @staticmethod
 def IsNaN(f):
  """
  IsNaN(f: Single) -> bool

  

   Returns a value indicating whether the specified number evaluates to not a number 

    (System.Single.NaN).

  

  

   f: A single-precision floating-point number.

   Returns: true if f evaluates to not a number (System.Single.NaN); otherwise,false.
  """
  pass
 @staticmethod
 def IsNegativeInfinity(f):
  """
  IsNegativeInfinity(f: Single) -> bool

  

   Returns a value indicating whether the specified number evaluates to negative infinity.

  

   f: A single-precision floating-point number.

   Returns: true if f evaluates to System.Single.NegativeInfinity; otherwise,false.
  """
  pass
 @staticmethod
 def IsPositiveInfinity(f):
  """
  IsPositiveInfinity(f: Single) -> bool

  

   Returns a value indicating whether the specified number evaluates to positive infinity.

  

   f: A single-precision floating-point number.

   Returns: true if f evaluates to System.Single.PositiveInfinity; otherwise,false.
  """
  pass
 @staticmethod
 def Parse(s,*__args):
  """
  Parse(s: str,provider: IFormatProvider) -> Single

  

   Converts the string representation of a number in a specified culture-specific format to its 

    single-precision floating-point number equivalent.

  

  

   s: A string that contains a number to convert.

   provider: An object that supplies culture-specific formatting information about s.

   Returns: A single-precision floating-point number equivalent to the numeric value or symbol specified in 

    s.

  

  Parse(s: str,style: NumberStyles,provider: IFormatProvider) -> Single

  

   Converts the string representation of a number in a specified style and culture-specific format 

    to its single-precision floating-point number equivalent.

  

  

   s: A string that contains a number to convert.

   style: A bitwise combination of enumeration values that indicates the style elements that can be 

    present in s. A typical value to specify is System.Globalization.NumberStyles.Float combined 

    with System.Globalization.NumberStyles.AllowThousands.

  

   provider: An object that supplies culture-specific formatting information about s.

   Returns: A single-precision floating-point number equivalent to the numeric value or symbol specified in 

    s.

  

  Parse(s: str) -> Single

  

   Converts the string representation of a number to its single-precision floating-point number 

    equivalent.

  

  

   s: A string that contains a number to convert.

   Returns: A single-precision floating-point number equivalent to the numeric value or symbol specified in 

    s.

  

  Parse(s: str,style: NumberStyles) -> Single

  

   Converts the string representation of a number in a specified style to its single-precision 

    floating-point number equivalent.

  

  

   s: A string that contains a number to convert.

   style: A bitwise combination of enumeration values that indicates the style elements that can be 

    present in s. A typical value to specify is System.Globalization.NumberStyles.Float combined 

    with System.Globalization.NumberStyles.AllowThousands.

  

   Returns: A single-precision floating-point number that is equivalent to the numeric value or symbol 

    specified in s.
  """
  pass
 def ToString(self,*__args):
  """
  ToString(self: Single,format: str) -> str

  

   Converts the numeric value of this instance to its equivalent string representation,using the 

    specified format.

  

  

   format: A numeric format string.

   Returns: The string representation of the value of this instance as specified by format.

  ToString(self: Single,format: str,provider: IFormatProvider) -> str

  

   Converts the numeric value of this instance to its equivalent string representation using the 

    specified format and culture-specific format information.

  

  

   format: A numeric format string.

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of the value of this instance as specified by format and provider.

  ToString(self: Single) -> str

  

   Converts the numeric value of this instance to its equivalent string representation.

   Returns: The string representation of the value of this instance.

  ToString(self: Single,provider: IFormatProvider) -> str

  

   Converts the numeric value of this instance to its equivalent string representation using the 

    specified culture-specific format information.

  

  

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of the value of this instance as specified by provider.
  """
  pass
 @staticmethod
 def TryParse(s,*__args):
  """
  TryParse(s: str,style: NumberStyles,provider: IFormatProvider) -> (bool,Single)

  

   Converts the string representation of a number in a specified style and culture-specific format 

    to its single-precision floating-point number equivalent. A return value indicates whether the 

    conversion succeeded or failed.

  

  

   s: A string representing a number to convert.

   style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical 

    value to specify is System.Globalization.NumberStyles.Float combined with 

    System.Globalization.NumberStyles.AllowThousands.

  

   provider: An object that supplies culture-specific formatting information about s.

   Returns: true if s was converted successfully; otherwise,false.

  TryParse(s: str) -> (bool,Single)

  

   Converts the string representation of a number to its single-precision floating-point number 

    equivalent. A return value indicates whether the conversion succeeded or failed.

  

  

   s: A string representing a number to convert.

   Returns: true if s was converted successfully; otherwise,false.
  """
  pass
 def __abs__(self,*args):
  """ x.__abs__() <==> abs(x) """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __div__(self,*args):
  """ x.__div__(y) <==> x/y """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __float__(self,*args):
  """ __float__(x: Single) -> float """
  pass
 def __floordiv__(self,*args):
  """ x.__floordiv__(y) <==> x//y """
  pass
 def __format__(self,*args):
  """ __format__(self: Single,formatSpec: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __hash__(self,*args):
  """ x.__hash__() <==> hash(x) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __int__(self,*args):
  """ __int__(x: Single) -> int """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
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
  __new__(cls: type,s: IList[Byte]) -> object

  __new__(cls: type,x: object) -> object

  __new__(cls: type) -> object
  """
  pass
 def __ne__(self,*args):
  pass
 def __nonzero__(self,*args):
  """ __nonzero__(x: Single) -> bool """
  pass
 def __pos__(self,*args):
  """ __pos__(x: Single) -> Single """
  pass
 def __pow__(self,*args):
  """ x.__pow__(y[,z]) <==> pow(x,y[,z]) """
  pass
 def __radd__(self,*args):
  """ __radd__(x: Single,y: Single) -> Single """
  pass
 def __rdiv__(self,*args):
  """ __rdiv__(x: Single,y: Single) -> Single """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: Single) -> str """
  pass
 def __rfloordiv__(self,*args):
  """ __rfloordiv__(x: Single,y: Single) -> Single """
  pass
 def __rmod__(self,*args):
  """ __rmod__(x: Single,y: Single) -> Single """
  pass
 def __rmul__(self,*args):
  """ __rmul__(x: Single,y: Single) -> Single """
  pass
 def __rpow__(self,*args):
  """ __rpow__(x: Single,y: Single) -> Single """
  pass
 def __rsub__(self,*args):
  """ __rsub__(x: Single,y: Single) -> Single """
  pass
 def __rtruediv__(self,*args):
  """ __rtruediv__(x: Single,y: Single) -> Single """
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
  """ __trunc__(x: Single) -> object """
  pass
 Epsilon=None
 imag=None
 MaxValue=None
 MinValue=None
 NaN=None
 NegativeInfinity=None
 PositiveInfinity=None
 real=None

