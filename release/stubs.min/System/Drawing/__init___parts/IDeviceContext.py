class IDeviceContext(IDisposable):
 """ Defines methods for obtaining and releasing an existing handle to a Windows device context. """
 def Instance(self):
  """ This function has been arbitrarily put into the stubs"""
  return IDeviceContext()

 def GetHdc(self):
  """
  GetHdc(self: IDeviceContext) -> IntPtr
  
   Returns the handle to a Windows device context.
   Returns: An System.IntPtr representing the handle of a device context.
  """
  pass
 def ReleaseHdc(self):
  """
  ReleaseHdc(self: IDeviceContext)
   Releases the handle of a Windows device context.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
