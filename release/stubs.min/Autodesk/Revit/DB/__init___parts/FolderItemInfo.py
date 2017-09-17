class FolderItemInfo(object,IDisposable):
 """ Contains data for each folder item in the organization settings of the project browser including folder parameter Id and folder name. """
 def Dispose(self):
  """ Dispose(self: FolderItemInfo) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FolderItemInfo,disposing: bool) """
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
 ElementId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The folder parameter Id

Get: ElementId(self: FolderItemInfo) -> ElementId

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FolderItemInfo) -> bool

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The folder name

Get: Name(self: FolderItemInfo) -> str

"""


