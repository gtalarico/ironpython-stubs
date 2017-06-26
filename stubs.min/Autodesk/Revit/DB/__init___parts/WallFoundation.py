class WallFoundation(HostObject,IDisposable):
 """ An object that represents a wall foundation element. """
 @staticmethod
 def Create(document,typeId,wallId):
  """
  Create(document: Document,typeId: ElementId,wallId: ElementId) -> WallFoundation
  
   Creates a new wall foundation within the project.
  
   document: The document.
   typeId: The id of the wall foundation type of the newly created wall foundation.
   wallId: The id of the host wall of the newly created wall foundation.
   Returns: If successful,returns the newly created wall foundation,ll otherwise.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetFoundationType(self):
  """
  GetFoundationType(self: WallFoundation) -> WallFoundationType
  
   Gets an object that represents the type of the foundation.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetFoundationType(self,type):
  """
  SetFoundationType(self: WallFoundation,type: WallFoundationType)
   Sets an object that represents the type of the foundation.
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
 WallId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the id of the host wall.

Get: WallId(self: WallFoundation) -> ElementId

"""


