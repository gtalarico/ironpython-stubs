class ContextMenu(Menu,IComponent,IDisposable):
 """
 Represents a shortcut menu. Although System.Windows.Forms.ContextMenuStrip replaces and adds functionality to the System.Windows.Forms.ContextMenu control of previous versions,System.Windows.Forms.ContextMenu is retained for both backward compatibility and future use if you choose.

 

 ContextMenu()

 ContextMenu(menuItems: Array[MenuItem])
 """
 def CloneMenu(self,*args):
  """
  CloneMenu(self: Menu,menuSrc: Menu)

   Copies the System.Windows.Forms.Menu that is passed as a parameter to the current 

    System.Windows.Forms.Menu.

  

  

   menuSrc: The System.Windows.Forms.Menu to copy.
  """
  pass
 def CreateMenuHandle(self,*args):
  """
  CreateMenuHandle(self: Menu) -> IntPtr

  

   Creates a new handle to the System.Windows.Forms.Menu.

   Returns: A handle to the menu if the method succeeds; otherwise,null.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: Menu,disposing: bool)

   Disposes of the resources,other than memory,used by the System.Windows.Forms.Menu.

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def FindMergePosition(self,*args):
  """
  FindMergePosition(self: Menu,mergeOrder: int) -> int

  

   Returns the position at which a menu item should be inserted into the menu.

  

   mergeOrder: The merge order position for the menu item to be merged.

   Returns: The position at which a menu item should be inserted into the menu.
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
 def OnCollapse(self,*args):
  """
  OnCollapse(self: ContextMenu,e: EventArgs)

   Raises the System.Windows.Forms.ContextMenu.Collapse event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnPopup(self,*args):
  """
  OnPopup(self: ContextMenu,e: EventArgs)

   Raises the System.Windows.Forms.ContextMenu.Popup event

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def ProcessCmdKey(self,*args):
  """
  ProcessCmdKey(self: ContextMenu,msg: Message,keyData: Keys,control: Control) -> (bool,Message)

  

   Processes a command key.

  

   msg: A System.Windows.Forms.Message,passed by reference,that represents the window message to 

    process.

  

   keyData: One of the System.Windows.Forms.Keys values that represents the key to process.

   control: The control to which the command key applies.

   Returns: true if the character was processed by the control; otherwise,false.

  ProcessCmdKey(self: Menu,msg: Message,keyData: Keys) -> (bool,Message)

  

   Processes a command key.

  

   msg: A System.Windows.Forms.Message,passed by reference that represents the window message to 

    process.

  

   keyData: One of the System.Windows.Forms.Keys values that represents the key to process.

   Returns: true if the character was processed by the control; otherwise,false.
  """
  pass
 def Show(self,control,pos,alignment=None):
  """
  Show(self: ContextMenu,control: Control,pos: Point,alignment: LeftRightAlignment)

   Displays the shortcut menu at the specified position and with the specified alignment.

  

   control: A System.Windows.Forms.Control that specifies the control with which this shortcut menu is 

    associated.

  

   pos: A System.Drawing.Point that specifies the coordinates at which to display the menu. These 

    coordinates are specified relative to the client coordinates of the control specified in the 

    control parameter.

  

   alignment: A System.Windows.Forms.LeftRightAlignment that specifies the alignment of the control relative 

    to the pos parameter.

  

  Show(self: ContextMenu,control: Control,pos: Point)

   Displays the shortcut menu at the specified position.

  

   control: A System.Windows.Forms.Control that specifies the control with which this shortcut menu is 

    associated.

  

   pos: A System.Drawing.Point that specifies the coordinates at which to display the menu. These 

    coordinates are specified relative to the client coordinates of the control specified in the 

    control parameter.
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
 def __new__(self,menuItems=None):
  """
  __new__(cls: type)

  __new__(cls: type,menuItems: Array[MenuItem])
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

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 RightToLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether text displayed by the control is displayed from right to left.



Get: RightToLeft(self: ContextMenu) -> RightToLeft



Set: RightToLeft(self: ContextMenu)=value

"""

 SourceControl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the control that is displaying the shortcut menu.



Get: SourceControl(self: ContextMenu) -> Control



"""


 Collapse=None
 Popup=None

