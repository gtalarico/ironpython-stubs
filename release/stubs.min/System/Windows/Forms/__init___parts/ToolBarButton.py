class ToolBarButton(Component,IComponent,IDisposable):
 """
 Represents a Windows toolbar button. Although System.Windows.Forms.ToolStripButton replaces and extends the System.Windows.Forms.ToolBarButton control of previous versions,System.Windows.Forms.ToolBarButton is retained for both backward compatibility and future use if you choose.

 

 ToolBarButton()

 ToolBarButton(text: str)
 """
 def Dispose(self):
  """
  Dispose(self: ToolBarButton,disposing: bool)

   Releases the unmanaged resources used by the System.Windows.Forms.ToolBarButton and optionally 

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
 def ToString(self):
  """
  ToString(self: ToolBarButton) -> str

  

   Returns a string that represents the System.Windows.Forms.ToolBarButton control.

   Returns: A string that represents the current System.Windows.Forms.ToolBarButton.
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
 def __new__(self,text=None):
  """
  __new__(cls: type)

  __new__(cls: type,text: str)
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

 DropDownMenu=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the menu to be displayed in the drop-down toolbar button.



Get: DropDownMenu(self: ToolBarButton) -> Menu



Set: DropDownMenu(self: ToolBarButton)=value

"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the button is enabled.



Get: Enabled(self: ToolBarButton) -> bool



Set: Enabled(self: ToolBarButton)=value

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 ImageIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the index value of the image assigned to the button.



Get: ImageIndex(self: ToolBarButton) -> int



Set: ImageIndex(self: ToolBarButton)=value

"""

 ImageKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the image assigned to the button.



Get: ImageKey(self: ToolBarButton) -> str



Set: ImageKey(self: ToolBarButton)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the button.



Get: Name(self: ToolBarButton) -> str



Set: Name(self: ToolBarButton)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the toolbar control that the toolbar button is assigned to.



Get: Parent(self: ToolBarButton) -> ToolBar



"""

 PartialPush=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether a toggle-style toolbar button is partially pushed.



Get: PartialPush(self: ToolBarButton) -> bool



Set: PartialPush(self: ToolBarButton)=value

"""

 Pushed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether a toggle-style toolbar button is currently in the pushed state.



Get: Pushed(self: ToolBarButton) -> bool



Set: Pushed(self: ToolBarButton)=value

"""

 Rectangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the bounding rectangle for a toolbar button.



Get: Rectangle(self: ToolBarButton) -> Rectangle



"""

 Style=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style of the toolbar button.



Get: Style(self: ToolBarButton) -> ToolBarButtonStyle



Set: Style(self: ToolBarButton)=value

"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object that contains data about the toolbar button.



Get: Tag(self: ToolBarButton) -> object



Set: Tag(self: ToolBarButton)=value

"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text displayed on the toolbar button.



Get: Text(self: ToolBarButton) -> str



Set: Text(self: ToolBarButton)=value

"""

 ToolTipText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text that appears as a ToolTip for the button.



Get: ToolTipText(self: ToolBarButton) -> str



Set: ToolTipText(self: ToolBarButton)=value

"""

 Visible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the toolbar button is visible.



Get: Visible(self: ToolBarButton) -> bool



Set: Visible(self: ToolBarButton)=value

"""


