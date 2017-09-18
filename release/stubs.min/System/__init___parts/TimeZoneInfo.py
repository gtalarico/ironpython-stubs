class TimeZoneInfo(object,IEquatable[TimeZoneInfo],ISerializable,IDeserializationCallback):
 """ Represents any time zone in the world. """
 @staticmethod
 def ClearCachedData():
  """
  ClearCachedData()

   Clears cached time zone data.
  """
  pass
 @staticmethod
 def ConvertTime(*__args):
  """
  ConvertTime(dateTime: DateTime,sourceTimeZone: TimeZoneInfo,destinationTimeZone: TimeZoneInfo) -> DateTime

  

   Converts a time from one time zone to another.

  

   dateTime: The date and time to convert.

   sourceTimeZone: The time zone of dateTime.

   destinationTimeZone: The time zone to convert dateTime to.

   Returns: The date and time in the destination time zone that corresponds to the dateTime parameter in the 

    source time zone.

  

  ConvertTime(dateTime: DateTime,destinationTimeZone: TimeZoneInfo) -> DateTime

  

   Converts a time to the time in a particular time zone.

  

   dateTime: The date and time to convert.

   destinationTimeZone: The time zone to convert dateTime to.

   Returns: The date and time in the destination time zone.

  ConvertTime(dateTimeOffset: DateTimeOffset,destinationTimeZone: TimeZoneInfo) -> DateTimeOffset

  

   Converts a time to the time in a particular time zone.

  

   dateTimeOffset: The date and time to convert.

   destinationTimeZone: The time zone to convert dateTime to.

   Returns: The date and time in the destination time zone.
  """
  pass
 @staticmethod
 def ConvertTimeBySystemTimeZoneId(*__args):
  """
  ConvertTimeBySystemTimeZoneId(dateTime: DateTime,sourceTimeZoneId: str,destinationTimeZoneId: str) -> DateTime

  

   Converts a time from one time zone to another based on time zone identifiers.

  

   dateTime: The date and time to convert.

   sourceTimeZoneId: The identifier of the source time zone.

   destinationTimeZoneId: The identifier of the destination time zone.

   Returns: The date and time in the destination time zone that corresponds to the dateTime parameter in the 

    source time zone.

  

  ConvertTimeBySystemTimeZoneId(dateTime: DateTime,destinationTimeZoneId: str) -> DateTime

  

   Converts a time to the time in another time zone based on the time zone's identifier.

  

   dateTime: The date and time to convert.

   destinationTimeZoneId: The identifier of the destination time zone.

   Returns: The date and time in the destination time zone.

  ConvertTimeBySystemTimeZoneId(dateTimeOffset: DateTimeOffset,destinationTimeZoneId: str) -> DateTimeOffset

  

   Converts a time to the time in another time zone based on the time zone's identifier.

  

   dateTimeOffset: The date and time to convert.

   destinationTimeZoneId: The identifier of the destination time zone.

   Returns: The date and time in the destination time zone.
  """
  pass
 @staticmethod
 def ConvertTimeFromUtc(dateTime,destinationTimeZone):
  """
  ConvertTimeFromUtc(dateTime: DateTime,destinationTimeZone: TimeZoneInfo) -> DateTime

  

   Converts a Coordinated Universal Time (UTC) to the time in a specified time zone.

  

   dateTime: The Coordinated Universal Time (UTC).

   destinationTimeZone: The time zone to convert dateTime to.

   Returns: The date and time in the destination time zone. Its System.DateTime.Kind property is 

    System.DateTimeKind.Utc if destinationTimeZone is System.TimeZoneInfo.Utc; otherwise,its 

    System.DateTime.Kind property is System.DateTimeKind.Unspecified.
  """
  pass
 @staticmethod
 def ConvertTimeToUtc(dateTime,sourceTimeZone=None):
  """
  ConvertTimeToUtc(dateTime: DateTime,sourceTimeZone: TimeZoneInfo) -> DateTime

  

   Converts the time in a specified time zone to Coordinated Universal Time (UTC).

  

   dateTime: The date and time to convert.

   sourceTimeZone: The time zone of dateTime.

   Returns: The Coordinated Universal Time (UTC) that corresponds to the dateTime parameter. The 

    System.DateTime object's System.DateTime.Kind property is always set to System.DateTimeKind.Utc.

  

  ConvertTimeToUtc(dateTime: DateTime) -> DateTime

  

   Converts the current date and time to Coordinated Universal Time (UTC).

  

   dateTime: The date and time to convert.

   Returns: The Coordinated Universal Time (UTC) that corresponds to the dateTime parameter. The 

    System.DateTime value's System.DateTime.Kind property is always set to System.DateTimeKind.Utc.
  """
  pass
 @staticmethod
 def CreateCustomTimeZone(id,baseUtcOffset,displayName,standardDisplayName,daylightDisplayName=None,adjustmentRules=None,disableDaylightSavingTime=None):
  """
  CreateCustomTimeZone(id: str,baseUtcOffset: TimeSpan,displayName: str,standardDisplayName: str,daylightDisplayName: str,adjustmentRules: Array[AdjustmentRule],disableDaylightSavingTime: bool) -> TimeZoneInfo

  CreateCustomTimeZone(id: str,baseUtcOffset: TimeSpan,displayName: str,standardDisplayName: str,daylightDisplayName: str,adjustmentRules: Array[AdjustmentRule]) -> TimeZoneInfo

  CreateCustomTimeZone(id: str,baseUtcOffset: TimeSpan,displayName: str,standardDisplayName: str) -> TimeZoneInfo

  

   Creates a custom time zone with a specified identifier,an offset from Coordinated Universal 

    Time (UTC),a display name,and a standard time display name.

  

  

   id: The time zone's identifier.

   baseUtcOffset: An object that represents the time difference between this time zone and Coordinated Universal 

    Time (UTC).

  

   displayName: The display name of the new time zone.

   standardDisplayName: The name of the new time zone's standard time.

   Returns: The new time zone.
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: TimeZoneInfo,obj: object) -> bool

  Equals(self: TimeZoneInfo,other: TimeZoneInfo) -> bool

  

   Determines whether the current System.TimeZoneInfo object and another System.TimeZoneInfo object 

    are equal.

  

  

   other: A second object to compare with the current object.

   Returns: true if the two System.TimeZoneInfo objects are equal; otherwise,false.
  """
  pass
 @staticmethod
 def FindSystemTimeZoneById(id):
  """
  FindSystemTimeZoneById(id: str) -> TimeZoneInfo

  

   Retrieves a System.TimeZoneInfo object from the registry based on its identifier.

  

   id: The time zone identifier,which corresponds to the System.TimeZoneInfo.Id property.

   Returns: An object whose identifier is the value of the id parameter.
  """
  pass
 @staticmethod
 def FromSerializedString(source):
  """
  FromSerializedString(source: str) -> TimeZoneInfo

  

   Deserializes a string to re-create an original serialized System.TimeZoneInfo object.

  

   source: The string representation of the serialized System.TimeZoneInfo object.

   Returns: The original serialized object.
  """
  pass
 def GetAdjustmentRules(self):
  """
  GetAdjustmentRules(self: TimeZoneInfo) -> Array[AdjustmentRule]

  

   Retrieves an array of System.TimeZoneInfo.AdjustmentRule objects that apply to the current 

    System.TimeZoneInfo object.

  

   Returns: An array of objects for this time zone.
  """
  pass
 def GetAmbiguousTimeOffsets(self,*__args):
  """
  GetAmbiguousTimeOffsets(self: TimeZoneInfo,dateTime: DateTime) -> Array[TimeSpan]

  

   Returns information about the possible dates and times that an ambiguous date and time can be 

    mapped to.

  

  

   dateTime: A date and time.

   Returns: An array of objects that represents possible Coordinated Universal Time (UTC) offsets that a 

    particular date and time can be mapped to.

  

  GetAmbiguousTimeOffsets(self: TimeZoneInfo,dateTimeOffset: DateTimeOffset) -> Array[TimeSpan]

  

   Returns information about the possible dates and times that an ambiguous date and time can be 

    mapped to.

  

  

   dateTimeOffset: A date and time.

   Returns: An array of objects that represents possible Coordinated Universal Time (UTC) offsets that a 

    particular date and time can be mapped to.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TimeZoneInfo) -> int

  

   Serves as a hash function for hashing algorithms and data structures such as hash tables.

   Returns: A 32-bit signed integer that serves as the hash code for this System.TimeZoneInfo object.
  """
  pass
 @staticmethod
 def GetSystemTimeZones():
  """
  GetSystemTimeZones() -> ReadOnlyCollection[TimeZoneInfo]

  

   Returns a sorted collection of all the time zones about which information is available on the 

    local system.

  

   Returns: A read-only collection of System.TimeZoneInfo objects.
  """
  pass
 def GetUtcOffset(self,*__args):
  """
  GetUtcOffset(self: TimeZoneInfo,dateTime: DateTime) -> TimeSpan

  

   Calculates the offset or difference between the time in this time zone and Coordinated Universal 

    Time (UTC) for a particular date and time.

  

  

   dateTime: The date and time to determine the offset for.

   Returns: An object that indicates the time difference between the two time zones.

  GetUtcOffset(self: TimeZoneInfo,dateTimeOffset: DateTimeOffset) -> TimeSpan

  

   Calculates the offset or difference between the time in this time zone and Coordinated Universal 

    Time (UTC) for a particular date and time.

  

  

   dateTimeOffset: The date and time to determine the offset for.

   Returns: An object that indicates the time difference between Coordinated Universal Time (UTC) and the 

    current time zone.
  """
  pass
 def HasSameRules(self,other):
  """
  HasSameRules(self: TimeZoneInfo,other: TimeZoneInfo) -> bool

  

   Indicates whether the current object and another System.TimeZoneInfo object have the same 

    adjustment rules.

  

  

   other: A second object to compare with the current System.TimeZoneInfo object.

   Returns: true if the two time zones have identical adjustment rules and an identical base offset; 

    otherwise,false.
  """
  pass
 def IsAmbiguousTime(self,*__args):
  """
  IsAmbiguousTime(self: TimeZoneInfo,dateTime: DateTime) -> bool

  

   Determines whether a particular date and time in a particular time zone is ambiguous and can be 

    mapped to two or more Coordinated Universal Time (UTC) times.

  

  

   dateTime: A date and time value.

   Returns: true if the dateTime parameter is ambiguous; otherwise,false.

  IsAmbiguousTime(self: TimeZoneInfo,dateTimeOffset: DateTimeOffset) -> bool

  

   Determines whether a particular date and time in a particular time zone is ambiguous and can be 

    mapped to two or more Coordinated Universal Time (UTC) times.

  

  

   dateTimeOffset: A date and time.

   Returns: true if the dateTimeOffset parameter is ambiguous in the current time zone; otherwise,false.
  """
  pass
 def IsDaylightSavingTime(self,*__args):
  """
  IsDaylightSavingTime(self: TimeZoneInfo,dateTime: DateTime) -> bool

  

   Indicates whether a specified date and time falls in the range of daylight saving time for the 

    time zone of the current System.TimeZoneInfo object.

  

  

   dateTime: A date and time value.

   Returns: true if the dateTime parameter is a daylight saving time; otherwise,false.

  IsDaylightSavingTime(self: TimeZoneInfo,dateTimeOffset: DateTimeOffset) -> bool

  

   Indicates whether a specified date and time falls in the range of daylight saving time for the 

    time zone of the current System.TimeZoneInfo object.

  

  

   dateTimeOffset: A date and time value.

   Returns: true if the dateTimeOffset parameter is a daylight saving time; otherwise,false.
  """
  pass
 def IsInvalidTime(self,dateTime):
  """
  IsInvalidTime(self: TimeZoneInfo,dateTime: DateTime) -> bool

  

   Indicates whether a particular date and time is invalid.

  

   dateTime: A date and time value.

   Returns: true if dateTime is invalid; otherwise,false.
  """
  pass
 def ToSerializedString(self):
  """
  ToSerializedString(self: TimeZoneInfo) -> str

  

   Converts the current System.TimeZoneInfo object to a serialized string.

   Returns: A string that represents the current System.TimeZoneInfo object.
  """
  pass
 def ToString(self):
  """
  ToString(self: TimeZoneInfo) -> str

  

   Returns the current System.TimeZoneInfo object's display name.

   Returns: The value of the System.TimeZoneInfo.DisplayName property of the current System.TimeZoneInfo 

    object.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 BaseUtcOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the time difference between the current time zone's standard time and Coordinated Universal Time (UTC).



Get: BaseUtcOffset(self: TimeZoneInfo) -> TimeSpan



"""

 DaylightName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the localized display name for the current time zone's daylight saving time.



Get: DaylightName(self: TimeZoneInfo) -> str



"""

 DisplayName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the localized general display name that represents the time zone.



Get: DisplayName(self: TimeZoneInfo) -> str



"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the time zone identifier.



Get: Id(self: TimeZoneInfo) -> str



"""

 StandardName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the localized display name for the time zone's standard time.



Get: StandardName(self: TimeZoneInfo) -> str



"""

 SupportsDaylightSavingTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the time zone has any daylight saving time rules.



Get: SupportsDaylightSavingTime(self: TimeZoneInfo) -> bool



"""


 AdjustmentRule=None
 Local=None
 TransitionTime=None
 Utc=None

