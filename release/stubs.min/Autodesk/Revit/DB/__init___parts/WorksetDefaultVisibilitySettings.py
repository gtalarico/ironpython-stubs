class WorksetDefaultVisibilitySettings(Element,IDisposable):
 """ An object that manages default visibility of worksets in a document. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 @staticmethod
 def GetWorksetDefaultVisibilitySettings(aDoc):
  """
  GetWorksetDefaultVisibilitySettings(aDoc: Document) -> WorksetDefaultVisibilitySettings

  

   Get the WorksetDefaultVisibilitySettings of the document.

  

   aDoc: The document.

   Returns: The WorksetDefaultVisibilitySettings of the document.
  """
  pass
 def IsWorksetVisible(self,worksetId):
  """
  IsWorksetVisible(self: WorksetDefaultVisibilitySettings,worksetId: WorksetId) -> bool

  

   Indicates whether the workset is visible by default.

  

   worksetId: Id of the workset.

   Returns: Whether the workset is visible by default.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetWorksetVisibility(self,worksetId,visible):
  """
  SetWorksetVisibility(self: WorksetDefaultVisibilitySettings,worksetId: WorksetId,visible: bool)

   Set the default visibility of a workset.

  

   worksetId: Id of the workset.

   visible: Whether the workset should be visible by default or not.
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
