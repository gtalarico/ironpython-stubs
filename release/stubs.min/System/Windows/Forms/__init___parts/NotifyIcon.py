class NotifyIcon(Component,IComponent,IDisposable):
 """
 Specifies a component that creates an icon in the notification area. This class cannot be inherited.

 

 NotifyIcon()

 NotifyIcon(container: IContainer)
 """
 def Dispose(self):
  """ Dispose(self: NotifyIcon,disposing: bool) """
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
 def ShowBalloonTip(self,timeout,tipTitle=None,tipText=None,tipIcon=None):
  """
  ShowBalloonTip(self: NotifyIcon,timeout: int,tipTitle: str,tipText: str,tipIcon: ToolTipIcon)

   Displays a balloon tip with the specified title,text,and icon in the taskbar for the specified 

    time period.

  

  

   timeout: The time period,in milliseconds,the balloon tip should display.

   tipTitle: The title to display on the balloon tip.

   tipText: The text to display on the balloon tip.

   tipIcon: One of the System.Windows.Forms.ToolTipIcon values.

  ShowBalloonTip(self: NotifyIcon,timeout: int)

   Displays a balloon tip in the taskbar for the specified time period.

  

   timeout: The time period,in milliseconds,the balloon tip should display.
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
 BalloonTipIcon=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the icon to display on the balloon tip associated with the System.Windows.Forms.NotifyIcon.



Get: BalloonTipIcon(self: NotifyIcon) -> ToolTipIcon



Set: BalloonTipIcon(self: NotifyIcon)=value

"""

 BalloonTipText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text to display on the balloon tip associated with the System.Windows.Forms.NotifyIcon.



Get: BalloonTipText(self: NotifyIcon) -> str



Set: BalloonTipText(self: NotifyIcon)=value

"""

 BalloonTipTitle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the title of the balloon tip displayed on the System.Windows.Forms.NotifyIcon.



Get: BalloonTipTitle(self: NotifyIcon) -> str



Set: BalloonTipTitle(self: NotifyIcon)=value

"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 ContextMenu=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the shortcut menu for the icon.



Get: ContextMenu(self: NotifyIcon) -> ContextMenu



Set: ContextMenu(self: NotifyIcon)=value

"""

 ContextMenuStrip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the shortcut menu associated with the System.Windows.Forms.NotifyIcon.



Get: ContextMenuStrip(self: NotifyIcon) -> ContextMenuStrip



Set: ContextMenuStrip(self: NotifyIcon)=value

"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 Icon=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current icon.



Get: Icon(self: NotifyIcon) -> Icon



Set: Icon(self: NotifyIcon)=value

"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an object that contains data about the System.Windows.Forms.NotifyIcon.



Get: Tag(self: NotifyIcon) -> object



Set: Tag(self: NotifyIcon)=value

"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the ToolTip text displayed when the mouse pointer rests on a notification area icon.



Get: Text(self: NotifyIcon) -> str



Set: Text(self: NotifyIcon)=value

"""

 Visible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the icon is visible in the notification area of the taskbar.



Get: Visible(self: NotifyIcon) -> bool



Set: Visible(self: NotifyIcon)=value

"""


 BalloonTipClicked=None
 BalloonTipClosed=None
 BalloonTipShown=None
 Click=None
 DoubleClick=None
 MouseClick=None
 MouseDoubleClick=None
 MouseDown=None
 MouseMove=None
 MouseUp=None

