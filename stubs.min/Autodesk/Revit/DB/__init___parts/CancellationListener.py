class CancellationListener(object,IDisposable):
 """
 Allows clients to poll the cancellation status of a background operation. Revit instantiates
    CancellationListener objects for internal background operation implementations only. As such,
    third-party developers are not expected to instantiate or handle CancellationListener objects.
 """
 def Dispose(self):
  """ Dispose(self: CancellationListener) """
  pass
 def IsCancelled(self):
  """
  IsCancelled(self: CancellationListener) -> bool
  
   Returns true if the operation associated with this instance has been cancelled.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: CancellationListener,disposing: bool) """
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

Get: IsValidObject(self: CancellationListener) -> bool

"""


