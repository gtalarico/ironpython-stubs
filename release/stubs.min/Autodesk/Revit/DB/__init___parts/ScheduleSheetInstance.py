class ScheduleSheetInstance(Element,IDisposable):
 """ An element that represents a particular placement of a schedule on a sheet. """
 @staticmethod
 def Create(document,viewSheetId,scheduleId,origin):
  """
  Create(document: Document,viewSheetId: ElementId,scheduleId: ElementId,origin: XYZ) -> ScheduleSheetInstance

  

   Create an instance of a schedule on a sheet.

  

   document: The document

   viewSheetId: The id of the sheet where the schedule will be placed.

   scheduleId: The id of the schedule view.

   origin: Location on the sheet where the schedule will be placed.

   Returns: The new ScheduleInstance.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
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
 IsTitleblockRevisionSchedule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if this ScheduleSheetInstance is a revision schedule in a titleblock family.



Get: IsTitleblockRevisionSchedule(self: ScheduleSheetInstance) -> bool



"""

 Point=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Location on the sheet where the ScheduleInstance is placed (in sheet coordinates).



Get: Point(self: ScheduleSheetInstance) -> XYZ



Set: Point(self: ScheduleSheetInstance)=value

"""

 Rotation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Rotation of the ScheduleInstance.



Get: Rotation(self: ScheduleSheetInstance) -> ViewportRotation



Set: Rotation(self: ScheduleSheetInstance)=value

"""

 ScheduleId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Id of the "master" schedule that generates this ScheduleInstance.



Get: ScheduleId(self: ScheduleSheetInstance) -> ElementId



"""


