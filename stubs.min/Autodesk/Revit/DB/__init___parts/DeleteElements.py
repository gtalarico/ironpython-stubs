class DeleteElements(FailureResolution,IDisposable):
 """ Deletes element(s) related to the failure. """
 @staticmethod
 def Create(document,*__args):
  """
  Create(document: Document,ids: ISet[ElementId]) -> FailureResolution
  Create(document: Document,ids: IList[ElementId]) -> FailureResolution
  Create(document: Document,id: ElementId) -> FailureResolution
  
   Creates an instance of the DeleteElements resolution.
  
   document: The document which owns the element to delete.
   id: The id of the element that will be deleted when this resolution is chosen.
   Returns: The instance of the DeletedElements resolution.
  """
  pass
 def Dispose(self):
  """ Dispose(self: FailureResolution,A_0: bool) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FailureResolution,disposing: bool) """
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
