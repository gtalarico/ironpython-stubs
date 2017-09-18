class Process(Component,IComponent,IDisposable):
 """
 Provides access to local and remote processes and enables you to start and stop local system processes.

 

 Process()
 """
 def BeginErrorReadLine(self):
  """
  BeginErrorReadLine(self: Process)

   Begins asynchronous read operations on the redirected System.Diagnostics.Process.StandardError 

    stream of the application.
  """
  pass
 def BeginOutputReadLine(self):
  """
  BeginOutputReadLine(self: Process)

   Begins asynchronous read operations on the redirected System.Diagnostics.Process.StandardOutput 

    stream of the application.
  """
  pass
 def CancelErrorRead(self):
  """
  CancelErrorRead(self: Process)

   Cancels the asynchronous read operation on the redirected 

    System.Diagnostics.Process.StandardError stream of an application.
  """
  pass
 def CancelOutputRead(self):
  """
  CancelOutputRead(self: Process)

   Cancels the asynchronous read operation on the redirected 

    System.Diagnostics.Process.StandardOutput stream of an application.
  """
  pass
 def Close(self):
  """
  Close(self: Process)

   Frees all the resources that are associated with this component.
  """
  pass
 def CloseMainWindow(self):
  """
  CloseMainWindow(self: Process) -> bool

  

   Closes a process that has a user interface by sending a close message to its main window.

   Returns: true if the close message was successfully sent; false if the associated process does not have a 

    main window or if the main window is disabled (for example if a modal dialog is being shown).
  """
  pass
 def Dispose(self):
  """
  Dispose(self: Process,disposing: bool)

   Release all resources used by this process.

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 @staticmethod
 def EnterDebugMode():
  """
  EnterDebugMode()

   Puts a System.Diagnostics.Process component in state to interact with operating system processes 

    that run in a special mode by enabling the native property SeDebugPrivilege on the current 

    thread.
  """
  pass
 @staticmethod
 def GetCurrentProcess():
  """
  GetCurrentProcess() -> Process

  

   Gets a new System.Diagnostics.Process component and associates it with the currently active 

    process.

  

   Returns: A new System.Diagnostics.Process component associated with the process resource that is running 

    the calling application.
  """
  pass
 @staticmethod
 def GetProcessById(processId,machineName=None):
  """
  GetProcessById(processId: int) -> Process

  

   Returns a new System.Diagnostics.Process component,given the identifier of a process on the 

    local computer.

  

  

   processId: The system-unique identifier of a process resource.

   Returns: A System.Diagnostics.Process component that is associated with the local process resource 

    identified by the processId parameter.

  

  GetProcessById(processId: int,machineName: str) -> Process

  

   Returns a new System.Diagnostics.Process component,given a process identifier and the name of a 

    computer on the network.

  

  

   processId: The system-unique identifier of a process resource.

   machineName: The name of a computer on the network.

   Returns: A System.Diagnostics.Process component that is associated with a remote process resource 

    identified by the processId parameter.
  """
  pass
 @staticmethod
 def GetProcesses(machineName=None):
  """
  GetProcesses(machineName: str) -> Array[Process]

  

   Creates a new System.Diagnostics.Process component for each process resource on the specified 

    computer.

  

  

   machineName: The computer from which to read the list of processes.

   Returns: An array of type System.Diagnostics.Process that represents all the process resources running on 

    the specified computer.

  

  GetProcesses() -> Array[Process]

  

   Creates a new System.Diagnostics.Process component for each process resource on the local 

    computer.

  

   Returns: An array of type System.Diagnostics.Process that represents all the process resources running on 

    the local computer.
  """
  pass
 @staticmethod
 def GetProcessesByName(processName,machineName=None):
  """
  GetProcessesByName(processName: str,machineName: str) -> Array[Process]

  

   Creates an array of new System.Diagnostics.Process components and associates them with all the 

    process resources on a remote computer that share the specified process name.

  

  

   processName: The friendly name of the process.

   machineName: The name of a computer on the network.

   Returns: An array of type System.Diagnostics.Process that represents the process resources running the 

    specified application or file.

  

  GetProcessesByName(processName: str) -> Array[Process]

  

   Creates an array of new System.Diagnostics.Process components and associates them with all the 

    process resources on the local computer that share the specified process name.

  

  

   processName: The friendly name of the process.

   Returns: An array of type System.Diagnostics.Process that represents the process resources running the 

    specified application or file.
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
 def Kill(self):
  """
  Kill(self: Process)

   Immediately stops the associated process.
  """
  pass
 @staticmethod
 def LeaveDebugMode():
  """
  LeaveDebugMode()

   Takes a System.Diagnostics.Process component out of the state that lets it interact with 

    operating system processes that run in a special mode.
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
 def OnExited(self,*args):
  """
  OnExited(self: Process)

   Raises the System.Diagnostics.Process.Exited event.
  """
  pass
 def Refresh(self):
  """
  Refresh(self: Process)

   Discards any information about the associated process that has been cached inside the process 

    component.
  """
  pass
 def Start(self,*__args):
  """
  Start(fileName: str) -> Process

  

   Starts a process resource by specifying the name of a document or application file and 

    associates the resource with a new System.Diagnostics.Process component.

  

  

   fileName: The name of a document or application file to run in the process.

   Returns: A new System.Diagnostics.Process component that is associated with the process resource,or 

    null,if no process resource is started (for example,if an existing process is reused).

  

  Start(fileName: str,arguments: str) -> Process

  

   Starts a process resource by specifying the name of an application and a set of command-line 

    arguments,and associates the resource with a new System.Diagnostics.Process component.

  

  

   fileName: The name of an application file to run in the process.

   arguments: Command-line arguments to pass when starting the process.

   Returns: A new System.Diagnostics.Process component that is associated with the process,or null,if no 

    process resource is started (for example,if an existing process is reused).

  

  Start(startInfo: ProcessStartInfo) -> Process

  

   Starts the process resource that is specified by the parameter containing process start 

    information (for example,the file name of the process to start) and associates the resource 

    with a new System.Diagnostics.Process component.

  

  

   startInfo: The System.Diagnostics.ProcessStartInfo that contains the information that is used to start the 

    process,including the file name and any command-line arguments.

  

   Returns: A new System.Diagnostics.Process component that is associated with the process resource,or null 

    if no process resource is started (for example,if an existing process is reused).

  

  Start(self: Process) -> bool

  

   Starts (or reuses) the process resource that is specified by the 

    System.Diagnostics.Process.StartInfo property of this System.Diagnostics.Process component and 

    associates it with the component.

  

   Returns: true if a process resource is started; false if no new process resource is started (for example,

    if an existing process is reused).

  

  Start(fileName: str,userName: str,password: SecureString,domain: str) -> Process

  

   Starts a process resource by specifying the name of an application,a user name,a password,and 

    a domain and associates the resource with a new System.Diagnostics.Process component.

  

  

   fileName: The name of an application file to run in the process.

   userName: The user name to use when starting the process.

   password: A System.Security.SecureString that contains the password to use when starting the process.

   domain: The domain to use when starting the process.

   Returns: A new System.Diagnostics.Process component that is associated with the process resource,or null 

    if no process resource is started (for example,if an existing process is reused).

  

  Start(fileName: str,arguments: str,userName: str,password: SecureString,domain: str) -> Process

  

   Starts a process resource by specifying the name of an application,a set of command-line 

    arguments,a user name,a password,and a domain and associates the resource with a new 

    System.Diagnostics.Process component.

  

  

   fileName: The name of an application file to run in the process.

   arguments: Command-line arguments to pass when starting the process.

   userName: The user name to use when starting the process.

   password: A System.Security.SecureString that contains the password to use when starting the process.

   domain: The domain to use when starting the process.

   Returns: A new System.Diagnostics.Process component that is associated with the process resource,or null 

    if no process resource is started (for example,if an existing process is reused).
  """
  pass
 def ToString(self):
  """
  ToString(self: Process) -> str

  

   Formats the process's name as a string,combined with the parent component type,if applicable.

   Returns: The System.Diagnostics.Process.ProcessName,combined with the base component's 

    System.Object.ToString return value.
  """
  pass
 def WaitForExit(self,milliseconds=None):
  """
  WaitForExit(self: Process)

   Instructs the System.Diagnostics.Process component to wait indefinitely for the associated 

    process to exit.

  

  WaitForExit(self: Process,milliseconds: int) -> bool

  

   Instructs the System.Diagnostics.Process component to wait the specified number of milliseconds 

    for the associated process to exit.

  

  

   milliseconds: The amount of time,in milliseconds,to wait for the associated process to exit. The maximum is 

    the largest possible value of a 32-bit integer,which represents infinity to the operating 

    system.

  

   Returns: true if the associated process has exited; otherwise,false.
  """
  pass
 def WaitForInputIdle(self,milliseconds=None):
  """
  WaitForInputIdle(self: Process) -> bool

  

   Causes the System.Diagnostics.Process component to wait indefinitely for the associated process 

    to enter an idle state. This overload applies only to processes with a user interface and,

    therefore,a message loop.

  

   Returns: true if the associated process has reached an idle state.

  WaitForInputIdle(self: Process,milliseconds: int) -> bool

  

   Causes the System.Diagnostics.Process component to wait the specified number of milliseconds for 

    the associated process to enter an idle state. This overload applies only to processes with a 

    user interface and,therefore,a message loop.

  

  

   milliseconds: A value of 1 to System.Int32.MaxValue that specifies the amount of time,in milliseconds,to 

    wait for the associated process to become idle. A value of 0 specifies an immediate return,and 

    a value of -1 specifies an infinite wait.

  

   Returns: true if the associated process has reached an idle state; otherwise,false.
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
 BasePriority=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the base priority of the associated process.



Get: BasePriority(self: Process) -> int



"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 EnableRaisingEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether the System.Diagnostics.Process.Exited event should be raised when the process terminates.



Get: EnableRaisingEvents(self: Process) -> bool



Set: EnableRaisingEvents(self: Process)=value

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 ExitCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value that the associated process specified when it terminated.



Get: ExitCode(self: Process) -> int



"""

 ExitTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the time that the associated process exited.



Get: ExitTime(self: Process) -> DateTime



"""

 Handle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the native handle of the associated process.



Get: Handle(self: Process) -> IntPtr



"""

 HandleCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of handles opened by the process.



Get: HandleCount(self: Process) -> int



"""

 HasExited=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the associated process has been terminated.



Get: HasExited(self: Process) -> bool



"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the unique identifier for the associated process.



Get: Id(self: Process) -> int



"""

 MachineName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the computer the associated process is running on.



Get: MachineName(self: Process) -> str



"""

 MainModule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the main module for the associated process.



Get: MainModule(self: Process) -> ProcessModule



"""

 MainWindowHandle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the window handle of the main window of the associated process.



Get: MainWindowHandle(self: Process) -> IntPtr



"""

 MainWindowTitle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the caption of the main window of the process.



Get: MainWindowTitle(self: Process) -> str



"""

 MaxWorkingSet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum allowable working set size for the associated process.



Get: MaxWorkingSet(self: Process) -> IntPtr



Set: MaxWorkingSet(self: Process)=value

"""

 MinWorkingSet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the minimum allowable working set size for the associated process.



Get: MinWorkingSet(self: Process) -> IntPtr



Set: MinWorkingSet(self: Process)=value

"""

 Modules=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the modules that have been loaded by the associated process.



Get: Modules(self: Process) -> ProcessModuleCollection



"""

 NonpagedSystemMemorySize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the nonpaged system memory size allocated to this process.



Get: NonpagedSystemMemorySize(self: Process) -> int



"""

 NonpagedSystemMemorySize64=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the amount of nonpaged system memory allocated for the associated process.



Get: NonpagedSystemMemorySize64(self: Process) -> Int64



"""

 PagedMemorySize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the paged memory size.



Get: PagedMemorySize(self: Process) -> int



"""

 PagedMemorySize64=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the amount of paged memory allocated for the associated process.



Get: PagedMemorySize64(self: Process) -> Int64



"""

 PagedSystemMemorySize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the paged system memory size.



Get: PagedSystemMemorySize(self: Process) -> int



"""

 PagedSystemMemorySize64=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the amount of pageable system memory allocated for the associated process.



Get: PagedSystemMemorySize64(self: Process) -> Int64



"""

 PeakPagedMemorySize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the peak paged memory size.



Get: PeakPagedMemorySize(self: Process) -> int



"""

 PeakPagedMemorySize64=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the maximum amount of memory in the virtual memory paging file used by the associated process.



Get: PeakPagedMemorySize64(self: Process) -> Int64



"""

 PeakVirtualMemorySize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the peak virtual memory size.



Get: PeakVirtualMemorySize(self: Process) -> int



"""

 PeakVirtualMemorySize64=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the maximum amount of virtual memory used by the associated process.



Get: PeakVirtualMemorySize64(self: Process) -> Int64



"""

 PeakWorkingSet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the peak working set size for the associated process.



Get: PeakWorkingSet(self: Process) -> int



"""

 PeakWorkingSet64=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the maximum amount of physical memory used by the associated process.



Get: PeakWorkingSet64(self: Process) -> Int64



"""

 PriorityBoostEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the associated process priority should temporarily be boosted by the operating system when the main window has the focus.



Get: PriorityBoostEnabled(self: Process) -> bool



Set: PriorityBoostEnabled(self: Process)=value

"""

 PriorityClass=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the overall priority category for the associated process.



Get: PriorityClass(self: Process) -> ProcessPriorityClass



Set: PriorityClass(self: Process)=value

"""

 PrivateMemorySize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the private memory size.



Get: PrivateMemorySize(self: Process) -> int



"""

 PrivateMemorySize64=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the amount of private memory allocated for the associated process.



Get: PrivateMemorySize64(self: Process) -> Int64



"""

 PrivilegedProcessorTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the privileged processor time for this process.



Get: PrivilegedProcessorTime(self: Process) -> TimeSpan



"""

 ProcessName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the process.



Get: ProcessName(self: Process) -> str



"""

 ProcessorAffinity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the processors on which the threads in this process can be scheduled to run.



Get: ProcessorAffinity(self: Process) -> IntPtr



Set: ProcessorAffinity(self: Process)=value

"""

 Responding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the user interface of the process is responding.



Get: Responding(self: Process) -> bool



"""

 SafeHandle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SafeHandle(self: Process) -> SafeProcessHandle



"""

 SessionId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Terminal Services session identifier for the associated process.



Get: SessionId(self: Process) -> int



"""

 StandardError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a stream used to read the error output of the application.



Get: StandardError(self: Process) -> StreamReader



"""

 StandardInput=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a stream used to write the input of the application.



Get: StandardInput(self: Process) -> StreamWriter



"""

 StandardOutput=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a stream used to read the output of the application.



Get: StandardOutput(self: Process) -> StreamReader



"""

 StartInfo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the properties to pass to the System.Diagnostics.Process.Start method of the System.Diagnostics.Process.



Get: StartInfo(self: Process) -> ProcessStartInfo



Set: StartInfo(self: Process)=value

"""

 StartTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the time that the associated process was started.



Get: StartTime(self: Process) -> DateTime



"""

 SynchronizingObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object used to marshal the event handler calls that are issued as a result of a process exit event.



Get: SynchronizingObject(self: Process) -> ISynchronizeInvoke



Set: SynchronizingObject(self: Process)=value

"""

 Threads=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the set of threads that are running in the associated process.



Get: Threads(self: Process) -> ProcessThreadCollection



"""

 TotalProcessorTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the total processor time for this process.



Get: TotalProcessorTime(self: Process) -> TimeSpan



"""

 UserProcessorTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the user processor time for this process.



Get: UserProcessorTime(self: Process) -> TimeSpan



"""

 VirtualMemorySize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the size of the process's virtual memory.



Get: VirtualMemorySize(self: Process) -> int



"""

 VirtualMemorySize64=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the amount of the virtual memory allocated for the associated process.



Get: VirtualMemorySize64(self: Process) -> Int64



"""

 WorkingSet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the associated process's physical memory usage.



Get: WorkingSet(self: Process) -> int



"""

 WorkingSet64=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the amount of physical memory allocated for the associated process.



Get: WorkingSet64(self: Process) -> Int64



"""


 ErrorDataReceived=None
 Exited=None
 OutputDataReceived=None

