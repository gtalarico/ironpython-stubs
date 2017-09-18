class DateTime(object,IComparable,IFormattable,IConvertible,ISerializable,IComparable[DateTime],IEquatable[DateTime]):
 """
 Represents an instant in time,typically expressed as a date and time of day.

 

 DateTime(ticks: Int64)

 DateTime(ticks: Int64,kind: DateTimeKind)

 DateTime(year: int,month: int,day: int)

 DateTime(year: int,month: int,day: int,calendar: Calendar)

 DateTime(year: int,month: int,day: int,hour: int,minute: int,second: int)

 DateTime(year: int,month: int,day: int,hour: int,minute: int,second: int,kind: DateTimeKind)

 DateTime(year: int,month: int,day: int,hour: int,minute: int,second: int,calendar: Calendar)

 DateTime(year: int,month: int,day: int,hour: int,minute: int,second: int,millisecond: int)

 DateTime(year: int,month: int,day: int,hour: int,minute: int,second: int,millisecond: int,kind: DateTimeKind)

 DateTime(year: int,month: int,day: int,hour: int,minute: int,second: int,millisecond: int,calendar: Calendar)

 DateTime(year: int,month: int,day: int,hour: int,minute: int,second: int,millisecond: int,calendar: Calendar,kind: DateTimeKind)
 """
 def Add(self,value):
  """
  Add(self: DateTime,value: TimeSpan) -> DateTime

  

   Returns a new System.DateTime that adds the value of the specified System.TimeSpan to the value 

    of this instance.

  

  

   value: A positive or negative time interval.

   Returns: An object whose value is the sum of the date and time represented by this instance and the time 

    interval represented by value.
  """
  pass
 def AddDays(self,value):
  """
  AddDays(self: DateTime,value: float) -> DateTime

  

   Returns a new System.DateTime that adds the specified number of days to the value of this 

    instance.

  

  

   value: A number of whole and fractional days. The value parameter can be negative or positive.

   Returns: An object whose value is the sum of the date and time represented by this instance and the 

    number of days represented by value.
  """
  pass
 def AddHours(self,value):
  """
  AddHours(self: DateTime,value: float) -> DateTime

  

   Returns a new System.DateTime that adds the specified number of hours to the value of this 

    instance.

  

  

   value: A number of whole and fractional hours. The value parameter can be negative or positive.

   Returns: An object whose value is the sum of the date and time represented by this instance and the 

    number of hours represented by value.
  """
  pass
 def AddMilliseconds(self,value):
  """
  AddMilliseconds(self: DateTime,value: float) -> DateTime

  

   Returns a new System.DateTime that adds the specified number of milliseconds to the value of 

    this instance.

  

  

   value: A number of whole and fractional milliseconds. The value parameter can be negative or positive. 

    Note that this value is rounded to the nearest integer.

  

   Returns: An object whose value is the sum of the date and time represented by this instance and the 

    number of milliseconds represented by value.
  """
  pass
 def AddMinutes(self,value):
  """
  AddMinutes(self: DateTime,value: float) -> DateTime

  

   Returns a new System.DateTime that adds the specified number of minutes to the value of this 

    instance.

  

  

   value: A number of whole and fractional minutes. The value parameter can be negative or positive.

   Returns: An object whose value is the sum of the date and time represented by this instance and the 

    number of minutes represented by value.
  """
  pass
 def AddMonths(self,months):
  """
  AddMonths(self: DateTime,months: int) -> DateTime

  

   Returns a new System.DateTime that adds the specified number of months to the value of this 

    instance.

  

  

   months: A number of months. The months parameter can be negative or positive.

   Returns: An object whose value is the sum of the date and time represented by this instance and months.
  """
  pass
 def AddSeconds(self,value):
  """
  AddSeconds(self: DateTime,value: float) -> DateTime

  

   Returns a new System.DateTime that adds the specified number of seconds to the value of this 

    instance.

  

  

   value: A number of whole and fractional seconds. The value parameter can be negative or positive.

   Returns: An object whose value is the sum of the date and time represented by this instance and the 

    number of seconds represented by value.
  """
  pass
 def AddTicks(self,value):
  """
  AddTicks(self: DateTime,value: Int64) -> DateTime

  

   Returns a new System.DateTime that adds the specified number of ticks to the value of this 

    instance.

  

  

   value: A number of 100-nanosecond ticks. The value parameter can be positive or negative.

   Returns: An object whose value is the sum of the date and time represented by this instance and the time 

    represented by value.
  """
  pass
 def AddYears(self,value):
  """
  AddYears(self: DateTime,value: int) -> DateTime

  

   Returns a new System.DateTime that adds the specified number of years to the value of this 

    instance.

  

  

   value: A number of years. The value parameter can be negative or positive.

   Returns: An object whose value is the sum of the date and time represented by this instance and the 

    number of years represented by value.
  """
  pass
 @staticmethod
 def Compare(t1,t2):
  """
  Compare(t1: DateTime,t2: DateTime) -> int

  

   Compares two instances of System.DateTime and returns an integer that indicates whether the 

    first instance is earlier than,the same as,or later than the second instance.

  

  

   t1: The first object to compare.

   t2: The second object to compare.

   Returns: A signed number indicating the relative values of t1 and t2.Value Type Condition Less than zero 

    t1 is earlier than t2. Zero t1 is the same as t2. Greater than zero t1 is later than t2.
  """
  pass
 def CompareTo(self,value):
  """
  CompareTo(self: DateTime,value: DateTime) -> int

  

   Compares the value of this instance to a specified System.DateTime value and returns an integer 

    that indicates whether this instance is earlier than,the same as,or later than the specified 

    System.DateTime value.

  

  

   value: The object to compare to the current instance.

   Returns: A signed number indicating the relative values of this instance and the value parameter.Value 

    Description Less than zero This instance is earlier than value. Zero This instance is the same 

    as value. Greater than zero This instance is later than value.

  

  CompareTo(self: DateTime,value: object) -> int

  

   Compares the value of this instance to a specified object that contains a specified 

    System.DateTime value,and returns an integer that indicates whether this instance is earlier 

    than,the same as,or later than the specified System.DateTime value.

  

  

   value: A boxed object to compare,or null.

   Returns: A signed number indicating the relative values of this instance and value.Value Description Less 

    than zero This instance is earlier than value. Zero This instance is the same as value. Greater 

    than zero This instance is later than value,or value is null.
  """
  pass
 @staticmethod
 def DaysInMonth(year,month):
  """
  DaysInMonth(year: int,month: int) -> int

  

   Returns the number of days in the specified month and year.

  

   year: The year.

   month: The month (a number ranging from 1 to 12).

   Returns: The number of days in month for the specified year.For example,if month equals 2 for February,

    the return value is 28 or 29 depending upon whether year is a leap year.
  """
  pass
 def Equals(self,*__args):
  """
  Equals(t1: DateTime,t2: DateTime) -> bool

  

   Returns a value indicating whether two System.DateTime instances have the same date and time 

    value.

  

  

   t1: The first object to compare.

   t2: The second object to compare.

   Returns: true if the two values are equal; otherwise,false.

  Equals(self: DateTime,value: DateTime) -> bool

  

   Returns a value indicating whether the value of this instance is equal to the value of the 

    specified System.DateTime instance.

  

  

   value: The object to compare to this instance.

   Returns: true if the value parameter equals the value of this instance; otherwise,false.

  Equals(self: DateTime,value: object) -> bool

  

   Returns a value indicating whether this instance is equal to a specified object.

  

   value: The object to compare to this instance.

   Returns: true if value is an instance of System.DateTime and equals the value of this instance; 

    otherwise,false.
  """
  pass
 @staticmethod
 def FromBinary(dateData):
  """
  FromBinary(dateData: Int64) -> DateTime

  

   Deserializes a 64-bit binary value and recreates an original serialized System.DateTime object.

  

   dateData: A 64-bit signed integer that encodes the System.DateTime.Kind property in a 2-bit field and the 

    System.DateTime.Ticks property in a 62-bit field.

  

   Returns: An object that is equivalent to the System.DateTime object that was serialized by the 

    System.DateTime.ToBinary method.
  """
  pass
 @staticmethod
 def FromFileTime(fileTime):
  """
  FromFileTime(fileTime: Int64) -> DateTime

  

   Converts the specified Windows file time to an equivalent local time.

  

   fileTime: A Windows file time expressed in ticks.

   Returns: An object that represents the local time equivalent of the date and time represented by the 

    fileTime parameter.
  """
  pass
 @staticmethod
 def FromFileTimeUtc(fileTime):
  """
  FromFileTimeUtc(fileTime: Int64) -> DateTime

  

   Converts the specified Windows file time to an equivalent UTC time.

  

   fileTime: A Windows file time expressed in ticks.

   Returns: An object that represents the UTC time equivalent of the date and time represented by the 

    fileTime parameter.
  """
  pass
 @staticmethod
 def FromOADate(d):
  """
  FromOADate(d: float) -> DateTime

  

   Returns a System.DateTime equivalent to the specified OLE Automation Date.

  

   d: An OLE Automation Date value.

   Returns: An object that represents the same date and time as d.
  """
  pass
 def GetDateTimeFormats(self,*__args):
  """
  GetDateTimeFormats(self: DateTime,format: Char) -> Array[str]

  

   Converts the value of this instance to all the string representations supported by the specified 

    standard date and time format specifier.

  

  

   format: A standard date and time format string (see Remarks).

   Returns: A string array where each element is the representation of the value of this instance formatted 

    with the format standard date and time format specifier.

  

  GetDateTimeFormats(self: DateTime,format: Char,provider: IFormatProvider) -> Array[str]

  

   Converts the value of this instance to all the string representations supported by the specified 

    standard date and time format specifier and culture-specific formatting information.

  

  

   format: A date and time format string (see Remarks).

   provider: An object that supplies culture-specific formatting information about this instance.

   Returns: A string array where each element is the representation of the value of this instance formatted 

    with one of the standard date and time format specifiers.

  

  GetDateTimeFormats(self: DateTime) -> Array[str]

  

   Converts the value of this instance to all the string representations supported by the standard 

    date and time format specifiers.

  

   Returns: A string array where each element is the representation of the value of this instance formatted 

    with one of the standard date and time format specifiers.

  

  GetDateTimeFormats(self: DateTime,provider: IFormatProvider) -> Array[str]

  

   Converts the value of this instance to all the string representations supported by the standard 

    date and time format specifiers and the specified culture-specific formatting information.

  

  

   provider: An object that supplies culture-specific formatting information about this instance.

   Returns: A string array where each element is the representation of the value of this instance formatted 

    with one of the standard date and time format specifiers.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DateTime) -> int

  

   Returns the hash code for this instance.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def GetTypeCode(self):
  """
  GetTypeCode(self: DateTime) -> TypeCode

  

   Returns the System.TypeCode for value type System.DateTime.

   Returns: The enumerated constant,System.TypeCode.DateTime.
  """
  pass
 def IsDaylightSavingTime(self):
  """
  IsDaylightSavingTime(self: DateTime) -> bool

  

   Indicates whether this instance of System.DateTime is within the daylight saving time range for 

    the current time zone.

  

   Returns: true if System.DateTime.Kind is System.DateTimeKind.Local or System.DateTimeKind.Unspecified and 

    the value of this instance of System.DateTime is within the daylight saving time range for the 

    current time zone. false if System.DateTime.Kind is System.DateTimeKind.Utc.
  """
  pass
 @staticmethod
 def IsLeapYear(year):
  """
  IsLeapYear(year: int) -> bool

  

   Returns an indication whether the specified year is a leap year.

  

   year: A 4-digit year.

   Returns: true if year is a leap year; otherwise,false.
  """
  pass
 @staticmethod
 def Parse(s,provider=None,styles=None):
  """
  Parse(s: str,provider: IFormatProvider,styles: DateTimeStyles) -> DateTime

  

   Converts the specified string representation of a date and time to its System.DateTime 

    equivalent using the specified culture-specific format information and formatting style.

  

  

   s: A string containing a date and time to convert.

   provider: An object that supplies culture-specific formatting information about s.

   styles: A bitwise combination of the enumeration values that indicates the style elements that can be 

    present in s for the parse operation to succeed and that defines how to interpret the parsed 

    date in relation to the current time zone or the current date. A typical value to specify is 

    System.Globalization.DateTimeStyles.None.

  

   Returns: An object that is equivalent to the date and time contained in s,as specified by provider and 

    styles.

  

  Parse(s: str,provider: IFormatProvider) -> DateTime

  

   Converts the specified string representation of a date and time to its System.DateTime 

    equivalent using the specified culture-specific format information.

  

  

   s: A string containing a date and time to convert.

   provider: An object that supplies culture-specific format information about s.

   Returns: An object that is equivalent to the date and time contained in s as specified by provider.

  Parse(s: str) -> DateTime

  

   Converts the specified string representation of a date and time to its System.DateTime 

    equivalent.

  

  

   s: A string containing a date and time to convert.

   Returns: An object that is equivalent to the date and time contained in s.
  """
  pass
 @staticmethod
 def ParseExact(s,*__args):
  """
  ParseExact(s: str,formats: Array[str],provider: IFormatProvider,style: DateTimeStyles) -> DateTime

  

   Converts the specified string representation of a date and time to its System.DateTime 

    equivalent using the specified array of formats,culture-specific format information,and style. 

    The format of the string representation must match at least one of the specified formats exactly 

    or an exception is thrown.

  

  

   s: A string containing one or more dates and times to convert.

   formats: An array of allowable formats of s.

   provider: An object that supplies culture-specific format information about s.

   style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical 

    value to specify is System.Globalization.DateTimeStyles.None.

  

   Returns: An object that is equivalent to the date and time contained in s,as specified by formats,

    provider,and style.

  

  ParseExact(s: str,format: str,provider: IFormatProvider,style: DateTimeStyles) -> DateTime

  

   Converts the specified string representation of a date and time to its System.DateTime 

    equivalent using the specified format,culture-specific format information,and style. The 

    format of the string representation must match the specified format exactly or an exception is 

    thrown.

  

  

   s: A string containing a date and time to convert.

   format: A format specifier that defines the required format of s.

   provider: An object that supplies culture-specific formatting information about s.

   style: A bitwise combination of the enumeration values that provides additional information about s,

    about style elements that may be present in s,or about the conversion from s to a 

    System.DateTime value. A typical value to specify is System.Globalization.DateTimeStyles.None.

  

   Returns: An object that is equivalent to the date and time contained in s,as specified by format,

    provider,and style.

  

  ParseExact(s: str,format: str,provider: IFormatProvider) -> DateTime

  

   Converts the specified string representation of a date and time to its System.DateTime 

    equivalent using the specified format and culture-specific format information. The format of the 

    string representation must match the specified format exactly.

  

  

   s: A string that contains a date and time to convert.

   format: A format specifier that defines the required format of s.

   provider: An object that supplies culture-specific format information about s.

   Returns: An object that is equivalent to the date and time contained in s,as specified by format and 

    provider.
  """
  pass
 @staticmethod
 def SpecifyKind(value,kind):
  """
  SpecifyKind(value: DateTime,kind: DateTimeKind) -> DateTime

  

   Creates a new System.DateTime object that has the same number of ticks as the specified 

    System.DateTime,but is designated as either local time,Coordinated Universal Time (UTC),or 

    neither,as indicated by the specified System.DateTimeKind value.

  

  

   value: A date and time.

   kind: One of the enumeration values that indicates whether the new object represents local time,UTC,

    or neither.

  

   Returns: A new object that has the same number of ticks as the object represented by the value parameter 

    and the System.DateTimeKind value specified by the kind parameter.
  """
  pass
 def Subtract(self,value):
  """
  Subtract(self: DateTime,value: TimeSpan) -> DateTime

  

   Subtracts the specified duration from this instance.

  

   value: The time interval to subtract.

   Returns: An object that is equal to the date and time represented by this instance minus the time 

    interval represented by value.

  

  Subtract(self: DateTime,value: DateTime) -> TimeSpan

  

   Subtracts the specified date and time from this instance.

  

   value: The date and time value to subtract.

   Returns: A time interval that is equal to the date and time represented by this instance minus the date 

    and time represented by value.
  """
  pass
 def ToBinary(self):
  """
  ToBinary(self: DateTime) -> Int64

  

   Serializes the current System.DateTime object to a 64-bit binary value that subsequently can be 

    used to recreate the System.DateTime object.

  

   Returns: A 64-bit signed integer that encodes the System.DateTime.Kind and System.DateTime.Ticks 

    properties.
  """
  pass
 def ToFileTime(self):
  """
  ToFileTime(self: DateTime) -> Int64

  

   Converts the value of the current System.DateTime object to a Windows file time.

   Returns: The value of the current System.DateTime object expressed as a Windows file time.
  """
  pass
 def ToFileTimeUtc(self):
  """
  ToFileTimeUtc(self: DateTime) -> Int64

  

   Converts the value of the current System.DateTime object to a Windows file time.

   Returns: The value of the current System.DateTime object expressed as a Windows file time.
  """
  pass
 def ToLocalTime(self):
  """
  ToLocalTime(self: DateTime) -> DateTime

  

   Converts the value of the current System.DateTime object to local time.

   Returns: An object whose System.DateTime.Kind property is System.DateTimeKind.Local,and whose value is 

    the local time equivalent to the value of the current System.DateTime object,or 

    System.DateTime.MaxValue if the converted value is too large to be represented by a 

    System.DateTime object,or System.DateTime.MinValue if the converted value is too small to be 

    represented as a System.DateTime object.
  """
  pass
 def ToLongDateString(self):
  """
  ToLongDateString(self: DateTime) -> str

  

   Converts the value of the current System.DateTime object to its equivalent long date string 

    representation.

  

   Returns: A string that contains the long date string representation of the current System.DateTime object.
  """
  pass
 def ToLongTimeString(self):
  """
  ToLongTimeString(self: DateTime) -> str

  

   Converts the value of the current System.DateTime object to its equivalent long time string 

    representation.

  

   Returns: A string that contains the long time string representation of the current System.DateTime object.
  """
  pass
 def ToOADate(self):
  """
  ToOADate(self: DateTime) -> float

  

   Converts the value of this instance to the equivalent OLE Automation date.

   Returns: A double-precision floating-point number that contains an OLE Automation date equivalent to the 

    value of this instance.
  """
  pass
 def ToShortDateString(self):
  """
  ToShortDateString(self: DateTime) -> str

  

   Converts the value of the current System.DateTime object to its equivalent short date string 

    representation.

  

   Returns: A string that contains the short date string representation of the current System.DateTime 

    object.
  """
  pass
 def ToShortTimeString(self):
  """
  ToShortTimeString(self: DateTime) -> str

  

   Converts the value of the current System.DateTime object to its equivalent short time string 

    representation.

  

   Returns: A string that contains the short time string representation of the current System.DateTime 

    object.
  """
  pass
 def ToString(self,*__args):
  """
  ToString(self: DateTime,provider: IFormatProvider) -> str

  

   Converts the value of the current System.DateTime object to its equivalent string representation 

    using the specified culture-specific format information.

  

  

   provider: An object that supplies culture-specific formatting information.

   Returns: A string representation of value of the current System.DateTime object as specified by provider.

  ToString(self: DateTime,format: str,provider: IFormatProvider) -> str

  

   Converts the value of the current System.DateTime object to its equivalent string representation 

    using the specified format and culture-specific format information.

  

  

   format: A standard or custom date and time format string.

   provider: An object that supplies culture-specific formatting information.

   Returns: A string representation of value of the current System.DateTime object as specified by format 

    and provider.

  

  ToString(self: DateTime) -> str

  

   Converts the value of the current System.DateTime object to its equivalent string representation.

   Returns: A string representation of the value of the current System.DateTime object.

  ToString(self: DateTime,format: str) -> str

  

   Converts the value of the current System.DateTime object to its equivalent string representation 

    using the specified format.

  

  

   format: A standard or custom date and time format string (see Remarks).

   Returns: A string representation of value of the current System.DateTime object as specified by format.
  """
  pass
 def ToUniversalTime(self):
  """
  ToUniversalTime(self: DateTime) -> DateTime

  

   Converts the value of the current System.DateTime object to Coordinated Universal Time (UTC).

   Returns: An object whose System.DateTime.Kind property is System.DateTimeKind.Utc,and whose value is the 

    UTC equivalent to the value of the current System.DateTime object,or System.DateTime.MaxValue 

    if the converted value is too large to be represented by a System.DateTime object,or 

    System.DateTime.MinValue if the converted value is too small to be represented by a 

    System.DateTime object.
  """
  pass
 @staticmethod
 def TryParse(s,*__args):
  """
  TryParse(s: str,provider: IFormatProvider,styles: DateTimeStyles) -> (bool,DateTime)

  

   Converts the specified string representation of a date and time to its System.DateTime 

    equivalent using the specified culture-specific format information and formatting style,and 

    returns a value that indicates whether the conversion succeeded.

  

  

   s: A string containing a date and time to convert.

   provider: An object that supplies culture-specific formatting information about s.

   styles: A bitwise combination of enumeration values that defines how to interpret the parsed date in 

    relation to the current time zone or the current date. A typical value to specify is 

    System.Globalization.DateTimeStyles.None.

  

   Returns: true if the s parameter was converted successfully; otherwise,false.

  TryParse(s: str) -> (bool,DateTime)

  

   Converts the specified string representation of a date and time to its System.DateTime 

    equivalent and returns a value that indicates whether the conversion succeeded.

  

  

   s: A string containing a date and time to convert.

   Returns: true if the s parameter was converted successfully; otherwise,false.
  """
  pass
 @staticmethod
 def TryParseExact(s,*__args):
  """
  TryParseExact(s: str,formats: Array[str],provider: IFormatProvider,style: DateTimeStyles) -> (bool,DateTime)

  

   Converts the specified string representation of a date and time to its System.DateTime 

    equivalent using the specified array of formats,culture-specific format information,and style. 

    The format of the string representation must match at least one of the specified formats 

    exactly. The method returns a value that indicates whether the conversion succeeded.

  

  

   s: A string containing one or more dates and times to convert.

   formats: An array of allowable formats of s.

   provider: An object that supplies culture-specific format information about s.

   style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical 

    value to specify is System.Globalization.DateTimeStyles.None.

  

   Returns: true if the s parameter was converted successfully; otherwise,false.

  TryParseExact(s: str,format: str,provider: IFormatProvider,style: DateTimeStyles) -> (bool,DateTime)

  

   Converts the specified string representation of a date and time to its System.DateTime 

    equivalent using the specified format,culture-specific format information,and style. The 

    format of the string representation must match the specified format exactly. The method returns 

    a value that indicates whether the conversion succeeded.

  

  

   s: A string containing a date and time to convert.

   format: The required format of s.

   provider: An object that supplies culture-specific formatting information about s.

   style: A bitwise combination of one or more enumeration values that indicate the permitted format of s.

   Returns: true if s was converted successfully; otherwise,false.
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
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,ticks: Int64)

  __new__(cls: type,ticks: Int64,kind: DateTimeKind)

  __new__(cls: type,year: int,month: int,day: int)

  __new__(cls: type,year: int,month: int,day: int,calendar: Calendar)

  __new__(cls: type,year: int,month: int,day: int,hour: int,minute: int,second: int)

  __new__(cls: type,year: int,month: int,day: int,hour: int,minute: int,second: int,kind: DateTimeKind)

  __new__(cls: type,year: int,month: int,day: int,hour: int,minute: int,second: int,calendar: Calendar)

  __new__(cls: type,year: int,month: int,day: int,hour: int,minute: int,second: int,millisecond: int)

  __new__(cls: type,year: int,month: int,day: int,hour: int,minute: int,second: int,millisecond: int,kind: DateTimeKind)

  __new__(cls: type,year: int,month: int,day: int,hour: int,minute: int,second: int,millisecond: int,calendar: Calendar)

  __new__(cls: type,year: int,month: int,day: int,hour: int,minute: int,second: int,millisecond: int,calendar: Calendar,kind: DateTimeKind)

  __new__[DateTime]() -> DateTime
  """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __rsub__(self,*args):
  """
  __rsub__(d1: DateTime,d2: DateTime) -> TimeSpan

  

   Subtracts a specified date and time from another specified date and time and returns a time 

    interval.

  

  

   d1: The date and time value to subtract from (the minuend).

   d2: The date and time value to subtract (the subtrahend).

   Returns: The time interval between d1 and d2; that is,d1 minus d2.
  """
  pass
 def __str__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
  pass
 Date=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the date component of this instance.



Get: Date(self: DateTime) -> DateTime



"""

 Day=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the day of the month represented by this instance.



Get: Day(self: DateTime) -> int



"""

 DayOfWeek=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the day of the week represented by this instance.



Get: DayOfWeek(self: DateTime) -> DayOfWeek



"""

 DayOfYear=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the day of the year represented by this instance.



Get: DayOfYear(self: DateTime) -> int



"""

 Hour=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the hour component of the date represented by this instance.



Get: Hour(self: DateTime) -> int



"""

 Kind=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the time represented by this instance is based on local time,Coordinated Universal Time (UTC),or neither.



Get: Kind(self: DateTime) -> DateTimeKind



"""

 Millisecond=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the milliseconds component of the date represented by this instance.



Get: Millisecond(self: DateTime) -> int



"""

 Minute=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the minute component of the date represented by this instance.



Get: Minute(self: DateTime) -> int



"""

 Month=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the month component of the date represented by this instance.



Get: Month(self: DateTime) -> int



"""

 Second=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the seconds component of the date represented by this instance.



Get: Second(self: DateTime) -> int



"""

 Ticks=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of ticks that represent the date and time of this instance.



Get: Ticks(self: DateTime) -> Int64



"""

 TimeOfDay=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the time of day for this instance.



Get: TimeOfDay(self: DateTime) -> TimeSpan



"""

 Year=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the year component of the date represented by this instance.



Get: Year(self: DateTime) -> int



"""


 MaxValue=None
 MinValue=None
 Now=None
 Today=None
 UtcNow=None

