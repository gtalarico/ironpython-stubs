class HelpProvider(Component,IComponent,IDisposable,IExtenderProvider):
 """
 Provides pop-up or online Help for controls.

 

 HelpProvider()
 """
 def CanExtend(self,target):
  """
  CanExtend(self: HelpProvider,target: object) -> bool

  

   Specifies whether this object can provide its extender properties to the specified object.

  

   target: The object that the externder properties are provided to.

   Returns: true if this object can provide its extender properties; otherwise,false.
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
 def GetHelpKeyword(self,ctl):
  """
  GetHelpKeyword(self: HelpProvider,ctl: Control) -> str

  

   Returns the Help keyword for the specified control.

  

   ctl: A System.Windows.Forms.Control from which to retrieve the Help topic.

   Returns: The Help keyword associated with this control,or null if the System.Windows.Forms.HelpProvider 

    is currently configured to display the entire Help file or is configured to provide a Help 

    string.
  """
  pass
 def GetHelpNavigator(self,ctl):
  """
  GetHelpNavigator(self: HelpProvider,ctl: Control) -> HelpNavigator

  

   Returns the current System.Windows.Forms.HelpNavigator setting for the specified control.

  

   ctl: A System.Windows.Forms.Control from which to retrieve the Help navigator.

   Returns: The System.Windows.Forms.HelpNavigator setting for the specified control. The default is 

    System.Windows.Forms.HelpNavigator.AssociateIndex.
  """
  pass
 def GetHelpString(self,ctl):
  """
  GetHelpString(self: HelpProvider,ctl: Control) -> str

  

   Returns the contents of the pop-up Help window for the specified control.

  

   ctl: A System.Windows.Forms.Control from which to retrieve the Help string.

   Returns: The Help string associated with this control. The default is null.
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
 def GetShowHelp(self,ctl):
  """
  GetShowHelp(self: HelpProvider,ctl: Control) -> bool

  

   Returns a value indicating whether the specified control's Help should be displayed.

  

   ctl: A System.Windows.Forms.Control for which Help will be displayed.

   Returns: true if Help will be displayed for the control; otherwise,false.
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
 def ResetShowHelp(self,ctl):
  """
  ResetShowHelp(self: HelpProvider,ctl: Control)

   Removes the Help associated with the specified control.

  

   ctl: The control to remove Help from.
  """
  pass
 def SetHelpKeyword(self,ctl,keyword):
  """
  SetHelpKeyword(self: HelpProvider,ctl: Control,keyword: str)

   Specifies the keyword used to retrieve Help when the user invokes Help for the specified control.

  

   ctl: A System.Windows.Forms.Control that specifies the control for which to set the Help topic.

   keyword: The Help keyword to associate with the control.
  """
  pass
 def SetHelpNavigator(self,ctl,navigator):
  """
  SetHelpNavigator(self: HelpProvider,ctl: Control,navigator: HelpNavigator)

   Specifies the Help command to use when retrieving Help from the Help file for the specified 

    control.

  

  

   ctl: A System.Windows.Forms.Control for which to set the Help keyword.

   navigator: One of the System.Windows.Forms.HelpNavigator values.
  """
  pass
 def SetHelpString(self,ctl,helpString):
  """
  SetHelpString(self: HelpProvider,ctl: Control,helpString: str)

   Specifies the Help string associated with the specified control.

  

   ctl: A System.Windows.Forms.Control with which to associate the Help string.

   helpString: The Help string associated with the control.
  """
  pass
 def SetShowHelp(self,ctl,value):
  """
  SetShowHelp(self: HelpProvider,ctl: Control,value: bool)

   Specifies whether Help is displayed for the specified control.

  

   ctl: A System.Windows.Forms.Control for which Help is turned on or off.

   value: true if Help displays for the control; otherwise,false.
  """
  pass
 def ToString(self):
  """
  ToString(self: HelpProvider) -> str

  

   Returns a string that represents the current System.Windows.Forms.HelpProvider.

   Returns: A string that represents the current System.Windows.Forms.HelpProvider.
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
 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 HelpNamespace=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value specifying the name of the Help file associated with this System.Windows.Forms.HelpProvider object.



Get: HelpNamespace(self: HelpProvider) -> str



Set: HelpNamespace(self: HelpProvider)=value

"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object that contains supplemental data about the System.Windows.Forms.HelpProvider.



Get: Tag(self: HelpProvider) -> object



Set: Tag(self: HelpProvider)=value

"""


