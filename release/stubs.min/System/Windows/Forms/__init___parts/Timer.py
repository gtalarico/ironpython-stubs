class Timer(Component,IComponent,IDisposable):
 """
 Implements a timer that raises an event at user-defined intervals. This timer is optimized for use in Windows Forms applications and must be used in a window.

 

 Timer()

 Timer(container: IContainer)
 """
 def Dispose(self):
  """
  Dispose(self: Timer,disposing: bool)

   Disposes of the resources,other than memory,used by the timer.

  

   disposing: true to release both managed and unmanaged resources. false to release only the unmanaged 

    resources.
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
 def OnTick(self,*args):
  """
  OnTick(self: Timer,e: EventArgs)

   Raises the System.Windows.Forms.Timer.Tick event.

  

   e: An System.EventArgs that contains the event data. This is always System.EventArgs.Empty.
  """
  pass
 def Start(self):
  """
  Start(self: Timer)

   Starts the timer.
  """
  pass
 def Stop(self):
  """
  Stop(self: Timer)

   Stops the timer.
  """
  pass
 def ToString(self):
  """
  ToString(self: Timer) -> str

  

   Returns a string that represents the System.Windows.Forms.Timer.

   Returns: A string that represents the current System.Windows.Forms.Timer.
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
 def __new__(self,container=None):
  """
  __new__(cls: type)

  __new__(cls: type,container: IContainer)
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

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether the timer is running.



Get: Enabled(self: Timer) -> bool



Set: Enabled(self: Timer)=value

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 Interval=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the time,in milliseconds,before the System.Windows.Forms.Timer.Tick event is raised relative to the last occurrence of the System.Windows.Forms.Timer.Tick event.



Get: Interval(self: Timer) -> int



Set: Interval(self: Timer)=value

"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an arbitrary string representing some type of user state.



Get: Tag(self: Timer) -> object



Set: Tag(self: Timer)=value

"""


 Tick=None

