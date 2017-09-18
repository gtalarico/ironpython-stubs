class ScheduleFilter(object,IDisposable):
 """
 A filter in a schedule.

 

 ScheduleFilter(fieldId: ScheduleFieldId,filterType: ScheduleFilterType,value: ElementId)

 ScheduleFilter(fieldId: ScheduleFieldId,filterType: ScheduleFilterType,value: str)

 ScheduleFilter(fieldId: ScheduleFieldId,filterType: ScheduleFilterType,value: float)

 ScheduleFilter(fieldId: ScheduleFieldId,filterType: ScheduleFilterType,value: int)

 ScheduleFilter(fieldId: ScheduleFieldId,filterType: ScheduleFilterType)

 ScheduleFilter()
 """
 def Dispose(self):
  """ Dispose(self: ScheduleFilter) """
  pass
 def GetDoubleValue(self):
  """
  GetDoubleValue(self: ScheduleFilter) -> float

  

   Gets the filter value for a filter using a double value.

   Returns: The filter value.
  """
  pass
 def GetElementIdValue(self):
  """
  GetElementIdValue(self: ScheduleFilter) -> ElementId

  

   Gets the filter value for a filter using an ElementId value.

   Returns: The filter value.
  """
  pass
 def GetIntegerValue(self):
  """
  GetIntegerValue(self: ScheduleFilter) -> int

  

   Gets the filter value for a filter using an integer value.

   Returns: The filter value.
  """
  pass
 def GetStringValue(self):
  """
  GetStringValue(self: ScheduleFilter) -> str

  

   Gets the filter value for a filter using a string value.

   Returns: The filter value.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ScheduleFilter,disposing: bool) """
  pass
 def SetNullValue(self):
  """
  SetNullValue(self: ScheduleFilter)

   Sets the filter to have no specified value (used for HasParameter filters).
  """
  pass
 def SetValue(self,*__args):
  """
  SetValue(self: ScheduleFilter,value: float)

   Set the filter value to a double.

  

   value: The filter value.

  SetValue(self: ScheduleFilter,value: int)

   Set the filter value to an integer.

  

   value: The filter value.

  SetValue(self: ScheduleFilter,id: ElementId)

   Set the filter value to an ElementId.

  

   id: The filter value.

  SetValue(self: ScheduleFilter,string: str)

   Set the filter value to a string.

  

   string: The filter value.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,fieldId=None,filterType=None,value=None):
  """
  __new__(cls: type,fieldId: ScheduleFieldId,filterType: ScheduleFilterType,value: ElementId)

  __new__(cls: type,fieldId: ScheduleFieldId,filterType: ScheduleFilterType,value: str)

  __new__(cls: type,fieldId: ScheduleFieldId,filterType: ScheduleFilterType,value: float)

  __new__(cls: type,fieldId: ScheduleFieldId,filterType: ScheduleFilterType,value: int)

  __new__(cls: type,fieldId: ScheduleFieldId,filterType: ScheduleFilterType)

  __new__(cls: type)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 FieldId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The ID of the field used to filter the schedule.



Get: FieldId(self: ScheduleFilter) -> ScheduleFieldId



Set: FieldId(self: ScheduleFilter)=value

"""

 FilterType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The filter type.



Get: FilterType(self: ScheduleFilter) -> ScheduleFilterType



Set: FilterType(self: ScheduleFilter)=value

"""

 IsDoubleValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the filter has a double value.



Get: IsDoubleValue(self: ScheduleFilter) -> bool



"""

 IsElementIdValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the filter has an ElementId value.



Get: IsElementIdValue(self: ScheduleFilter) -> bool



"""

 IsIntegerValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the filter has an integer value.



Get: IsIntegerValue(self: ScheduleFilter) -> bool



"""

 IsNullValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the filter has no specified value.



Get: IsNullValue(self: ScheduleFilter) -> bool



"""

 IsStringValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the filter has a string value.



Get: IsStringValue(self: ScheduleFilter) -> bool



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: ScheduleFilter) -> bool



"""


