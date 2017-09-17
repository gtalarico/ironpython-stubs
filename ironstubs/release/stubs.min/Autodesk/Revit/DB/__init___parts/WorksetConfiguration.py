class WorksetConfiguration(object,IDisposable):
 """
 A configuration class that is passed in to methods that open Revit documents to specify which user-created worksets are opened/closed.
 
 WorksetConfiguration(option: WorksetConfigurationOption)
 WorksetConfiguration()
 WorksetConfiguration(other: WorksetConfiguration)
 """
 def Close(self,worksetsToClose):
  """ Close(self: WorksetConfiguration,worksetsToClose: IList[WorksetId]) """
  pass
 def Dispose(self):
  """ Dispose(self: WorksetConfiguration) """
  pass
 def Open(self,worksetsToOpen):
  """ Open(self: WorksetConfiguration,worksetsToOpen: IList[WorksetId]) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: WorksetConfiguration,disposing: bool) """
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
 def __new__(self,*__args):
  """
  __new__(cls: type,option: WorksetConfigurationOption)
  __new__(cls: type)
  __new__(cls: type,other: WorksetConfiguration)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: WorksetConfiguration) -> bool

"""


