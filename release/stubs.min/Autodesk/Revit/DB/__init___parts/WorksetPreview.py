class WorksetPreview(object,IDisposable):
 """ Represents an accessor for workset data which can be obtained from an unopened document. """
 def Dispose(self):
  """ Dispose(self: WorksetPreview) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: WorksetPreview,disposing: bool) """
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
 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Id of the workset.



Get: Id(self: WorksetPreview) -> WorksetId



"""

 IsDefaultWorkset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether the workset is the default one.



Get: IsDefaultWorkset(self: WorksetPreview) -> bool



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: WorksetPreview) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Name of the workset.



Get: Name(self: WorksetPreview) -> str



"""

 Owner=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """User name of the workset.



Get: Owner(self: WorksetPreview) -> str



"""

 UniqueId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """UniqueId of the workset.



Get: UniqueId(self: WorksetPreview) -> Guid



"""


