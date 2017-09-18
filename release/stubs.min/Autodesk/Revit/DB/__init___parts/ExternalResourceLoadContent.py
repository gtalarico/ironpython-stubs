class ExternalResourceLoadContent(object,IDisposable):
 """
 This class contains the actual content data and other results of an external resource load operation that are
    returned by an IExternalResourceServer to Revit.
 """
 def Dispose(self):
  """ Dispose(self: ExternalResourceLoadContent) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ExternalResourceLoadContent,disposing: bool) """
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

Get: IsValidObject(self: ExternalResourceLoadContent) -> bool

"""

 LoadStatus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A value to indicate the status of an external resource load operation.  IExternalResourceServers
   should set this in the LoadResource() method.

Get: LoadStatus(self: ExternalResourceLoadContent) -> ExternalResourceLoadStatus

Set: LoadStatus(self: ExternalResourceLoadContent)=value
"""

 Version=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The version of the external data that the server is providing in this object.

Get: Version(self: ExternalResourceLoadContent) -> str

Set: Version(self: ExternalResourceLoadContent)=value
"""


