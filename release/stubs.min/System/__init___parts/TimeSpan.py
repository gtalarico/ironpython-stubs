class TimeSpan(object,IComparable,IComparable[TimeSpan],IEquatable[TimeSpan],IFormattable):
 """
 Represents a time interval.

 

 TimeSpan(ticks: Int64)

 TimeSpan(hours: int,minutes: int,seconds: int)

 TimeSpan(days: int,hours: int,minutes: int,seconds: int)

 TimeSpan(days: int,hours: int,minutes: int,seconds: int,milliseconds: int)
 """
 def Add(self,ts):
  """
  Add(self: TimeSpan,ts: TimeSpan) -> TimeSpan

  

   Returns a new System.TimeSpan object whose value is the sum of the specified System.TimeSpan 

    object and this instance.

  

  

   ts: The time interval to add.

   Returns: A new object that represents the value of this instance plus the value of ts.
  """
  pass
 @staticmethod
 def Compare(t1,t2):
  """
  Compare(t1: TimeSpan,t2: TimeSpan) -> int

  

   Compares two System.TimeSpan values and returns an integer that indicates whether the first 

    value is shorter than,equal to,or longer than the second value.

  

  

   t1: The first time interval to compare.

   t2: The second time interval to compare.

   Returns: One of the following values.Value Description -1 t1 is shorter than t2. 0 t1 is equal to t2. 1 

    t1 is longer than t2.
  """
  pass
 def CompareTo(self,value):
  """
  CompareTo(self: TimeSpan,value: TimeSpan) -> int

  

   Compares this instance to a specified System.TimeSpan object and returns an integer that 

    indicates whether this instance is shorter than,equal to,or longer than the System.TimeSpan 

    object.

  

  

   value: An object to compare to this instance.

   Returns: A signed number indicating the relative values of this instance and value.Value Description A 

    negative integer This instance is shorter than value. Zero This instance is equal to value. A 

    positive integer This instance is longer than value.

  

  CompareTo(self: TimeSpan,value: object) -> int

  

   Compares this instance to a specified object and returns an integer that indicates whether this 

    instance is shorter than,equal to,or longer than the specified object.

  

  

   value: An object to compare,or null.

   Returns: One of the following values.Value Description -1 This instance is shorter than value. 0 This 

    instance is equal to value. 1 This instance is longer than value.-or- value is null.
  """
  pass
 def Duration(self):
  """
  Duration(self: TimeSpan) -> TimeSpan

  

   Returns a new System.TimeSpan object whose value is the absolute value of the current 

    System.TimeSpan object.

  

   Returns: A new object whose value is the absolute value of the current System.TimeSpan object.
  """
  pass
 def Equals(self,*__args):
  """
  Equals(t1: TimeSpan,t2: TimeSpan) -> bool

  

   Returns a value that indicates whether two specified instances of System.TimeSpan are equal.

  

   t1: The first time interval to compare.

   t2: The second time interval to compare.

   Returns: true if the values of t1 and t2 are equal; otherwise,false.

  Equals(self: TimeSpan,obj: TimeSpan) -> bool

  

   Returns a value indicating whether this instance is equal to a specified System.TimeSpan object.

  

   obj: An object to compare with this instance.

   Returns: true if obj represents the same time interval as this instance; otherwise,false.

  Equals(self: TimeSpan,value: object) -> bool

  

   Returns a value indicating whether this instance is equal to a specified object.

  

   value: An object to compare with this instance.

   Returns: true if value is a System.TimeSpan object that represents the same time interval as the current 

    System.TimeSpan structure; otherwise,false.
  """
  pass
 @staticmethod
 def FromDays(value):
  """
  FromDays(value: float) -> TimeSpan

  

   Returns a System.TimeSpan that represents a specified number of days,where the specification is 

    accurate to the nearest millisecond.

  

  

   value: A number of days,accurate to the nearest millisecond.

   Returns: An object that represents value.
  """
  pass
 @staticmethod
 def FromHours(value):
  """
  FromHours(value: float) -> TimeSpan

  

   Returns a System.TimeSpan that represents a specified number of hours,where the specification 

    is accurate to the nearest millisecond.

  

  

   value: A number of hours accurate to the nearest millisecond.

   Returns: An object that represents value.
  """
  pass
 @staticmethod
 def FromMilliseconds(value):
  """
  FromMilliseconds(value: float) -> TimeSpan

  

   Returns a System.TimeSpan that represents a specified number of milliseconds.

  

   value: A number of milliseconds.

   Returns: An object that represents value.
  """
  pass
 @staticmethod
 def FromMinutes(value):
  """
  FromMinutes(value: float) -> TimeSpan

  

   Returns a System.TimeSpan that represents a specified number of minutes,where the specification 

    is accurate to the nearest millisecond.

  

  

   value: A number of minutes,accurate to the nearest millisecond.

   Returns: An object that represents value.
  """
  pass
 @staticmethod
 def FromSeconds(value):
  """
  FromSeconds(value: float) -> TimeSpan

  

   Returns a System.TimeSpan that represents a specified number of seconds,where the specification 

    is accurate to the nearest millisecond.

  

  

   value: A number of seconds,accurate to the nearest millisecond.

   Returns: An object that represents value.
  """
  pass
 @staticmethod
 def FromTicks(value):
  """
  FromTicks(value: Int64) -> TimeSpan

  

   Returns a System.TimeSpan that represents a specified time,where the specification is in units 

    of ticks.

  

  

   value: A number of ticks that represent a time.

   Returns: An object that represents value.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TimeSpan) -> int

  

   Returns a hash code for this instance.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def Negate(self):
  """
  Negate(self: TimeSpan) -> TimeSpan

  

   Returns a new System.TimeSpan object whose value is the negated value of this instance.

   Returns: A new object with the same numeric value as this instance,but with the opposite sign.
  """
  pass
 @staticmethod
 def Parse(*__args):
  """
  Parse(input: str,formatProvider: IFormatProvider) -> TimeSpan

  

   Converts the string representation of a time interval to its System.TimeSpan equivalent by using 

    the specified culture-specific format information.

  

  

   input: A string that specifies the time interval to convert.

   formatProvider: An object that supplies culture-specific formatting information.

   Returns: A time interval that corresponds to input,as specified by formatProvider.

  Parse(s: str) -> TimeSpan

  

   Converts the string representation of a time interval to its System.TimeSpan equivalent.

  

   s: A string that specifies the time interval to convert.

   Returns: A time interval that corresponds to s.
  """
  pass
 @staticmethod
 def ParseExact(input,*__args):
  """
  ParseExact(input: str,format: str,formatProvider: IFormatProvider,styles: TimeSpanStyles) -> TimeSpan

  

   Converts the string representation of a time interval to its System.TimeSpan equivalent by using 

    the specified format,culture-specific format information,and styles. The format of the string 

    representation must match the specified format exactly.

  

  

   input: A string that specifies the time interval to convert.

   format: A standard or custom format string that defines the required format of input.

   formatProvider: An object that provides culture-specific formatting information.

   styles: A bitwise combination of enumeration values that defines the style elements that may be present 

    in input.

  

   Returns: A time interval that corresponds to input,as specified by format,formatProvider,and styles.

  ParseExact(input: str,formats: Array[str],formatProvider: IFormatProvider,styles: TimeSpanStyles) -> TimeSpan

  

   Converts the string representation of a time interval to its System.TimeSpan equivalent by using 

    the specified formats,culture-specific format information,and styles. The format of the string 

    representation must match one of the specified formats exactly.

  

  

   input: A string that specifies the time interval to convert.

   formats: A array of standard or custom format strings that define the required format of input.

   formatProvider: An object that provides culture-specific formatting information.

   styles: A bitwise combination of enumeration values that defines the style elements that may be present 

    in input.

  

   Returns: A time interval that corresponds to input,as specified by formats,formatProvider,and styles.

  ParseExact(input: str,format: str,formatProvider: IFormatProvider) -> TimeSpan

  

   Converts the string representation of a time interval to its System.TimeSpan equivalent by using 

    the specified format and culture-specific format information. The format of the string 

    representation must match the specified format exactly.

  

  

   input: A string that specifies the time interval to convert.

   format: A standard or custom format string that defines the required format of input.

   formatProvider: An object that provides culture-specific formatting information.

   Returns: A time interval that corresponds to input,as specified by format and formatProvider.

  ParseExact(input: str,formats: Array[str],formatProvider: IFormatProvider) -> TimeSpan

  

   Converts the string representation of a time interval to its System.TimeSpan equivalent by using 

    the specified array of format strings and culture-specific format information. The format of the 

    string representation must match one of the specified formats exactly.

  

  

   input: A string that specifies the time interval to convert.

   formats: A array of standard or custom format strings that defines the required format of input.

   formatProvider: An object that provides culture-specific formatting information.

   Returns: A time interval that corresponds to input,as specified by formats and formatProvider.
  """
  pass
 def Subtract(self,ts):
  """
  Subtract(self: TimeSpan,ts: TimeSpan) -> TimeSpan

  

   Returns a new System.TimeSpan object whose value is the difference between the specified 

    System.TimeSpan object and this instance.

  

  

   ts: The time interval to be subtracted.

   Returns: A new time interval whose value is the result of the value of this instance minus the value of 

    ts.
  """
  pass
 def ToString(self,format=None,formatProvider=None):
  """
  ToString(self: TimeSpan,format: str,formatProvider: IFormatProvider) -> str

  

   Converts the value of the current System.TimeSpan object to its equivalent string representation 

    by using the specified format and culture-specific formatting information.

  

  

   format: A standard or custom System.TimeSpan format string.

   formatProvider: An object that supplies culture-specific formatting information.

   Returns: The string representation of the current System.TimeSpan value,as specified by format and 

    formatProvider.

  

  ToString(self: TimeSpan,format: str) -> str

  

   Converts the value of the current System.TimeSpan object to its equivalent string representation 

    by using the specified format.

  

  

   format: A standard or custom System.TimeSpan format string.

   Returns: The string representation of the current System.TimeSpan value in the format specified by the 

    format parameter.

  

  ToString(self: TimeSpan) -> str

  

   Converts the value of the current System.TimeSpan object to its equivalent string representation.

   Returns: The string representation of the current System.TimeSpan value.
  """
  pass
 @staticmethod
 def TryParse(*__args):
  """
  TryParse(input: str,formatProvider: IFormatProvider) -> (bool,TimeSpan)

  

   Converts the string representation of a time interval to its System.TimeSpan equivalent by using 

    the specified culture-specific formatting information,and returns a value that indicates 

    whether the conversion succeeded.

  

  

   input: A string that specifies the time interval to convert.

   formatProvider: An object that supplies culture-specific formatting information.

   Returns: true if input was converted successfully; otherwise,false. This operation returns false if the 

    input parameter is null or System.String.Empty,has an invalid format,represents a time 

    interval that is less than System.TimeSpan.MinValue or greater than System.TimeSpan.MaxValue,or 

    has at least one days,hours,minutes,or seconds component outside its valid range.

  

  TryParse(s: str) -> (bool,TimeSpan)

  

   Converts the string representation of a time interval to its System.TimeSpan equivalent and 

    returns a value that indicates whether the conversion succeeded.

  

  

   s: A string that specifies the time interval to convert.

   Returns: true if s was converted successfully; otherwise,false. This operation returns false if the s 

    parameter is null or System.String.Empty,has an invalid format,represents a time interval that 

    is less than System.TimeSpan.MinValue or greater than System.TimeSpan.MaxValue,or has at least 

    one days,hours,minutes,or seconds component outside its valid range.
  """
  pass
 @staticmethod
 def TryParseExact(input,*__args):
  """
  TryParseExact(input: str,format: str,formatProvider: IFormatProvider,styles: TimeSpanStyles) -> (bool,TimeSpan)

  

   Converts the string representation of a time interval to its System.TimeSpan equivalent by using 

    the specified format,culture-specific format information,and styles,and returns a value that 

    indicates whether the conversion succeeded. The format of the string representation must match 

    the specified format exactly.

  

  

   input: A string that specifies the time interval to convert.

   format: A standard or custom format string that defines the required format of input.

   formatProvider: An object that provides culture-specific formatting information.

   styles: One or more enumeration values that indicate the style of input.

   Returns: true if input was converted successfully; otherwise,false.

  TryParseExact(input: str,formats: Array[str],formatProvider: IFormatProvider,styles: TimeSpanStyles) -> (bool,TimeSpan)

  

   Converts the specified string representation of a time interval to its System.TimeSpan 

    equivalent by using the specified formats,culture-specific format information,and styles,and 

    returns a value that indicates whether the conversion succeeded. The format of the string 

    representation must match one of the specified formats exactly.

  

  

   input: A string that specifies the time interval to convert.

   formats: A array of standard or custom format strings that define the acceptable formats of input.

   formatProvider: An object that supplies culture-specific formatting information.

   styles: One or more enumeration values that indicate the style of input.

   Returns: true if input was converted successfully; otherwise,false.

  TryParseExact(input: str,format: str,formatProvider: IFormatProvider) -> (bool,TimeSpan)

  

   Converts the string representation of a time interval to its System.TimeSpan equivalent by using 

    the specified format and culture-specific format information,and returns a value that indicates 

    whether the conversion succeeded. The format of the string representation must match the 

    specified format exactly.

  

  

   input: A string that specifies the time interval to convert.

   format: A standard or custom format string that defines the required format of input.

   formatProvider: An object that supplies culture-specific formatting information.

   Returns: true if input was converted successfully; otherwise,false.

  TryParseExact(input: str,formats: Array[str],formatProvider: IFormatProvider) -> (bool,TimeSpan)

  

   Converts the specified string representation of a time interval to its System.TimeSpan 

    equivalent by using the specified formats and culture-specific format information,and returns a 

    value that indicates whether the conversion succeeded. The format of the string representation 

    must match one of the specified formats exactly.

  

  

   input: A string that specifies the time interval to convert.

   formats: A array of standard or custom format strings that define the acceptable formats of input.

   formatProvider: An object that provides culture-specific formatting information.

   Returns: true if input was converted successfully; otherwise,false.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __cmp__(self,*args):
  """ x.__cmp__(y) <==> cmp(x,y) """
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
 def __neg__(self,*args):
  """ x.__neg__() <==> -x """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,ticks: Int64)

  __new__(cls: type,hours: int,minutes: int,seconds: int)

  __new__(cls: type,days: int,hours: int,minutes: int,seconds: int)

  __new__(cls: type,days: int,hours: int,minutes: int,seconds: int,milliseconds: int)

  __new__[TimeSpan]() -> TimeSpan
  """
  pass
 def __ne__(self,*args):
  pass
 def __pos__(self,*args):
  """
  __pos__(t: TimeSpan) -> TimeSpan

  

   Returns the specified instance of System.TimeSpan.

  

   t: The time interval to return.

   Returns: The time interval specified by t.
  """
  pass
 def __radd__(self,*args):
  """
  __radd__(t1: TimeSpan,t2: TimeSpan) -> TimeSpan

  

   Adds two specified System.TimeSpan instances.

  

   t1: The first time interval to add.

   t2: The second time interval to add.

   Returns: An object whose value is the sum of the values of t1 and t2.
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __rsub__(self,*args):
  """
  __rsub__(t1: TimeSpan,t2: TimeSpan) -> TimeSpan

  

   Subtracts a specified System.TimeSpan from another specified System.TimeSpan.

  

   t1: The minuend.

   t2: The subtrahend.

   Returns: An object whose value is the result of the value of t1 minus the value of t2.
  """
  pass
 def __str__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-y """
  pass
 Days=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the days component of the time interval represented by the current System.TimeSpan structure.



Get: Days(self: TimeSpan) -> int



"""

 Hours=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the hours component of the time interval represented by the current System.TimeSpan structure.



Get: Hours(self: TimeSpan) -> int



"""

 Milliseconds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the milliseconds component of the time interval represented by the current System.TimeSpan structure.



Get: Milliseconds(self: TimeSpan) -> int



"""

 Minutes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the minutes component of the time interval represented by the current System.TimeSpan structure.



Get: Minutes(self: TimeSpan) -> int



"""

 Seconds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the seconds component of the time interval represented by the current System.TimeSpan structure.



Get: Seconds(self: TimeSpan) -> int



"""

 Ticks=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of ticks that represent the value of the current System.TimeSpan structure.



Get: Ticks(self: TimeSpan) -> Int64



"""

 TotalDays=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value of the current System.TimeSpan structure expressed in whole and fractional days.



Get: TotalDays(self: TimeSpan) -> float



"""

 TotalHours=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value of the current System.TimeSpan structure expressed in whole and fractional hours.



Get: TotalHours(self: TimeSpan) -> float



"""

 TotalMilliseconds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value of the current System.TimeSpan structure expressed in whole and fractional milliseconds.



Get: TotalMilliseconds(self: TimeSpan) -> float



"""

 TotalMinutes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value of the current System.TimeSpan structure expressed in whole and fractional minutes.



Get: TotalMinutes(self: TimeSpan) -> float



"""

 TotalSeconds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value of the current System.TimeSpan structure expressed in whole and fractional seconds.



Get: TotalSeconds(self: TimeSpan) -> float



"""


 MaxValue=None
 MinValue=None
 TicksPerDay=None
 TicksPerHour=None
 TicksPerMillisecond=None
 TicksPerMinute=None
 TicksPerSecond=None
 Zero=None

