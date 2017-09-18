class PerformanceCounter(Component,IComponent,IDisposable,ISupportInitialize):
 """
 Represents a Windows NT performance counter component.

 

 PerformanceCounter()

 PerformanceCounter(categoryName: str,counterName: str,instanceName: str,machineName: str)

 PerformanceCounter(categoryName: str,counterName: str,instanceName: str)

 PerformanceCounter(categoryName: str,counterName: str,instanceName: str,readOnly: bool)

 PerformanceCounter(categoryName: str,counterName: str)

 PerformanceCounter(categoryName: str,counterName: str,readOnly: bool)
 """
 def BeginInit(self):
  """
  BeginInit(self: PerformanceCounter)

   Begins the initialization of a System.Diagnostics.PerformanceCounter instance used on a form or 

    by another component. The initialization occurs at runtime.
  """
  pass
 def Close(self):
  """
  Close(self: PerformanceCounter)

   Closes the performance counter and frees all the resources allocated by this performance counter 

    instance.
  """
  pass
 @staticmethod
 def CloseSharedResources():
  """
  CloseSharedResources()

   Frees the performance counter library shared state allocated by the counters.
  """
  pass
 def Decrement(self):
  """
  Decrement(self: PerformanceCounter) -> Int64

  

   Decrements the associated performance counter by one through an efficient atomic operation.

   Returns: The decremented counter value.
  """
  pass
 def Dispose(self):
  """ Dispose(self: PerformanceCounter,disposing: bool) """
  pass
 def EndInit(self):
  """
  EndInit(self: PerformanceCounter)

   Ends the initialization of a System.Diagnostics.PerformanceCounter instance that is used on a 

    form or by another component. The initialization occurs at runtime.
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
 def Increment(self):
  """
  Increment(self: PerformanceCounter) -> Int64

  

   Increments the associated performance counter by one through an efficient atomic operation.

   Returns: The incremented counter value.
  """
  pass
 def IncrementBy(self,value):
  """
  IncrementBy(self: PerformanceCounter,value: Int64) -> Int64

  

   Increments or decrements the value of the associated performance counter by a specified amount 

    through an efficient atomic operation.

  

  

   value: The value to increment by. (A negative value decrements the counter.)

   Returns: The new counter value.
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
 def NextSample(self):
  """
  NextSample(self: PerformanceCounter) -> CounterSample

  

   Obtains a counter sample,and returns the raw,or uncalculated,value for it.

   Returns: A System.Diagnostics.CounterSample that represents the next raw value that the system obtains 

    for this counter.
  """
  pass
 def NextValue(self):
  """
  NextValue(self: PerformanceCounter) -> Single

  

   Obtains a counter sample and returns the calculated value for it.

   Returns: The next calculated value that the system obtains for this counter.
  """
  pass
 def RemoveInstance(self):
  """
  RemoveInstance(self: PerformanceCounter)

   Deletes the category instance specified by the System.Diagnostics.PerformanceCounter object 

    System.Diagnostics.PerformanceCounter.InstanceName property.
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
 def __new__(self,categoryName=None,counterName=None,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,categoryName: str,counterName: str,instanceName: str,machineName: str)

  __new__(cls: type,categoryName: str,counterName: str,instanceName: str)

  __new__(cls: type,categoryName: str,counterName: str,instanceName: str,readOnly: bool)

  __new__(cls: type,categoryName: str,counterName: str)

  __new__(cls: type,categoryName: str,counterName: str,readOnly: bool)
  """
  pass
 def __str__(self,*args):
  pass
 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 CategoryName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the performance counter category for this performance counter.



Get: CategoryName(self: PerformanceCounter) -> str



Set: CategoryName(self: PerformanceCounter)=value

"""

 CounterHelp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the description for this performance counter.



Get: CounterHelp(self: PerformanceCounter) -> str



"""

 CounterName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the performance counter that is associated with this System.Diagnostics.PerformanceCounter instance.



Get: CounterName(self: PerformanceCounter) -> str



Set: CounterName(self: PerformanceCounter)=value

"""

 CounterType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the counter type of the associated performance counter.



Get: CounterType(self: PerformanceCounter) -> PerformanceCounterType



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 InstanceLifetime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the lifetime of a process.



Get: InstanceLifetime(self: PerformanceCounter) -> PerformanceCounterInstanceLifetime



Set: InstanceLifetime(self: PerformanceCounter)=value

"""

 InstanceName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an instance name for this performance counter.



Get: InstanceName(self: PerformanceCounter) -> str



Set: InstanceName(self: PerformanceCounter)=value

"""

 MachineName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the computer name for this performance counter



Get: MachineName(self: PerformanceCounter) -> str



Set: MachineName(self: PerformanceCounter)=value

"""

 RawValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the raw,or uncalculated,value of this counter.



Get: RawValue(self: PerformanceCounter) -> Int64



Set: RawValue(self: PerformanceCounter)=value

"""

 ReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether this System.Diagnostics.PerformanceCounter instance is in read-only mode.



Get: ReadOnly(self: PerformanceCounter) -> bool



Set: ReadOnly(self: PerformanceCounter)=value

"""


 DefaultFileMappingSize=524288

