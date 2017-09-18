class DateTimeOffset(object,IComparable,IFormattable,ISerializable,IDeserializationCallback,IComparable[DateTimeOffset],IEquatable[DateTimeOffset]):
 """
 Represents a point in time,typically expressed as a date and time of day,relative to Coordinated Universal Time (UTC).

 

 DateTimeOffset(ticks: Int64,offset: TimeSpan)

 DateTimeOffset(dateTime: DateTime)

 DateTimeOffset(dateTime: DateTime,offset: TimeSpan)

 DateTimeOffset(year: int,month: int,day: int,hour: int,minute: int,second: int,offset: TimeSpan)

 DateTimeOffset(year: int,month: int,day: int,hour: int,minute: int,second: int,millisecond: int,offset: TimeSpan)

 DateTimeOffset(year: int,month: int,day: int,hour: int,minute: int,second: int,millisecond: int,calendar: Calendar,offset: TimeSpan)
 """
 def Add(self,timeSpan):
  """
  Add(self: DateTimeOffset,timeSpan: TimeSpan) -> DateTimeOffset

  

   Adds a specified time interval to a System.DateTimeOffset object.

  

   timeSpan: A System.TimeSpan object that represents a positive or a negative time interval.

   Returns: An object whose value is the sum of the date and time represented by the current 

    System.DateTimeOffset object and the time interval represented by timeSpan.
  """
  pass
 def AddDays(self,days):
  """
  AddDays(self: DateTimeOffset,days: float) -> DateTimeOffset

  

   Adds a specified number of whole and fractional days to the current System.DateTimeOffset object.

  

   days: A number of whole and fractional days. The number can be negative or positive.

   Returns: An object whose value is the sum of the date and time represented by the current 

    System.DateTimeOffset object and the number of days represented by days.
  """
  pass
 def AddHours(self,hours):
  """
  AddHours(self: DateTimeOffset,hours: float) -> DateTimeOffset

  

   Adds a specified number of whole and fractional hours to the current System.DateTimeOffset 

    object.

  

  

   hours: A number of whole and fractional hours. The number can be negative or positive.

   Returns: An object whose value is the sum of the date and time represented by the current 

    System.DateTimeOffset object and the number of hours represented by hours.
  """
  pass
 def AddMilliseconds(self,milliseconds):
  """
  AddMilliseconds(self: DateTimeOffset,milliseconds: float) -> DateTimeOffset

  

   Adds a specified number of milliseconds to the current System.DateTimeOffset object.

  

   milliseconds: A number of whole and fractional milliseconds. The number can be negative or positive.

   Returns: An object whose value is the sum of the date and time represented by the current 

    System.DateTimeOffset object and the number of whole milliseconds represented by milliseconds.
  """
  pass
 def AddMinutes(self,minutes):
  """
  AddMinutes(self: DateTimeOffset,minutes: float) -> DateTimeOffset

  

   Adds a specified number of whole and fractional minutes to the current System.DateTimeOffset 

    object.

  

  

   minutes: A number of whole and fractional minutes. The number can be negative or positive.

   Returns: An object whose value is the sum of the date and time represented by the current 

    System.DateTimeOffset object and the number of minutes represented by minutes.
  """
  pass
 def AddMonths(self,months):
  """
  AddMonths(self: DateTimeOffset,months: int) -> DateTimeOffset

  

   Adds a specified number of months to the current System.DateTimeOffset object.

  

   months: A number of whole months. The number can be negative or positive.

   Returns: An object whose value is the sum of the date and time represented by the current 

    System.DateTimeOffset object and the number of months represented by months.
  """
  pass
 def AddSeconds(self,seconds):
  """
  AddSeconds(self: DateTimeOffset,seconds: float) -> DateTimeOffset

  

   Adds a specified number of whole and fractional seconds to the current System.DateTimeOffset 

    object.

  

  

   seconds: A number of whole and fractional seconds. The number can be negative or positive.

   Returns: An object whose value is the sum of the date and time represented by the current 

    System.DateTimeOffset object and the number of seconds represented by seconds.
  """
  pass
 def AddTicks(self,ticks):
  """
  AddTicks(self: DateTimeOffset,ticks: Int64) -> DateTimeOffset

  

   Adds a specified number of ticks to the current System.DateTimeOffset object.

  

   ticks: A number of 100-nanosecond ticks. The number can be negative or positive.

   Returns: An object whose value is the sum of the date and time represented by the current 

    System.DateTimeOffset object and the number of ticks represented by ticks.
  """
  pass
 def AddYears(self,years):
  """
  AddYears(self: DateTimeOffset,years: int) -> DateTimeOffset

  

   Adds a specified number of years to the System.DateTimeOffset object.

  

   years: A number of years. The number can be negative or positive.

   Returns: An object whose value is the sum of the date and time represented by the current 

    System.DateTimeOffset object and the number of years represented by years.
  """
  pass
 @staticmethod
 def Compare(first,second):
  """
  Compare(first: DateTimeOffset,second: DateTimeOffset) -> int

  

   Compares two System.DateTimeOffset objects and indicates whether the first is earlier than the 

    second,equal to the second,or later than the second.

  

  

   first: The first object to compare.

   second: The second object to compare.

   Returns: A signed integer that indicates whether the value of the first parameter is earlier than,later 

    than,or the same time as the value of the second parameter,as the following table shows.Return 

    valueMeaningLess than zerofirst is earlier than second.Zerofirst is equal to second.Greater than 

    zerofirst is later than second.
  """
  pass
 def CompareTo(self,other):
  """
  CompareTo(self: DateTimeOffset,other: DateTimeOffset) -> int

  

   Compares the current System.DateTimeOffset object to a specified System.DateTimeOffset object 

    and indicates whether the current object is earlier than,the same as,or later than the second 

    System.DateTimeOffset object.

  

  

   other: An object to compare with the current System.DateTimeOffset object.

   Returns: A signed integer that indicates the relationship between the current System.DateTimeOffset 

    object and other,as the following table shows.Return ValueDescriptionLess than zeroThe current 

    System.DateTimeOffset object is earlier than other.ZeroThe current System.DateTimeOffset object 

    is the same as other.Greater than zero.The current System.DateTimeOffset object is later than 

    other.
  """
  pass
 def Equals(self,*__args):
  """
  Equals(first: DateTimeOffset,second: DateTimeOffset) -> bool

  

   Determines whether two specified System.DateTimeOffset objects represent the same point in time.

  

   first: The first object to compare.

   second: The second object to compare.

   Returns: true if the two System.DateTimeOffset objects have the same System.DateTimeOffset.UtcDateTime 

    value; otherwise,false.

  

  Equals(self: DateTimeOffset,other: DateTimeOffset) -> bool

  

   Determines whether the current System.DateTimeOffset object represents the same point in time as 

    a specified System.DateTimeOffset object.

  

  

   other: An object to compare to the current System.DateTimeOffset object.

   Returns: true if both System.DateTimeOffset objects have the same System.DateTimeOffset.UtcDateTime 

    value; otherwise,false.

  

  Equals(self: DateTimeOffset,obj: object) -> bool

  

   Determines whether a System.DateTimeOffset object represents the same point in time as a 

    specified object.

  

  

   obj: The object to compare to the current System.DateTimeOffset object.

   Returns: true if the obj parameter is a System.DateTimeOffset object and represents the same point in 

    time as the current System.DateTimeOffset object; otherwise,false.
  """
  pass
 def EqualsExact(self,other):
  """
  EqualsExact(self: DateTimeOffset,other: DateTimeOffset) -> bool

  

   Determines whether the current System.DateTimeOffset object represents the same time and has the 

    same offset as a specified System.DateTimeOffset object.

  

  

   other: The object to compare to the current System.DateTimeOffset object.

   Returns: true if the current System.DateTimeOffset object and other have the same date and time value and 

    the same System.DateTimeOffset.Offset value; otherwise,false.
  """
  pass
 @staticmethod
 def FromFileTime(fileTime):
  """
  FromFileTime(fileTime: Int64) -> DateTimeOffset

  

   Converts the specified Windows file time to an equivalent local time.

  

   fileTime: A Windows file time,expressed in ticks.

   Returns: An object that represents the date and time of fileTime with the offset set to the local time 

    offset.
  """
  pass
 @staticmethod
 def FromUnixTimeMilliseconds(milliseconds):
  """ FromUnixTimeMilliseconds(milliseconds: Int64) -> DateTimeOffset """
  pass
 @staticmethod
 def FromUnixTimeSeconds(seconds):
  """ FromUnixTimeSeconds(seconds: Int64) -> DateTimeOffset """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DateTimeOffset) -> int

  

   Returns the hash code for the current System.DateTimeOffset object.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 @staticmethod
 def Parse(input,formatProvider=None,styles=None):
  """
  Parse(input: str,formatProvider: IFormatProvider,styles: DateTimeStyles) -> DateTimeOffset

  

   Converts the specified string representation of a date and time to its System.DateTimeOffset 

    equivalent using the specified culture-specific format information and formatting style.

  

  

   input: A string that contains a date and time to convert.

   formatProvider: An object that provides culture-specific format information about input.

   styles: A bitwise combination of enumeration values that indicates the permitted format of input. A 

    typical value to specify is System.Globalization.DateTimeStyles.None.

  

   Returns: An object that is equivalent to the date and time that is contained in input as specified by 

    formatProvider and styles.

  

  Parse(input: str,formatProvider: IFormatProvider) -> DateTimeOffset

  

   Converts the specified string representation of a date and time to its System.DateTimeOffset 

    equivalent using the specified culture-specific format information.

  

  

   input: A string that contains a date and time to convert.

   formatProvider: An object that provides culture-specific format information about input.

   Returns: An object that is equivalent to the date and time that is contained in input,as specified by 

    formatProvider.

  

  Parse(input: str) -> DateTimeOffset

  

   Converts the specified string representation of a date,time,and offset to its 

    System.DateTimeOffset equivalent.

  

  

   input: A string that contains a date and time to convert.

   Returns: An object that is equivalent to the date and time that is contained in input.
  """
  pass
 @staticmethod
 def ParseExact(input,*__args):
  """
  ParseExact(input: str,formats: Array[str],formatProvider: IFormatProvider,styles: DateTimeStyles) -> DateTimeOffset

  

   Converts the specified string representation of a date and time to its System.DateTimeOffset 

    equivalent using the specified formats,culture-specific format information,and style. The 

    format of the string representation must match one of the specified formats exactly.

  

  

   input: A string that contains a date and time to convert.

   formats: An array of format specifiers that define the expected formats of input.

   formatProvider: An object that supplies culture-specific formatting information about input.

   styles: A bitwise combination of enumeration values that indicates the permitted format of input.

   Returns: An object that is equivalent to the date and time that is contained in the input parameter,as 

    specified by the formats,formatProvider,and styles parameters.

  

  ParseExact(input: str,format: str,formatProvider: IFormatProvider,styles: DateTimeStyles) -> DateTimeOffset

  

   Converts the specified string representation of a date and time to its System.DateTimeOffset 

    equivalent using the specified format,culture-specific format information,and style. The 

    format of the string representation must match the specified format exactly.

  

  

   input: A string that contains a date and time to convert.

   format: A format specifier that defines the expected format of input.

   formatProvider: An object that supplies culture-specific formatting information about input.

   styles: A bitwise combination of enumeration values that indicates the permitted format of input.

   Returns: An object that is equivalent to the date and time that is contained in the input parameter,as 

    specified by the format,formatProvider,and styles parameters.

  

  ParseExact(input: str,format: str,formatProvider: IFormatProvider) -> DateTimeOffset

  

   Converts the specified string representation of a date and time to its System.DateTimeOffset 

    equivalent using the specified format and culture-specific format information. The format of the 

    string representation must match the specified format exactly.

  

  

   input: A string that contains a date and time to convert.

   format: A format specifier that defines the expected format of input.

   formatProvider: An object that supplies culture-specific formatting information about input.

   Returns: An object that is equivalent to the date and time that is contained in input as specified by 

    format and formatProvider.
  """
  pass
 def Subtract(self,value):
  """
  Subtract(self: DateTimeOffset,value: TimeSpan) -> DateTimeOffset

  

   Subtracts a specified time interval from the current System.DateTimeOffset object.

  

   value: The time interval to subtract.

   Returns: An object that is equal to the date and time represented by the current System.DateTimeOffset 

    object,minus the time interval represented by value.

  

  Subtract(self: DateTimeOffset,value: DateTimeOffset) -> TimeSpan

  

   Subtracts a System.DateTimeOffset value that represents a specific date and time from the 

    current System.DateTimeOffset object.

  

  

   value: An object that represents the value to subtract.

   Returns: An object that specifies the interval between the two System.DateTimeOffset objects.
  """
  pass
 def ToFileTime(self):
  """
  ToFileTime(self: DateTimeOffset) -> Int64

  

   Converts the value of the current System.DateTimeOffset object to a Windows file time.

   Returns: The value of the current System.DateTimeOffset object,expressed as a Windows file time.
  """
  pass
 def ToLocalTime(self):
  """
  ToLocalTime(self: DateTimeOffset) -> DateTimeOffset

  

   Converts the current System.DateTimeOffset object to a System.DateTimeOffset object that 

    represents the local time.

  

   Returns: An object that represents the date and time of the current System.DateTimeOffset object 

    converted to local time.
  """
  pass
 def ToOffset(self,offset):
  """
  ToOffset(self: DateTimeOffset,offset: TimeSpan) -> DateTimeOffset

  

   Converts the value of the current System.DateTimeOffset object to the date and time specified by 

    an offset value.

  

  

   offset: The offset to convert the System.DateTimeOffset value to.

   Returns: An object that is equal to the original System.DateTimeOffset object (that is,their 

    System.DateTimeOffset.ToUniversalTime methods return identical points in time) but whose 

    System.DateTimeOffset.Offset property is set to offset.
  """
  pass
 def ToString(self,*__args):
  """
  ToString(self: DateTimeOffset,formatProvider: IFormatProvider) -> str

  

   Converts the value of the current System.DateTimeOffset object to its equivalent string 

    representation using the specified culture-specific formatting information.

  

  

   formatProvider: An object that supplies culture-specific formatting information.

   Returns: A string representation of the value of the current System.DateTimeOffset object,as specified 

    by formatProvider.

  

  ToString(self: DateTimeOffset,format: str,formatProvider: IFormatProvider) -> str

  

   Converts the value of the current System.DateTimeOffset object to its equivalent string 

    representation using the specified format and culture-specific format information.

  

  

   format: A format string.

   formatProvider: An object that supplies culture-specific formatting information.

   Returns: A string representation of the value of the current System.DateTimeOffset object,as specified 

    by format and provider.

  

  ToString(self: DateTimeOffset) -> str

  

   Converts the value of the current System.DateTimeOffset object to its equivalent string 

    representation.

  

   Returns: A string representation of a System.DateTimeOffset object that includes the offset appended at 

    the end of the string.

  

  ToString(self: DateTimeOffset,format: str) -> str

  

   Converts the value of the current System.DateTimeOffset object to its equivalent string 

    representation using the specified format.

  

  

   format: A format string.

   Returns: A string representation of the value of the current System.DateTimeOffset object,as specified 

    by format.
  """
  pass
 def ToUniversalTime(self):
  """
  ToUniversalTime(self: DateTimeOffset) -> DateTimeOffset

  

   Converts the current System.DateTimeOffset object to a System.DateTimeOffset value that 

    represents the Coordinated Universal Time (UTC).

  

   Returns: An object that represents the date and time of the current System.DateTimeOffset object 

    converted to Coordinated Universal Time (UTC).
  """
  pass
 def ToUnixTimeMilliseconds(self):
  """ ToUnixTimeMilliseconds(self: DateTimeOffset) -> Int64 """
  pass
 def ToUnixTimeSeconds(self):
  """ ToUnixTimeSeconds(self: DateTimeOffset) -> Int64 """
  pass
 @staticmethod
 def TryParse(input,*__args):
  """
  TryParse(input: str,formatProvider: IFormatProvider,styles: DateTimeStyles) -> (bool,DateTimeOffset)

  

   Tries to convert a specified string representation of a date and time to its 

    System.DateTimeOffset equivalent,and returns a value that indicates whether the conversion 

    succeeded.

  

  

   input: A string that contains a date and time to convert.

   formatProvider: An object that provides culture-specific formatting information about input.

   styles: A bitwise combination of enumeration values that indicates the permitted format of input.

   Returns: true if the input parameter is successfully converted; otherwise,false.

  TryParse(input: str) -> (bool,DateTimeOffset)

  

   Tries to converts a specified string representation of a date and time to its 

    System.DateTimeOffset equivalent,and returns a value that indicates whether the conversion 

    succeeded.

  

  

   input: A string that contains a date and time to convert.

   Returns: true if the input parameter is successfully converted; otherwise,false.
  """
  pass
 @staticmethod
 def TryParseExact(input,*__args):
  """
  TryParseExact(input: str,formats: Array[str],formatProvider: IFormatProvider,styles: DateTimeStyles) -> (bool,DateTimeOffset)

  

   Converts the specified string representation of a date and time to its System.DateTimeOffset 

    equivalent using the specified array of formats,culture-specific format information,and style. 

    The format of the string representation must match one of the specified formats exactly.

  

  

   input: A string that contains a date and time to convert.

   formats: An array that defines the expected formats of input.

   formatProvider: An object that supplies culture-specific formatting information about input.

   styles: A bitwise combination of enumeration values that indicates the permitted format of input. A 

    typical value to specify is None.

  

   Returns: true if the input parameter is successfully converted; otherwise,false.

  TryParseExact(input: str,format: str,formatProvider: IFormatProvider,styles: DateTimeStyles) -> (bool,DateTimeOffset)

  

   Converts the specified string representation of a date and time to its System.DateTimeOffset 

    equivalent using the specified format,culture-specific format information,and style. The 

    format of the string representation must match the specified format exactly.

  

  

   input: A string that contains a date and time to convert.

   format: A format specifier that defines the required format of input.

   formatProvider: An object that supplies culture-specific formatting information about input.

   styles: A bitwise combination of enumeration values that indicates the permitted format of input. A 

    typical value to specify is None.

  

   Returns: true if the input parameter is successfully converted; otherwise,false.
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
  __new__(cls: type,ticks: Int64,offset: TimeSpan)

  __new__(cls: type,dateTime: DateTime)

  __new__(cls: type,dateTime: DateTime,offset: TimeSpan)

  __new__(cls: type,year: int,month: int,day: int,hour: int,minute: int,second: int,offset: TimeSpan)

  __new__(cls: type,year: int,month: int,day: int,hour: int,minute: int,second: int,millisecond: int,offset: TimeSpan)

  __new__(cls: type,year: int,month: int,day: int,hour: int,minute: int,second: int,millisecond: int,calendar: Calendar,offset: TimeSpan)

  __new__[DateTimeOffset]() -> DateTimeOffset
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
  __rsub__(left: DateTimeOffset,right: DateTimeOffset) -> TimeSpan

  

   Subtracts one System.DateTimeOffset object from another and yields a time interval.

  

   left: The minuend.

   right: The subtrahend.

   Returns: An object that represents the difference between left and right.
  """
  pass
 def __str__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
  pass
 Date=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.DateTime value that represents the date component of the current System.DateTimeOffset object.



Get: Date(self: DateTimeOffset) -> DateTime



"""

 DateTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.DateTime value that represents the date and time of the current System.DateTimeOffset object.



Get: DateTime(self: DateTimeOffset) -> DateTime



"""

 Day=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the day of the month represented by the current System.DateTimeOffset object.



Get: Day(self: DateTimeOffset) -> int



"""

 DayOfWeek=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the day of the week represented by the current System.DateTimeOffset object.



Get: DayOfWeek(self: DateTimeOffset) -> DayOfWeek



"""

 DayOfYear=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the day of the year represented by the current System.DateTimeOffset object.



Get: DayOfYear(self: DateTimeOffset) -> int



"""

 Hour=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the hour component of the time represented by the current System.DateTimeOffset object.



Get: Hour(self: DateTimeOffset) -> int



"""

 LocalDateTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.DateTime value that represents the local date and time of the current System.DateTimeOffset object.



Get: LocalDateTime(self: DateTimeOffset) -> DateTime



"""

 Millisecond=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the millisecond component of the time represented by the current System.DateTimeOffset object.



Get: Millisecond(self: DateTimeOffset) -> int



"""

 Minute=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the minute component of the time represented by the current System.DateTimeOffset object.



Get: Minute(self: DateTimeOffset) -> int



"""

 Month=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the month component of the date represented by the current System.DateTimeOffset object.



Get: Month(self: DateTimeOffset) -> int



"""

 Offset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the time's offset from Coordinated Universal Time (UTC).



Get: Offset(self: DateTimeOffset) -> TimeSpan



"""

 Second=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the second component of the clock time represented by the current System.DateTimeOffset object.



Get: Second(self: DateTimeOffset) -> int



"""

 Ticks=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of ticks that represents the date and time of the current System.DateTimeOffset object in clock time.



Get: Ticks(self: DateTimeOffset) -> Int64



"""

 TimeOfDay=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the time of day for the current System.DateTimeOffset object.



Get: TimeOfDay(self: DateTimeOffset) -> TimeSpan



"""

 UtcDateTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.DateTime value that represents the Coordinated Universal Time (UTC) date and time of the current System.DateTimeOffset object.



Get: UtcDateTime(self: DateTimeOffset) -> DateTime



"""

 UtcTicks=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of ticks that represents the date and time of the current System.DateTimeOffset object in Coordinated Universal Time (UTC).



Get: UtcTicks(self: DateTimeOffset) -> Int64



"""

 Year=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the year component of the date represented by the current System.DateTimeOffset object.



Get: Year(self: DateTimeOffset) -> int



"""


 MaxValue=None
 MinValue=None
 Now=None
 UtcNow=None

