class UpdaterInfo(object,IDisposable):
 """ Information of an updater,such as: Name,AdditionalInformation,name of the application that owns the updater,etc. """
 def Dispose(self):
  """ Dispose(self: UpdaterInfo) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: UpdaterInfo,disposing: bool) """
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
 AdditionalInformation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Additional information about the updater.



Get: AdditionalInformation(self: UpdaterInfo) -> str



"""

 ApplicationName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Name of the application that owns the updater.



Get: ApplicationName(self: UpdaterInfo) -> str



"""

 IsOptional=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether the updater is optional or not.



Get: IsOptional(self: UpdaterInfo) -> bool



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: UpdaterInfo) -> bool



"""

 UpdaterName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Name of the updater.



Get: UpdaterName(self: UpdaterInfo) -> str



"""


