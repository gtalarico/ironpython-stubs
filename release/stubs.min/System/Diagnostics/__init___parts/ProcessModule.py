class ProcessModule(Component,IComponent,IDisposable):
 """ Represents a.dll or .exe file that is loaded into a particular process. """
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
 def ToString(self):
  """
  ToString(self: ProcessModule) -> str

  

   Converts the name of the module to a string.

   Returns: The value of the System.Diagnostics.ProcessModule.ModuleName property.
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
 BaseAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the memory address where the module was loaded.



Get: BaseAddress(self: ProcessModule) -> IntPtr



"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 EntryPointAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the memory address for the function that runs when the system loads and runs the module.



Get: EntryPointAddress(self: ProcessModule) -> IntPtr



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 FileName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the full path to the module.



Get: FileName(self: ProcessModule) -> str



"""

 FileVersionInfo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets version information about the module.



Get: FileVersionInfo(self: ProcessModule) -> FileVersionInfo



"""

 ModuleMemorySize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the amount of memory that is required to load the module.



Get: ModuleMemorySize(self: ProcessModule) -> int



"""

 ModuleName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the process module.



Get: ModuleName(self: ProcessModule) -> str



"""


