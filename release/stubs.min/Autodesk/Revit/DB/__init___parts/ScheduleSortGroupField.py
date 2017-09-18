class ScheduleSortGroupField(object,IDisposable):
 """
 A field that is used for sorting and/or grouping in a schedule.

 

 ScheduleSortGroupField(fieldId: ScheduleFieldId,sortOrder: ScheduleSortOrder)

 ScheduleSortGroupField(fieldId: ScheduleFieldId)

 ScheduleSortGroupField()
 """
 def Dispose(self):
  """ Dispose(self: ScheduleSortGroupField) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ScheduleSortGroupField,disposing: bool) """
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
 def __new__(self,fieldId=None,sortOrder=None):
  """
  __new__(cls: type,fieldId: ScheduleFieldId,sortOrder: ScheduleSortOrder)

  __new__(cls: type,fieldId: ScheduleFieldId)

  __new__(cls: type)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 FieldId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The ID of the field that the schedule will be sorted or grouped by.



Get: FieldId(self: ScheduleSortGroupField) -> ScheduleFieldId



Set: FieldId(self: ScheduleSortGroupField)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: ScheduleSortGroupField) -> bool



"""

 ShowBlankLine=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if an empty row should be displayed between groups.



Get: ShowBlankLine(self: ScheduleSortGroupField) -> bool



Set: ShowBlankLine(self: ScheduleSortGroupField)=value

"""

 ShowFooter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if a footer row should be displayed after each group.



Get: ShowFooter(self: ScheduleSortGroupField) -> bool



Set: ShowFooter(self: ScheduleSortGroupField)=value

"""

 ShowFooterCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the footer row should display a count of elements in the group.



Get: ShowFooterCount(self: ScheduleSortGroupField) -> bool



Set: ShowFooterCount(self: ScheduleSortGroupField)=value

"""

 ShowFooterTitle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the footer row should display a title.



Get: ShowFooterTitle(self: ScheduleSortGroupField) -> bool



Set: ShowFooterTitle(self: ScheduleSortGroupField)=value

"""

 ShowHeader=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if a header row should be displayed before each group.



Get: ShowHeader(self: ScheduleSortGroupField) -> bool



Set: ShowHeader(self: ScheduleSortGroupField)=value

"""

 SortOrder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if elements in the schedule will be sorted in

   ascending or descending order.



Get: SortOrder(self: ScheduleSortGroupField) -> ScheduleSortOrder



Set: SortOrder(self: ScheduleSortGroupField)=value

"""


