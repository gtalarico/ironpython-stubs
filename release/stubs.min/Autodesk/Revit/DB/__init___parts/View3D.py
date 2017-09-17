class View3D(View,IDisposable):
 """ Class for 3D views """
 def CanResetCameraTarget(self):
  """
  CanResetCameraTarget(self: View3D) -> bool
  
   Checks whether the camera target can be reset for this view.
   Returns: True if camera target can be reset for this view,false otherwise.
  """
  pass
 def CanSaveOrientation(self):
  """
  CanSaveOrientation(self: View3D) -> bool
  
   Returns true if the View3D's orientation can be saved,false otherwise.
   Returns: True if the View3D's orientation can be saved,false otherwise.
  """
  pass
 def CanToggleBetweenPerspectiveAndIsometric(self):
  """
  CanToggleBetweenPerspectiveAndIsometric(self: View3D) -> bool
  
   Checks whether this view can toggle between perspective and isometric.
   Returns: True if this view can be toggled,false otherwise.
  """
  pass
 @staticmethod
 def CreateIsometric(document,viewFamilyTypeId):
  """
  CreateIsometric(document: Document,viewFamilyTypeId: ElementId) -> View3D
  
   Returns a new isometric View3D.
  
   document: The document to which the new View3D will be added.
   viewFamilyTypeId: The id of the ViewFamilyType which will be used by the new View3D.  The type 
    needs to be a ThreeDimensional ViewType.
  
   Returns: The new isometric View3D.
  """
  pass
 @staticmethod
 def CreatePerspective(document,viewFamilyTypeId):
  """
  CreatePerspective(document: Document,viewFamilyTypeId: ElementId) -> View3D
  
   Returns a new perspective View3D.
  
   document: The document to which the new View3D will be added.
   viewFamilyTypeId: The id of the ViewFamilyType which will be used by the new View3D.  The type 
    needs to be a ThreeDimensional ViewType.
  
   Returns: The new perspective View3D.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: View,view: View) -> BoundingBoxXYZ """
  pass
 def GetOrientation(self):
  """
  GetOrientation(self: View3D) -> ViewOrientation3D
  
   Gets the current non-saved orientation of the View3D.
   Returns: The current non-saved orientation of the View3D.
  """
  pass
 def GetRenderingSettings(self):
  """
  GetRenderingSettings(self: View3D) -> RenderingSettings
  
   Returns the current rendering settings for this 3d view.
   Returns: The returned object represents the current rendering settings.
     If you 
    change the returned object,you need to call SetRenderingSettings to apply the 
    new settings back to Revit.
  """
  pass
 def GetSavedOrientation(self):
  """
  GetSavedOrientation(self: View3D) -> ViewOrientation3D
  
   Gets the saved orientation of the View3D.
   Returns: The saved orientation of the View3D.
  """
  pass
 def GetSectionBox(self):
  """
  GetSectionBox(self: View3D) -> BoundingBoxXYZ
  
   Gets a copy of the section box for this 3D view.
   Returns: The section box.  Note that the section box can be rotated and transformed and 
    thus you will need to use
     Autodesk.Revit.DB.BoundingBoxXYZ.Transform to
     
    interpret the coordinates of the corners or sides of the box in model 
    coordinates.
  """
  pass
 def HasBeenLocked(self):
  """
  HasBeenLocked(self: View3D) -> bool
  
   Identifies if the view has ever been locked.
  """
  pass
 def OrientTo(self,forwardDirection):
  """
  OrientTo(self: View3D,forwardDirection: XYZ)
   Reorients the view to align with the forward direction.
  
   forwardDirection: The forward direction.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def ResetCameraTarget(self):
  """
  ResetCameraTarget(self: View3D)
   Resets the camera target to the center of the field of view.
  """
  pass
 def RestoreOrientationAndLock(self):
  """
  RestoreOrientationAndLock(self: View3D)
   Locks the view and restores its orientation.
  """
  pass
 def SaveOrientation(self):
  """
  SaveOrientation(self: View3D)
   Converts the temporary orientation of the View3D into its saved orientation.
  """
  pass
 def SaveOrientationAndLock(self):
  """
  SaveOrientationAndLock(self: View3D)
   Locks the view and saves its orientation
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetOrientation(self,newViewOrientation3D):
  """
  SetOrientation(self: View3D,newViewOrientation3D: ViewOrientation3D)
   Sets the temporary orientation of the View3D.  The new orientation is not saved 
    in the document.
  
  
   newViewOrientation3D: The new orientation to set.
  """
  pass
 def SetRenderingSettings(self,settings):
  """
  SetRenderingSettings(self: View3D,settings: RenderingSettings)
   Changes the rendering settings for this 3d view.
  
   settings: The new rendering settings to be applied to this view.
  """
  pass
 def SetSectionBox(self,boundingBoxXYZ):
  """
  SetSectionBox(self: View3D,boundingBoxXYZ: BoundingBoxXYZ)
   Sets the section box for this 3D view.
  
   boundingBoxXYZ: The bounding box to use for the section box.  To turn off the section box,set 
    Autodesk.Revit.DB.View3D.IsSectionBoxActive to false.
     Individual bound 
    enabled flags in the input box are ignored.
  """
  pass
 def ToggleToIsometric(self):
  """
  ToggleToIsometric(self: View3D)
   Toggles this view to isometric.
  """
  pass
 def ToggleToPerspective(self):
  """
  ToggleToPerspective(self: View3D)
   Toggles this view to perspective.
  """
  pass
 def Unlock(self):
  """
  Unlock(self: View3D)
   Unlocks the view. Has no effect if the view is already unlocked.
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
 IsLocked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the view is locked.

Get: IsLocked(self: View3D) -> bool

"""

 IsPerspective=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies whether this is a perspective view.

Get: IsPerspective(self: View3D) -> bool

"""

 IsSectionBoxActive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies whether or not the section box is active in this 3D view.

Get: IsSectionBoxActive(self: View3D) -> bool

Set: IsSectionBoxActive(self: View3D)=value
"""


