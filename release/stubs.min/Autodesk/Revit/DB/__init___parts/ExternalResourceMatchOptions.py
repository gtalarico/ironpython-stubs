class ExternalResourceMatchOptions(object,IDisposable):
 """
 Represents match options used to filter external resources when listing them from external resource server.

 

 ExternalResourceMatchOptions(resourceType: ExternalResourceType)
 """
 def Dispose(self):
  """ Dispose(self: ExternalResourceMatchOptions) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ExternalResourceMatchOptions,disposing: bool) """
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
 def __new__(self,resourceType):
  """ __new__(cls: type,resourceType: ExternalResourceType) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: ExternalResourceMatchOptions) -> bool



"""

 ResourceType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The desired resource type which external resources should match.



Get: ResourceType(self: ExternalResourceMatchOptions) -> ExternalResourceType



"""


