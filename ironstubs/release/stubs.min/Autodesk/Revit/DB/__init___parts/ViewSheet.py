class ViewSheet(View,IDisposable):
 """ Class for ViewSheet """
 def ConvertToRealSheet(self,titleBlockTypeId):
  """
  ConvertToRealSheet(self: ViewSheet,titleBlockTypeId: ElementId)
   Converts a placeholder sheet to a real one with an optional titleblock.
  
   titleBlockTypeId: The id of the placeholder sheet,or invalidElementId if no titleblock should be 
    added.
  """
  pass
 @staticmethod
 def Create(document,titleBlockTypeId):
  """
  Create(document: Document,titleBlockTypeId: ElementId) -> ViewSheet
  
   Creates a new ViewSheet.
  
   document: The document to which the ViewSheet will be added.
   titleBlockTypeId: The type id of the TitleBlock type which will be used by the new ViewSheet.
     
    For no TitleBlock,pass invalid element ID.
  
   Returns: The new ViewSheet.
  """
  pass
 @staticmethod
 def CreatePlaceholder(aDoc):
  """
  CreatePlaceholder(aDoc: Document) -> ViewSheet
  
   Creates a placeholder sheet in a document.
  
   aDoc: The document.
   Returns: The placeholder sheet.
  """
  pass
 def DeleteViewport(self,viewport):
  """
  DeleteViewport(self: ViewSheet,viewport: Viewport)
   Removes a viewport from the sheet by deleting it from the document.
  
   viewport: The viewport that will be deleted and removed from the sheet.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def GetAdditionalRevisionIds(self):
  """
  GetAdditionalRevisionIds(self: ViewSheet) -> ICollection[ElementId]
  
   Gets the Revisions that are additionally included in the sheet's revision 
    schedules.
  
   Returns: The additionally included Revisions for the sheet's revision schedules.
  """
  pass
 def GetAllPlacedViews(self):
  """
  GetAllPlacedViews(self: ViewSheet) -> ISet[ElementId]
  
   Returns the ElementIds of Views placed on this sheet.
   Returns: The ids of the views on this sheet.
  """
  pass
 def GetAllRevisionIds(self):
  """
  GetAllRevisionIds(self: ViewSheet) -> IList[ElementId]
  
   Gets the ordered array of Revisions which participate in the sheet's revision 
    schedules.
  
   Returns: The ordered array of ids of Revisions participating in the sheet's revision 
    schedules.
  """
  pass
 def GetAllViewports(self):
  """
  GetAllViewports(self: ViewSheet) -> ICollection[ElementId]
  
   Returns the ElementIds of Viewports on this sheet.
   Returns: The Viewports on this sheet.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: View,view: View) -> BoundingBoxXYZ """
  pass
 def GetCurrentRevision(self):
  """
  GetCurrentRevision(self: ViewSheet) -> ElementId
  
   Returns the most recent numbered Revision shown on this ViewSheet.
   Returns: The Id of the most recent numbered Revision shown on this ViewSheet or 
    InvalidElementId if none are shown.
  """
  pass
 def GetRevisionCloudNumberOnSheet(self,revisionCloudId):
  """
  GetRevisionCloudNumberOnSheet(self: ViewSheet,revisionCloudId: ElementId) -> str
  
   Gets the Revision Number for a RevisionCloud on this sheet.
  
   revisionCloudId: The id of the RevisionCLoud.
   Returns: Returns the Revision Number as it will appear on this sheet or ll if there is 
    no Revision Number assigned on this sheet.
  """
  pass
 def GetRevisionNumberOnSheet(self,revisionId):
  """
  GetRevisionNumberOnSheet(self: ViewSheet,revisionId: ElementId) -> str
  
   Gets the Revision Number for a particular Revision as it will appear on this 
    sheet.
  
  
   revisionId: The id of the Revision.
   Returns: Returns the Revision Number as it will appear on this sheet or ll if the 
    Revision does not appear on this sheet.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def SetAdditionalRevisionIds(self,projectRevisionIds):
  """ SetAdditionalRevisionIds(self: ViewSheet,projectRevisionIds: ICollection[ElementId]) """
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
 IsPlaceholder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies whether or not the view sheet represents a placeholder sheet.

Get: IsPlaceholder(self: ViewSheet) -> bool

"""

 SheetNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The sheet number of the document.

Get: SheetNumber(self: ViewSheet) -> str

Set: SheetNumber(self: ViewSheet)=value
"""


