class Decimal(object,IFormattable,IComparable,IConvertible,IDeserializationCallback,IComparable[Decimal],IEquatable[Decimal]):
 """
 Represents a decimal number.

 

 Decimal(value: int)

 Decimal(value: UInt32)

 Decimal(value: Int64)

 Decimal(value: UInt64)

 Decimal(value: Single)

 Decimal(value: float)

 Decimal(bits: Array[int])

 Decimal(lo: int,mid: int,hi: int,isNegative: bool,scale: Byte)
 """
 @staticmethod
 def Add(d1,d2):
  """
  Add(d1: Decimal,d2: Decimal) -> Decimal

  

   Adds two specified System.Decimal values.

  

   d1: The first value to add.

   d2: The second value to add.

   Returns: The sum of d1 and d2.
  """
  pass
 @staticmethod
 def Ceiling(d):
  """
  Ceiling(d: Decimal) -> Decimal

  

   Returns the smallest integral value that is greater than or equal to the specified decimal 

    number.

  

  

   d: A decimal number.

   Returns: The smallest integral value that is greater than or equal to the d parameter. Note that this 

    method returns a System.Decimal instead of an integral type.
  """
  pass
 @staticmethod
 def Compare(d1,d2):
  """
  Compare(d1: Decimal,d2: Decimal) -> int

  

   Compares two specified System.Decimal values.

  

   d1: The first value to compare.

   d2: The second value to compare.

   Returns: A signed number indicating the relative values of d1 and d2.Return Value Meaning Less than zero 

    d1 is less than d2. Zero d1 and d2 are equal. Greater than zero d1 is greater than d2.
  """
  pass
 def CompareTo(self,value):
  """
  CompareTo(self: Decimal,value: Decimal) -> int

  

   Compares this instance to a specified System.Decimal object.

  

   value: The object to compare with this instance.

   Returns: A signed number indicating the relative values of this instance and value.Return Value Meaning 

    Less than zero This instance is less than value. Zero This instance is equal to value. Greater 

    than zero This instance is greater than value.

  

  CompareTo(self: Decimal,value: object) -> int

  

   Compares this instance to a specified System.Object.

  

   value: The object to compare with this instance,or null.

   Returns: A signed number indicating the relative values of this instance and value.Return Value Meaning 

    Less than zero This instance is less than value. Zero This instance is equal to value. Greater 

    than zero This instance is greater than value.-or- value is null.
  """
  pass
 @staticmethod
 def Divide(d1,d2):
  """
  Divide(d1: Decimal,d2: Decimal) -> Decimal

  

   Divides two specified System.Decimal values.

  

   d1: The dividend.

   d2: The divisor.

   Returns: The result of dividing d1 by d2.
  """
  pass
 def Equals(self,*__args):
  """
  Equals(d1: Decimal,d2: Decimal) -> bool

  

   Returns a value indicating whether two specified instances of System.Decimal represent the same 

    value.

  

  

   d1: The first value to compare.

   d2: The second value to compare.

   Returns: true if d1 and d2 are equal; otherwise,false.

  Equals(self: Decimal,value: Decimal) -> bool

  

   Returns a value indicating whether this instance and a specified System.Decimal object represent 

    the same value.

  

  

   value: An object to compare to this instance.

   Returns: true if value is equal to this instance; otherwise,false.

  Equals(self: Decimal,value: object) -> bool

  

   Returns a value indicating whether this instance and a specified System.Object represent the 

    same type and value.

  

  

   value: The object to compare with this instance.

   Returns: true if value is a System.Decimal and equal to this instance; otherwise,false.
  """
  pass
 @staticmethod
 def Floor(d):
  """
  Floor(d: Decimal) -> Decimal

  

   Rounds a specified System.Decimal number to the closest integer toward negative infinity.

  

   d: The value to round.

   Returns: If d has a fractional part,the next whole System.Decimal number toward negative infinity that 

    is less than d.-or- If d doesn't have a fractional part,d is returned unchanged.
  """
  pass
 @staticmethod
 def FromOACurrency(cy):
  """
  FromOACurrency(cy: Int64) -> Decimal

  

   Converts the specified 64-bit signed integer,which contains an OLE Automation Currency value,

    to the equivalent System.Decimal value.

  

  

   cy: An OLE Automation Currency value.

   Returns: A System.Decimal that contains the equivalent of cy.
  """
  pass
 @staticmethod
 def GetBits(d):
  """
  GetBits(d: Decimal) -> Array[int]

  

   Converts the value of a specified instance of System.Decimal to its equivalent binary 

    representation.

  

  

   d: The value to convert.

   Returns: A 32-bit signed integer array with four elements that contain the binary representation of d.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Decimal) -> int

  

   Returns the hash code for this instance.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def GetTypeCode(self):
  """
  GetTypeCode(self: Decimal) -> TypeCode

  

   Returns the System.TypeCode for value type System.Decimal.

   Returns: The enumerated constant System.TypeCode.Decimal.
  """
  pass
 @staticmethod
 def Multiply(d1,d2):
  """
  Multiply(d1: Decimal,d2: Decimal) -> Decimal

  

   Multiplies two specified System.Decimal values.

  

   d1: The multiplicand.

   d2: The multiplier.

   Returns: The result of multiplying d1 and d2.
  """
  pass
 @staticmethod
 def Negate(d):
  """
  Negate(d: Decimal) -> Decimal

  

   Returns the result of multiplying the specified System.Decimal value by negative one.

  

   d: The value to negate.

   Returns: A decimal number with the value of d,but the opposite sign.-or- Zero,if d is zero.
  """
  pass
 @staticmethod
 def Parse(s,*__args):
  """
  Parse(s: str,provider: IFormatProvider) -> Decimal

  

   Converts the string representation of a number to its System.Decimal equivalent using the 

    specified culture-specific format information.

  

  

   s: The string representation of the number to convert.

   provider: An System.IFormatProvider that supplies culture-specific parsing information about s.

   Returns: The System.Decimal number equivalent to the number contained in s as specified by provider.

  Parse(s: str,style: NumberStyles,provider: IFormatProvider) -> Decimal

  

   Converts the string representation of a number to its System.Decimal equivalent using the 

    specified style and culture-specific format.

  

  

   s: The string representation of the number to convert.

   style: A bitwise combination of System.Globalization.NumberStyles values that indicates the style 

    elements that can be present in s. A typical value to specify is 

    System.Globalization.NumberStyles.Number.

  

   provider: An System.IFormatProvider object that supplies culture-specific information about the format of 

    s.

  

   Returns: The System.Decimal number equivalent to the number contained in s as specified by style and 

    provider.

  

  Parse(s: str) -> Decimal

  

   Converts the string representation of a number to its System.Decimal equivalent.

  

   s: The string representation of the number to convert.

   Returns: The equivalent to the number contained in s.

  Parse(s: str,style: NumberStyles) -> Decimal

  

   Converts the string representation of a number in a specified style to its System.Decimal 

    equivalent.

  

  

   s: The string representation of the number to convert.

   style: A bitwise combination of System.Globalization.NumberStyles values that indicates the style 

    elements that can be present in s. A typical value to specify is 

    System.Globalization.NumberStyles.Number.

  

   Returns: The System.Decimal number equivalent to the number contained in s as specified by style.
  """
  pass
 @staticmethod
 def Remainder(d1,d2):
  """
  Remainder(d1: Decimal,d2: Decimal) -> Decimal

  

   Computes the remainder after dividing two System.Decimal values.

  

   d1: The dividend.

   d2: The divisor.

   Returns: The remainder after dividing d1 by d2.
  """
  pass
 @staticmethod
 def Round(d,*__args):
  """
  Round(d: Decimal,mode: MidpointRounding) -> Decimal

  

   Rounds a decimal value to the nearest integer. A parameter specifies how to round the value if 

    it is midway between two other numbers.

  

  

   d: A decimal number to round.

   mode: A value that specifies how to round d if it is midway between two other numbers.

   Returns: The integer that is nearest to the d parameter. If d is halfway between two numbers,one of 

    which is even and the other odd,the mode parameter determines which of the two numbers is 

    returned.

  

  Round(d: Decimal,decimals: int,mode: MidpointRounding) -> Decimal

  

   Rounds a decimal value to a specified precision. A parameter specifies how to round the value if 

    it is midway between two other numbers.

  

  

   d: A decimal number to round.

   decimals: The number of significant decimal places (precision) in the return value.

   mode: A value that specifies how to round d if it is midway between two other numbers.

   Returns: The number that is nearest to the d parameter with a precision equal to the decimals parameter. 

    If d is halfway between two numbers,one of which is even and the other odd,the mode parameter 

    determines which of the two numbers is returned. If the precision of d is less than decimals,d 

    is returned unchanged.

  

  Round(d: Decimal) -> Decimal

  

   Rounds a decimal value to the nearest integer.

  

   d: A decimal number to round.

   Returns: The integer that is nearest to the d parameter. If d is halfway between two integers,one of 

    which is even and the other odd,the even number is returned.

  

  Round(d: Decimal,decimals: int) -> Decimal

  

   Rounds a System.Decimal value to a specified number of decimal places.

  

   d: A decimal number to round.

   decimals: A value from 0 to 28 that specifies the number of decimal places to round to.

   Returns: The decimal number equivalent to d rounded to decimals number of decimal places.
  """
  pass
 @staticmethod
 def Subtract(d1,d2):
  """
  Subtract(d1: Decimal,d2: Decimal) -> Decimal

  

   Subtracts one specified System.Decimal value from another.

  

   d1: The minuend.

   d2: The subtrahend.

   Returns: The result of subtracting d2 from d1.
  """
  pass
 @staticmethod
 def ToByte(value):
  """
  ToByte(value: Decimal) -> Byte

  

   Converts the value of the specified System.Decimal to the equivalent 8-bit unsigned integer.

  

   value: The decimal number to convert.

   Returns: An 8-bit unsigned integer equivalent to value.
  """
  pass
 @staticmethod
 def ToDouble(d):
  """
  ToDouble(d: Decimal) -> float

  

   Converts the value of the specified System.Decimal to the equivalent double-precision 

    floating-point number.

  

  

   d: The decimal number to convert.

   Returns: A double-precision floating-point number equivalent to d.
  """
  pass
 @staticmethod
 def ToInt16(value):
  """
  ToInt16(value: Decimal) -> Int16

  

   Converts the value of the specified System.Decimal to the equivalent 16-bit signed integer.

  

   value: The decimal number to convert.

   Returns: A 16-bit signed integer equivalent to value.
  """
  pass
 @staticmethod
 def ToInt32(d):
  """
  ToInt32(d: Decimal) -> int

  

   Converts the value of the specified System.Decimal to the equivalent 32-bit signed integer.

  

   d: The decimal number to convert.

   Returns: A 32-bit signed integer equivalent to the value of d.
  """
  pass
 @staticmethod
 def ToInt64(d):
  """
  ToInt64(d: Decimal) -> Int64

  

   Converts the value of the specified System.Decimal to the equivalent 64-bit signed integer.

  

   d: The decimal number to convert.

   Returns: A 64-bit signed integer equivalent to the value of d.
  """
  pass
 @staticmethod
 def ToOACurrency(value):
  """
  ToOACurrency(value: Decimal) -> Int64

  

   Converts the specified System.Decimal value to the equivalent OLE Automation Currency value,

    which is contained in a 64-bit signed integer.

  

  

   value: The decimal number to convert.

   Returns: A 64-bit signed integer that contains the OLE Automation equivalent of value.
  """
  pass
 @staticmethod
 def ToSByte(value):
  """
  ToSByte(value: Decimal) -> SByte

  

   Converts the value of the specified System.Decimal to the equivalent 8-bit signed integer.

  

   value: The decimal number to convert.

   Returns: An 8-bit signed integer equivalent to value.
  """
  pass
 @staticmethod
 def ToSingle(d):
  """
  ToSingle(d: Decimal) -> Single

  

   Converts the value of the specified System.Decimal to the equivalent single-precision 

    floating-point number.

  

  

   d: The decimal number to convert.

   Returns: A single-precision floating-point number equivalent to the value of d.
  """
  pass
 def ToString(self,*__args):
  """
  ToString(self: Decimal,provider: IFormatProvider) -> str

  

   Converts the numeric value of this instance to its equivalent string representation using the 

    specified culture-specific format information.

  

  

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of the value of this instance as specified by provider.

  ToString(self: Decimal,format: str,provider: IFormatProvider) -> str

  

   Converts the numeric value of this instance to its equivalent string representation using the 

    specified format and culture-specific format information.

  

  

   format: A numeric format string (see Remarks).

   provider: An object that supplies culture-specific formatting information.

   Returns: The string representation of the value of this instance as specified by format and provider.

  ToString(self: Decimal) -> str

  

   Converts the numeric value of this instance to its equivalent string representation.

   Returns: A string that represents the value of this instance.

  ToString(self: Decimal,format: str) -> str

  

   Converts the numeric value of this instance to its equivalent string representation,using the 

    specified format.

  

  

   format: A standard or custom numeric format string (see Remarks).

   Returns: The string representation of the value of this instance as specified by format.
  """
  pass
 @staticmethod
 def ToUInt16(value):
  """
  ToUInt16(value: Decimal) -> UInt16

  

   Converts the value of the specified System.Decimal to the equivalent 16-bit unsigned integer.

  

   value: The decimal number to convert.

   Returns: A 16-bit unsigned integer equivalent to the value of value.
  """
  pass
 @staticmethod
 def ToUInt32(d):
  """
  ToUInt32(d: Decimal) -> UInt32

  

   Converts the value of the specified System.Decimal to the equivalent 32-bit unsigned integer.

  

   d: The decimal number to convert.

   Returns: A 32-bit unsigned integer equivalent to the value of d.
  """
  pass
 @staticmethod
 def ToUInt64(d):
  """
  ToUInt64(d: Decimal) -> UInt64

  

   Converts the value of the specified System.Decimal to the equivalent 64-bit unsigned integer.

  

   d: The decimal number to convert.

   Returns: A 64-bit unsigned integer equivalent to the value of d.
  """
  pass
 @staticmethod
 def Truncate(d):
  """
  Truncate(d: Decimal) -> Decimal

  

   Returns the integral digits of the specified System.Decimal; any fractional digits are discarded.

  

   d: The decimal number to truncate.

   Returns: The result of d rounded toward zero,to the nearest whole number.
  """
  pass
 @staticmethod
 def TryParse(s,*__args):
  """
  TryParse(s: str,style: NumberStyles,provider: IFormatProvider) -> (bool,Decimal)

  

   Converts the string representation of a number to its System.Decimal equivalent using the 

    specified style and culture-specific format. A return value indicates whether the conversion 

    succeeded or failed.

  

  

   s: The string representation of the number to convert.

   style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical 

    value to specify is System.Globalization.NumberStyles.Number.

  

   provider: An object that supplies culture-specific parsing information about s.

   Returns: true if s was converted successfully; otherwise,false.

  TryParse(s: str) -> (bool,Decimal)

  

   Converts the string representation of a number to its System.Decimal equivalent. A return value 

    indicates whether the conversion succeeded or failed.

  

  

   s: The string representation of the number to convert.

   Returns: true if s was converted successfully; otherwise,false.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __cmp__(self,*args):
  """ x.__cmp__(y) <==> cmp(x,y) """
  pass
 def __complex__(self,*args):
  """ __complex__(value: Decimal) -> float """
  pass
 def __div__(self,*args):
  """ x.__div__(y) <==> x/y """
  pass
 def __float__(self,*args):
  """ __complex__(value: Decimal) -> float """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __hash__(self,*args):
  """ x.__hash__() <==> hash(x) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __int__(self,*args):
  """ __int__(value: Decimal) -> int """
  pass
 def __long__(self,*args):
  """ __int__(value: Decimal) -> int """
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
 def __new__(self,*__args):
  """
  __new__(cls: type,value: int)

  __new__(cls: type,value: UInt32)

  __new__(cls: type,value: Int64)

  __new__(cls: type,value: UInt64)

  __new__(cls: type,value: Single)

  __new__(cls: type,value: float)

  __new__(cls: type,bits: Array[int])

  __new__(cls: type,lo: int,mid: int,hi: int,isNegative: bool,scale: Byte)

  __new__[Decimal]() -> Decimal
  """
  pass
 def __nonzero__(self,*args):
  """ __nonzero__(x: Decimal) -> bool """
  pass
 def __pos__(self,*args):
  """
  __pos__(d: Decimal) -> Decimal

  

   Returns the value of the System.Decimal operand (the sign of the operand is unchanged).

  

   d: The operand to return.

   Returns: The value of the operand,d.
  """
  pass
 def __radd__(self,*args):
  """
  __radd__(d1: Decimal,d2: Decimal) -> Decimal

  

   Adds two specified System.Decimal values.

  

   d1: The first value to add.

   d2: The second value to add.

   Returns: The result of adding d1 and d2.
  """
  pass
 def __rdiv__(self,*args):
  """
  __rdiv__(d1: Decimal,d2: Decimal) -> Decimal

  

   Divides two specified System.Decimal values.

  

   d1: The dividend.

   d2: The divisor.

   Returns: The result of dividing d1 by d2.
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(x: Decimal) -> str """
  pass
 def __rmod__(self,*args):
  """
  __rmod__(d1: Decimal,d2: Decimal) -> Decimal

  

   Returns the remainder resulting from dividing two specified System.Decimal values.

  

   d1: The dividend.

   d2: The divisor.

   Returns: The remainder resulting from dividing d1 by d2.
  """
  pass
 def __rmul__(self,*args):
  """
  __rmul__(d1: Decimal,d2: Decimal) -> Decimal

  

   Multiplies two specified System.Decimal values.

  

   d1: The first value to multiply.

   d2: The second value to multiply.

   Returns: The result of multiplying d1 by d2.
  """
  pass
 def __rsub__(self,*args):
  """
  __rsub__(d1: Decimal,d2: Decimal) -> Decimal

  

   Subtracts two specified System.Decimal values.

  

   d1: The minuend.

   d2: The subtrahend.

   Returns: The result of subtracting d2 from d1.
  """
  pass
 def __str__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-y """
  pass
 MaxValue=None
 MinusOne=None
 MinValue=None
 One=None
 Zero=None

