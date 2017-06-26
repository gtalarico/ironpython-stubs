class Viewport(Element,IDisposable):
 """ An element that establishes the placement of a view on a sheet. """
 @staticmethod
 def CanAddViewToSheet(document,viewSheetId,viewId):
  """
  CanAddViewToSheet(document: Document,viewSheetId: ElementId,viewId: ElementId) -> bool
  
   Verifies that the view can be added to the ViewSheet.
  
   document: The document in which the views reside.
   viewSheetId: The ViewSheet on which the view will be placed.
   viewId: The view which will be checked to see if it can be placed on the sheet.
   Returns: True if the view can be added to the ViewSheet,false otherwise.
  """
  pass
 @staticmethod
 def Create(document,viewSheetId,viewId,point):
  """
  Create(document: Document,viewSheetId: ElementId,viewId: ElementId,point: XYZ) -> Viewport
  
   Creates a new Viewport at a given location on a sheet.
  
   document: The document to which the new Viewport will be added.
   viewSheetId: The ViewSheet on which the new Viewport will be placed.
   viewId: The view shown in the Viewport.
   point: The new Viewport will be centered on this point.
   Returns: The new Viewport.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetBoxCenter(self):
  """
  GetBoxCenter(self: Viewport) -> XYZ
  
   Returns the center of the outline of the viewport on the sheet,excluding the 
    viewport label.
  
   Returns: The center of the outline of the viewport on the sheet.
  """
  pass
 def GetBoxOutline(self):
  """
  GetBoxOutline(self: Viewport) -> Outline
  
   Returns the outline of the viewport on the sheet,excluding the viewport label.
   Returns: The outline of the viewport on the sheet.
  """
  pass
 def GetLabelOutline(self):
  """
  GetLabelOutline(self: Viewport) -> Outline
  
   Gets the outline viewport's label on the sheet.
   Returns: The outline of the viewport's label on the sheet.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def SetBoxCenter(self,newCenterPoint):
  """
  SetBoxCenter(self: Viewport,newCenterPoint: XYZ)
   Moves this viewport so that the center of the box outline (excluding the 
    viewport label) is at a given point.
  
  
   newCenterPoint: The desired center for the box outline.
  """
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
 Rotation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The rotation of the viewport on the sheet.

Get: Rotation(self: Viewport) -> ViewportRotation

Set: Rotation(self: Viewport)=value
"""

 SheetId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The element id of the ViewSheet on which the viewport appears,
   or InvalidElementId if this viewport does not associate a view
   with placement onto a sheet.

Get: SheetId(self: Viewport) -> ElementId

"""

 ViewId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The element id of the associated View.

Get: ViewId(self: Viewport) -> ElementId

"""


