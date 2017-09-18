class MenuItem(Menu,IComponent,IDisposable):
 """
 Represents an individual item that is displayed within a System.Windows.Forms.MainMenu or System.Windows.Forms.ContextMenu. Although System.Windows.Forms.ToolStripMenuItem replaces and adds functionality to the System.Windows.Forms.MenuItem control of previous versions,System.Windows.Forms.MenuItem is retained for both backward compatibility and future use if you choose.

 

 MenuItem()

 MenuItem(text: str)

 MenuItem(text: str,onClick: EventHandler)

 MenuItem(text: str,onClick: EventHandler,shortcut: Shortcut)

 MenuItem(text: str,items: Array[MenuItem])

 MenuItem(mergeType: MenuMerge,mergeOrder: int,shortcut: Shortcut,text: str,onClick: EventHandler,onPopup: EventHandler,onSelect: EventHandler,items: Array[MenuItem])
 """
 def CloneMenu(self):
  """
  CloneMenu(self: MenuItem) -> MenuItem

  

   Creates a copy of the current System.Windows.Forms.MenuItem.

   Returns: A System.Windows.Forms.MenuItem that represents the duplicated menu item.
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
  Dispose(self: MenuItem,disposing: bool)

   Disposes of the resources (other than memory) used by the System.Windows.Forms.MenuItem.

  

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
 def MergeMenu(self,*__args):
  """
  MergeMenu(self: MenuItem,itemSrc: MenuItem)

   Merges another menu item with this menu item.

  

   itemSrc: A System.Windows.Forms.MenuItem that specifies the menu item to merge with this one.

  MergeMenu(self: MenuItem) -> MenuItem

  

   Merges this System.Windows.Forms.MenuItem with another System.Windows.Forms.MenuItem and returns 

    the resulting merged System.Windows.Forms.MenuItem.

  

   Returns: A System.Windows.Forms.MenuItem that represents the merged menu item.
  """
  pass
 def OnClick(self,*args):
  """
  OnClick(self: MenuItem,e: EventArgs)

   Raises the System.Windows.Forms.MenuItem.Click event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDrawItem(self,*args):
  """
  OnDrawItem(self: MenuItem,e: DrawItemEventArgs)

   Raises the System.Windows.Forms.MenuItem.DrawItem event.

  

   e: A System.Windows.Forms.DrawItemEventArgs that contains the event data.
  """
  pass
 def OnInitMenuPopup(self,*args):
  """
  OnInitMenuPopup(self: MenuItem,e: EventArgs)

   Raises the System.Windows.Forms.MenuItem.Popup event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnMeasureItem(self,*args):
  """
  OnMeasureItem(self: MenuItem,e: MeasureItemEventArgs)

   Raises the System.Windows.Forms.MenuItem.MeasureItem event.

  

   e: A System.Windows.Forms.MeasureItemEventArgs that contains the event data.
  """
  pass
 def OnPopup(self,*args):
  """
  OnPopup(self: MenuItem,e: EventArgs)

   Raises the System.Windows.Forms.MenuItem.Popup event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnSelect(self,*args):
  """
  OnSelect(self: MenuItem,e: EventArgs)

   Raises the System.Windows.Forms.MenuItem.Select event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def PerformClick(self):
  """
  PerformClick(self: MenuItem)

   Generates a System.Windows.Forms.Control.Click event for the System.Windows.Forms.MenuItem,

    simulating a click by a user.
  """
  pass
 def PerformSelect(self):
  """
  PerformSelect(self: MenuItem)

   Raises the System.Windows.Forms.MenuItem.Select event for this menu item.
  """
  pass
 def ProcessCmdKey(self,*args):
  """
  ProcessCmdKey(self: Menu,msg: Message,keyData: Keys) -> (bool,Message)

  

   Processes a command key.

  

   msg: A System.Windows.Forms.Message,passed by reference that represents the window message to 

    process.

  

   keyData: One of the System.Windows.Forms.Keys values that represents the key to process.

   Returns: true if the character was processed by the control; otherwise,false.
  """
  pass
 def ToString(self):
  """
  ToString(self: MenuItem) -> str

  

   Returns a string that represents the System.Windows.Forms.MenuItem.

   Returns: A string that represents the current System.Windows.Forms.MenuItem. The string includes the type 

    and the System.Windows.Forms.MenuItem.Text property of the control.
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
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,text: str)

  __new__(cls: type,text: str,onClick: EventHandler)

  __new__(cls: type,text: str,onClick: EventHandler,shortcut: Shortcut)

  __new__(cls: type,text: str,items: Array[MenuItem])

  __new__(cls: type,mergeType: MenuMerge,mergeOrder: int,shortcut: Shortcut,text: str,onClick: EventHandler,onPopup: EventHandler,onSelect: EventHandler,items: Array[MenuItem])
  """
  pass
 def __str__(self,*args):
  pass
 BarBreak=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.MenuItem is placed on a new line (for a menu item added to a System.Windows.Forms.MainMenu object) or in a new column (for a submenu item or menu item displayed in a System.Windows.Forms.ContextMenu).



Get: BarBreak(self: MenuItem) -> bool



Set: BarBreak(self: MenuItem)=value

"""

 Break=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the item is placed on a new line (for a menu item added to a System.Windows.Forms.MainMenu object) or in a new column (for a menu item or submenu item displayed in a System.Windows.Forms.ContextMenu).



Get: Break(self: MenuItem) -> bool



Set: Break(self: MenuItem)=value

"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 Checked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether a check mark appears next to the text of the menu item.



Get: Checked(self: MenuItem) -> bool



Set: Checked(self: MenuItem)=value

"""

 DefaultItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the menu item is the default menu item.



Get: DefaultItem(self: MenuItem) -> bool



Set: DefaultItem(self: MenuItem)=value

"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the menu item is enabled.



Get: Enabled(self: MenuItem) -> bool



Set: Enabled(self: MenuItem)=value

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the position of the menu item in its parent menu.



Get: Index(self: MenuItem) -> int



Set: Index(self: MenuItem)=value

"""

 IsParent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the menu item contains child menu items.



Get: IsParent(self: MenuItem) -> bool



"""

 MdiList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the menu item will be populated with a list of the Multiple Document Interface (MDI) child windows that are displayed within the associated form.



Get: MdiList(self: MenuItem) -> bool



Set: MdiList(self: MenuItem)=value

"""

 MenuID=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating the Windows identifier for this menu item.



"""

 MergeOrder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the relative position of the menu item when it is merged with another.



Get: MergeOrder(self: MenuItem) -> int



Set: MergeOrder(self: MenuItem)=value

"""

 MergeType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the behavior of this menu item when its menu is merged with another.



Get: MergeType(self: MenuItem) -> MenuMerge



Set: MergeType(self: MenuItem)=value

"""

 Mnemonic=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating the mnemonic character that is associated with this menu item.



Get: Mnemonic(self: MenuItem) -> Char



"""

 OwnerDraw=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the code that you provide draws the menu item or Windows draws the menu item.



Get: OwnerDraw(self: MenuItem) -> bool



Set: OwnerDraw(self: MenuItem)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating the menu that contains this menu item.



Get: Parent(self: MenuItem) -> Menu



"""

 RadioCheck=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.MenuItem,if checked,displays a radio-button instead of a check mark.



Get: RadioCheck(self: MenuItem) -> bool



Set: RadioCheck(self: MenuItem)=value

"""

 Shortcut=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the shortcut key associated with the menu item.



Get: Shortcut(self: MenuItem) -> Shortcut



Set: Shortcut(self: MenuItem)=value

"""

 ShowShortcut=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the shortcut key that is associated with the menu item is displayed next to the menu item caption.



Get: ShowShortcut(self: MenuItem) -> bool



Set: ShowShortcut(self: MenuItem)=value

"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the caption of the menu item.



Get: Text(self: MenuItem) -> str



Set: Text(self: MenuItem)=value

"""

 Visible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the menu item is visible.



Get: Visible(self: MenuItem) -> bool



Set: Visible(self: MenuItem)=value

"""


 Click=None
 DrawItem=None
 MeasureItem=None
 Popup=None
 Select=None

