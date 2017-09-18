class ProcessThread(Component,IComponent,IDisposable):
 """ Represents an operating system process thread. """
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
 def ResetIdealProcessor(self):
  """
  ResetIdealProcessor(self: ProcessThread)

   Resets the ideal processor for this thread to indicate that there is no single ideal processor. 

    In other words,so that any processor is ideal.
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
 """Gets the base priority of the thread.



Get: BasePriority(self: ProcessThread) -> int



"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 CurrentPriority=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current priority of the thread.



Get: CurrentPriority(self: ProcessThread) -> int



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the unique identifier of the thread.



Get: Id(self: ProcessThread) -> int



"""

 IdealProcessor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Sets the preferred processor for this thread to run on.



Set: IdealProcessor(self: ProcessThread)=value

"""

 PriorityBoostEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the operating system should temporarily boost the priority of the associated thread whenever the main window of the thread's process receives the focus.



Get: PriorityBoostEnabled(self: ProcessThread) -> bool



Set: PriorityBoostEnabled(self: ProcessThread)=value

"""

 PriorityLevel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the priority level of the thread.



Get: PriorityLevel(self: ProcessThread) -> ThreadPriorityLevel



Set: PriorityLevel(self: ProcessThread)=value

"""

 PrivilegedProcessorTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the amount of time that the thread has spent running code inside the operating system core.



Get: PrivilegedProcessorTime(self: ProcessThread) -> TimeSpan



"""

 ProcessorAffinity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Sets the processors on which the associated thread can run.



Set: ProcessorAffinity(self: ProcessThread)=value

"""

 StartAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the memory address of the function that the operating system called that started this thread.



Get: StartAddress(self: ProcessThread) -> IntPtr



"""

 StartTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the time that the operating system started the thread.



Get: StartTime(self: ProcessThread) -> DateTime



"""

 ThreadState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current state of this thread.



Get: ThreadState(self: ProcessThread) -> ThreadState



"""

 TotalProcessorTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the total amount of time that this thread has spent using the processor.



Get: TotalProcessorTime(self: ProcessThread) -> TimeSpan



"""

 UserProcessorTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the amount of time that the associated thread has spent running code inside the application.



Get: UserProcessorTime(self: ProcessThread) -> TimeSpan



"""

 WaitReason=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the reason that the thread is waiting.



Get: WaitReason(self: ProcessThread) -> ThreadWaitReason



"""


