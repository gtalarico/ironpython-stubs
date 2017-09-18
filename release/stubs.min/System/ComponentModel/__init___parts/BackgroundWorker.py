class BackgroundWorker(Component,IComponent,IDisposable):
 """
 Executes an operation on a separate thread.

 

 BackgroundWorker()
 """
 def CancelAsync(self):
  """
  CancelAsync(self: BackgroundWorker)

   Requests cancellation of a pending background operation.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: Component,disposing: bool)

   Releases the unmanaged resources used by the System.ComponentModel.Component and optionally 

    releases the managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def GetService(self,*args):
  """
  GetService(self: Component,service: Type) -> object

  

   Returns an object that represents a service provided by the System.ComponentModel.Component or 

    by its System.ComponentModel.Container.

  

  

   service: A service provided by the System.ComponentModel.Component.

   Returns: An System.Object that represents a service provided by the System.ComponentModel.Component,or 

    null if the System.ComponentModel.Component does not provide the specified service.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject

  

   Creates a shallow copy of the current System.MarshalByRefObject object.

  

   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the 

    object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 

    false is usually appropriate. true to copy the current System.MarshalByRefObject object's 

    identity to its clone,which will cause remoting client calls to be routed to the remote server 

    object.

  

   Returns: A shallow copy of the current System.MarshalByRefObject object.

  MemberwiseClone(self: object) -> object

  

   Creates a shallow copy of the current System.Object.

   Returns: A shallow copy of the current System.Object.
  """
  pass
 def OnDoWork(self,*args):
  """
  OnDoWork(self: BackgroundWorker,e: DoWorkEventArgs)

   Raises the System.ComponentModel.BackgroundWorker.DoWork event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnProgressChanged(self,*args):
  """
  OnProgressChanged(self: BackgroundWorker,e: ProgressChangedEventArgs)

   Raises the System.ComponentModel.BackgroundWorker.ProgressChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnRunWorkerCompleted(self,*args):
  """
  OnRunWorkerCompleted(self: BackgroundWorker,e: RunWorkerCompletedEventArgs)

   Raises the System.ComponentModel.BackgroundWorker.RunWorkerCompleted event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def ReportProgress(self,percentProgress,userState=None):
  """
  ReportProgress(self: BackgroundWorker,percentProgress: int,userState: object)

   Raises the System.ComponentModel.BackgroundWorker.ProgressChanged event.

  

   percentProgress: The percentage,from 0 to 100,of the background operation that is complete.

   userState: The state object passed to System.ComponentModel.BackgroundWorker.RunWorkerAsync(System.Object).

  ReportProgress(self: BackgroundWorker,percentProgress: int)

   Raises the System.ComponentModel.BackgroundWorker.ProgressChanged event.

  

   percentProgress: The percentage,from 0 to 100,of the background operation that is complete.
  """
  pass
 def RunWorkerAsync(self,argument=None):
  """
  RunWorkerAsync(self: BackgroundWorker,argument: object)

   Starts execution of a background operation.

  

   argument: A parameter for use by the background operation to be executed in the 

    System.ComponentModel.BackgroundWorker.DoWork event handler.

  

  RunWorkerAsync(self: BackgroundWorker)

   Starts execution of a background operation.
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
 def __str__(self,*args):
  pass
 CancellationPending=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the application has requested cancellation of a background operation.



Get: CancellationPending(self: BackgroundWorker) -> bool



"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 IsBusy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.ComponentModel.BackgroundWorker is running an asynchronous operation.



Get: IsBusy(self: BackgroundWorker) -> bool



"""

 WorkerReportsProgress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.ComponentModel.BackgroundWorker can report progress updates.



Get: WorkerReportsProgress(self: BackgroundWorker) -> bool



Set: WorkerReportsProgress(self: BackgroundWorker)=value

"""

 WorkerSupportsCancellation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.ComponentModel.BackgroundWorker supports asynchronous cancellation.



Get: WorkerSupportsCancellation(self: BackgroundWorker) -> bool



Set: WorkerSupportsCancellation(self: BackgroundWorker)=value

"""


 DoWork=None
 ProgressChanged=None
 RunWorkerCompleted=None

