class TimeZone(object):
 """ Represents a time zone. """
 def GetDaylightChanges(self,year):
  """
  GetDaylightChanges(self: TimeZone,year: int) -> DaylightTime

  

   Returns the daylight saving time period for a particular year.

  

   year: The year that the daylight saving time period applies to.

   Returns: A System.Globalization.DaylightTime object that contains the start and end date for daylight 

    saving time in year.
  """
  pass
 def GetUtcOffset(self,time):
  """
  GetUtcOffset(self: TimeZone,time: DateTime) -> TimeSpan

  

   Returns the Coordinated Universal Time (UTC) offset for the specified local time.

  

   time: A date and time value.

   Returns: The Coordinated Universal Time (UTC) offset from Time.
  """
  pass
 def IsDaylightSavingTime(self,time,daylightTimes=None):
  """
  IsDaylightSavingTime(time: DateTime,daylightTimes: DaylightTime) -> bool

  

   Returns a value indicating whether the specified date and time is within the specified daylight 

    saving time period.

  

  

   time: A date and time.

   daylightTimes: A daylight saving time period.

   Returns: true if time is in daylightTimes; otherwise,false.

  IsDaylightSavingTime(self: TimeZone,time: DateTime) -> bool

  

   Returns a value indicating whether the specified date and time is within a daylight saving time 

    period.

  

  

   time: A date and time.

   Returns: true if time is in a daylight saving time period; otherwise,false.
  """
  pass
 def ToLocalTime(self,time):
  """
  ToLocalTime(self: TimeZone,time: DateTime) -> DateTime

  

   Returns the local time that corresponds to a specified date and time value.

  

   time: A Coordinated Universal Time (UTC) time.

   Returns: A System.DateTime object whose value is the local time that corresponds to time.
  """
  pass
 def ToUniversalTime(self,time):
  """
  ToUniversalTime(self: TimeZone,time: DateTime) -> DateTime

  

   Returns the Coordinated Universal Time (UTC) that corresponds to a specified time.

  

   time: A date and time.

   Returns: A System.DateTime object whose value is the Coordinated Universal Time (UTC) that corresponds to 

    time.
  """
  pass
 DaylightName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the daylight saving time zone name.



Get: DaylightName(self: TimeZone) -> str



"""

 StandardName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the standard time zone name.



Get: StandardName(self: TimeZone) -> str



"""


 CurrentTimeZone=None

