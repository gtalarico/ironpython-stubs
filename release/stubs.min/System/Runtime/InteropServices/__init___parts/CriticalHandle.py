class CriticalHandle(CriticalFinalizerObject,IDisposable):
 """ Represents a wrapper class for handle resources. """
 def Close(self):
  """
  Close(self: CriticalHandle)

   Marks the handle for releasing and freeing resources.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: CriticalHandle)

   Releases all resources used by the System.Runtime.InteropServices.CriticalHandle.
  """
  pass
 def ReleaseHandle(self,*args):
  """
  ReleaseHandle(self: CriticalHandle) -> bool

  

   When overridden in a derived class,executes the code required to free the handle.

   Returns: true if the handle is released successfully; otherwise,in the event of a catastrophic failure,

    false. In this case,it generates a releaseHandleFailed MDA Managed Debugging Assistant.
  """
  pass
 def SetHandle(self,*args):
  """
  SetHandle(self: CriticalHandle,handle: IntPtr)

   Sets the handle to the specified pre-existing handle.

  

   handle: The pre-existing handle to use.
  """
  pass
 def SetHandleAsInvalid(self):
  """
  SetHandleAsInvalid(self: CriticalHandle)

   Marks a handle as invalid.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,invalidHandleValue: IntPtr) """
  pass
 IsClosed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the handle is closed.



Get: IsClosed(self: CriticalHandle) -> bool



"""

 IsInvalid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets a value indicating whether the handle value is invalid.



Get: IsInvalid(self: CriticalHandle) -> bool



"""


 handle=None

