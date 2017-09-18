class Math(object):
 """ Provides constants and static methods for trigonometric,logarithmic,and other common mathematical functions. """
 @staticmethod
 def Abs(value):
  """
  Abs(value: Single) -> Single

  

   Returns the absolute value of a single-precision floating-point number.

  

   value: A number that is greater than or equal to System.Single.MinValue,but less than or equal to 

    System.Single.MaxValue.

  

    Abs(value: float) -> float

  

   Returns the absolute value of a double-precision floating-point number.

  

   value: A number that is greater than or equal to System.Double.MinValue,but less than or equal to 

    System.Double.MaxValue.

  

    Abs(value: Decimal) -> Decimal

  

   Returns the absolute value of a System.Decimal number.

  

   value: A number that is greater than or equal to System.Decimal.MinValue,but less than or equal to 

    System.Decimal.MaxValue.

  

    Abs(value: Int64) -> Int64

  

   Returns the absolute value of a 64-bit signed integer.

  

   value: A number that is greater than System.Int64.MinValue,but less than or equal to 

    System.Int64.MaxValue.

  

    Abs(value: SByte) -> SByte

  

   Returns the absolute value of an 8-bit signed integer.

  

   value: A number that is greater than System.SByte.MinValue,but less than or equal to 

    System.SByte.MaxValue.

  

    Abs(value: Int16) -> Int16

  

   Returns the absolute value of a 16-bit signed integer.

  

   value: A number that is greater than System.Int16.MinValue,but less than or equal to 

    System.Int16.MaxValue.

  

    Abs(value: int) -> int

  

   Returns the absolute value of a 32-bit signed integer.

  

   value: A number that is greater than System.Int32.MinValue,but less than or equal to 

    System.Int32.MaxValue.

  

    """
  pass
 @staticmethod
 def Acos(d):
  """
  Acos(d: float) -> float

  

   Returns the angle whose cosine is the specified number.

  

   d: A number representing a cosine,where d must be greater than or equal to -1,but less than or 

    equal to 1.

  

      equals System.Double.NaN.
  """
  pass
 @staticmethod
 def Asin(d):
  """
  Asin(d: float) -> float

  

   Returns the angle whose sine is the specified number.

  

   d: A number representing a sine,where d must be greater than or equal to -1,but less than or 

    equal to 1.

  

      1 or d equals System.Double.NaN.
  """
  pass
 @staticmethod
 def Atan(d):
  """
  Atan(d: float) -> float

  

   Returns the angle whose tangent is the specified number.

  

   d: A number representing a tangent.

          System.Double.PositiveInfinity.
  """
  pass
 @staticmethod
 def Atan2(y,x):
  """
  Atan2(y: float,x: float) -> float

  

   Returns the angle whose tangent is the quotient of two specified numbers.

  

   y: The y coordinate of a point.

   x: The x coordinate of a point.

                either System.Double.PositiveInfinity or System.Double.NegativeInfinity,the method returns 

    System.Double.NaN.
  """
  pass
 @staticmethod
 def BigMul(a,b):
  """
  BigMul(a: int,b: int) -> Int64

  

   Produces the full product of two 32-bit numbers.

  

   a: The first number to multiply.

   b: The second number to multiply.

   Returns: The number containing the product of the specified numbers.
  """
  pass
 @staticmethod
 def Ceiling(*__args):
  """
  Ceiling(a: float) -> float

  

   Returns the smallest integral value that is greater than or equal to the specified 

    double-precision floating-point number.

  

  

   a: A double-precision floating-point number.

   Returns: The smallest integral value that is greater than or equal to a. If a is equal to 

    System.Double.NaN,System.Double.NegativeInfinity,or System.Double.PositiveInfinity,that value 

    is returned. Note that this method returns a System.Double instead of an integral type.

  

  Ceiling(d: Decimal) -> Decimal

  

   Returns the smallest integral value that is greater than or equal to the specified decimal 

    number.

  

  

   d: A decimal number.

   Returns: The smallest integral value that is greater than or equal to d. Note that this method returns a 

    System.Decimal instead of an integral type.
  """
  pass
 @staticmethod
 def Cos(d):
  """
  Cos(d: float) -> float

  

   Returns the cosine of the specified angle.

  

   d: An angle,measured in radians.

   Returns: The cosine of d. If d is equal to System.Double.NaN,System.Double.NegativeInfinity,or 

    System.Double.PositiveInfinity,this method returns System.Double.NaN.
  """
  pass
 @staticmethod
 def Cosh(value):
  """
  Cosh(value: float) -> float

  

   Returns the hyperbolic cosine of the specified angle.

  

   value: An angle,measured in radians.

   Returns: The hyperbolic cosine of value. If value is equal to System.Double.NegativeInfinity or 

    System.Double.PositiveInfinity,System.Double.PositiveInfinity is returned. If value is equal to 

    System.Double.NaN,System.Double.NaN is returned.
  """
  pass
 @staticmethod
 def DivRem(a,b,result):
  """
  DivRem(a: Int64,b: Int64) -> (Int64,Int64)

  

   Calculates the quotient of two 64-bit signed integers and also returns the remainder in an 

    output parameter.

  

  

   a: The dividend.

   b: The divisor.

   Returns: The quotient of the specified numbers.

  DivRem(a: int,b: int) -> (int,int)

  

   Calculates the quotient of two 32-bit signed integers and also returns the remainder in an 

    output parameter.

  

  

   a: The dividend.

   b: The divisor.

   Returns: The quotient of the specified numbers.
  """
  pass
 @staticmethod
 def Exp(d):
  """
  Exp(d: float) -> float

  

   Returns e raised to the specified power.

  

   d: A number specifying a power.

   Returns: The number e raised to the power d. If d equals System.Double.NaN or 

    System.Double.PositiveInfinity,that value is returned. If d equals 

    System.Double.NegativeInfinity,0 is returned.
  """
  pass
 @staticmethod
 def Floor(d):
  """
  Floor(d: float) -> float

  

   Returns the largest integer less than or equal to the specified double-precision floating-point 

    number.

  

  

   d: A double-precision floating-point number.

   Returns: The largest integer less than or equal to d. If d is equal to System.Double.NaN,

    System.Double.NegativeInfinity,or System.Double.PositiveInfinity,that value is returned.

  

  Floor(d: Decimal) -> Decimal

  

   Returns the largest integer less than or equal to the specified decimal number.

  

   d: A decimal number.

   Returns: The largest integer less than or equal to d.
  """
  pass
 @staticmethod
 def IEEERemainder(x,y):
  """
  IEEERemainder(x: float,y: float) -> float

  

   Returns the remainder resulting from the division of a specified number by another specified 

    number.

  

  

   x: A dividend.

   y: A divisor.

   Returns: A number equal to x - (y Q),where Q is the quotient of x / y rounded to the nearest integer (if 

    x / y falls halfway between two integers,the even integer is returned).If x - (y Q) is zero,

    the value +0 is returned if x is positive,or -0 if x is negative.If y=0,System.Double.NaN is 

    returned.
  """
  pass
 @staticmethod
 def Log(*__args):
  """
  Log(a: float,newBase: float) -> float

  

   Returns the logarithm of a specified number in a specified base.

  

   a: A number whose logarithm is to be found.

   newBase: The base of the logarithm.

   Returns: One of the values in the following table. (+Infinity denotes System.Double.PositiveInfinity,

    -Infinity denotes System.Double.NegativeInfinity,and NaN denotes 

    System.Double.NaN.)anewBaseReturn valuea> 0(0 <newBase< 1) -or-(newBase> 1)lognewBase(a)a< 0(any 

    value)NaN(any value)newBase< 0NaNa != 1newBase=0NaNa != 1newBase=+InfinityNaNa=NaN(any 

    value)NaN(any value)newBase=NaNNaN(any value)newBase=1NaNa=00 <newBase< 1 +Infinitya=

    0newBase> 1-Infinitya= +Infinity0 <newBase< 1-Infinitya= +InfinitynewBase> 1+Infinitya=

    1newBase=00a=1newBase=+Infinity0

  

  Log(d: float) -> float

  

   Returns the natural (base e) logarithm of a specified number.

  

   d: A number whose logarithm is to be found.

   Returns: One of the values in the following table. d parameterReturn value Positive The natural logarithm 

    of d; that is,ln d,or log edZero System.Double.NegativeInfinityNegative System.Double.NaNEqual 

    to System.Double.NaNSystem.Double.NaNEqual to 

    System.Double.PositiveInfinitySystem.Double.PositiveInfinity
  """
  pass
 @staticmethod
 def Log10(d):
  """
  Log10(d: float) -> float

  

   Returns the base 10 logarithm of a specified number.

  

   d: A number whose logarithm is to be found.

   Returns: One of the values in the following table. d parameter Return value Positive The base 10 log of 

    d; that is,log 10d. Zero System.Double.NegativeInfinityNegative System.Double.NaNEqual to 

    System.Double.NaNSystem.Double.NaNEqual to 

    System.Double.PositiveInfinitySystem.Double.PositiveInfinity
  """
  pass
 @staticmethod
 def Max(val1,val2):
  """
  Max(val1: UInt64,val2: UInt64) -> UInt64

  

   Returns the larger of two 64-bit unsigned integers.

  

   val1: The first of two 64-bit unsigned integers to compare.

   val2: The second of two 64-bit unsigned integers to compare.

   Returns: Parameter val1 or val2,whichever is larger.

  Max(val1: Int64,val2: Int64) -> Int64

  

   Returns the larger of two 64-bit signed integers.

  

   val1: The first of two 64-bit signed integers to compare.

   val2: The second of two 64-bit signed integers to compare.

   Returns: Parameter val1 or val2,whichever is larger.

  Max(val1: Single,val2: Single) -> Single

  

   Returns the larger of two single-precision floating-point numbers.

  

   val1: The first of two single-precision floating-point numbers to compare.

   val2: The second of two single-precision floating-point numbers to compare.

   Returns: Parameter val1 or val2,whichever is larger. If val1,or val2,or both val1 and val2 are equal 

    to System.Single.NaN,System.Single.NaN is returned.

  

  Max(val1: Decimal,val2: Decimal) -> Decimal

  

   Returns the larger of two decimal numbers.

  

   val1: The first of two decimal numbers to compare.

   val2: The second of two decimal numbers to compare.

   Returns: Parameter val1 or val2,whichever is larger.

  Max(val1: float,val2: float) -> float

  

   Returns the larger of two double-precision floating-point numbers.

  

   val1: The first of two double-precision floating-point numbers to compare.

   val2: The second of two double-precision floating-point numbers to compare.

   Returns: Parameter val1 or val2,whichever is larger. If val1,val2,or both val1 and val2 are equal to 

    System.Double.NaN,System.Double.NaN is returned.

  

  Max(val1: UInt32,val2: UInt32) -> UInt32

  

   Returns the larger of two 32-bit unsigned integers.

  

   val1: The first of two 32-bit unsigned integers to compare.

   val2: The second of two 32-bit unsigned integers to compare.

   Returns: Parameter val1 or val2,whichever is larger.

  Max(val1: Byte,val2: Byte) -> Byte

  

   Returns the larger of two 8-bit unsigned integers.

  

   val1: The first of two 8-bit unsigned integers to compare.

   val2: The second of two 8-bit unsigned integers to compare.

   Returns: Parameter val1 or val2,whichever is larger.

  Max(val1: SByte,val2: SByte) -> SByte

  

   Returns the larger of two 8-bit signed integers.

  

   val1: The first of two 8-bit signed integers to compare.

   val2: The second of two 8-bit signed integers to compare.

   Returns: Parameter val1 or val2,whichever is larger.

  Max(val1: Int16,val2: Int16) -> Int16

  

   Returns the larger of two 16-bit signed integers.

  

   val1: The first of two 16-bit signed integers to compare.

   val2: The second of two 16-bit signed integers to compare.

   Returns: Parameter val1 or val2,whichever is larger.

  Max(val1: int,val2: int) -> int

  

   Returns the larger of two 32-bit signed integers.

  

   val1: The first of two 32-bit signed integers to compare.

   val2: The second of two 32-bit signed integers to compare.

   Returns: Parameter val1 or val2,whichever is larger.

  Max(val1: UInt16,val2: UInt16) -> UInt16

  

   Returns the larger of two 16-bit unsigned integers.

  

   val1: The first of two 16-bit unsigned integers to compare.

   val2: The second of two 16-bit unsigned integers to compare.

   Returns: Parameter val1 or val2,whichever is larger.
  """
  pass
 @staticmethod
 def Min(val1,val2):
  """
  Min(val1: UInt64,val2: UInt64) -> UInt64

  

   Returns the smaller of two 64-bit unsigned integers.

  

   val1: The first of two 64-bit unsigned integers to compare.

   val2: The second of two 64-bit unsigned integers to compare.

   Returns: Parameter val1 or val2,whichever is smaller.

  Min(val1: Int64,val2: Int64) -> Int64

  

   Returns the smaller of two 64-bit signed integers.

  

   val1: The first of two 64-bit signed integers to compare.

   val2: The second of two 64-bit signed integers to compare.

   Returns: Parameter val1 or val2,whichever is smaller.

  Min(val1: Single,val2: Single) -> Single

  

   Returns the smaller of two single-precision floating-point numbers.

  

   val1: The first of two single-precision floating-point numbers to compare.

   val2: The second of two single-precision floating-point numbers to compare.

   Returns: Parameter val1 or val2,whichever is smaller. If val1,val2,or both val1 and val2 are equal to 

    System.Single.NaN,System.Single.NaN is returned.

  

  Min(val1: Decimal,val2: Decimal) -> Decimal

  

   Returns the smaller of two decimal numbers.

  

   val1: The first of two decimal numbers to compare.

   val2: The second of two decimal numbers to compare.

   Returns: Parameter val1 or val2,whichever is smaller.

  Min(val1: float,val2: float) -> float

  

   Returns the smaller of two double-precision floating-point numbers.

  

   val1: The first of two double-precision floating-point numbers to compare.

   val2: The second of two double-precision floating-point numbers to compare.

   Returns: Parameter val1 or val2,whichever is smaller. If val1,val2,or both val1 and val2 are equal to 

    System.Double.NaN,System.Double.NaN is returned.

  

  Min(val1: UInt32,val2: UInt32) -> UInt32

  

   Returns the smaller of two 32-bit unsigned integers.

  

   val1: The first of two 32-bit unsigned integers to compare.

   val2: The second of two 32-bit unsigned integers to compare.

   Returns: Parameter val1 or val2,whichever is smaller.

  Min(val1: Byte,val2: Byte) -> Byte

  

   Returns the smaller of two 8-bit unsigned integers.

  

   val1: The first of two 8-bit unsigned integers to compare.

   val2: The second of two 8-bit unsigned integers to compare.

   Returns: Parameter val1 or val2,whichever is smaller.

  Min(val1: SByte,val2: SByte) -> SByte

  

   Returns the smaller of two 8-bit signed integers.

  

   val1: The first of two 8-bit signed integers to compare.

   val2: The second of two 8-bit signed integers to compare.

   Returns: Parameter val1 or val2,whichever is smaller.

  Min(val1: Int16,val2: Int16) -> Int16

  

   Returns the smaller of two 16-bit signed integers.

  

   val1: The first of two 16-bit signed integers to compare.

   val2: The second of two 16-bit signed integers to compare.

   Returns: Parameter val1 or val2,whichever is smaller.

  Min(val1: int,val2: int) -> int

  

   Returns the smaller of two 32-bit signed integers.

  

   val1: The first of two 32-bit signed integers to compare.

   val2: The second of two 32-bit signed integers to compare.

   Returns: Parameter val1 or val2,whichever is smaller.

  Min(val1: UInt16,val2: UInt16) -> UInt16

  

   Returns the smaller of two 16-bit unsigned integers.

  

   val1: The first of two 16-bit unsigned integers to compare.

   val2: The second of two 16-bit unsigned integers to compare.

   Returns: Parameter val1 or val2,whichever is smaller.
  """
  pass
 @staticmethod
 def Pow(x,y):
  """
  Pow(x: float,y: float) -> float

  

   Returns a specified number raised to the specified power.

  

   x: A double-precision floating-point number to be raised to a power.

   y: A double-precision floating-point number that specifies a power.

   Returns: The number x raised to the power y.
  """
  pass
 @staticmethod
 def Round(*__args):
  """
  Round(d: Decimal,decimals: int) -> Decimal

  

   Rounds a decimal value to a specified number of fractional digits.

  

   d: A decimal number to be rounded.

   decimals: The number of decimal places in the return value.

   Returns: The number nearest to d that contains a number of fractional digits equal to decimals.

  Round(d: Decimal) -> Decimal

  

   Rounds a decimal value to the nearest integral value.

  

   d: A decimal number to be rounded.

   Returns: The integer nearest parameter d. If the fractional component of d is halfway between two 

    integers,one of which is even and the other odd,the even number is returned. Note that this 

    method returns a System.Decimal instead of an integral type.

  

  Round(d: Decimal,decimals: int,mode: MidpointRounding) -> Decimal

  

   Rounds a decimal value to a specified number of fractional digits. A parameter specifies how to 

    round the value if it is midway between two other numbers.

  

  

   d: A decimal number to be rounded.

   decimals: The number of decimal places in the return value.

   mode: Specification for how to round d if it is midway between two other numbers.

   Returns: The number nearest to d that contains a number of fractional digits equal to decimals. If d has 

    fewer fractional digits than decimals,d is returned unchanged.

  

  Round(d: Decimal,mode: MidpointRounding) -> Decimal

  

   Rounds a decimal value to the nearest integer. A parameter specifies how to round the value if 

    it is midway between two other numbers.

  

  

   d: A decimal number to be rounded.

   mode: Specification for how to round d if it is midway between two other numbers.

   Returns: The integer nearest d. If d is halfway between two numbers,one of which is even and the other 

    odd,then mode determines which of the two is returned.

  

  Round(value: float,digits: int) -> float

  

   Rounds a double-precision floating-point value to a specified number of fractional digits.

  

   value: A double-precision floating-point number to be rounded.

   digits: The number of fractional digits in the return value.

   Returns: The number nearest to value that contains a number of fractional digits equal to digits.

  Round(a: float) -> float

  

   Rounds a double-precision floating-point value to the nearest integral value.

  

   a: A double-precision floating-point number to be rounded.

   Returns: The integer nearest a. If the fractional component of a is halfway between two integers,one of 

    which is even and the other odd,then the even number is returned. Note that this method returns 

    a System.Double instead of an integral type.

  

  Round(value: float,digits: int,mode: MidpointRounding) -> float

  

   Rounds a double-precision floating-point value to the specified number of fractional digits. A 

    parameter specifies how to round the value if it is midway between two other numbers.

  

  

   value: A double-precision floating-point number to be rounded.

   digits: The number of fractional digits in the return value.

   mode: Specification for how to round value if it is midway between two other numbers.

   Returns: The number nearest to value that has a number of fractional digits equal to digits. If value has 

    fewer fractional digits than digits,value is returned unchanged.

  

  Round(value: float,mode: MidpointRounding) -> float

  

   Rounds a double-precision floating-point value to the nearest integer. A parameter specifies how 

    to round the value if it is midway between two other numbers.

  

  

   value: A double-precision floating-point number to be rounded.

   mode: Specification for how to round value if it is midway between two other numbers.

   Returns: The integer nearest value. If value is halfway between two integers,one of which is even and 

    the other odd,then mode determines which of the two is returned.
  """
  pass
 @staticmethod
 def Sign(value):
  """
  Sign(value: Single) -> int

  

   Returns a value indicating the sign of a single-precision floating-point number.

  

   value: A signed number.

   Returns: A number that indicates the sign of value,as shown in the following table.Return value Meaning 

    -1 value is less than zero. 0 value is equal to zero. 1 value is greater than zero.

  

  Sign(value: float) -> int

  

   Returns a value indicating the sign of a double-precision floating-point number.

  

   value: A signed number.

   Returns: A number that indicates the sign of value,as shown in the following table.Return value Meaning 

    -1 value is less than zero. 0 value is equal to zero. 1 value is greater than zero.

  

  Sign(value: Decimal) -> int

  

   Returns a value indicating the sign of a decimal number.

  

   value: A signed decimal number.

   Returns: A number that indicates the sign of value,as shown in the following table.Return value Meaning 

    -1 value is less than zero. 0 value is equal to zero. 1 value is greater than zero.

  

  Sign(value: Int64) -> int

  

   Returns a value indicating the sign of a 64-bit signed integer.

  

   value: A signed number.

   Returns: A number that indicates the sign of value,as shown in the following table.Return value Meaning 

    -1 value is less than zero. 0 value is equal to zero. 1 value is greater than zero.

  

  Sign(value: SByte) -> int

  

   Returns a value indicating the sign of an 8-bit signed integer.

  

   value: A signed number.

   Returns: A number that indicates the sign of value,as shown in the following table.Return value Meaning 

    -1 value is less than zero. 0 value is equal to zero. 1 value is greater than zero.

  

  Sign(value: Int16) -> int

  

   Returns a value indicating the sign of a 16-bit signed integer.

  

   value: A signed number.

   Returns: A number that indicates the sign of value,as shown in the following table.Return value Meaning 

    -1 value is less than zero. 0 value is equal to zero. 1 value is greater than zero.

  

  Sign(value: int) -> int

  

   Returns a value indicating the sign of a 32-bit signed integer.

  

   value: A signed number.

   Returns: A number that indicates the sign of value,as shown in the following table.Return value Meaning 

    -1 value is less than zero. 0 value is equal to zero. 1 value is greater than zero.
  """
  pass
 @staticmethod
 def Sin(a):
  """
  Sin(a: float) -> float

  

   Returns the sine of the specified angle.

  

   a: An angle,measured in radians.

   Returns: The sine of a. If a is equal to System.Double.NaN,System.Double.NegativeInfinity,or 

    System.Double.PositiveInfinity,this method returns System.Double.NaN.
  """
  pass
 @staticmethod
 def Sinh(value):
  """
  Sinh(value: float) -> float

  

   Returns the hyperbolic sine of the specified angle.

  

   value: An angle,measured in radians.

   Returns: The hyperbolic sine of value. If value is equal to System.Double.NegativeInfinity,

    System.Double.PositiveInfinity,or System.Double.NaN,this method returns a System.Double equal 

    to value.
  """
  pass
 @staticmethod
 def Sqrt(d):
  """
  Sqrt(d: float) -> float

  

   Returns the square root of a specified number.

  

   d: A number.

   Returns: One of the values in the following table. d parameter Return value Zero,or positive The 

    positive square root of d. Negative System.Double.NaNEquals 

    System.Double.NaNSystem.Double.NaNEquals 

    System.Double.PositiveInfinitySystem.Double.PositiveInfinity
  """
  pass
 @staticmethod
 def Tan(a):
  """
  Tan(a: float) -> float

  

   Returns the tangent of the specified angle.

  

   a: An angle,measured in radians.

   Returns: The tangent of a. If a is equal to System.Double.NaN,System.Double.NegativeInfinity,or 

    System.Double.PositiveInfinity,this method returns System.Double.NaN.
  """
  pass
 @staticmethod
 def Tanh(value):
  """
  Tanh(value: float) -> float

  

   Returns the hyperbolic tangent of the specified angle.

  

   value: An angle,measured in radians.

   Returns: The hyperbolic tangent of value. If value is equal to System.Double.NegativeInfinity,this 

    method returns -1. If value is equal to System.Double.PositiveInfinity,this method returns 1. 

    If value is equal to System.Double.NaN,this method returns System.Double.NaN.
  """
  pass
 @staticmethod
 def Truncate(d):
  """
  Truncate(d: float) -> float

  

   Calculates the integral part of a specified double-precision floating-point number.

  

   d: A number to truncate.

   Returns: The integral part of d; that is,the number that remains after any fractional digits have been 

    discarded,or one of the values listed in the following table. dReturn 

    valueSystem.Double.NaNSystem.Double.NaNSystem.Double.NegativeInfinitySystem.Double.NegativeInfini

    tySystem.Double.PositiveInfinitySystem.Double.PositiveInfinity

  

  Truncate(d: Decimal) -> Decimal

  

   Calculates the integral part of a specified decimal number.

  

   d: A number to truncate.

   Returns: The integral part of d; that is,the number that remains after any fractional digits have been 

    discarded.
  """
  pass
 E=2.7182818284590451
 PI=3.1415926535897931
 __all__=[
  'Abs',
  'Acos',
  'Asin',
  'Atan',
  'Atan2',
  'BigMul',
  'Ceiling',
  'Cos',
  'Cosh',
  'DivRem',
  'E',
  'Exp',
  'Floor',
  'IEEERemainder',
  'Log',
  'Log10',
  'Max',
  'Min',
  'PI',
  'Pow',
  'Round',
  'Sign',
  'Sin',
  'Sinh',
  'Sqrt',
  'Tan',
  'Tanh',
  'Truncate',
 ]

