class DocumentPreviewSettings(object,IDisposable):
 """ Contains the settings related to the saving of preview images for a given document. """
 def Dispose(self):
  """ Dispose(self: DocumentPreviewSettings) """
  pass
 def ForceViewUpdate(self,forceViewUpdate):
  """
  ForceViewUpdate(self: DocumentPreviewSettings,forceViewUpdate: bool)

   Sets Revit to update the preview view if necessary.

  

   forceViewUpdate: True to force update of the preview view.  False to skip update if necessary 

    (the default).
  """
  pass
 def IsViewIdValidForPreview(self,viewId):
  """
  IsViewIdValidForPreview(self: DocumentPreviewSettings,viewId: ElementId) -> bool

  

   Identifies if the view id is valid as a preview view id.

  

   viewId: The view id.

   Returns: True if the view id is valid for preview,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: DocumentPreviewSettings,disposing: bool) """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: DocumentPreviewSettings) -> bool



"""

 IsViewUpdateForced=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if Revit will update the preview view if necessary.



Get: IsViewUpdateForced(self: DocumentPreviewSettings) -> bool



"""

 PreviewViewId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The view id that will be used to generate the preview.



Get: PreviewViewId(self: DocumentPreviewSettings) -> ElementId



Set: PreviewViewId(self: DocumentPreviewSettings)=value

"""


