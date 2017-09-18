class SafeHandle(CriticalFinalizerObject,IDisposable):
 """ Represents a wrapper class for operating system handles. This class must be inherited. """
 def Close(self):
  """
  Close(self: SafeHandle)

   Marks the handle for releasing and freeing resources.
  """
  pass
 def DangerousAddRef(self,success):
  """
  DangerousAddRef(self: SafeHandle,success: bool) -> bool

  

   Manually increments the reference counter on System.Runtime.InteropServices.SafeHandle instances.

  

   success: true if the reference counter was successfully incremented; otherwise,false.
  """
  pass
 def DangerousGetHandle(self):
  """
  DangerousGetHandle(self: SafeHandle) -> IntPtr

  

   Returns the value of the System.Runtime.InteropServices.SafeHandle.handle field.

   Returns: An IntPtr representing the value of the System.Runtime.InteropServices.SafeHandle.handle field. 

    If the handle has been marked invalid with 

    System.Runtime.InteropServices.SafeHandle.SetHandleAsInvalid,this method still returns the 

    original handle value,which can be a stale value.
  """
  pass
 def DangerousRelease(self):
  """
  DangerousRelease(self: SafeHandle)

   Manually decrements the reference counter on a System.Runtime.InteropServices.SafeHandle 

    instance.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: SafeHandle)

   Releases all resources used by the System.Runtime.InteropServices.SafeHandle class.
  """
  pass
 def ReleaseHandle(self,*args):
  """
  ReleaseHandle(self: SafeHandle) -> bool

  

   When overridden in a derived class,executes the code required to free the handle.

   Returns: true if the handle is released successfully; otherwise,in the event of a catastrophic failure,

    false. In this case,it generates a releaseHandleFailed MDA Managed Debugging Assistant.
  """
  pass
 def SetHandle(self,*args):
  """
  SetHandle(self: SafeHandle,handle: IntPtr)

   Sets the handle to the specified pre-existing handle.

  

   handle: The pre-existing handle to use.
  """
  pass
 def SetHandleAsInvalid(self):
  """
  SetHandleAsInvalid(self: SafeHandle)

   Marks a handle as no longer used.
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
  """ __new__(cls: type,invalidHandleValue: IntPtr,ownsHandle: bool) """
  pass
 IsClosed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the handle is closed.



Get: IsClosed(self: SafeHandle) -> bool



"""

 IsInvalid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets a value indicating whether the handle value is invalid.



Get: IsInvalid(self: SafeHandle) -> bool



"""


 handle=None

