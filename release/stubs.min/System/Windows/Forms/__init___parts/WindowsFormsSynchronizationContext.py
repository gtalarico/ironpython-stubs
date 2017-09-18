class WindowsFormsSynchronizationContext(SynchronizationContext,IDisposable):
 """
 Provides a synchronization context for the Windows Forms application model.

 

 WindowsFormsSynchronizationContext()
 """
 def CreateCopy(self):
  """
  CreateCopy(self: WindowsFormsSynchronizationContext) -> SynchronizationContext

  

   Copies the synchronization context.

   Returns: A copy of the synchronization context.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: WindowsFormsSynchronizationContext)

   Releases all resources used by the System.Windows.Forms.WindowsFormsSynchronizationContext.
  """
  pass
 def Post(self,d,state):
  """
  Post(self: WindowsFormsSynchronizationContext,d: SendOrPostCallback,state: object)

   Dispatches an asynchronous message to a synchronization context.

  

   d: The System.Threading.SendOrPostCallback delegate to call.

   state: The object passed to the delegate.
  """
  pass
 def Send(self,d,state):
  """
  Send(self: WindowsFormsSynchronizationContext,d: SendOrPostCallback,state: object)

   Dispatches a synchronous message to a synchronization context

  

   d: The System.Threading.SendOrPostCallback delegate to call.

   state: The object passed to the delegate.
  """
  pass
 def SetWaitNotificationRequired(self,*args):
  """
  SetWaitNotificationRequired(self: SynchronizationContext)

   Sets notification that wait notification is required and prepares the callback method so it can 

    be called more reliably when a wait occurs.
  """
  pass
 @staticmethod
 def Uninstall():
  """
  Uninstall()

   Uninstalls the currently installed System.Windows.Forms.WindowsFormsSynchronizationContext and 

    replaces it with the previously installed context.
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
 AutoInstall=True


# variables with complex values

