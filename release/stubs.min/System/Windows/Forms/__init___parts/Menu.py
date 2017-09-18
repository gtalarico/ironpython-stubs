class Menu(Component,IComponent,IDisposable):
 """ Represents the base functionality for all menus. Although System.Windows.Forms.ToolStripDropDown and System.Windows.Forms.ToolStripDropDownMenu replace and add functionality to the System.Windows.Forms.Menu control of previous versions,System.Windows.Forms.Menu is retained for both backward compatibility and future use if you choose. """
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
 def FindMenuItem(self,type,value):
  """
  FindMenuItem(self: Menu,type: int,value: IntPtr) -> MenuItem

  

   Gets the System.Windows.Forms.MenuItem that contains the value specified.

  

   type: The type of item to use to find the System.Windows.Forms.MenuItem.

   value: The item to use to find the System.Windows.Forms.MenuItem.

   Returns: The System.Windows.Forms.MenuItem that matches value; otherwise,null.
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
 def GetContextMenu(self):
  """
  GetContextMenu(self: Menu) -> ContextMenu

  

   Gets the System.Windows.Forms.ContextMenu that contains this menu.

   Returns: The System.Windows.Forms.ContextMenu that contains this menu. The default is null.
  """
  pass
 def GetMainMenu(self):
  """
  GetMainMenu(self: Menu) -> MainMenu

  

   Gets the System.Windows.Forms.MainMenu that contains this menu.

   Returns: The System.Windows.Forms.MainMenu that contains this menu.
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
 def MergeMenu(self,menuSrc):
  """
  MergeMenu(self: Menu,menuSrc: Menu)

   Merges the System.Windows.Forms.MenuItem objects of one menu with the current menu.

  

   menuSrc: The System.Windows.Forms.Menu whose menu items are merged with the menu items of the current 

    menu.
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
  ToString(self: Menu) -> str

  

   Returns a System.String that represents the System.Windows.Forms.Menu control.

   Returns: A System.String that represents the current System.Windows.Forms.Menu.
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
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,items: Array[MenuItem]) """
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

 Handle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value representing the window handle for the menu.



Get: Handle(self: Menu) -> IntPtr



"""

 IsParent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this menu contains any menu items. This property is read-only.



Get: IsParent(self: Menu) -> bool



"""

 MdiListItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating the System.Windows.Forms.MenuItem that is used to display a list of multiple document interface (MDI) child forms.



Get: MdiListItem(self: Menu) -> MenuItem



"""

 MenuItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating the collection of System.Windows.Forms.MenuItem objects associated with the menu.



Get: MenuItems(self: Menu) -> MenuItemCollection



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the System.Windows.Forms.Menu.



Get: Name(self: Menu) -> str



Set: Name(self: Menu)=value

"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets user-defined data associated with the control.



Get: Tag(self: Menu) -> object



Set: Tag(self: Menu)=value

"""


 FindHandle=0
 FindShortcut=1
 MenuItemCollection=None

