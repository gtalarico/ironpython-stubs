class EditScope(object,IDisposable):
 """ The base class for a scope object that provides special access and limitations related to editing certain elements. """
 def Cancel(self):
  """
  Cancel(self: EditScope)
   Cancels the edit scope.
  """
  pass
 def Commit(self,failurePreprocessor):
  """
  Commit(self: EditScope,failurePreprocessor: IFailuresPreprocessor)
   Finishes the edit scope.
  
   failurePreprocessor: Callback to be invoked in the beginning of failure processing.
  """
  pass
 def Dispose(self):
  """ Dispose(self: EditScope) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: EditScope,disposing: bool) """
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
 IsActive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Tells if the EditScope is active. In other words,the EditScope has started but not committed/canceled yet.

Get: IsActive(self: EditScope) -> bool

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: EditScope) -> bool

"""


