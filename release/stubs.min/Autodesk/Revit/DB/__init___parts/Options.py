class Options(APIObject,IDisposable):
 """
 User preferences for parsing of geometry.
 
 Options(pOptions: Options)
 Options()
 """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
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
 def __new__(self,pOptions=None):
  """
  __new__(cls: type,pOptions: Options)
  __new__(cls: type)
  """
  pass
 ComputeReferences=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines whether or not references to geometric objects are computed.

Get: ComputeReferences(self: Options) -> bool

 Checks whether references to geometric objects are computed.

Set: ComputeReferences(self: Options)
 Enables computing of references to geometric objects.
=value
"""

 DetailLevel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The detail level for the geometry extracted with these options.

Get: DetailLevel(self: Options) -> ViewDetailLevel

 Returns the preferred detail level.

Set: DetailLevel(self: Options)
 Sets the preferred detail level.
=value
"""

 IncludeNonVisibleObjects=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether to extract element geometry objects not set as Visible.  The default is false.

Get: IncludeNonVisibleObjects(self: Options) -> bool

Set: IncludeNonVisibleObjects(self: Options)=value
"""

 View=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The view used for geometry extraction.

Get: View(self: Options) -> View

 Retrieves the view that was set for this object.

Set: View(self: Options)
 Sets the view that drives extraction of geometry.
=value
"""


