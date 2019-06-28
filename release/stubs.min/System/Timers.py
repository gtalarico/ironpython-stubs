# encoding: utf-8
# module System.Timers calls itself Timers
# from System,Version=4.0.0.0,Culture=neutral,PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ElapsedEventArgs:
 """ Provides data for the System.Timers.Timer.Elapsed event. """
 SignalTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the time the System.Timers.Timer.Elapsed event was raised.

Get: SignalTime(self: ElapsedEventArgs) -> DateTime

"""



class ElapsedEventHandler:
 """
 Represents the method that will handle the System.Timers.Timer.Elapsed event of a System.Timers.Timer.
 
 ElapsedEventHandler(object: object,method: IntPtr)
 """
 def BeginInvoke(self,sender,e,callback,object):
  """ BeginInvoke(self: ElapsedEventHandler,sender: object,e: ElapsedEventArgs,callback: AsyncCallback,object: object) -> IAsyncResult """
  pass
 def CombineImpl(self,*args):
  """
  CombineImpl(self: MulticastDelegate,follow: Delegate) -> Delegate
  
   Combines this System.Delegate with the specified System.Delegate to form a new delegate.
  
   follow: The delegate to combine with this delegate.
   Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
  """
  pass
 def DynamicInvokeImpl(self,*args):
  """
  DynamicInvokeImpl(self: Delegate,args: Array[object]) -> object
  
   Dynamically invokes (late-bound) the method represented by the current delegate.
  
   args: An array of objects that are the arguments to pass to the method represented by the 
    current delegate.-or- null,if the method represented by the current delegate does not 
    require arguments.
  
   Returns: The object returned by the method represented by the delegate.
  """
  pass
 def EndInvoke(self,result):
  """ EndInvoke(self: ElapsedEventHandler,result: IAsyncResult) """
  pass
 def GetMethodImpl(self,*args):
  """
  GetMethodImpl(self: MulticastDelegate) -> MethodInfo
  
   Returns a static method represented by the current System.MulticastDelegate.
   Returns: A static method represented by the current System.MulticastDelegate.
  """
  pass
 def Invoke(self,sender,e):
  """ Invoke(self: ElapsedEventHandler,sender: object,e: ElapsedEventArgs) """
  pass
 def RemoveImpl(self,*args):
  """
  RemoveImpl(self: MulticastDelegate,value: Delegate) -> Delegate
  
   Removes an element from the invocation list of this System.MulticastDelegate that is 
    equal to the specified delegate.
  
  
   value: The delegate to search for in the invocation list.
   Returns: If value is found in the invocation list for this instance,then a new System.Delegate 
    without value in its invocation list; otherwise,this instance with its original 
    invocation list.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,object,method):
  """ __new__(cls: type,object: object,method: IntPtr) """
  pass
 def __reduce_ex__(self,*args):
  pass

class Timer:
 """
 Generates recurring events in an application.
 
 Timer()
 Timer(interval: float)
 """
 def BeginInit(self):
  """
  BeginInit(self: Timer)
   Begins the run-time initialization of a System.Timers.Timer that is used on a form or by 
    another component.
  """
  pass
 def Close(self):
  """
  Close(self: Timer)
   Releases the resources used by the System.Timers.Timer.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: Timer,disposing: bool)
   Releases all resources used by the current System.Timers.Timer.
  
   disposing: true to release both managed and unmanaged resources; false to release only unmanaged 
    resources.
  """
  pass
 def EndInit(self):
  """
  EndInit(self: Timer)
   Ends the run-time initialization of a System.Timers.Timer that is used on a form or by 
    another component.
  """
  pass
 def GetService(self,*args):
  """
  GetService(self: Component,service: Type) -> object
  
   Returns an object that represents a service provided by the 
    System.ComponentModel.Component or by its System.ComponentModel.Container.
  
  
   service: A service provided by the System.ComponentModel.Component.
   Returns: An System.Object that represents a service provided by the 
    System.ComponentModel.Component,or null if the System.ComponentModel.Component does not 
    provide the specified service.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject
  
   Creates a shallow copy of the current System.MarshalByRefObject object.
  
   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause 
    the object to be assigned a new identity when it is marshaled across a remoting boundary. 
    A value of false is usually appropriate. true to copy the current 
    System.MarshalByRefObject object's identity to its clone,which will cause remoting 
    client calls to be routed to the remote server object.
  
   Returns: A shallow copy of the current System.MarshalByRefObject object.
  MemberwiseClone(self: object) -> object
  
   Creates a shallow copy of the current System.Object.
   Returns: A shallow copy of the current System.Object.
  """
  pass
 def Start(self):
  """
  Start(self: Timer)
   Starts raising the System.Timers.Timer.Elapsed event by setting 
    System.Timers.Timer.Enabled to true.
  """
  pass
 def Stop(self):
  """
  Stop(self: Timer)
   Stops raising the System.Timers.Timer.Elapsed event by setting 
    System.Timers.Timer.Enabled to false.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,interval=None):
  """
  __new__(cls: type)
  __new__(cls: type,interval: float)
  """
  pass
 def __str__(self,*args):
  pass
 AutoReset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Timers.Timer should raise the System.Timers.Timer.Elapsed event each time the specified interval elapses or only after the first time it elapses.

Get: AutoReset(self: Timer) -> bool

Set: AutoReset(self: Timer)=value
"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.

"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Timers.Timer should raise the System.Timers.Timer.Elapsed event.

Get: Enabled(self: Timer) -> bool

Set: Enabled(self: Timer)=value
"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

 Interval=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the interval at which to raise the System.Timers.Timer.Elapsed event.

Get: Interval(self: Timer) -> float

Set: Interval(self: Timer)=value
"""

 Site=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the site that binds the System.Timers.Timer to its container in design mode.

Get: Site(self: Timer) -> ISite

Set: Site(self: Timer)=value
"""

 SynchronizingObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object used to marshal event-handler calls that are issued when an interval has elapsed.

Get: SynchronizingObject(self: Timer) -> ISynchronizeInvoke

Set: SynchronizingObject(self: Timer)=value
"""


 Elapsed=None


class TimersDescriptionAttribute:
 """
 Sets the description that visual designers can display when referencing an event,extender,or property.
 
 TimersDescriptionAttribute(description: str)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,description):
  """ __new__(cls: type,description: str) """
  pass
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the description that visual designers can display when referencing an event,extender,or property.

Get: Description(self: TimersDescriptionAttribute) -> str

"""

 DescriptionValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the string stored as the description.

"""



