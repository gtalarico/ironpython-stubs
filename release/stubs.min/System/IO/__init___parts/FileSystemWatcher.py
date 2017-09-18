class FileSystemWatcher(Component,IComponent,IDisposable,ISupportInitialize):
 """
 Listens to the file system change notifications and raises events when a directory,or file in a directory,changes.

 

 FileSystemWatcher()

 FileSystemWatcher(path: str)

 FileSystemWatcher(path: str,filter: str)
 """
 def BeginInit(self):
  """
  BeginInit(self: FileSystemWatcher)

   Begins the initialization of a System.IO.FileSystemWatcher used on a form or used by another 

    component. The initialization occurs at run time.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: FileSystemWatcher,disposing: bool)

   Releases the unmanaged resources used by the System.IO.FileSystemWatcher and optionally releases 

    the managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def EndInit(self):
  """
  EndInit(self: FileSystemWatcher)

   Ends the initialization of a System.IO.FileSystemWatcher used on a form or used by another 

    component. The initialization occurs at run time.
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
 def OnChanged(self,*args):
  """
  OnChanged(self: FileSystemWatcher,e: FileSystemEventArgs)

   Raises the System.IO.FileSystemWatcher.Changed event.

  

   e: A System.IO.FileSystemEventArgs that contains the event data.
  """
  pass
 def OnCreated(self,*args):
  """
  OnCreated(self: FileSystemWatcher,e: FileSystemEventArgs)

   Raises the System.IO.FileSystemWatcher.Created event.

  

   e: A System.IO.FileSystemEventArgs that contains the event data.
  """
  pass
 def OnDeleted(self,*args):
  """
  OnDeleted(self: FileSystemWatcher,e: FileSystemEventArgs)

   Raises the System.IO.FileSystemWatcher.Deleted event.

  

   e: A System.IO.FileSystemEventArgs that contains the event data.
  """
  pass
 def OnError(self,*args):
  """
  OnError(self: FileSystemWatcher,e: ErrorEventArgs)

   Raises the System.IO.FileSystemWatcher.Error event.

  

   e: An System.IO.ErrorEventArgs that contains the event data.
  """
  pass
 def OnRenamed(self,*args):
  """
  OnRenamed(self: FileSystemWatcher,e: RenamedEventArgs)

   Raises the System.IO.FileSystemWatcher.Renamed event.

  

   e: A System.IO.RenamedEventArgs that contains the event data.
  """
  pass
 def WaitForChanged(self,changeType,timeout=None):
  """
  WaitForChanged(self: FileSystemWatcher,changeType: WatcherChangeTypes,timeout: int) -> WaitForChangedResult

  

   A synchronous method that returns a structure that contains specific information on the change 

    that occurred,given the type of change you want to monitor and the time (in milliseconds) to 

    wait before timing out.

  

  

   changeType: The System.IO.WatcherChangeTypes to watch for.

   timeout: The time (in milliseconds) to wait before timing out.

   Returns: A System.IO.WaitForChangedResult that contains specific information on the change that occurred.

  WaitForChanged(self: FileSystemWatcher,changeType: WatcherChangeTypes) -> WaitForChangedResult

  

   A synchronous method that returns a structure that contains specific information on the change 

    that occurred,given the type of change you want to monitor.

  

  

   changeType: The System.IO.WatcherChangeTypes to watch for.

   Returns: A System.IO.WaitForChangedResult that contains specific information on the change that occurred.
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
 def __new__(self,path=None,filter=None):
  """
  __new__(cls: type)

  __new__(cls: type,path: str)

  __new__(cls: type,path: str,filter: str)
  """
  pass
 def __str__(self,*args):
  pass
 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 EnableRaisingEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the component is enabled.



Get: EnableRaisingEvents(self: FileSystemWatcher) -> bool



Set: EnableRaisingEvents(self: FileSystemWatcher)=value

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 Filter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the filter string used to determine what files are monitored in a directory.



Get: Filter(self: FileSystemWatcher) -> str



Set: Filter(self: FileSystemWatcher)=value

"""

 IncludeSubdirectories=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether subdirectories within the specified path should be monitored.



Get: IncludeSubdirectories(self: FileSystemWatcher) -> bool



Set: IncludeSubdirectories(self: FileSystemWatcher)=value

"""

 InternalBufferSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the size (in bytes) of the internal buffer.



Get: InternalBufferSize(self: FileSystemWatcher) -> int



Set: InternalBufferSize(self: FileSystemWatcher)=value

"""

 NotifyFilter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the type of changes to watch for.



Get: NotifyFilter(self: FileSystemWatcher) -> NotifyFilters



Set: NotifyFilter(self: FileSystemWatcher)=value

"""

 Path=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the path of the directory to watch.



Get: Path(self: FileSystemWatcher) -> str



Set: Path(self: FileSystemWatcher)=value

"""

 Site=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an System.ComponentModel.ISite for the System.IO.FileSystemWatcher.



Get: Site(self: FileSystemWatcher) -> ISite



Set: Site(self: FileSystemWatcher)=value

"""

 SynchronizingObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object used to marshal the event handler calls issued as a result of a directory change.



Get: SynchronizingObject(self: FileSystemWatcher) -> ISynchronizeInvoke



Set: SynchronizingObject(self: FileSystemWatcher)=value

"""


 Changed=None
 Created=None
 Deleted=None
 Error=None
 Renamed=None

